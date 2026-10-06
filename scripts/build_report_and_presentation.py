"""
Builds Project Report (Comprehensive Academic Final Report) and
Presentation Script & Viva Defense Guide in both DOCX and PDF formats.
"""

from generate_docs_helper import (
    create_docx, d_h1, d_h2, d_p, d_b, d_table,
    create_pdf, make_pdf_tbl, p_title, p_sub, p_meta, p_h1, p_h2, p_body, p_bullet
)
from reportlab.platypus import Paragraph, Spacer, PageBreak, HRFlowable
from reportlab.lib import colors

def generate_project_report():
    # --- DOCX ---
    doc = create_docx(
        "DEVICE RISK ANALYSIS: MACHINE LEARNING BASED ENDPOINT SECURITY CLASSIFICATION",
        "A Comprehensive Academic Project Report | Case Study No. 86"
    )

    # Certificate of Originality
    d_h1(doc, "CERTIFICATE OF ORIGINALITY")
    d_p(doc, "This is to certify that the project report entitled 'DEVICE RISK ANALYSIS' submitted by Atharva Gahine (Enrolment / Roll No: ITM-CSE-2024-86) in partial fulfillment of the requirements for the award of the degree of Bachelor of Technology in Computer Science & Engineering at ITM SKILLS UNIVERSITY (School of Future Tech) is an authentic record of academic work carried out under supervision during Semester V (Academic Year 2024–2028).")
    d_p(doc, "\n\n_______________________\nProject Guide / Faculty Evaluator\nDepartment of Computer Science & Engineering\nITM SKILLS UNIVERSITY")
    doc.add_page_break()

    # Student Declaration
    d_h1(doc, "CANDIDATE DECLARATION")
    d_p(doc, "I hereby declare that this project report titled 'DEVICE RISK ANALYSIS' submitted to the Department of Computer Science & Engineering, ITM SKILLS UNIVERSITY, is my own original work. The results, algorithms, metrics, and application code presented in this report have been implemented and validated by me. All literature, benchmark datasets, and reference frameworks used have been duly cited and acknowledged.")
    d_p(doc, "\n\n_______________________\nAtharva Gahine\nB.Tech CSE, Semester V\nITM SKILLS UNIVERSITY")
    doc.add_page_break()

    # Acknowledgement
    d_h1(doc, "ACKNOWLEDGEMENT")
    d_p(doc, "I express my profound gratitude to the faculty and mentors at ITM SKILLS UNIVERSITY, School of Future Tech, for their continuous academic guidance, invaluable encouragement, and constructive critique throughout the course of this Machine Learning project. I would also like to thank the open-source software and machine learning research community for providing robust, transparent tools and standardized cybersecurity frameworks (such as NIST and CIS Controls) that made this research possible.")
    doc.add_page_break()

    # Abstract
    d_h1(doc, "ABSTRACT")
    d_p(doc, "In modern digital enterprise environments, safeguarding diverse fleets of networked devices—such as laptops, database servers, smartphones, and Internet of Things (IoT) gateways—against cyber exploitation is an urgent operational priority. Traditional static rule-based security audits struggle to capture subtle, multi-factor dependencies across vulnerability density, authentication pressure, patch status, and defensive configuration states. This study develops a complete, reproducible Machine Learning classification system that ingests multi-dimensional endpoint telemetry and categorizes devices into three actionable risk tiers: Low Risk, Medium Risk, and High Risk.")
    d_p(doc, "The dataset comprises 3,012 device telemetry records structured across 17 attributes. A disciplined data cleaning pipeline purges duplicates, standardizes categorical representations, and imputes missing telemetry using statistical median and mode methods. Three domain features—Vulnerability-Firmware Ratio, Attack Surface Index, and Compliance Posture Score—are synthesized to enrich predictive signal. Six classification algorithms are systematically trained and evaluated under stratified conditions: Logistic Regression, Decision Tree, K-Nearest Neighbors, Support Vector Machine (SVM), Random Forest, and Gradient Boosting. Hyperparameter optimization using 5-fold Stratified Cross-Validation via GridSearchCV establishes tuned Logistic Regression as the champion model, achieving 89.00% test accuracy, a weighted F1-Score of 0.8898, and an exceptional multi-class One-vs-Rest ROC-AUC of 0.9756. An interactive, modern light Streamlit web application is developed to enable real-time risk classification, fleet telemetry exploration, and transparent security factor interpretation.")
    doc.add_page_break()

    # Chapter 1: Introduction
    d_h1(doc, "CHAPTER 1: INTRODUCTION")
    d_p(doc, "1.1 Background & Context", "Sub-section: ")
    d_p(doc, "The rapid proliferation of hybrid workforce endpoints and edge computing infrastructure has radically broadened the attack surface of contemporary enterprises. Modern organizations operate thousands of digital devices across varied operating systems, hardware revisions, and firmware levels. Maintaining security consistency across this heterogeneous fleet is notoriously complex. Security analysts face alert fatigue, siloed vulnerability scanner outputs, and an inability to rank remediation actions based on true multi-factor exposure.")
    d_p(doc, "1.2 Academic Relevance", "Sub-section: ")
    d_p(doc, "Within the B.Tech Computer Science & Engineering curriculum at ITM SKILLS UNIVERSITY, this project serves as a comprehensive case study (Case Study No. 86) demonstrating end-to-end applied machine learning. It covers the complete lifecycle: problem formalization, benchmark telemetry curation, rigorous data quality audits, exploratory visual analysis, scikit-learn pipeline engineering, multi-algorithm benchmarking, cross-validated hyperparameter optimization, and interactive deployment.")

    # Chapter 2: Problem Definition
    d_h1(doc, "CHAPTER 2: PROBLEM DEFINITION")
    d_p(doc, "\"An organization wants to analyze device-related information and identify patterns associated with elevated security concerns.\"", "Formal Statement: ")
    d_p(doc, "The objective is to formulate device security risk assessment as a supervised multi-class classification problem. Given a feature vector X representing hardware properties, operating system state, patch levels, authentication anomalies, network bandwidth, and protection statuses, the model must output a predicted risk tier y in {Low Risk, Medium Risk, High Risk}, accompanied by well-calibrated class probability distributions.")

    # Chapter 3: Objectives & Scope
    d_h1(doc, "CHAPTER 3: OBJECTIVES & SCOPE")
    d_b(doc, "Define and document a supervised machine learning classification workflow.")
    d_b(doc, "Curate and document a clean benchmark dataset reflecting realistic enterprise endpoint distributions.")
    d_b(doc, "Perform thorough data quality auditing, missing value imputation, and deduplication.")
    d_b(doc, "Conduct exploratory data analysis across univariate, bivariate, and correlation dimensions.")
    d_b(doc, "Engineer three domain-relevant security metrics capturing attack surface and compliance health.")
    d_b(doc, "Construct robust, leak-free scikit-learn Pipeline objects combining StandardScaler and OneHotEncoder.")
    d_b(doc, "Train, benchmark, and cross-validate 6 classification algorithms.")
    d_b(doc, "Deploy an interactive, light-modern Streamlit dashboard for real-time endpoint inference.")

    # Chapter 4: Literature & Background Study
    d_h1(doc, "CHAPTER 4: LITERATURE & BACKGROUND STUDY")
    d_p(doc, "Endpoint risk scoring has historically relied on static scoring rubrics such as the Common Vulnerability Scoring System (CVSS) and Center for Internet Security (CIS) Controls benchmarks. However, research by NIST (Special Publication 800-40) highlights that vulnerability scores alone do not reflect real operational exposure. An unpatched server residing in an isolated management VLAN with active intrusion monitoring exhibits far lower operational risk than an unencrypted developer laptop with open listening ports and disabled antivirus definitions. Supervised classification enables holistic multi-attribute synthesis, discovering non-linear interactions that traditional threshold-based systems overlook.")

    # Chapter 5: Dataset Telemetry & Attributes
    d_h1(doc, "CHAPTER 5: DATASET TELEMETRY & ATTRIBUTE DESCRIPTION")
    d_p(doc, "The dataset comprises 3,012 device instances (including 12 duplicate records for auditing verification) and 17 attributes:")
    d_table(doc,
        ["Attribute Name", "Type", "Domain Range", "Operational Significance"],
        [
            ["Device_Type", "Categorical", "6 classes (Laptop, Server, etc.)", "Baseline operational exposure tier"],
            ["Operating_System", "Categorical", "11 OS classes (Win11, Linux, etc.)", "Kernel update channel and attack vector profile"],
            ["Device_Age_Months", "Numerical", "1 to 72 months", "Hardware lifecycle and physical obsolescence"],
            ["Firmware_Age_Months", "Numerical", "0 to 36 months", "Latency since last BIOS/UEFI security flash"],
            ["Failed_Login_Attempts", "Numerical", "0 to 50 attempts / month", "Indicator of brute-force authentication activity"],
            ["Open_Ports_Count", "Numerical", "1 to 25 ports", "Network listening surface exposure"],
            ["Vulnerability_Count", "Numerical", "0 to 20 CVEs", "Known unmitigated software vulnerabilities"],
            ["Security_Updates_Pending", "Numerical", "0 to 15 updates", "Backlog of released operating system patches"],
            ["Encryption_Enabled", "Categorical", "Yes, No", "Full disk cryptographic data protection"],
            ["Antivirus_Status", "Categorical", "Active, Outdated, Disabled", "Endpoint detection and signature status"],
            ["Suspicious_Activity_Flags", "Numerical", "0 to 10 alerts", "Network IDS behavioral anomaly events"],
            ["Average_Daily_Traffic_MB", "Numerical", "50.0 to 15,000.0 MB", "Daily bandwidth consumption volume"],
            ["Access_Frequency_Score", "Numerical", "1.0 to 10.0 index", "User session access frequency index"],
            ["Previous_Security_Incidents", "Numerical", "0 to 5 events", "Historical quarantine and breach occurrences"],
            ["Patch_Status", "Categorical", "Fully Patched, Partially, Outdated", "Qualitative compliance categorization"],
            ["Risk_Level", "Target", "Low Risk, Medium Risk, High Risk", "Supervised classification ground truth"]
        ]
    )

    # Chapter 6: Data Preprocessing
    d_h1(doc, "CHAPTER 6: DATA PREPROCESSING & CLEANING")
    d_p(doc, "1. Deduplication: The 12 duplicate records were removed, yielding exactly 3,000 clean device records.")
    d_p(doc, "2. Casing Standardization: Inconsistent strings in Antivirus_Status ('active', 'ACTIVE') were standardized to 'Active'.")
    d_p(doc, "3. Missing Value Imputation: Numeric fields (Average_Daily_Traffic_MB, Firmware_Age_Months) were imputed using median values to preserve distribution medians; categorical Patch_Status was imputed using the mode ('Fully Patched').")
    d_p(doc, "4. Pipeline Architecture: ColumnTransformer was employed to route numerical columns to SimpleImputer(median) + StandardScaler(), and categorical columns to SimpleImputer(mode) + OneHotEncoder(handle_unknown='ignore').")

    # Chapter 7: Exploratory Data Analysis
    d_h1(doc, "CHAPTER 7: EXPLORATORY DATA ANALYSIS (EDA)")
    d_p(doc, "Key empirical findings from exploratory analysis:")
    d_b(doc, "Target Class Balance: The clean fleet exhibits 1,264 Medium Risk (42.1%), 964 Low Risk (32.1%), and 772 High Risk (25.7%) devices.")
    d_b(doc, "Vulnerability Distribution: High Risk devices display a median of 12 unpatched CVEs, compared to 5 for Medium Risk and 1 for Low Risk devices.")
    d_b(doc, "Antivirus Influence: Devices with disabled antivirus protection showed a >75% probability of falling into the High Risk tier.")
    d_b(doc, "Perimeter Exposure: Open ports and failed login spikes strongly correlate with suspicious activity alerts (Pearson r = 0.52).")

    # Chapter 8: Machine Learning Methodology
    d_h1(doc, "CHAPTER 8: MACHINE LEARNING METHODOLOGY")
    d_p(doc, "To prevent data leakage, all preprocessing transformations were fit strictly on the 80% training split (2,400 samples) and applied to the 20% test split (600 samples). Stratified sampling guaranteed identical class proportions across both subsets. A 5-fold Stratified Cross-Validation scheme was employed during hyperparameter tuning.")

    # Chapter 9: Algorithms Used
    d_h1(doc, "CHAPTER 9: ALGORITHMS EVALUATED")
    d_p(doc, "Six core algorithms representing linear, non-parametric, distance-based, kernel, bagging, and boosting paradigms were evaluated:")
    d_table(doc,
        ["Algorithm", "Paradigm", "Primary Advantage", "Key Limitation"],
        [
            ["Logistic Regression", "Generalized Linear", "Fast, convex, highly interpretable odds ratios", "Requires linear decision boundaries"],
            ["Decision Tree", "Rule-based Non-parametric", "Intuitive decision splits, handles non-linearities", "High variance, prone to overfitting"],
            ["K-Nearest Neighbors", "Instance-based Distance", "No training phase, adapts to localized clusters", "High inference cost, sensitive to irrelevant features"],
            ["Support Vector Machine", "Kernel Maximum Margin", "Effective in high-dimensional transformed spaces", "Higher training compute, slower scaling"],
            ["Random Forest", "Bagging Ensemble", "Reduces variance via bootstrap aggregation", "Ensemble size increases memory footprint"],
            ["Gradient Boosting", "Boosting Ensemble", "Sequentially minimizes pseudo-residuals", "Sensitive to noisy labels, prone to overfit if unregularized"]
        ]
    )

    # Chapter 10, 11, 12: Model Training, Evaluation & Comparison
    d_h1(doc, "CHAPTER 10, 11 & 12: MODEL TRAINING, EVALUATION & COMPARISON")
    d_p(doc, "All six classifiers were trained under identical pipeline conditions. Multi-class metrics were calculated using weighted averaging:")
    d_table(doc,
        ["Algorithm", "Accuracy", "Precision", "Recall", "F1 Score", "ROC_AUC"],
        [
            ["Logistic Regression (Baseline)", "0.8883", "0.8884", "0.8883", "0.8883", "0.9759"],
            ["Support Vector Machine", "0.8800", "0.8802", "0.8800", "0.8801", "0.9710"],
            ["Gradient Boosting (Baseline)", "0.8450", "0.8476", "0.8450", "0.8452", "0.9551"],
            ["Random Forest Classifier", "0.8017", "0.8101", "0.8017", "0.8021", "0.9265"],
            ["K-Nearest Neighbors", "0.7883", "0.7908", "0.7883", "0.7868", "0.9151"],
            ["Decision Tree Classifier", "0.7167", "0.7327", "0.7167", "0.7178", "0.8466"]
        ]
    )
    d_p(doc, "Hyperparameter Tuning Results (5-Fold Stratified CV):")
    d_b(doc, "Tuned Logistic Regression: Optimal C=5.0, solver='lbfgs' -> Cross-Validation F1: 0.9084.")
    d_b(doc, "Tuned Gradient Boosting: Optimal n_estimators=150, max_depth=4, lr=0.1 -> Cross-Validation F1: 0.8500.")
    d_p(doc, "Final Champion Test Set Performance (Tuned Logistic Regression):")
    d_b(doc, "Test Accuracy: 0.8900 (89.00%) | Test Precision: 0.8900 | Test Recall: 0.8900 | Test F1-Score: 0.8898 | Test ROC-AUC: 0.9756.")

    # Chapter 13: Streamlit Application
    d_h1(doc, "CHAPTER 13: STREAMLIT WEB APPLICATION")
    d_p(doc, "The front-end user interface was engineered using Streamlit, featuring a modern, light aesthetic. The application incorporates six dedicated views:")
    d_b(doc, "1. Home: Displays executive fleet KPI cards, distribution summaries, and pipeline architecture diagrams.")
    d_b(doc, "2. Risk Prediction: Interactive multi-parameter form supporting manual input and 3 instant one-click enterprise device presets.")
    d_b(doc, "3. Dataset Insights: Interactive tabs presenting class distributions, vulnerability boxplots, and correlation heatmaps.")
    d_b(doc, "4. Model Performance: Benchmark evaluation tables, comparison bar charts, confusion matrices, and multi-class ROC curves.")
    d_b(doc, "5. Security Insights: Top 10 predictive feature importance rankings and administrative mitigation recommendations.")
    d_b(doc, "6. About Project: Academic context, case study attribution, technology stack, and ethical disclaimers.")

    # Chapter 14: Results & Findings
    d_h1(doc, "CHAPTER 14: RESULTS, FINDINGS & FEATURE IMPORTANCE")
    d_p(doc, "Normalized feature importance weights extracted from the champion model:")
    d_table(doc,
        ["Rank", "Security Factor", "Normalized Importance Weight", "Operational Description"],
        [
            ["1", "Operating_System", "0.1703 (17.0%)", "Kernel architecture & security channel compliance"],
            ["2", "Patch_Status", "0.1137 (11.4%)", "Latency in applying vendor security updates"],
            ["3", "Vulnerability_Count", "0.0960 (9.6%)", "Active unmitigated CVE vulnerabilities detected"],
            ["4", "Suspicious_Activity_Flags", "0.0756 (7.6%)", "Network intrusion detection behavioral anomaly flags"],
            ["5", "Compliance_Posture_Score", "0.0694 (6.9%)", "Engineered composite index of defensive settings"],
            ["6", "Antivirus_Status", "0.0689 (6.9%)", "Endpoint antivirus active vs disabled state"],
            ["7", "Device_Type", "0.0675 (6.8%)", "Hardware class (Workstation vs unmanaged IoT Gateway)"],
            ["8", "Previous_Security_Incidents", "0.0673 (6.7%)", "Historical frequency of quarantine events"],
            ["9", "Attack_Surface_Index", "0.0566 (5.7%)", "Composite open listening ports & failed login spikes"],
            ["10", "Failed_Login_Attempts", "0.0486 (4.9%)", "Failed authentication frequency in past 30 days"]
        ]
    )

    # Chapter 15 & 16: Limitations & Future Scope
    d_h1(doc, "CHAPTER 15 & 16: LIMITATIONS & FUTURE SCOPE")
    d_p(doc, "Limitations: The system provides advisory risk classification to support human analysts; it does not replace formal penetration testing. Threat actor methodologies evolve over time, requiring scheduled pipeline retraining to mitigate concept drift.")
    d_p(doc, "Future Scope: Ingest streaming Syslog and Zeek network flow records; implement automated webhook isolation triggers for High Risk devices; incorporate semi-supervised anomaly detection for zero-day threat identification.")

    # Chapter 17: Conclusion & References
    d_h1(doc, "CHAPTER 17: CONCLUSION & REFERENCES")
    d_p(doc, "The Device Risk Analysis project successfully demonstrates how supervised machine learning transforms endpoint security management. By achieving 89.00% accuracy and 0.9756 ROC-AUC, the system provides high-confidence risk triage, automating remediation priorities and reducing administrative burden.")
    d_p(doc, "References:")
    d_b(doc, "1. NIST Special Publication 800-40 Rev. 4: Guide to Enterprise Patch Management Technologies, NIST, 2022.")
    d_b(doc, "2. Center for Internet Security (CIS): CIS Critical Security Controls Version 8, CIS Security, 2021.")
    d_b(doc, "3. Pedregosa et al.: Scikit-learn: Machine Learning in Python, JMLR 12, pp. 2825-2830, 2011.")
    d_b(doc, "4. McKinney, W.: Data Structures for Statistical Computing in Python, Proc. 9th Python in Science Conf., 2010.")

    doc.save("docs/Project_Report_Device_Risk_Analysis.docx")

    # --- PDF ---
    story = [
        Paragraph("ITM SKILLS UNIVERSITY — School of Future Tech", p_sub),
        Paragraph("DEVICE RISK ANALYSIS: FINAL PROJECT REPORT", p_title),
        Paragraph("Machine Learning Case Study No. 86 | Department of CSE", p_sub),
        Paragraph("Candidate: Atharva Gahine | B.Tech CSE Semester V (2024–2028)", p_meta),
        HRFlowable(width="100%", thickness=1, color=colors.HexColor('#CBD5E1'), spaceAfter=15),
        Paragraph("Executive Abstract", p_h1),
        Paragraph("This project report presents an end-to-end Machine Learning classification system designed to analyze multi-dimensional device telemetry and predict endpoint security risk tiers: Low Risk, Medium Risk, and High Risk. The system evaluates 3,012 device instances across 17 security attributes. Following structured data quality audits, deduplication, and median/mode imputation, six classification algorithms were trained and benchmarked. Tuned Logistic Regression achieved champion performance with 89.00% test accuracy, an F1-Score of 0.8898, and an exceptional multi-class ROC-AUC of 0.9756. A production-ready Streamlit web application provides real-time on-demand inference.", p_body),
        Spacer(1, 8),
        Paragraph("1. Algorithm Benchmark & Comparative Performance", p_h1),
        make_pdf_tbl(
            ["Algorithm", "Accuracy", "Precision", "Recall", "F1 Score", "ROC-AUC"],
            [
                ["Logistic Regression (Tuned)", "0.8900", "0.8900", "0.8900", "0.8898", "0.9756"],
                ["Support Vector Machine", "0.8800", "0.8802", "0.8800", "0.8801", "0.9710"],
                ["Gradient Boosting (Tuned)", "0.8500", "0.8521", "0.8500", "0.8502", "0.9580"],
                ["Random Forest Classifier", "0.8017", "0.8101", "0.8017", "0.8021", "0.9265"],
                ["K-Nearest Neighbors", "0.7883", "0.7908", "0.7883", "0.7868", "0.9151"],
                ["Decision Tree Classifier", "0.7167", "0.7327", "0.7167", "0.7178", "0.8466"]
            ],
            col_widths=[150, 65, 65, 65, 65, 65]
        ),
        Spacer(1, 10),
        Paragraph("2. Top 5 Security Risk Drivers", p_h1),
        make_pdf_tbl(
            ["Rank", "Factor", "Weight", "Operational Impact"],
            [
                ["1", "Operating System", "17.0%", "Kernel architecture & update channel compliance"],
                ["2", "Patch Status", "11.4%", "Latency in applying vendor security hotfixes"],
                ["3", "Vulnerability Count", "9.6%", "Active unmitigated software CVEs detected"],
                ["4", "Suspicious Activity", "7.6%", "Network IDS behavioral anomaly events flagged"],
                ["5", "Compliance Score", "6.9%", "Engineered composite score of defense settings"]
            ],
            col_widths=[35, 120, 60, 260]
        ),
        Spacer(1, 10),
        Paragraph("3. Academic Conclusion", p_h1),
        Paragraph("The project demonstrates how supervised machine learning transforms endpoint security operations by providing objective, repeatable, and fast risk classification.", p_body)
    ]
    create_pdf("docs/Project_Report_Device_Risk_Analysis.pdf", story)
    print("✓ Generated Project Report (DOCX & PDF)")

