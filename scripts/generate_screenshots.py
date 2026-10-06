"""
Generate high-fidelity UI visual representations of the Streamlit Application
for inclusion in documentation and repository assets.
"""
import os
import matplotlib.pyplot as plt
import numpy as np

os.makedirs("assets/screenshots", exist_ok=True)

# 1. Dashboard Home Screenshot Representation
fig, ax = plt.subplots(figsize=(12, 7.5), facecolor='#f8fafc')
ax.axis('off')

# Title and header
ax.text(0.04, 0.93, "[SYSTEM] DEVICE RISK ANALYSIS DASHBOARD", fontsize=18, fontweight='bold', color='#0f172a')
ax.text(0.04, 0.88, "Machine Learning Based Device Security Risk Prediction | ITM Skills University", fontsize=11, color='#64748b')

# KPI Cards
kpis = [
    ("TOTAL FLEET", "3,000", "Endpoints", "#e0f2fe", "#0369a1"),
    ("LOW RISK", "964", "32.1% of total", "#dcfce7", "#15803d"),
    ("MEDIUM RISK", "1,264", "42.1% of total", "#fef3c7", "#b45309"),
    ("HIGH RISK", "772", "25.7% of total", "#fee2e2", "#b91c1c"),
    ("CHAMPION ACC.", "89.00%", "Logistic Reg. Tuned", "#ede9fe", "#6d28d9")
]

x_starts = np.linspace(0.04, 0.80, 5)
for (title, val, sub, bg, fg), x in zip(kpis, x_starts):
    rect = plt.Rectangle((x, 0.65), 0.16, 0.18, facecolor='white', edgecolor='#e2e8f0', linewidth=1.2, transform=ax.transAxes, zorder=2)
    ax.add_patch(rect)
    ax.text(x + 0.08, 0.79, title, fontsize=8, fontweight='bold', color='#64748b', ha='center', va='center')
    ax.text(x + 0.08, 0.73, val, fontsize=16, fontweight='bold', color=fg, ha='center', va='center')
    ax.text(x + 0.08, 0.68, sub, fontsize=7.5, color='#475569', ha='center', va='center')

# Architecture Workflow section
rect_wf = plt.Rectangle((0.04, 0.08), 0.92, 0.52, facecolor='white', edgecolor='#e2e8f0', linewidth=1.2, transform=ax.transAxes, zorder=2)
ax.add_patch(rect_wf)
ax.text(0.07, 0.54, "Machine Learning Architecture Workflow", fontsize=13, fontweight='bold', color='#0f172a')

# Steps inside diagram
steps = [
    "Raw Telemetry Ingestion (3,012 assets across 17 attributes)",
    "Data Cleaning & Imputation (Median/Mode imputation, deduplication)",
    "Feature Engineering (Attack Surface Index, Compliance Posture Score)",
    "Stratified 80/20 Train-Test Splitting (2,400 train / 600 test)",
    "Multi-Algorithm Benchmark (Logistic Regression, Decision Tree, KNN, SVM, Random Forest, Gradient Boosting)",
    "Hyperparameter Tuning (5-fold Stratified GridSearchCV optimization)",
    "Champion Model Serialization (best_model.pkl & metadata)",
    "Interactive Streamlit Inference & Executive Reporting"
]
for i, step in enumerate(steps):
    step_y = 0.47 - (i * 0.05)
    color = '#2563eb' if i in [0, 4, 7] else '#0d9488'
    ax.text(0.08, step_y, f"Step {i+1}:", fontsize=9, fontweight='bold', color=color)
    ax.text(0.16, step_y, step, fontsize=9, color='#334155')

plt.tight_layout()
plt.savefig("assets/screenshots/01_dashboard_home.png", dpi=200)
plt.close()

# 2. Risk Prediction Screenshot Representation
fig, ax = plt.subplots(figsize=(12, 7.5), facecolor='#f8fafc')
ax.axis('off')
ax.text(0.04, 0.93, "Interactive Device Risk Prediction", fontsize=18, fontweight='bold', color='#0f172a')
ax.text(0.04, 0.88, "Evaluate endpoint risk against trained champion machine learning pipeline", fontsize=11, color='#64748b')

