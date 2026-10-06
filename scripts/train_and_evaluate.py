"""
Comprehensive Machine Learning Training, Evaluation, and Serialization Script
Project: Device Risk Analysis (Academic Case Study No. 86)
Author: Atharva Gahine (B.Tech CSE Semester V, ITM SKILLS UNIVERSITY)
"""

import os
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, confusion_matrix, classification_report, roc_curve, auc
)
from sklearn.preprocessing import label_binarize

# Algorithms
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

# Set style
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'Helvetica'
plt.rcParams['axes.edgecolor'] = '#cccccc'
plt.rcParams['axes.linewidth'] = 0.8

def run_pipeline():
    print("=" * 60)
    print("DEVICE RISK ANALYSIS - ML PIPELINE EXECUTION")
    print("=" * 60)
    
    # 1. Load Raw Dataset
    raw_path = "data/raw/device_risk_raw.csv"
    if not os.path.exists(raw_path):
        raise FileNotFoundError(f"Raw data not found at {raw_path}")
        
    df_raw = pd.read_csv(raw_path)
    print(f"Loaded raw dataset: {df_raw.shape[0]} rows, {df_raw.shape[1]} columns")
    
    # 2. Data Cleaning
    print("\n--- Data Cleaning ---")
    df_cleaned = df_raw.copy()
    
    # Duplicate check and removal
    dup_count = df_cleaned.duplicated().sum()
    print(f"Identified duplicate records: {dup_count}")
    if dup_count > 0:
        df_cleaned = df_cleaned.drop_duplicates().reset_index(drop=True)
        print(f"Dataset shape after dropping duplicates: {df_cleaned.shape}")
        
    # Standardize string categories (e.g. Antivirus_Status casing)
    df_cleaned['Antivirus_Status'] = df_cleaned['Antivirus_Status'].astype(str).str.capitalize()
    # Normalize valid categories
    valid_av = {'Active': 'Active', 'Outdated': 'Outdated', 'Disabled': 'Disabled'}
    df_cleaned['Antivirus_Status'] = df_cleaned['Antivirus_Status'].map(lambda x: valid_av.get(x, 'Outdated'))
    
    # Missing Value Handling
    # Numeric missing values: impute with median
    num_missing = ['Average_Daily_Traffic_MB', 'Firmware_Age_Months']
    for col in num_missing:
        median_val = df_cleaned[col].median()
        df_cleaned[col] = df_cleaned[col].fillna(median_val)
        
    # Categorical missing values: impute with mode
    cat_missing = ['Patch_Status']
    for col in cat_missing:
        mode_val = df_cleaned[col].mode()[0]
        df_cleaned[col] = df_cleaned[col].fillna(mode_val)
        
    print("Missing values after initial cleaning:")
    print(df_cleaned.isnull().sum()[df_cleaned.isnull().sum() > 0])
    
    # 3. Feature Engineering
    print("\n--- Feature Engineering ---")
    # A. Vulnerability to Firmware Ratio
    df_cleaned['Vulnerability_Firmware_Ratio'] = np.round(
        df_cleaned['Vulnerability_Count'] / (df_cleaned['Firmware_Age_Months'] + 1), 3
    )
    # B. Attack Surface Index (Composite of Open Ports and Failed Logins)
    df_cleaned['Attack_Surface_Index'] = np.round(
        (df_cleaned['Open_Ports_Count'] * 0.4) + (df_cleaned['Failed_Login_Attempts'] * 0.6), 2
    )
    # C. Compliance Posture Score (10 is best, decreases with unpatched/disabled protections)
    comp_score = 10.0
    comp_score = comp_score - (df_cleaned['Security_Updates_Pending'] * 0.5)
    comp_score = comp_score - (df_cleaned['Encryption_Enabled'] == 'No') * 2.5
    comp_score = comp_score - (df_cleaned['Antivirus_Status'] == 'Disabled') * 3.5
    comp_score = comp_score - (df_cleaned['Antivirus_Status'] == 'Outdated') * 1.5
    df_cleaned['Compliance_Posture_Score'] = np.clip(np.round(comp_score, 2), 0.0, 10.0)
    
    # Save Processed Dataset
    os.makedirs("data/processed", exist_ok=True)
    processed_path = "data/processed/device_risk_processed.csv"
    df_cleaned.to_csv(processed_path, index=False)
    print(f"Saved processed dataset to: {processed_path}")
    
    # 4. Generate & Save Figures (EDA & Quality)
    os.makedirs("outputs/figures", exist_ok=True)
    
    # Figure 1: Risk Distribution
    plt.figure(figsize=(7, 5))
    palette = {'Low Risk': '#2ecc71', 'Medium Risk': '#f39c12', 'High Risk': '#e74c3c'}
    ax = sns.countplot(data=df_cleaned, x='Risk_Level', order=['Low Risk', 'Medium Risk', 'High Risk'], hue='Risk_Level', palette=palette, legend=False)
    plt.title("Distribution of Device Risk Levels (Target Variable)", fontsize=13, fontweight='bold', pad=12)
    plt.xlabel("Risk Category", fontsize=11)
    plt.ylabel("Number of Devices", fontsize=11)
    for p in ax.patches:
        ax.annotate(f"{int(p.get_height())} ({p.get_height()/len(df_cleaned)*100:.1f}%)",
                    (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', xytext=(0, 7), textcoords='offset points', fontsize=10, fontweight='bold')
    plt.tight_layout()
    plt.savefig("outputs/figures/01_risk_distribution.png", dpi=300)
    plt.close()
    
    # Figure 2: Missing Values in Raw Data
    plt.figure(figsize=(8, 4))
    raw_missing = df_raw.isnull().sum()
    raw_missing = raw_missing[raw_missing > 0].sort_values(ascending=False)
    if len(raw_missing) > 0:
        ax2 = sns.barplot(x=raw_missing.values, y=raw_missing.index, hue=raw_missing.index, palette='Blues_r', legend=False)
        plt.title("Missing Values Identified in Raw Dataset", fontsize=13, fontweight='bold', pad=12)
        plt.xlabel("Count of Missing Entries", fontsize=11)
        plt.ylabel("Attribute", fontsize=11)
        for p in ax2.patches:
            ax2.annotate(f"{int(p.get_width())} ({p.get_width()/len(df_raw)*100:.1f}%)",
                         (p.get_width(), p.get_y() + p.get_height() / 2.),
                         ha='left', va='center', xytext=(5, 0), textcoords='offset points', fontsize=10)
    plt.tight_layout()
    plt.savefig("outputs/figures/02_missing_values.png", dpi=300)
    plt.close()
    
    # Figure 3: Correlation Heatmap of Numeric Features
    plt.figure(figsize=(11, 8))
    numeric_cols = df_cleaned.select_dtypes(include=[np.number]).columns
    corr = df_cleaned[numeric_cols].corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    sns.heatmap(corr, mask=mask, annot=True, fmt=".2f", cmap='coolwarm', cbar_kws={'shrink': 0.8},
                linewidths=0.5, annot_kws={"size": 8})
    plt.title("Pearson Correlation Matrix of Device Security Features", fontsize=13, fontweight='bold', pad=12)
    plt.tight_layout()
    plt.savefig("outputs/figures/03_correlation_heatmap.png", dpi=300)
    plt.close()
    
    # Figure 4: Vulnerabilities by Risk Level (Boxplot)
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df_cleaned, x='Risk_Level', y='Vulnerability_Count', order=['Low Risk', 'Medium Risk', 'High Risk'], hue='Risk_Level', palette=palette, legend=False)
    plt.title("Vulnerability Count Across Device Risk Levels", fontsize=13, fontweight='bold', pad=12)
    plt.xlabel("Risk Category", fontsize=11)
    plt.ylabel("Unpatched CVE Vulnerabilities", fontsize=11)
    plt.tight_layout()
    plt.savefig("outputs/figures/04_vulnerabilities_by_risk.png", dpi=300)
    plt.close()
    
    # Figure 5: Antivirus Status vs Risk Level (Grouped bar chart)
    plt.figure(figsize=(8, 5))
    av_risk = pd.crosstab(df_cleaned['Antivirus_Status'], df_cleaned['Risk_Level'], normalize='index')[['Low Risk', 'Medium Risk', 'High Risk']] * 100
    av_risk.plot(kind='bar', stacked=True, color=['#2ecc71', '#f39c12', '#e74c3c'], figsize=(8, 5), edgecolor='white')
    plt.title("Risk Composition by Antivirus Protection Status", fontsize=13, fontweight='bold', pad=12)
    plt.xlabel("Endpoint Protection Status", fontsize=11)
    plt.ylabel("Proportion of Devices (%)", fontsize=11)
    plt.legend(title="Risk Level", frameon=True)
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig("outputs/figures/05_antivirus_vs_risk.png", dpi=300)
    plt.close()
    
    # Figure 6: Failed Login Attempts Distribution
    plt.figure(figsize=(8, 5))
    for r_level, col in [('Low Risk', '#2ecc71'), ('Medium Risk', '#f39c12'), ('High Risk', '#e74c3c')]:
        subset = df_cleaned[df_cleaned['Risk_Level'] == r_level]
        sns.kdeplot(subset['Failed_Login_Attempts'], label=r_level, color=col, fill=True, alpha=0.3, linewidth=2)
    plt.title("Distribution of Failed Login Attempts by Risk Category", fontsize=13, fontweight='bold', pad=12)
    plt.xlabel("Failed Login Attempts (Past 30 Days)", fontsize=11)
    plt.ylabel("Density", fontsize=11)
    plt.legend(title="Risk Category")
    plt.tight_layout()
    plt.savefig("outputs/figures/06_failed_logins_distribution.png", dpi=300)
    plt.close()
    
    # 5. ML Preprocessing Setup
    print("\n--- Model Preparation & Train/Test Split ---")
    
    # Define features to use
    feature_cols = [
        'Device_Type', 'Operating_System', 'Device_Age_Months', 'Firmware_Age_Months',
        'Failed_Login_Attempts', 'Open_Ports_Count', 'Vulnerability_Count',
        'Security_Updates_Pending', 'Encryption_Enabled', 'Antivirus_Status',
        'Suspicious_Activity_Flags', 'Average_Daily_Traffic_MB', 'Access_Frequency_Score',
        'Previous_Security_Incidents', 'Patch_Status',
        'Vulnerability_Firmware_Ratio', 'Attack_Surface_Index', 'Compliance_Posture_Score'
    ]
    
    categorical_features = ['Device_Type', 'Operating_System', 'Encryption_Enabled', 'Antivirus_Status', 'Patch_Status']
    numerical_features = [col for col in feature_cols if col not in categorical_features]
    
    X = df_cleaned[feature_cols]
    y = df_cleaned['Risk_Level']
    
    # Target Encoding
    label_encoder = LabelEncoder()
    # Ensure consistent order: 0: High Risk, 1: Low Risk, 2: Medium Risk or standard
    # Let's map explicitly:
    target_mapping = {'Low Risk': 0, 'Medium Risk': 1, 'High Risk': 2}
    y_encoded = y.map(target_mapping)
    class_names = ['Low Risk', 'Medium Risk', 'High Risk']
    
    # Train-test split (80/20 stratified)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=0.20, random_state=42, stratify=y_encoded
    )
    print(f"Training set: {X_train.shape[0]} samples, Testing set: {X_test.shape[0]} samples")
    
    # Create Preprocessing Transformers
    num_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])
    
    cat_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('ohe', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
    ])
    
    preprocessor = ColumnTransformer([
        ('num', num_pipeline, numerical_features),
        ('cat', cat_pipeline, categorical_features)
    ])
    
    # Fit preprocessor on train data to inspect transformed feature names
    preprocessor.fit(X_train)
    cat_ohe_names = list(preprocessor.named_transformers_['cat'].named_steps['ohe'].get_feature_names_out(categorical_features))
    transformed_feature_names = numerical_features + cat_ohe_names
    
    # Save standalone scaler/preprocessor
    os.makedirs("models", exist_ok=True)
    joblib.dump(preprocessor, "models/scaler.pkl")
    print(f"Fitted preprocessor saved to models/scaler.pkl ({len(transformed_feature_names)} transformed features)")
    
    # 6. Train and Evaluate Multiple Classification Algorithms
    print("\n--- Training Multiple Classifiers ---")
    
    models = {
        'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
        'Decision Tree': DecisionTreeClassifier(max_depth=6, random_state=42),
        'K-Nearest Neighbors': KNeighborsClassifier(n_neighbors=7),
        'Support Vector Machine': SVC(probability=True, kernel='rbf', C=1.0, random_state=42),
        'Random Forest': RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42),
        'Gradient Boosting': GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=4, random_state=42)
    }
    
    results = []
    trained_pipelines = {}
    y_test_bin = label_binarize(y_test, classes=[0, 1, 2])
    
    for name, clf in models.items():
        pipe = Pipeline([
            ('preprocessor', preprocessor),
            ('classifier', clf)
        ])
        
        pipe.fit(X_train, y_train)
        y_pred = pipe.predict(X_test)
        
        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred, average='weighted')
        rec = recall_score(y_test, y_pred, average='weighted')
        f1 = f1_score(y_test, y_pred, average='weighted')
        
        # Multiclass ROC-AUC (OvR)
        try:
            y_proba = pipe.predict_proba(X_test)
            roc_auc = roc_auc_score(y_test_bin, y_proba, multi_class='ovr', average='weighted')
        except Exception:
            roc_auc = np.nan
            
        results.append({
            'Model': name,
            'Accuracy': round(acc, 4),
            'Precision': round(prec, 4),
            'Recall': round(rec, 4),
            'F1 Score': round(f1, 4),
            'ROC_AUC': round(roc_auc, 4)
        })
        trained_pipelines[name] = pipe
        print(f"✓ {name:24s} | Acc: {acc:.4f} | Prec: {prec:.4f} | Rec: {rec:.4f} | F1: {f1:.4f} | AUC: {roc_auc:.4f}")
        
    df_results = pd.DataFrame(results)
    df_results = df_results.sort_values(by='F1 Score', ascending=False).reset_index(drop=True)
    
    # Save Model Results CSV
    os.makedirs("outputs", exist_ok=True)
    df_results.to_csv("outputs/model_results.csv", index=False)
    print("\nModel Comparison Table:")
    print(df_results.to_string(index=False))
    
    # 7. Model Comparison Chart
    plt.figure(figsize=(10, 5))
    df_melt = pd.melt(df_results, id_vars=['Model'], value_vars=['Accuracy', 'Precision', 'Recall', 'F1 Score'],
                      var_name='Metric', value_name='Score')
    sns.barplot(data=df_melt, x='Model', y='Score', hue='Metric', palette='viridis')
    plt.title("Comparative Performance Across ML Classifiers", fontsize=13, fontweight='bold', pad=12)
    plt.ylabel("Score (0.0 to 1.0)", fontsize=11)
    plt.xlabel("Algorithm", fontsize=11)
    plt.ylim(0.65, 1.02)
    plt.xticks(rotation=20, ha='right')
    plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig("outputs/figures/07_model_comparison_bar.png", dpi=300)
    plt.close()
    
    # 8. Systematic Hyperparameter Tuning
    print("\n--- Systematic Hyperparameter Tuning via GridSearchCV ---")
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    
    # Tune Logistic Regression
    print("Tuning Logistic Regression...")
    lr_pipe = Pipeline([
        ('preprocessor', preprocessor),
        ('classifier', LogisticRegression(max_iter=1000, random_state=42))
    ])
    lr_grid = {
        'classifier__C': [0.1, 1.0, 5.0, 10.0],
        'classifier__solver': ['lbfgs']
    }
    lr_search = GridSearchCV(lr_pipe, lr_grid, cv=cv, scoring='f1_weighted', n_jobs=-1)
    lr_search.fit(X_train, y_train)
    lr_cv_score = lr_search.best_score_
    print(f"Logistic Regression Tuned CV F1: {lr_cv_score:.4f} (Best C: {lr_search.best_params_['classifier__C']})")
    
    # Tune Gradient Boosting
    print("Tuning Gradient Boosting Classifier...")
    gb_pipe = Pipeline([
        ('preprocessor', preprocessor),
        ('classifier', GradientBoostingClassifier(random_state=42))
    ])
    gb_grid = {
        'classifier__n_estimators': [100, 150],
        'classifier__learning_rate': [0.05, 0.1],
        'classifier__max_depth': [3, 4]
    }
    gb_search = GridSearchCV(gb_pipe, gb_grid, cv=cv, scoring='f1_weighted', n_jobs=-1)
    gb_search.fit(X_train, y_train)
    gb_cv_score = gb_search.best_score_
    print(f"Gradient Boosting Tuned CV F1: {gb_cv_score:.4f} (Best Params: {gb_search.best_params_})")
    
    # Select Champion Model based on 5-fold CV Weighted F1
    if lr_cv_score >= gb_cv_score:
        champion_name = "Logistic Regression (Tuned)"
        best_pipe = lr_search.best_estimator_
        best_params = lr_search.best_params_
        best_cv_score = lr_cv_score
        selected_model_type = "linear"
    else:
        champion_name = "Gradient Boosting (Tuned)"
        best_pipe = gb_search.best_estimator_
        best_params = gb_search.best_params_
        best_cv_score = gb_cv_score
        selected_model_type = "ensemble"
        
    print(f"\n★ CHAMPION MODEL SELECTED: {champion_name}")
    print(f"Validation Score (5-fold CV F1): {best_cv_score:.4f}")
    
    # Evaluate Final Tuned Model on Test Set
    y_test_pred = best_pipe.predict(X_test)
    y_test_proba = best_pipe.predict_proba(X_test)
    
    final_acc = accuracy_score(y_test, y_test_pred)
    final_prec = precision_score(y_test, y_test_pred, average='weighted')
    final_rec = recall_score(y_test, y_test_pred, average='weighted')
    final_f1 = f1_score(y_test, y_test_pred, average='weighted')
    final_auc = roc_auc_score(y_test_bin, y_test_proba, multi_class='ovr', average='weighted')
    
    print("\n--- Final Champion Model Test Set Evaluation ---")
    print(f"Test Accuracy:  {final_acc:.4f}")
    print(f"Test Precision: {final_prec:.4f}")
    print(f"Test Recall:    {final_rec:.4f}")
    print(f"Test F1 Score:  {final_f1:.4f}")
    print(f"Test ROC-AUC:   {final_auc:.4f}")
    
    print("\nClassification Report on Test Set:")
    print(classification_report(y_test, y_test_pred, target_names=class_names))
    
    # Figure 8: Confusion Matrix of Best Model
    plt.figure(figsize=(7, 6))
    cm = confusion_matrix(y_test, y_test_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=class_names, yticklabels=class_names,
                cbar_kws={'label': 'Number of Devices'})
    plt.title(f"Confusion Matrix: {champion_name}", fontsize=13, fontweight='bold', pad=12)
    plt.xlabel("Predicted Risk Level", fontsize=11)
    plt.ylabel("Actual True Risk Level", fontsize=11)
    plt.tight_layout()
    plt.savefig("outputs/figures/08_best_model_confusion_matrix.png", dpi=300)
    plt.close()
    
    # Figure 10: Multiclass One-vs-Rest ROC Curves
    plt.figure(figsize=(8, 6))
    colors = ['#2ecc71', '#f39c12', '#e74c3c']
    for i, (c_name, color) in enumerate(zip(class_names, colors)):
        fpr, tpr, _ = roc_curve(y_test_bin[:, i], y_test_proba[:, i])
        roc_auc_val = auc(fpr, tpr)
        plt.plot(fpr, tpr, color=color, lw=2.2, label=f'{c_name} (AUC = {roc_auc_val:.3f})')
        
    plt.plot([0, 1], [0, 1], 'k--', lw=1.5, label='Random Guess')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate (1 - Specificity)', fontsize=11)
    plt.ylabel('True Positive Rate (Sensitivity / Recall)', fontsize=11)
    plt.title(f'Multiclass ROC Curves (One-vs-Rest) - {champion_name}', fontsize=13, fontweight='bold', pad=12)
    plt.legend(loc="lower right", frameon=True)
    plt.tight_layout()
    plt.savefig("outputs/figures/10_multiclass_roc_curves.png", dpi=300)
    plt.close()
    
    # 9. Feature Importance Analysis
    print("\n--- Feature Importance Extraction ---")
    clf_step = best_pipe.named_steps['classifier']
    
    # Calculate feature importances
    if hasattr(clf_step, 'feature_importances_'):
        raw_weights = clf_step.feature_importances_
    elif hasattr(clf_step, 'coef_'):
        # For multiclass Logistic Regression: average absolute coefficient across all 3 classes
        raw_weights = np.mean(np.abs(clf_step.coef_), axis=0)
        # normalize to sum to 1.0
        raw_weights = raw_weights / np.sum(raw_weights)
    else:
        raw_weights = np.ones(len(transformed_feature_names)) / len(transformed_feature_names)
        
    df_feat_imp = pd.DataFrame({
        'Transformed_Feature': transformed_feature_names,
        'Raw_Weight': raw_weights
    })
    
    # Map back to base feature names
    base_feature_map = {}
    for feat in transformed_feature_names:
        matched = False
        for base in feature_cols:
            if feat.startswith(base):
                base_feature_map[feat] = base
                matched = True
                break
        if not matched:
            base_feature_map[feat] = feat
            
    df_feat_imp['Base_Feature'] = df_feat_imp['Transformed_Feature'].map(base_feature_map)
    df_base_imp = df_feat_imp.groupby('Base_Feature')['Raw_Weight'].sum().reset_index()
    df_base_imp.columns = ['Feature', 'Importance']
    df_base_imp['Importance'] = df_base_imp['Importance'].round(4)
    df_base_imp = df_base_imp.sort_values(by='Importance', ascending=False).reset_index(drop=True)
    
    df_base_imp.to_csv("outputs/feature_importance.csv", index=False)
    print("Top Security Risk Factors:")
    print(df_base_imp.head(10).to_string(index=False))
    
    # Figure 9: Feature Importance Plot
    plt.figure(figsize=(9, 6))
    top_10 = df_base_imp.head(10)
    sns.barplot(data=top_10, x='Importance', y='Feature', hue='Feature', palette='mako', legend=False)
    plt.title(f"Top 10 Security Risk Factors Associated with Prediction ({champion_name})", fontsize=12, fontweight='bold', pad=12)
    plt.xlabel("Normalized Importance Weight", fontsize=11)
    plt.ylabel("Device Security Factor", fontsize=11)
    for p in plt.gca().patches:
        plt.gca().annotate(f"{p.get_width():.3f}",
                           (p.get_width(), p.get_y() + p.get_height() / 2.),
                           ha='left', va='center', xytext=(5, 0), textcoords='offset points', fontsize=9)
    plt.tight_layout()
    plt.savefig("outputs/figures/09_feature_importance.png", dpi=300)
    plt.close()
        
    # Figure 11: Machine Learning Workflow Architecture Diagram
    plt.figure(figsize=(10, 8))
    plt.axis('off')
    workflow_steps = [
        "1. Raw Device Security Data Ingestion\n(3,012 device records across 17 attributes)",
        "2. Data Cleaning & Integrity Auditing\n(Imputation, deduplication, casing standardization)",
        "3. Exploratory Data Analysis (EDA)\n(Univariate, bivariate, correlation & class balance)",
        "4. Feature Engineering & Preprocessing Pipeline\n(Compliance Score, Attack Surface Index, StandardScaler, OneHotEncoder)",
        "5. Stratified Train-Test Splitting\n(80% Training: 2,400 samples | 20% Testing: 600 samples)",
        "6. Multi-Model Benchmark & Cross-Validation\n(Logistic Regression, Decision Tree, KNN, SVM, Random Forest, Gradient Boosting)",
        "7. Hyperparameter Tuning & Optimal Model Selection\n(GridSearchCV 5-fold Stratified CV for optimal generalization)",
        "8. Production Serialization & Artifact Generation\n(best_model.pkl, scaler.pkl, metadata, figures, metrics CSV)",
        "9. Interactive Streamlit Application Deployment\n(Real-time risk scoring, device health recommendations, visual analytics)"
    ]
    
    y_pos = np.linspace(0.92, 0.08, len(workflow_steps))
    for i, (text, y_p) in enumerate(zip(workflow_steps, y_pos)):
        box_color = '#1f77b4' if i in [0, 4, 8] else ('#2ca02c' if i in [6, 7] else '#ff7f0e')
        plt.text(0.5, y_p, text, ha='center', va='center', fontsize=9.5, fontweight='bold', color='white',
                 bbox=dict(boxstyle='round,pad=0.6', facecolor=box_color, edgecolor='none', alpha=0.9))
        if i < len(workflow_steps) - 1:
            next_y = y_pos[i+1]
            plt.annotate('', xy=(0.5, next_y + 0.04), xytext=(0.5, y_p - 0.04),
                         arrowprops=dict(arrowstyle='->', lw=2, color='#555555'))
                         
    plt.title("Machine Learning Architecture & Workflow Pipeline", fontsize=14, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig("outputs/figures/11_ml_architecture_workflow.png", dpi=300)
    plt.close()
    
    # 10. Save Final Model Artifacts & Metadata
    print("\n--- Saving Production Artifacts ---")
    joblib.dump(best_pipe, "models/best_model.pkl")
    print("Saved pipeline: models/best_model.pkl")
    
    metadata = {
        'model_name': champion_name,
        'best_hyperparameters': best_params,
        'cross_val_f1': round(best_cv_score, 4),
        'test_accuracy': round(final_acc, 4),
        'test_precision': round(final_prec, 4),
        'test_recall': round(final_rec, 4),
        'test_f1': round(final_f1, 4),
        'test_roc_auc': round(final_auc, 4),
        'target_mapping': target_mapping,
        'inv_target_mapping': {v: k for k, v in target_mapping.items()},
        'class_names': class_names,
        'feature_cols': feature_cols,
        'numerical_features': numerical_features,
        'categorical_features': categorical_features,
        'transformed_feature_names': transformed_feature_names,
        'n_train': len(X_train),
        'n_test': len(X_test),
        'total_samples': len(df_cleaned)
    }
    joblib.dump(metadata, "models/model_metadata.pkl")
    print("Saved metadata: models/model_metadata.pkl")
    
    # 11. Run Verification Inferences
    print("\n--- Model Verification Examples ---")
    sample_low = pd.DataFrame([{
        'Device_Type': 'Laptop', 'Operating_System': 'Windows 11', 'Device_Age_Months': 8,
        'Firmware_Age_Months': 2, 'Failed_Login_Attempts': 1, 'Open_Ports_Count': 2,
        'Vulnerability_Count': 0, 'Security_Updates_Pending': 0, 'Encryption_Enabled': 'Yes',
        'Antivirus_Status': 'Active', 'Suspicious_Activity_Flags': 0, 'Average_Daily_Traffic_MB': 420.0,
        'Access_Frequency_Score': 4.5, 'Previous_Security_Incidents': 0, 'Patch_Status': 'Fully Patched',
        'Vulnerability_Firmware_Ratio': 0.0, 'Attack_Surface_Index': 1.4, 'Compliance_Posture_Score': 10.0
    }])
    
    sample_high = pd.DataFrame([{
        'Device_Type': 'IoT_Gateway', 'Operating_System': 'Embedded Linux', 'Device_Age_Months': 58,
        'Firmware_Age_Months': 28, 'Failed_Login_Attempts': 24, 'Open_Ports_Count': 14,
        'Vulnerability_Count': 12, 'Security_Updates_Pending': 9, 'Encryption_Enabled': 'No',
        'Antivirus_Status': 'Disabled', 'Suspicious_Activity_Flags': 5, 'Average_Daily_Traffic_MB': 3800.0,
        'Access_Frequency_Score': 8.8, 'Previous_Security_Incidents': 3, 'Patch_Status': 'Outdated',
        'Vulnerability_Firmware_Ratio': 0.414, 'Attack_Surface_Index': 20.0, 'Compliance_Posture_Score': 0.0
    }])
    
    pred_low = best_pipe.predict(sample_low)[0]
    prob_low = best_pipe.predict_proba(sample_low)[0]
    pred_high = best_pipe.predict(sample_high)[0]
    prob_high = best_pipe.predict_proba(sample_high)[0]
    
    print(f"Sample Clean Device  -> Predicted: {class_names[pred_low]} (Probabilities: {prob_low.round(3)})")
    print(f"Sample Risky Device  -> Predicted: {class_names[pred_high]} (Probabilities: {prob_high.round(3)})")
    print("\n✓ Pipeline execution, model training, evaluation, figures, and serialization complete!")

if __name__ == "__main__":
    run_pipeline()
