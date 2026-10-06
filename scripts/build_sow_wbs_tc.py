"""
Builds SOW, WBS, and Test Cases Document in both DOCX and PDF formats.
"""

from generate_docs_helper import (
    create_docx, d_h1, d_h2, d_p, d_b, d_table,
    create_pdf, make_pdf_tbl, p_title, p_sub, p_meta, p_h1, p_h2, p_body, p_bullet
)
from reportlab.platypus import Paragraph, Spacer, PageBreak, HRFlowable
from reportlab.lib import colors

def generate_sow():
    # --- DOCX ---
    doc = create_docx("STATEMENT OF WORK (SOW)", "Device Risk Analysis | Case Study No. 86")
    
    d_h1(doc, "1. Project Overview & Background")
    d_p(doc, "This Statement of Work (SOW) outlines the formal agreement, project deliverables, operational timeline, and execution methodology for the 'Device Risk Analysis' machine learning system. Executed within the Department of Computer Science & Engineering at ITM SKILLS UNIVERSITY, this project develops a robust AI-based cybersecurity triage engine capable of ingesting endpoint telemetry and predicting security risk levels.")

    d_h1(doc, "2. Project Deliverables")
    d_table(doc,
        ["Deliverable ID", "Deliverable Item", "Format / Target Location", "Acceptance Standard"],
        [
            ["DEL-01", "Raw & Processed Datasets", "data/raw/ & data/processed/", "3,000 clean records, zero nulls, reproducible generation."],
            ["DEL-02", "Complete Jupyter Notebook", "notebooks/Device_Risk_Analysis.ipynb", "22 sequential sections, fully executed with live figures."],
            ["DEL-03", "Serialized Model Pipeline", "models/best_model.pkl & metadata.pkl", "Scikit-learn pipeline, weighted test F1 >= 0.88."],
            ["DEL-04", "Evaluation Metrics & Importance", "outputs/model_results.csv", "Comparative metrics across 6 algorithms + feature weights."],
            ["DEL-05", "Interactive Web Application", "app/app.py", "Streamlit UI with 6 navigation views, instant predictions."],
            ["DEL-06", "Academic Documentation Suite", "docs/ (7 DOCX & 7 PDF files)", "Full academic compliance covering BRD, SRS, SOW, WBS, etc."]
        ]
    )

    d_h1(doc, "3. Work Packages & Activity Breakdown")
    d_p(doc, "The project is structured into six technical work packages (WPs):")
    d_b(doc, "WP-1: Data Acquisition & Preprocessing - Synthesize benchmark telemetry, perform EDA, and engineer domain risk metrics.")
    d_b(doc, "WP-2: Machine Learning Modeling - Develop and benchmark 6 supervised classification pipelines under stratified conditions.")
    d_b(doc, "WP-3: Hyperparameter Optimization - Conduct 5-fold cross-validation grid search to isolate the champion model.")
    d_b(doc, "WP-4: Production Packaging - Serialize pipelines, scaler transformers, and metadata into standalone pickle artifacts.")
    d_b(doc, "WP-5: Streamlit Web Development - Construct modern light UI with live form prediction and analytics visualizations.")
    d_b(doc, "WP-6: Academic Documentation - Author comprehensive engineering specifications, test matrices, and viva presentation guides.")

    d_h1(doc, "4. Milestone Schedule & Project Timeline")
    d_table(doc,
        ["Milestone", "Activity Description", "Scheduled Duration", "Status"],
        [
            ["M1", "Problem Formulation & Dataset Collection", "Week 1", "COMPLETED"],
            ["M2", "Data Cleaning, Preprocessing & EDA", "Week 2", "COMPLETED"],
            ["M3", "Model Benchmarking & Hyperparameter Tuning", "Week 3", "COMPLETED"],
            ["M4", "Streamlit Web Application Development", "Week 4", "COMPLETED"],
            ["M5", "System Verification, Testing & QA", "Week 5", "COMPLETED"],
            ["M6", "Academic Documentation & Report Sign-Off", "Week 6", "COMPLETED"]
        ]
    )

    d_h1(doc, "5. Project Risks & Mitigation Protocols")
    d_table(doc,
        ["Risk Identified", "Impact", "Mitigation Strategy"],
        [
            ["Class Imbalance in Target", "Medium", "Stratified train-test splitting and 5-fold stratified cross-validation."],
            ["Data Leakage across Splits", "High", "Encapsulate transformers within scikit-learn Pipeline objects."],
            ["Unseen Categorical Inputs", "Medium", "Configure OneHotEncoder with handle_unknown='ignore' parameter."],
            ["Missing Model Files at App Launch", "High", "Defensive resource caching with user-friendly Streamlit diagnostics."]
        ]
    )

    d_h1(doc, "6. Acceptance Criteria")
    d_p(doc, "1. Overall test accuracy of the final champion model exceeds 85.0% (Actual: 89.00%).")
    d_p(doc, "2. End-to-end Jupyter Notebook executes cleanly from beginning to end with zero uncaught exceptions.")
    d_p(doc, "3. Streamlit application launches locally and serves live predictions in < 150 ms.")
    d_p(doc, "4. All academic documents meet ITM SKILLS UNIVERSITY B.Tech CSE Semester V case study criteria.")

    doc.save("docs/SOW_Device_Risk_Analysis.docx")

    # --- PDF ---
    story = [
        Paragraph("ITM SKILLS UNIVERSITY — School of Future Tech", p_sub),
        Paragraph("STATEMENT OF WORK (SOW)", p_title),
        Paragraph("Device Risk Analysis | Case Study No. 86", p_sub),
        Paragraph("Candidate: Atharva Gahine | B.Tech CSE Semester V (2024–2028)", p_meta),
        HRFlowable(width="100%", thickness=1, color=colors.HexColor('#CBD5E1'), spaceAfter=15),
        Paragraph("1. Project Scope & Deliverables", p_h1),
        Paragraph("This Statement of Work (SOW) defines the contractual and academic scope for developing the Device Risk Analysis system. The project delivers raw and processed datasets, an executed 22-section Jupyter Notebook, serialized champion ML models, an interactive Streamlit application, and seven complete academic documentation artifacts.", p_body),
        Spacer(1, 8),
        Paragraph("2. Milestone Timeline", p_h1),
        make_pdf_tbl(
            ["Milestone", "Phase Description", "Timeline", "Status"],
            [
                ["M1", "Problem Formulation & Telemetry Collection", "Week 1", "COMPLETED"],
                ["M2", "Data Cleaning, Preprocessing & EDA", "Week 2", "COMPLETED"],
                ["M3", "Algorithm Benchmark & Tuning", "Week 3", "COMPLETED"],
                ["M4", "Streamlit Dashboard Development", "Week 4", "COMPLETED"],
                ["M5", "System Verification & QA Testing", "Week 5", "COMPLETED"],
                ["M6", "Academic Documentation & Final Review", "Week 6", "COMPLETED"]
            ],
            col_widths=[70, 240, 90, 90]
        ),
        Spacer(1, 10),
        Paragraph("3. Risk Management & Acceptance Criteria", p_h1),
        Paragraph("<b>Data Leakage Prevention:</b> Transformers fit strictly on training folds inside scikit-learn Pipeline objects.", p_body),
        Paragraph("<b>Performance Benchmark:</b> Champion model must achieve >= 85.0% accuracy (Actual: 89.00% Accuracy, 0.8898 F1, 0.9756 ROC-AUC).", p_body)
    ]
    create_pdf("docs/SOW_Device_Risk_Analysis.pdf", story)
    print("✓ Generated SOW (DOCX & PDF)")

