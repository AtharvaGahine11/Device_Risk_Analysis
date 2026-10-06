<div align="center">

🛡️ DEVICE RISK ANALYSIS
🔐 Machine Learning Powered Cybersecurity Risk Classification
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=22&pause=900&color=00C2FF&center=true&vCenter=true&width=800&lines=Detect+Device+Security+Risk;Low+%7C+Medium+%7C+High;Compare+6+Machine+Learning+Models;Tune+%26+Evaluate+the+Champion;Deploy+with+Streamlit" alt="Typing SVG" />

<p>
<img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/Scikit--Learn-1.4%2B-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white">
<img src="https://img.shields.io/badge/Streamlit-1.35%2B-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
<img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge">
</p>

Case Study No. 86 • Machine Learning • B.Tech CSE • ITM Skills University
👨‍💻 Developed by Atharva Gahine
</div>


### 🎓 Academic Information
* **Student Name:** Atharva Gahine
* **Degree Program:** B.Tech Computer Science & Engineering
* **Semester:** Semester V | Academic Batch: 2024–2028
* **Institution:** School of Future Tech, ITM SKILLS UNIVERSITY
* **Course:** Machine Learning (Case Study No. 86)

---

## 📋 Problem Statement

> **"An organization wants to analyze device-related information and identify patterns associated with elevated security concerns."**

Modern enterprises oversee heterogeneous device fleets—ranging from employee workstations and cloud servers to mobile devices and Internet of Things (IoT) gateways. Security teams face immense alert fatigue and struggle to objectively prioritize patching. Traditional rule-based thresholds fail to capture multi-factor trade-offs across vulnerability accumulation, open port exposures, and endpoint protection statuses.

This project delivers an automated Machine Learning pipeline that classifies devices into three actionable risk categories:
* **Low Risk:** Compliant, fully patched endpoints with active protections.
* **Medium Risk:** Devices with moderate patch latency or minor configuration exposures.
* **High Risk:** Acute vulnerability density, unencrypted storage, or active intrusion flags requiring immediate quarantine.

---

## 🏗️ Machine Learning Architecture Workflow

```
Raw Device Telemetry (3,012 assets, 17 attributes)
       │
       ▼
Data Cleaning & Quality Audit (Deduplication, median/mode imputation, casing normalization)
       │
       ▼
Exploratory Data Analysis (Univariate, bivariate distributions, Pearson correlation heatmap)
       │
       ▼
Feature Engineering (Attack Surface Index, Compliance Score, Vulnerability/Firmware Ratio)
       │
       ▼
Stratified Train-Test Split (80% Train: 2,400 samples | 20% Test: 600 samples)
       │
       ▼
Multi-Model Benchmark (Logistic Regression, Decision Tree, KNN, SVM, Random Forest, Gradient Boosting)
       │
       ▼
Hyperparameter Tuning (5-fold Stratified GridSearchCV optimization)
       │
       ▼
Champion Model Selection (Tuned Logistic Regression: 89.00% Accuracy, 0.8898 F1, 0.9756 ROC-AUC)
       │
       ▼
Production Serialization (models/best_model.pkl, scaler.pkl, model_metadata.pkl)
       │
       ▼
Interactive Streamlit Web Dashboard (Real-time single-endpoint scoring, fleet analytics, recommendations)
```

---

## 📊 Empirical Model Results

All six algorithms were trained on the identical 80% training split using a leak-free `ColumnTransformer` pipeline and evaluated on the held-out 20% test set (600 devices) using multi-class weighted metrics:

| Model | Accuracy | Weighted Precision | Weighted Recall | Weighted F1-Score | Multi-Class ROC-AUC | Status |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Logistic Regression (Tuned)** | **0.8900** | **0.8900** | **0.8900** | **0.8898** | **0.9756** | 🏆 **Champion** |
| **Support Vector Machine (SVM)** | 0.8800 | 0.8802 | 0.8800 | 0.8801 | 0.9710 | Baseline Benchmark |
| **Gradient Boosting (Tuned)** | 0.8500 | 0.8521 | 0.8500 | 0.8502 | 0.9580 | Tuned Ensemble |
| **Random Forest Classifier** | 0.8017 | 0.8101 | 0.8017 | 0.8021 | 0.9265 | Bagging Ensemble |
| **K-Nearest Neighbors (KNN)** | 0.7883 | 0.7908 | 0.7883 | 0.7868 | 0.9151 | Distance Metric |
| **Decision Tree Classifier** | 0.7167 | 0.7327 | 0.7167 | 0.7178 | 0.8466 | Single Tree |

---

## 🔍 Key Security Risk Factors

Normalized feature importance weights extracted from the champion model:

1. **Operating System Architecture (17.0%):** Kernel architecture and update release channel.
2. **Patch Compliance Status (11.4%):** Latency in applying vendor-released hotfixes.
3. **Vulnerability Count (9.6%):** Active unmitigated software CVEs detected in scans.
4. **Suspicious Network Activity (7.6%):** Behavioral alerts flagged by network intrusion sensors.
5. **Compliance Posture Score (6.9%):** Engineered composite index of defensive settings.
6. **Antivirus / EDR Protection (6.9%):** Active vs disabled endpoint protection state.
7. **Hardware Class (6.8%):** Managed workstation vs unmanaged IoT field gateway baseline risk.
8. **Previous Security Incidents (6.7%):** Historical frequency of endpoint quarantine events.
9. **Attack Surface Index (5.7%):** Combined listening ports and brute-force login frequency.
10. **Failed Login Attempts (4.9%):** Authentication pressure in the past 30 days.

---

## 📁 Repository Structure

```
device-risk-analysis/
│
├── data/
│   ├── raw/
│   │   └── device_risk_raw.csv                # Raw telemetry (3,012 records, 17 columns)
│   └── processed/
│       └── device_risk_processed.csv          # Cleaned dataset (3,000 unique records)
│
├── notebooks/
│   └── Device_Risk_Analysis.ipynb             # Comprehensive 22-section Jupyter Notebook
│
├── app/
│   └── app.py                                 # Interactive Streamlit Web Application
│
├── models/
│   ├── best_model.pkl                         # Serialized Champion Pipeline (Preprocessor + Classifier)
│   ├── scaler.pkl                             # Standalone fitted ColumnTransformer
│   └── model_metadata.pkl                     # Metrics, hyperparameters, and feature specifications
│
├── assets/
│   ├── logo.png                               # Cybersecurity project emblem
│   └── screenshots/                           # UI visualization mockups (01 to 05)
│
├── outputs/
│   ├── figures/                               # High-resolution generated charts (01 to 11)
│   ├── model_results.csv                      # Comparative algorithm evaluation table
│   └── feature_importance.csv                 # Ranked security risk weights
│
├── docs/
│   ├── BRD_Device_Risk_Analysis.docx          # Business Requirements Document (+ PDF)
│   ├── SRS_Device_Risk_Analysis.docx          # Software Requirements Specification (+ PDF)
│   ├── SOW_Device_Risk_Analysis.docx          # Statement of Work (+ PDF)
│   ├── WBS_Device_Risk_Analysis.docx          # Work Breakdown Structure (+ PDF)
│   ├── Test_Cases_Device_Risk_Analysis.docx   # Test Matrix with 15 scenarios (+ PDF)
│   ├── Project_Report_Device_Risk_Analysis.docx # Final Academic Project Report (+ PDF)
│   └── Presentation_Script_Device_Risk_Analysis.docx # Oral Viva Defense Script (+ PDF)
│
├── scripts/                                   # Automation and reproduction scripts
├── requirements.txt                           # Project dependencies
├── README.md                                  # Repository documentation
└── .gitignore                                 # Git exclusions
```

---

## 🚀 Quick Start & Installation

### 1. Clone & Set Up Environment
```bash
# Clone the repository
git clone https://github.com/sanchitaaa10/Greenpeace_India_clone.git
cd "DEVICE RISK ANALYSIS"

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required dependencies
pip install -r requirements.txt
```

### 2. Run Complete ML Pipeline
```bash
# Execute end-to-end data cleaning, model training, evaluation & serialization
python scripts/train_and_evaluate.py
```

### 3. Launch Interactive Streamlit App
```bash
streamlit run app/app.py
```
Open your browser at `http://localhost:8501` to test live device predictions!

### 4. Open Jupyter Notebook
```bash
jupyter notebook notebooks/Device_Risk_Analysis.ipynb
```

---

## 📸 Application Preview

The Streamlit web application features 6 responsive pages:
* **Home:** Executive KPI cards, fleet overview, and architecture diagram.
* **Risk Prediction:** Instant single-endpoint risk classification with one-click presets.
* **Dataset Insights:** Interactive distribution and correlation plots.
* **Model Performance:** Algorithm comparison benchmarks, confusion matrix, and ROC curves.
* **Security Insights:** Top 10 feature importance rankings and mitigation recommendations.
* **About Project:** Academic metadata, case study details, and methodology disclaimers.

---

## ⚖️ Ethical & Operational Disclaimers

1. **Advisory Decision Support:** Model predictions are statistical estimates to assist security analysts in prioritizing queues; they do not replace formal penetration testing or human judgment.
2. **Defensive Scope:** This application is strictly for risk classification; it contains no offensive cyber exploitation tools.
3. **Concept Drift:** Telemetry distributions evolve as threat actor techniques shift; periodic retraining on updated enterprise logs is recommended.

---

## 👩‍💻 Author & Academic Attribution
- Candidate: Atharva Gahine
- Degree: B.Tech Computer Science & Engineering (Semester V)
- University: ITM SKILLS UNIVERSITY, School of Future Tech
- Case Study: Case Study No. 86 (Device Risk Analysis)
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00C2FF,50:7F5CFF,100:00FF88&height=130&section=footer&text=DEVICE%20RISK%20ANALYSIS&fontSize=28&fontColor=ffffff&animation=twinkling" alt="Animated footer">

⭐ If you found this project useful, consider starring the repository!
Built with 🧠 Machine Learning • 🐍 Python • 🛡️ Cybersecurity
</div>
