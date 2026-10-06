"""
Builds BRD (Business Requirements Document) and SRS (Software Requirements Specification)
in both DOCX and PDF formats.
"""

from generate_docs_helper import (
    create_docx, d_h1, d_h2, d_p, d_b, d_table,
    create_pdf, make_pdf_tbl, p_title, p_sub, p_meta, p_h1, p_h2, p_body, p_bullet
)
from reportlab.platypus import Paragraph, Spacer, PageBreak, HRFlowable
from reportlab.lib import colors

def generate_brd():
    # --- DOCX ---
    doc = create_docx("BUSINESS REQUIREMENTS DOCUMENT (BRD)", "Device Risk Analysis | Case Study No. 86")
    
    d_h1(doc, "1. Executive Summary & Project Identification")
    d_p(doc, "This Business Requirements Document (BRD) establishes the operational justification, business needs, and functional criteria for developing an AI-driven Device Risk Analysis system. In enterprise operational environments, cyber threats exploit vulnerable, misconfigured, or unpatched endpoints. This project defines a supervised machine learning solution capable of assessing multi-dimensional telemetry from workstations, servers, mobile units, and IoT gateways, classifying each asset into an actionable security risk tier: Low Risk, Medium Risk, or High Risk.")
    
    d_h1(doc, "2. Problem Statement & Business Opportunity")
    d_p(doc, "\"An organization wants to analyze device-related information and identify patterns associated with elevated security concerns.\"", "Formal Statement: ")
    d_p(doc, "Traditional Security Operations Centers (SOCs) struggle with alert fatigue and manual asset auditing across thousands of endpoints. Analysts spend an estimated 25% to 35% of their working hours cross-referencing vulnerability scan reports against patch management and network log files. By deploying a predictive machine learning classification engine, the organization automates device posture scoring, reduces Mean Time to Detect (MTTD), and prioritizes patch deployment effectively.")

    d_h1(doc, "3. Project Stakeholders & RACI Matrix")
    d_table(doc,
        ["Stakeholder Role", "Primary Responsibility", "RACI Designation"],
        [
            ["Chief Information Security Officer (CISO)", "Strategic risk governance & compliance sign-off", "Accountable (A)"],
            ["SOC Lead Analyst", "Operational triage workflows & threat alert monitoring", "Responsible (R)"],
            ["IT Endpoint Infrastructure Manager", "Patch deployment, endpoint OS maintenance & encryption", "Consulted (C)"],
            ["Academic Project Evaluator", "Assessment of methodology, rigor, and model validity", "Informed (I)"],
            ["Lead ML Developer (Atharva G.)", "End-to-end ML development, validation & dashboard deployment", "Responsible (R)"]
        ]
    )

    d_h1(doc, "4. Scope of the System")
    d_h2(doc, "4.1 In-Scope Deliverables")
    d_b(doc, "Ingestion and preprocessing of 17 device telemetry attributes across hardware, network, and vulnerability dimensions.")
    d_b(doc, "Automated data cleaning: deduplication, string casing normalization, and median/mode missing value imputation.")
    d_b(doc, "Domain-driven feature engineering: Attack Surface Index, Vulnerability-to-Firmware Ratio, and Compliance Posture Score.")
    d_b(doc, "Benchmarking 6 classification algorithms (Logistic Regression, Decision Tree, KNN, SVM, Random Forest, Gradient Boosting).")
    d_b(doc, "Interactive light modern Streamlit web application providing real-time single-device risk scoring and fleet analytics.")

    d_h2(doc, "4.2 Out-of-Scope Elements")
    d_b(doc, "Automated active packet payload deep packet inspection (DPI) or kernel-level network packet sniffing.")
    d_b(doc, "Automated active remote shell exploitation or offensive cyber payload deployment.")
    d_b(doc, "Complex enterprise microservices, Kubernetes clusters, or multi-tenant database infrastructure.")

    d_h1(doc, "5. Functional Business Requirements")
    d_table(doc,
        ["Req ID", "Business Requirement Description", "Priority"],
        [
            ["BR-FR-01", "The system shall ingest tabular endpoint telemetry including OS, device age, firmware age, CVEs, ports, and protections.", "High"],
            ["BR-FR-02", "The system shall automatically clean raw data, imputing missing values and removing duplicate device reports.", "High"],
            ["BR-FR-03", "The system shall categorize devices into three mutually exclusive risk tiers: Low Risk, Medium Risk, High Risk.", "High"],
            ["BR-FR-04", "The system shall evaluate multiple supervised classifiers and select the champion model based on cross-validated F1 score.", "High"],
            ["BR-FR-05", "The system shall present an interactive web dashboard for on-demand device profiling and confidence score display.", "High"],
            ["BR-FR-06", "The system shall provide feature importance rankings to identify primary risk drivers without claiming unverified causality.", "Medium"],
            ["BR-FR-07", "The system shall display defensive remediation guidance tailored to the predicted risk level.", "Medium"]
        ]
    )

    d_h1(doc, "6. Non-Functional Business Requirements")
    d_table(doc,
        ["Req ID", "Non-Functional Category", "Target Metric / Specification"],
        [
            ["BR-NFR-01", "Prediction Latency", "Sub-second inference time (< 150 ms) for single device profile inputs."],
            ["BR-NFR-02", "Classification Accuracy", "Overall multi-class test accuracy >= 85.0% and weighted F1-Score >= 0.85."],
            ["BR-NFR-03", "Reproducibility", "Deterministic pipeline execution utilizing fixed random seeds (random_state=42)."],
            ["BR-NFR-04", "Usability & UI", "Clean, responsive, light-themed modern web interface with no prerequisite coding knowledge."],
            ["BR-NFR-05", "Interpretability", "Transparent feature weighting explaining model outputs for audit compliance."]
        ]
    )

    d_h1(doc, "7. Expected Business Outcomes & Success Criteria")
    d_b(doc, "Achieve over 88% classification accuracy (Actual Champion: 89.00% Accuracy, 0.8898 F1-Score, 0.9756 ROC-AUC).")
    d_b(doc, "Eliminate manual calculation of composite endpoint risk by automating multi-factor security scoring.")
    d_b(doc, "Successfully demonstrate production-grade machine learning pipelines aligned with academic Semester V standards.")

    doc.save("docs/BRD_Device_Risk_Analysis.docx")

    # --- PDF ---
    story = [
        Paragraph("ITM SKILLS UNIVERSITY — School of Future Tech", p_sub),
        Paragraph("BUSINESS REQUIREMENTS DOCUMENT (BRD)", p_title),
        Paragraph("Device Risk Analysis | Case Study No. 86", p_sub),
        Paragraph("Candidate: Atharva Gahine | B.Tech CSE Semester V (2024–2028)", p_meta),
        HRFlowable(width="100%", thickness=1, color=colors.HexColor('#CBD5E1'), spaceAfter=15),
        Paragraph("1. Executive Summary & Problem Formulation", p_h1),
        Paragraph("This Business Requirements Document (BRD) establishes the organizational rationale and requirements for the Device Risk Analysis machine learning system. Modern enterprises face severe security challenges monitoring heterogeneous hardware endpoints. The core problem statement: <i>'An organization wants to analyze device-related information and identify patterns associated with elevated security concerns.'</i> The system automates multi-dimensional risk classification into Low Risk, Medium Risk, and High Risk tiers.", p_body),
        Spacer(1, 8),
        Paragraph("2. Project Stakeholders & RACI Structure", p_h1),
        make_pdf_tbl(
            ["Stakeholder", "Role Responsibility", "RACI"],
            [
                ["CISO / InfoSec Lead", "Strategic risk oversight & governance sign-off", "Accountable"],
                ["SOC Lead Analyst", "Operational triage workflows & threat alert monitoring", "Responsible"],
                ["Endpoint Administrator", "Patch deployment & OS antivirus configuration", "Consulted"],
                ["Lead ML Engineer", "End-to-end ML development, validation & Streamlit app", "Responsible"]
            ],
            col_widths=[140, 260, 90]
        ),
        Spacer(1, 10),
        Paragraph("3. Scope of Work", p_h1),
        Paragraph("<b>In-Scope:</b> Ingestion of 17 telemetry attributes across 3,000 devices; automated data cleaning; domain feature engineering; benchmarking 6 ML algorithms; hyperparameter tuning; interactive Streamlit dashboard; comprehensive documentation.", p_body),
        Paragraph("<b>Out-of-Scope:</b> Real-time packet payload interception; automated active exploitation; enterprise microservices / Kubernetes orchestrations.", p_body),
        Spacer(1, 8),
        Paragraph("4. Functional Requirements", p_h1),
        make_pdf_tbl(
            ["Req ID", "Requirement Description", "Priority"],
            [
                ["BR-FR-01", "Ingest multi-dimensional device telemetry across 17 attributes", "High"],
                ["BR-FR-02", "Execute automated imputation and deduplication cleaning", "High"],
                ["BR-FR-03", "Classify endpoints into Low, Medium, or High Risk tiers", "High"],
                ["BR-FR-04", "Benchmark 6 classifiers and select champion based on cross-validated F1", "High"],
                ["BR-FR-05", "Interactive Streamlit web dashboard with confidence scoring", "High"],
                ["BR-FR-06", "Feature importance breakdown for explainable security insights", "Medium"]
            ],
            col_widths=[80, 330, 80]
        ),
        Spacer(1, 10),
        Paragraph("5. Non-Functional Criteria & Success Metrics", p_h1),
        Paragraph("<b>Accuracy & Generalization:</b> Model must achieve >= 85.0% accuracy on unseen test data (Actual: 89.00% Accuracy, 0.8898 F1, 0.9756 ROC-AUC).", p_body),
        Paragraph("<b>Inference Latency:</b> Real-time single-endpoint inference under 150 milliseconds via Streamlit.", p_body),
        Paragraph("<b>Reproducibility:</b> Deterministic random state (seed 42) ensures 100% reproducible experiments.", p_body)
    ]
    create_pdf("docs/BRD_Device_Risk_Analysis.pdf", story)
    print("✓ Generated BRD (DOCX & PDF)")