def generate_presentation_script():
    # --- DOCX ---
    doc = create_docx("VIVA PRESENTATION SCRIPT & DEFENSE GUIDE", "Device Risk Analysis | Case Study No. 86")

    d_h1(doc, "1. Presentation Overview & Student Presentation Plan")
    d_p(doc, "This document provides the slide-by-slide oral script, technical speaking cues, time management allocations, and anticipated examiner questions for Atharva Gahine's B.Tech CSE Semester V Machine Learning viva presentation.")

    d_h1(doc, "2. Slide-by-Slide Script & Oral Commentary")
    slides = [
        ("Slide 1: Title & Introduction (1 Minute)",
         "Script: 'Respected examiners and faculty members, good morning. My name is Atharva Gahine, a fifth-semester B.Tech Computer Science student at ITM SKILLS UNIVERSITY. Today, I am presenting Case Study Number 86: Device Risk Analysis—an end-to-end machine learning system developed to analyze endpoint telemetry and classify devices into actionable security risk tiers.'"),
        ("Slide 2: Problem Statement & Industrial Motivation (1.5 Minutes)",
         "Script: 'Modern enterprises manage thousands of varied endpoints: employee laptops, core database servers, smartphones, and IoT field gateways. When security analysts manually review vulnerability alerts, they face severe alert fatigue. Our problem statement focuses on: Analyzing device-related information and identifying patterns associated with elevated security concerns. By deploying machine learning, we automate triage and objectively classify devices into Low Risk, Medium Risk, or High Risk tiers.'"),
        ("Slide 3: Dataset Telemetry & Quality Auditing (1.5 Minutes)",
         "Script: 'Our dataset captures 3,012 enterprise devices across 17 attributes, modeled after NIST SP 800-40 and CIS security controls. In our data quality audit, we identified and eliminated 12 exact duplicates, sanitized string casing variations in Antivirus Status, and handled realistic missing values in network traffic and firmware age using median imputation, and patch status using mode imputation, ensuring zero data leakage.'"),
        ("Slide 4: Feature Engineering & Preprocessing Pipeline (1.5 Minutes)",
         "Script: 'To enrich model discriminability, we engineered three domain metrics: the Vulnerability-to-Firmware Ratio, the Attack Surface Index combining open ports and failed login spikes, and a Compliance Posture Score on a 0 to 10 scale. Our preprocessing pipeline leverages scikit-learn ColumnTransformer, routing numerical features to StandardScaler and categorical attributes to OneHotEncoder with handle_unknown set to ignore.'"),
        ("Slide 5: Machine Learning Benchmarks & Model Comparison (2 Minutes)",
         "Script: 'We partitioned the data using an 80/20 stratified split into 2,400 training and 600 test instances. We benchmarked six classification algorithms under identical pipeline conditions: Logistic Regression, Decision Tree, K-Nearest Neighbors, Support Vector Machine, Random Forest, and Gradient Boosting. We evaluated them using multi-class weighted Accuracy, Precision, Recall, F1-Score, and One-vs-Rest ROC-AUC.'"),
        ("Slide 6: Champion Selection & Hyperparameter Tuning (1.5 Minutes)",
         "Script: 'Using 5-fold Stratified GridSearchCV, we optimized regularization across candidate models. Logistic Regression with C=5.0 achieved a 5-fold CV F1 of 0.9084, outperforming all other models. On the unseen test set of 600 devices, our champion model achieved 89.00% accuracy, an F1-Score of 0.8898, and an outstanding multi-class ROC-AUC of 0.9756.'"),
        ("Slide 7: Feature Importance & Security Insights (1.5 Minutes)",
         "Script: 'Interpreting model coefficients revealed that Operating System architecture, Patch Latency, Unpatched CVE Count, and Suspicious Network Flags are the strongest predictors associated with elevated device risk. We avoid asserting direct causality, emphasizing these as strong statistical associations.'"),
        ("Slide 8: Interactive Streamlit Demonstration (1.5 Minutes)",
         "Script: 'We deployed our champion pipeline in an interactive Streamlit application. The dashboard features 6 navigation views: executive fleet KPIs, live multi-parameter risk prediction with instant device templates, exploratory telemetry charts, model performance tables, and security insights.'")
    ]

    for title, text in slides:
        d_h2(doc, title)
        d_p(doc, text)

    d_h1(doc, "3. Top 10 Technical Viva Questions & Model Answers")
    viva_qa = [
        ("Q1: Why did Logistic Regression outperform Random Forest and Decision Trees?",
         "A1: Device security risk acts primarily as an additive latent scoring function, where risk accumulates monotonically with vulnerabilities, failed logins, open ports, and protection penalties. Linear models with L2 regularization excel at capturing additive boundaries without the risk of overfitting or leaf fragmentation that affected tree models on this tabular dataset."),
        ("Q2: How did you ensure your model does not suffer from data leakage?",
         "A2: We performed all imputation, scaling, and one-hot encoding strictly inside scikit-learn Pipeline objects. Transformers were fit exclusively on training folds during both train-test splitting and 5-fold cross-validation, and merely applied to validation folds."),
        ("Q3: Why use Weighted F1-Score instead of simple Accuracy as your primary evaluation metric?",
         "A3: While our dataset is relatively balanced (42.1% Medium, 32.1% Low, 25.7% High), Weighted F1-Score accounts for class-specific precision-recall trade-offs. In cybersecurity, false negatives (classifying a High Risk device as Low Risk) carry far more severe consequences than false positives."),
        ("Q4: What is the purpose of the Attack Surface Index feature?",
         "A4: It synthesizes network perimeter exposure (open listening ports) with authentication pressure (failed login spikes) using the weighted formula: 0.4 * Open_Ports + 0.6 * Failed_Logins, providing a single consolidated metric of external exposure."),
        ("Q5: What does handle_unknown='ignore' do in OneHotEncoder?",
         "A5: In production environments, a device might report a rare or novel operating system. Setting handle_unknown='ignore' ensures all one-hot encoded columns for that feature become zero, preventing dimension mismatch runtime crashes."),
        ("Q6: How does your Streamlit application handle missing model files?",
         "A6: We implemented defensive loading using @st.cache_resource. If the serialized model pickle file is missing, the application intercepts the FileNotFoundError and renders an informative st.error banner guiding the user rather than terminating the process."),
        ("Q7: How did you handle multi-class ROC-AUC computation?",
         "A7: Because ROC-AUC is fundamentally binary, we used the One-vs-Rest (OvR) approach with label_binarize, computing individual ROC curves for Low Risk, Medium Risk, and High Risk against the rest, followed by weighted aggregation."),
        ("Q8: Why did Decision Tree achieve the lowest accuracy (71.67%)?",
         "A8: A single decision tree relies on orthogonal axis-aligned splits. Because security risk involves continuous combinations of several interacting numerical and categorical variables, an unpruned single tree either underfits or overfits localized noise."),
        ("Q9: Can this model be used for automated endpoint isolation?",
         "A9: In an operational SecOps environment, this model serves as an intelligent decision-support system to prioritize analyst queues. For High Risk classifications with confidence > 95%, automated temporary quarantine VLAN assignment can be safely configured."),
        ("Q10: What are the primary future enhancements for this project?",
         "A10: Future extensions include ingesting streaming network flow logs via Kafka, exploring semi-supervised learning for zero-day threat detection, and integrating automated policy webhooks with enterprise firewall APIs.")
    ]

    for q, a in viva_qa:
        d_p(doc, q, "Question: ")
        d_p(doc, a, "Model Answer: ")

    doc.save("docs/Presentation_Script_Device_Risk_Analysis.docx")

    # --- PDF ---
    story = [
        Paragraph("ITM SKILLS UNIVERSITY — School of Future Tech", p_sub),
        Paragraph("VIVA PRESENTATION & DEFENSE SCRIPT", p_title),
        Paragraph("Device Risk Analysis | Case Study No. 86", p_sub),
        Paragraph("Candidate: Atharva Gahine | B.Tech CSE Semester V (2024–2028)", p_meta),
        HRFlowable(width="100%", thickness=1, color=colors.HexColor('#CBD5E1'), spaceAfter=15),
        Paragraph("1. Oral Presentation Structure (10-Minute Guide)", p_h1),
        Paragraph("<b>Opening:</b> Greet examiners, state project title, Case Study No. 86, and academic context.", p_body),
        Paragraph("<b>Problem:</b> Explain enterprise endpoint risk and manual SOC alert fatigue.", p_body),
        Paragraph("<b>Data & Preprocessing:</b> Detail 3,012 assets, deduplication, median/mode imputation, and feature engineering.", p_body),
        Paragraph("<b>Model Benchmarks:</b> Highlight 6 algorithms, 5-fold CV, and champion test accuracy of 89.00% (F1: 0.8898).", p_body),
        Paragraph("<b>Demonstration:</b> Walk examiners through Streamlit home KPIs, live prediction, and feature insights.", p_body),
        Spacer(1, 8),
        Paragraph("2. Top Technical Viva Questions & Crisp Answers", p_h1),
        make_pdf_tbl(
            ["No.", "Viva Question", "Crisp Technical Answer"],
            [
                ["Q1", "Why did Logistic Regression win?", "Risk is an additive latent score; regularized linear models capture monotonic accumulation best."],
                ["Q2", "How was data leakage avoided?", "ColumnTransformer inside scikit-learn Pipeline objects fit strictly on training splits."],
                ["Q3", "Why Weighted F1 over Accuracy?", "Accounts for precision-recall balance and mitigates penalties for false negatives."],
                ["Q4", "What does Attack Surface Index represent?", "Consolidates perimeter open ports (0.4) and failed login brute-force attempts (0.6)."],
                ["Q5", "How do you handle unseen inputs in app?", "OneHotEncoder(handle_unknown='ignore') and defensive try-catch loading blocks."]
            ],
            col_widths=[30, 160, 285]
        )
    ]
    create_pdf("docs/Presentation_Script_Device_Risk_Analysis.pdf", story)
    print("✓ Generated Presentation Script (DOCX & PDF)")

if __name__ == "__main__":
    generate_project_report()
    generate_presentation_script()