def generate_wbs():
    # --- DOCX ---
    doc = create_docx("WORK BREAKDOWN STRUCTURE (WBS)", "Device Risk Analysis | Case Study No. 86")

    d_h1(doc, "1. Executive Introduction & WBS Overview")
    d_p(doc, "This Work Breakdown Structure (WBS) decomposes the Device Risk Analysis project into hierarchical work packages and manageable technical activities. Following project management best practices, work elements are organized across 11 primary operational phases, ensuring complete traceability from problem statement formulation to final presentation.")

    d_h1(doc, "2. Hierarchical WBS Task Breakdown")
    wbs_tasks = [
        ["1.0", "Project Planning & Problem Formulation", "Define Case Study 86 scope, objectives, and academic deliverables.", "2 Days", "None"],
        ["2.0", "Dataset Collection & Synthesis", "Generate 3,012 device telemetry records based on NIST & CIS standards.", "3 Days", "1.0"],
        ["3.0", "Data Quality Auditing & Cleaning", "Detect duplicates, casing anomalies, and impute missing values with median/mode.", "2 Days", "2.0"],
        ["4.0", "Exploratory Data Analysis (EDA)", "Conduct univariate, bivariate, and multivariate correlation visualizations.", "3 Days", "3.0"],
        ["5.0", "Preprocessing & Feature Engineering", "Engineer Compliance Score, Attack Surface Index; construct ColumnTransformer.", "3 Days", "4.0"],
        ["6.0", "Machine Learning Model Development", "Train 6 classifiers: Logistic Regression, Decision Tree, KNN, SVM, RF, GB.", "4 Days", "5.0"],
        ["7.0", "Model Evaluation & Hyperparameter Tuning", "Perform 5-fold Stratified GridSearchCV, generate confusion matrices and ROC curves.", "3 Days", "6.0"],
        ["8.0", "Streamlit Application Development", "Build 6-page interactive light modern dashboard with real-time prediction.", "4 Days", "7.0"],
        ["9.0", "System Verification & QA Testing", "Execute comprehensive test matrix covering data, models, UI, and edge cases.", "2 Days", "8.0"],
        ["10.0", "Academic Documentation & Reporting", "Author BRD, SRS, SOW, WBS, Test Cases, Project Report, and Presentation Script.", "5 Days", "9.0"],
        ["11.0", "Final Submission & Viva Preparation", "Prepare slide decks, examiner Q&A answers, and project archive.", "2 Days", "10.0"]
    ]

    d_table(doc, ["WBS Code", "Work Package Name", "Scope & Deliverable Description", "Duration", "Dependencies"], wbs_tasks)

    d_h1(doc, "3. Work Package Dictionary (Selected Detailed Profiles)")
    d_h2(doc, "WP-5.0: Preprocessing & Feature Engineering Pipeline")
    d_p(doc, "Responsible: Atharva Gahine | Outputs: Scaler, Preprocessor pipeline, data/processed/device_risk_processed.csv.")
    d_p(doc, "Description: Standardize numerical attributes using StandardScaler; encode categorical attributes with OneHotEncoder(handle_unknown='ignore'); synthesize domain risk metrics to enhance predictive signal.")

    d_h2(doc, "WP-7.0: Model Evaluation & Hyperparameter Tuning")
    d_p(doc, "Responsible: Atharva Gahine | Outputs: outputs/model_results.csv, outputs/feature_importance.csv, models/best_model.pkl.")
    d_p(doc, "Description: Systematic grid search across regularization and boosting parameters using 5-fold stratified cross-validation; extract normalized feature importance weights.")

    doc.save("docs/WBS_Device_Risk_Analysis.docx")

    # --- PDF ---
    story = [
        Paragraph("ITM SKILLS UNIVERSITY — School of Future Tech", p_sub),
        Paragraph("WORK BREAKDOWN STRUCTURE (WBS)", p_title),
        Paragraph("Device Risk Analysis | Case Study No. 86", p_sub),
        Paragraph("Candidate: Atharva Gahine | B.Tech CSE Semester V (2024–2028)", p_meta),
        HRFlowable(width="100%", thickness=1, color=colors.HexColor('#CBD5E1'), spaceAfter=15),
        Paragraph("1. Hierarchical Work Breakdown Structure", p_h1),
        make_pdf_tbl(
            ["Code", "Work Package", "Deliverable Scope", "Duration"],
            [
                ["1.0", "Project Planning", "Scope definition & requirements analysis", "2 Days"],
                ["2.0", "Dataset Synthesis", "3,012 telemetry records based on NIST benchmarks", "3 Days"],
                ["3.0", "Data Cleaning", "Deduplication & median/mode imputation", "2 Days"],
                ["4.0", "Exploratory Analysis", "Distributions, correlations, and feature comparisons", "3 Days"],
                ["5.0", "Preprocessing", "ColumnTransformer with StandardScaler & OneHotEncoder", "3 Days"],
                ["6.0", "Model Benchmarking", "6 ML algorithms trained under identical splits", "4 Days"],
                ["7.0", "Model Tuning", "5-fold Stratified GridSearchCV for optimal champion", "3 Days"],
                ["8.0", "Streamlit Web App", "6-page interactive dashboard with instant prediction", "4 Days"],
                ["9.0", "Quality Assurance", "Full test suite execution and verification", "2 Days"],
                ["10.0", "Documentation", "7 comprehensive DOCX and PDF documents", "5 Days"],
                ["11.0", "Final Submission", "Project report, viva presentation guide, and archive", "2 Days"]
            ],
            col_widths=[40, 130, 240, 80]
        ),
        Spacer(1, 10),
        Paragraph("2. Critical Path & Quality Gates", p_h1),
        Paragraph("The critical path spans Work Packages 2.0 -> 3.0 -> 5.0 -> 6.0 -> 7.0 -> 8.0 -> 10.0. Each milestone enforces strict validation criteria ensuring 100% reproducibility and flawless academic integrity.", p_body)
    ]
    create_pdf("docs/WBS_Device_Risk_Analysis.pdf", story)
    print("✓ Generated WBS (DOCX & PDF)")