def generate_srs():
    # --- DOCX ---
    doc = create_docx("SOFTWARE REQUIREMENTS SPECIFICATION (SRS)", "Device Risk Analysis | Case Study No. 86")

    d_h1(doc, "1. Introduction")
    d_h2(doc, "1.1 Purpose")
    d_p(doc, "This Software Requirements Specification (SRS) provides a comprehensive technical description of the Device Risk Analysis software system. It documents functional capabilities, system interfaces, hardware/software specifications, mathematical feature transformations, and performance criteria for academic evaluation and software reproduction.")
    
    d_h2(doc, "1.2 Document Conventions")
    d_p(doc, "This document adheres to IEEE Std 830-1998 standards for software requirements documentation. Functional requirements are denoted with 'FR-' prefixes, non-functional requirements with 'NFR-', and data requirements with 'DR-'.")

    d_h1(doc, "2. System Overview & Architecture")
    d_p(doc, "The software comprises an end-to-end Machine Learning data science pipeline connected to a Streamlit front-end user interface. Raw device telemetry is cleaned and preprocessed using scikit-learn Pipelines, passing through numerical scalers (StandardScaler) and categorical encoders (OneHotEncoder). A champion multi-class Logistic Regression classifier outputs class probabilities and predicted risk tiers.")

    d_h1(doc, "3. Data Requirements & Schema Specification")
    d_p(doc, "The system processes 17 attributes per device record, defined in the following data dictionary:")
    d_table(doc,
        ["Field Name", "Type", "Domain Range", "Missing Value Handling"],
        [
            ["Device_ID", "String", "DEV-1000 to DEV-4012", "Identifier (Excluded from features)"],
            ["Device_Type", "Categorical", "6 classes (Laptop, Server, IoT, etc.)", "Mode imputation"],
            ["Operating_System", "Categorical", "11 OS classes (Win11, Linux, etc.)", "Mode imputation"],
            ["Device_Age_Months", "Integer", "1 to 72 months", "Median imputation"],
            ["Firmware_Age_Months", "Integer", "0 to 36 months", "Median imputation"],
            ["Failed_Login_Attempts", "Integer", "0 to 50 attempts / month", "Median imputation"],
            ["Open_Ports_Count", "Integer", "1 to 25 ports", "Median imputation"],
            ["Vulnerability_Count", "Integer", "0 to 20 CVEs", "Median imputation"],
            ["Security_Updates_Pending", "Integer", "0 to 15 updates", "Median imputation"],
            ["Encryption_Enabled", "Categorical", "Yes, No", "Mode imputation"],
            ["Antivirus_Status", "Categorical", "Active, Outdated, Disabled", "Mode imputation"],
            ["Suspicious_Activity_Flags", "Integer", "0 to 10 alert counts", "Median imputation"],
            ["Average_Daily_Traffic_MB", "Float", "50.0 to 15,000.0 MB", "Median imputation"],
            ["Access_Frequency_Score", "Float", "1.0 to 10.0 index", "Median imputation"],
            ["Previous_Security_Incidents", "Integer", "0 to 5 incidents", "Median imputation"],
            ["Patch_Status", "Categorical", "Fully Patched, Partially, Outdated", "Mode imputation"],
            ["Risk_Level (Target)", "Categorical", "Low Risk, Medium Risk, High Risk", "Supervised Target Label"]
        ]
    )

    d_h1(doc, "4. Functional Requirements")
    d_table(doc,
        ["Req ID", "Module", "Description"],
        [
            ["FR-01", "Ingestion", "Load raw telemetry from CSV format verifying header integrity."],
            ["FR-02", "Sanitization", "Identify and drop identical duplicate rows based on all features."],
            ["FR-03", "Casing Normalizer", "Standardize categorical variations (e.g. 'active', 'ACTIVE' -> 'Active')."],
            ["FR-04", "Feature Synthesis", "Compute Vulnerability-Firmware Ratio, Attack Surface Index, and Compliance Score."],
            ["FR-05", "Column Transformer", "Execute scikit-learn ColumnTransformer applying StandardScaler and OneHotEncoder."],
            ["FR-06", "Stratified Splitter", "Partition data into 80% train and 20% test using stratified random sampling."],
            ["FR-07", "Model Benchmark", "Fit and record metrics for 6 classifiers using weighted multiclass formulas."],
            ["FR-08", "Hyperparameter Search", "Execute 5-fold Stratified GridSearchCV for optimal regularization parameters."],
            ["FR-09", "Artifact Serializer", "Persist best_model.pkl, scaler.pkl, and model_metadata.pkl using Joblib."],
            ["FR-10", "Web Interface", "Provide 6 navigation pages in Streamlit for prediction, insights, and benchmarks."]
        ]
    )

    d_h1(doc, "5. Hardware and Software Specifications")
    d_h2(doc, "5.1 Hardware Environment")
    d_b(doc, "Processor: 64-bit multi-core CPU (Apple Silicon M-series or Intel/AMD x86_64).")
    d_b(doc, "RAM: 8 GB minimum (16 GB recommended for seamless cross-validation).")
    d_b(doc, "Storage: 1.0 GB free disk space for repository datasets, artifacts, and figures.")

    d_h2(doc, "5.2 Software Environment")
    d_b(doc, "Operating System: macOS 11+, Linux Ubuntu 20.04+, or Windows 10/11.")
    d_b(doc, "Programming Runtime: Python 3.12 (Virtual Environment recommended).")
    d_b(doc, "Core Packages: scikit-learn (>=1.4.0), pandas (>=2.0.0), numpy (>=1.26.0), streamlit (>=1.35.0), joblib, matplotlib, seaborn.")

    d_h1(doc, "6. Error Handling & Exception Management")
    d_p(doc, "1. Missing Model Files: The Streamlit application performs defensive checks on startup. If best_model.pkl is absent, it renders a non-crashing diagnostic alert guiding the user to run the training script.")
    d_p(doc, "2. Unseen Categorical Inputs: OneHotEncoder uses handle_unknown='ignore' so novel categories in user input do not cause runtime dimension mismatch errors.")
    d_p(doc, "3. Out-of-bounds Numerical Inputs: Streamlit sliders bound numerical values within realistic physical domains.")

    doc.save("docs/SRS_Device_Risk_Analysis.docx")

    # --- PDF ---
    story = [
        Paragraph("ITM SKILLS UNIVERSITY — School of Future Tech", p_sub),
        Paragraph("SOFTWARE REQUIREMENTS SPECIFICATION (SRS)", p_title),
        Paragraph("Device Risk Analysis | Case Study No. 86", p_sub),
        Paragraph("Candidate: Atharva Gahine | B.Tech CSE Semester V (2024–2028)", p_meta),
        HRFlowable(width="100%", thickness=1, color=colors.HexColor('#CBD5E1'), spaceAfter=15),
        Paragraph("1. System Purpose & Architecture", p_h1),
        Paragraph("This document specifies the software architecture, data schemas, functional requirements, and operating constraints for the Device Risk Analysis software. The solution implements a complete supervised machine learning workflow encapsulated within a modern Streamlit user interface.", p_body),
        Spacer(1, 8),
        Paragraph("2. Telemetry Schema & Data Dictionary", p_h1),
        make_pdf_tbl(
            ["Field Name", "Type", "Domain Range", "Null Imputation"],
            [
                ["Device_Type", "Categorical", "6 classes (Laptop, Server, etc.)", "Mode"],
                ["Operating_System", "Categorical", "11 classes (Win11, Linux, etc.)", "Mode"],
                ["Device_Age_Months", "Integer", "1 to 72 months", "Median"],
                ["Firmware_Age_Months", "Integer", "0 to 36 months", "Median"],
                ["Failed_Login_Attempts", "Integer", "0 to 50 attempts", "Median"],
                ["Open_Ports_Count", "Integer", "1 to 25 ports", "Median"],
                ["Vulnerability_Count", "Integer", "0 to 20 CVEs", "Median"],
                ["Encryption_Enabled", "Categorical", "Yes, No", "Mode"],
                ["Antivirus_Status", "Categorical", "Active, Outdated, Disabled", "Mode"],
                ["Risk_Level (Target)", "Categorical", "Low Risk, Medium Risk, High Risk", "Supervised Target"]
            ],
            col_widths=[120, 80, 190, 100]
        ),
        Spacer(1, 10),
        Paragraph("3. Functional Requirements Summary", p_h1),
        make_pdf_tbl(
            ["ID", "Module", "Description"],
            [
                ["FR-01", "Ingestion", "Load raw CSV telemetry validating column headers"],
                ["FR-02", "Cleaning", "Automated duplicate deletion and missing value imputation"],
                ["FR-03", "Pipeline", "ColumnTransformer with StandardScaler & OneHotEncoder"],
                ["FR-04", "Benchmark", "Train and compare 6 classification models (F1-weighted)"],
                ["FR-05", "Tuning", "5-fold Stratified GridSearchCV for optimal regularization"],
                ["FR-06", "Web App", "6-page Streamlit application for on-demand predictions"]
            ],
            col_widths=[60, 90, 340]
        ),
        Spacer(1, 10),
        Paragraph("4. Software & Runtime Constraints", p_h1),
        Paragraph("<b>Python Version:</b> Python 3.12 within dedicated virtual environment.", p_body),
        Paragraph("<b>Fault Tolerance:</b> Defensive loading handles missing model files gracefully without application termination.", p_body)
    ]
    create_pdf("docs/SRS_Device_Risk_Analysis.pdf", story)
    print("✓ Generated SRS (DOCX & PDF)")

if __name__ == "__main__":
    generate_brd()
    generate_srs()