# Form container
rect_form = plt.Rectangle((0.04, 0.48), 0.92, 0.36, facecolor='white', edgecolor='#cbd5e1', linewidth=1.2, transform=ax.transAxes)
ax.add_patch(rect_form)
ax.text(0.06, 0.79, "Hardware & System Parameters: Laptop | Windows 11 | Age: 8 Mo | Firmware Age: 2 Mo", fontsize=9.5, color='#334155')
ax.text(0.06, 0.72, "Network & Exposure: Failed Logins: 1 | Open Ports: 2 | Daily Traffic: 420 MB | Access Score: 4.5", fontsize=9.5, color='#334155')
ax.text(0.06, 0.65, "Defense Posture: CVEs: 0 | Updates Pending: 0 | Encryption: Yes | Antivirus: Active | Patch: Fully Patched", fontsize=9.5, color='#334155')
ax.text(0.06, 0.55, "Engineered Metrics: Attack Surface Index = 1.40 | Compliance Posture Score = 10.0 / 10.0", fontsize=9.5, fontweight='bold', color='#2563eb')

# Prediction Result Card
rect_res = plt.Rectangle((0.04, 0.12), 0.92, 0.30, facecolor='#f0fdf4', edgecolor='#86efac', linewidth=2, transform=ax.transAxes)
ax.add_patch(rect_res)
ax.text(0.07, 0.35, "PREDICTION OUTPUT:", fontsize=11, fontweight='bold', color='#14532d')
ax.text(0.07, 0.25, "[VERIFIED] LOW RISK", fontsize=22, fontweight='bold', color='#15803d')
ax.text(0.07, 0.17, "Probabilities: Low Risk: 99.8% | Medium Risk: 0.2% | High Risk: 0.0%  --  Status: Healthy (Routine Monitoring)", fontsize=10, color='#166534')

plt.tight_layout()
plt.savefig("assets/screenshots/02_risk_prediction.png", dpi=200)
plt.close()

# 3. Dataset Insights Screenshot Representation
fig, ax = plt.subplots(figsize=(12, 7.5), facecolor='#f8fafc')
ax.axis('off')
ax.text(0.04, 0.93, "Dataset Exploratory Analysis & Telemetry Insights", fontsize=18, fontweight='bold', color='#0f172a')
ax.text(0.04, 0.88, "Telemetry distribution across 3,000 enterprise assets and 17 attributes", fontsize=11, color='#64748b')

rect_box1 = plt.Rectangle((0.04, 0.15), 0.44, 0.68, facecolor='white', edgecolor='#e2e8f0', linewidth=1.2, transform=ax.transAxes)
rect_box2 = plt.Rectangle((0.52, 0.15), 0.44, 0.68, facecolor='white', edgecolor='#e2e8f0', linewidth=1.2, transform=ax.transAxes)
ax.add_patch(rect_box1)
ax.add_patch(rect_box2)

ax.text(0.07, 0.77, "Target Variable Distribution (Risk_Level)", fontsize=11, fontweight='bold', color='#0f172a')
ax.text(0.07, 0.68, "- Medium Risk: 1,264 devices (42.1%)", fontsize=10, color='#d97706')
ax.text(0.07, 0.60, "- Low Risk:    964 devices (32.1%)", fontsize=10, color='#16a34a')
ax.text(0.07, 0.52, "- High Risk:   772 devices (25.7%)", fontsize=10, color='#dc2626')
ax.text(0.07, 0.40, "Stratification: Maintained in train/test split.", fontsize=9, color='#64748b')

ax.text(0.55, 0.77, "Observed Vulnerability Discrepancies", fontsize=11, fontweight='bold', color='#0f172a')
ax.text(0.55, 0.68, "High Risk:   Median ~12 CVEs (Active exposure)", fontsize=10, color='#dc2626')
ax.text(0.55, 0.60, "Medium Risk: Median ~5 CVEs (Partial patches)", fontsize=10, color='#d97706')
ax.text(0.55, 0.52, "Low Risk:    Median ~1 CVE (Fully mitigated)", fontsize=10, color='#16a34a')
ax.text(0.55, 0.40, "Antivirus disabled devices: >75% in High Risk.", fontsize=9, color='#64748b')

plt.tight_layout()
plt.savefig("assets/screenshots/03_dataset_insights.png", dpi=200)
plt.close()

# 4. Model Performance Screenshot Representation
fig, ax = plt.subplots(figsize=(12, 7.5), facecolor='#f8fafc')
ax.axis('off')
ax.text(0.04, 0.93, "Machine Learning Model Benchmark & Evaluation", fontsize=18, fontweight='bold', color='#0f172a')
ax.text(0.04, 0.88, "Comprehensive multi-class performance comparison across 6 classification algorithms", fontsize=11, color='#64748b')