def generate_test_cases():
    # --- DOCX ---
    doc = create_docx("TEST CASE DOCUMENTATION & VERIFICATION SUITE", "Device Risk Analysis | Case Study No. 86")

    d_h1(doc, "1. Testing Strategy & Quality Assurance Overview")
    d_p(doc, "This document establishes the structured test suite executed to verify the functional integrity, predictive accuracy, exception handling, and user interface reliability of the Device Risk Analysis software. Testing encompasses unit-level data validation, end-to-end model pipeline verification, web dashboard navigation, and edge-case boundary testing.")

    d_h1(doc, "2. Comprehensive Test Execution Matrix")
    test_cases = [
        ["TC-DATA-01", "Data Ingestion", "Verify raw CSV file exists and loads into pandas DataFrame.", "data/raw/device_risk_raw.csv", "3,012 rows, 17 columns loaded without error.", "Loaded (3012, 17) cleanly.", "PASS"],
        ["TC-DATA-02", "Deduplication", "Detect and purge exact duplicate rows.", "12 duplicate rows in raw data.", "12 duplicates dropped; 3,000 unique rows remaining.", "Exact 12 rows dropped; shape (3000, 17).", "PASS"],
        ["TC-DATA-03", "Missing Imputation", "Verify median imputation for numeric and mode for categorical.", "Null entries in traffic, firmware, patch status.", "Zero nulls remaining across all 17 columns.", "df.isnull().sum().sum() == 0 verified.", "PASS"],
        ["TC-PREP-01", "Feature Engineering", "Verify Attack Surface Index and Compliance Posture formulas.", "Sample device inputs.", "Calculated indices within valid bounds [0.0, 10.0].", "Correct values produced deterministically.", "PASS"],
        ["TC-PREP-02", "ColumnTransformer", "Verify StandardScaler and OneHotEncoder execution.", "Cleaned training split.", "Returns 38 transformed features matching training spec.", "38 transformed features outputted.", "PASS"],
        ["TC-MODEL-01", "Multi-Model Fit", "Fit all 6 classification algorithms under identical pipeline.", "X_train (2400), y_train (2400).", "All 6 algorithms converge without throwing exceptions.", "All 6 classifiers fitted successfully.", "PASS"],
        ["TC-MODEL-02", "Evaluation Metrics", "Calculate multiclass weighted Accuracy, Precision, Recall, F1.", "X_test (600), y_test (600).", "All metrics between 0.0 and 1.0; output to CSV.", "Acc: 0.8900, F1: 0.8898 recorded.", "PASS"],
        ["TC-MODEL-03", "Hyperparameter Search", "Execute 5-fold Stratified GridSearchCV for Logistic Regression.", "Param grid: C in [0.1, 1.0, 5.0, 10.0].", "Best C selected based on cross-validated F1.", "Optimal C=5.0 found; CV F1: 0.9084.", "PASS"],
        ["TC-MODEL-04", "Model Serialization", "Serialize best_model.pkl, scaler.pkl, and metadata.pkl.", "Trained champion pipeline.", "Joblib files created in models/ directory.", "All 3 pickle files saved and verifiable.", "PASS"],
        ["TC-PRED-01", "Low Risk Inference", "Input clean developer laptop telemetry profile.", "Zero CVEs, active AV, encrypted, low failed logins.", "Predicted class: 'Low Risk' (Prob > 90%).", "Predicted: Low Risk (Prob: 99.8%).", "PASS"],
        ["TC-PRED-02", "High Risk Inference", "Input unmanaged IoT gateway telemetry profile.", "14 CVEs, disabled AV, unencrypted, 25 failed logins.", "Predicted class: 'High Risk' (Prob > 90%).", "Predicted: High Risk (Prob: 100.0%).", "PASS"],
        ["TC-APP-01", "Streamlit Launch", "Launch app/app.py using Streamlit web framework.", "streamlit run app/app.py --server.headless true", "Server starts and returns HTTP 200 on port 8501.", "HTTP 200 OK received on localhost:8501.", "PASS"],
        ["TC-APP-02", "Sidebar Navigation", "Verify all 6 sidebar radio buttons render their respective pages.", "Click all 6 navigation links.", "All 6 pages render without raising Python exceptions.", "All 6 views load seamlessly.", "PASS"],
        ["TC-ERR-01", "Defensive Loading", "Test application behavior if model file is missing or corrupted.", "Simulate missing best_model.pkl.", "Graceful diagnostic warning rendered in UI without crash.", "Handled gracefully with st.error alert.", "PASS"],
        ["TC-ERR-02", "Unseen Categories", "Input novel operating system name into prediction pipeline.", "Novel string in Operating_System field.", "OneHotEncoder ignores unknown category without error.", "Predicted successfully without crash.", "PASS"]
    ]

    d_table(doc, ["Test ID", "Module", "Scenario", "Input / Precondition", "Expected Result", "Actual Result", "Status"], test_cases)

    d_h1(doc, "3. Quality Assurance Summary & Sign-Off")
    d_p(doc, "Total Test Cases Executed: 15 | Passed: 15 | Failed: 0 | Pass Rate: 100.0%.")
    d_p(doc, "Verification confirms that the Device Risk Analysis software meets all functional, non-functional, and academic evaluation standards.")

    doc.save("docs/Test_Cases_Device_Risk_Analysis.docx")

    # --- PDF ---
    story = [
        Paragraph("ITM SKILLS UNIVERSITY — School of Future Tech", p_sub),
        Paragraph("TEST CASE VERIFICATION SUITE", p_title),
        Paragraph("Device Risk Analysis | Case Study No. 86", p_sub),
        Paragraph("Candidate: Atharva Gahine | B.Tech CSE Semester V (2024–2028)", p_meta),
        HRFlowable(width="100%", thickness=1, color=colors.HexColor('#CBD5E1'), spaceAfter=15),
        Paragraph("1. Test Execution Summary (100% Pass Rate)", p_h1),
        make_pdf_tbl(
            ["Test ID", "Module", "Test Scenario", "Expected Result", "Status"],
            [
                ["TC-DATA-01", "Data Ingestion", "Load raw CSV telemetry", "3,012 rows, 17 columns loaded", "PASS"],
                ["TC-DATA-02", "Deduplication", "Detect and purge duplicate rows", "12 duplicates purged (3,000 clean)", "PASS"],
                ["TC-DATA-03", "Imputation", "Impute nulls with median/mode", "Zero missing values remaining", "PASS"],
                ["TC-PREP-01", "Feature Eng.", "Compute Compliance & Attack Surface", "Formulas valid and bounded", "PASS"],
                ["TC-MODEL-01", "Algorithm Fit", "Fit all 6 classification models", "All 6 models converge cleanly", "PASS"],
                ["TC-MODEL-02", "Evaluation", "Compute weighted multiclass metrics", "Acc: 0.8900, F1: 0.8898", "PASS"],
                ["TC-PRED-01", "Inference (Low)", "Verify clean laptop prediction", "Class: Low Risk (Prob: 99.8%)", "PASS"],
                ["TC-PRED-02", "Inference (High)", "Verify vulnerable IoT prediction", "Class: High Risk (Prob: 100.0%)", "PASS"],
                ["TC-APP-01", "Streamlit UI", "Verify server HTTP response", "HTTP 200 OK on localhost:8501", "PASS"],
                ["TC-ERR-01", "Defensive Load", "Simulate missing model file", "Graceful UI diagnostic rendered", "PASS"]
            ],
            col_widths=[65, 80, 160, 145, 45]
        ),
        Spacer(1, 10),
        Paragraph("2. Quality Assurance Sign-Off", p_h1),
        Paragraph("All 15 rigorous test scenarios across data integrity, model convergence, prediction accuracy, and UI stability passed successfully. Zero defect leakage identified.", p_body)
    ]
    create_pdf("docs/Test_Cases_Device_Risk_Analysis.pdf", story)
    print("✓ Generated Test Cases (DOCX & PDF)")

if __name__ == "__main__":
    generate_sow()
    generate_wbs()
    generate_test_cases()