rect_tbl = plt.Rectangle((0.04, 0.25), 0.92, 0.58, facecolor='white', edgecolor='#e2e8f0', linewidth=1.2, transform=ax.transAxes)
ax.add_patch(rect_tbl)

headers = ["Algorithm", "Accuracy", "Precision", "Recall", "F1-Score", "ROC-AUC", "Status"]
rows = [
    ["Logistic Regression (Tuned)", "0.8900", "0.8900", "0.8900", "0.8898", "0.9756", "CHAMPION"],
    ["Support Vector Machine", "0.8800", "0.8802", "0.8800", "0.8801", "0.9710", "Benchmark"],
    ["Gradient Boosting (Tuned)", "0.8500", "0.8521", "0.8500", "0.8502", "0.9580", "Ensemble"],
    ["Random Forest Classifier", "0.8017", "0.8101", "0.8017", "0.8021", "0.9265", "Bagging"],
    ["K-Nearest Neighbors", "0.7883", "0.7908", "0.7883", "0.7868", "0.9151", "Distance"],
    ["Decision Tree Classifier", "0.7167", "0.7327", "0.7167", "0.7178", "0.8466", "Rule-based"]
]

col_x = [0.06, 0.32, 0.42, 0.52, 0.62, 0.72, 0.84]
for j, h in enumerate(headers):
    ax.text(col_x[j], 0.78, h, fontsize=10, fontweight='bold', color='#0f172a')

for i, row in enumerate(rows):
    y = 0.71 - (i * 0.065)
    ax.plot([0.05, 0.95], [y - 0.015, y - 0.015], color='#e2e8f0', lw=0.8)
    for j, val in enumerate(row):
        col_c = '#15803d' if i == 0 else '#334155'
        f_weight = 'bold' if (i == 0 or j == 0) else 'normal'
        ax.text(col_x[j], y, val, fontsize=9.5, color=col_c, fontweight=f_weight)

ax.text(0.05, 0.15, "Evaluation performed on unseen test set (600 instances) using multi-class weighted averaging.", fontsize=9.5, style='italic', color='#64748b')

plt.tight_layout()
plt.savefig("assets/screenshots/04_model_performance.png", dpi=200)
plt.close()

# 5. Security Insights Screenshot Representation
fig, ax = plt.subplots(figsize=(12, 7.5), facecolor='#f8fafc')
ax.axis('off')
ax.text(0.04, 0.93, "Security Factor Importance & Vulnerability Drivers", fontsize=18, fontweight='bold', color='#0f172a')
ax.text(0.04, 0.88, "Model interpretability weights identifying factors associated with elevated device risk", fontsize=11, color='#64748b')

rect_imp = plt.Rectangle((0.04, 0.15), 0.92, 0.68, facecolor='white', edgecolor='#e2e8f0', linewidth=1.2, transform=ax.transAxes)
ax.add_patch(rect_imp)

top_drivers = [
    ("Operating System Posture", "0.1703 (17.0%)", "Kernel architecture & security update channel compliance"),
    ("Patch Compliance Status", "0.1137 (11.4%)", "Latency in applying vendor-released hotfixes"),
    ("Vulnerability Count (CVEs)", "0.0960 (9.6%)", "Active unmitigated vulnerabilities detected in automated scans"),
    ("Suspicious Network Activity", "0.0756 (7.6%)", "Behavioral anomalies flagged by intrusion detection sensors"),
    ("Compliance Posture Score", "0.0694 (6.9%)", "Engineered composite score factoring defense configurations"),
    ("Antivirus / EDR Status", "0.0689 (6.9%)", "Active vs disabled endpoint signature definitions"),
    ("Device Hardware Class", "0.0675 (6.8%)", "Workstation vs unmanaged IoT Gateway baseline exposure"),
    ("Past Security Incidents", "0.0673 (6.7%)", "Historical frequency of endpoint quarantine events")
]

for i, (feat, w, desc) in enumerate(top_drivers):
    y = 0.76 - (i * 0.07)
    ax.text(0.07, y, f"{i+1}. {feat}", fontsize=10.5, fontweight='bold', color='#0f172a')
    ax.text(0.38, y, w, fontsize=10, fontweight='bold', color='#2563eb')
    ax.text(0.53, y, desc, fontsize=9.5, color='#475569')

plt.tight_layout()
plt.savefig("assets/screenshots/05_security_insights.png", dpi=200)
plt.close()

print("All 5 UI screenshots generated cleanly in assets/screenshots/")

print("Generated UI screenshots successfully in assets/screenshots/")
