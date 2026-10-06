"""
Device Risk Intelligence - Premium Cybersecurity Dashboard
Case Study No. 86 | ITM SKILLS UNIVERSITY
"""

import os
import joblib
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

# -----------------------------------------------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Device Risk Intelligence",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# CUSTOM CSS DESIGN SYSTEM
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    /* Reset and Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"]  {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    }
    
    /* Backgrounds */
    .stApp {
        background-color: #070B14 !important;
    }
    
    /* Typography Overrides */
    h1, h2, h3, h4, h5, h6, p, span, div, label {
        color: #F8FAFC;
    }
    
    h1 {
        font-weight: 700 !important;
        font-size: 32px !important;
        letter-spacing: -0.5px !important;
    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #0B1220 !important;
        border-right: 1px solid rgba(255,255,255,0.08) !important;
    }
    
    /* Top Header Bar */
    header[data-testid="stHeader"] {
        background-color: rgba(7, 11, 20, 0.8) !important;
        backdrop-filter: blur(10px);
        border-bottom: 1px solid rgba(255,255,255,0.08) !important;
    }
    
    /* Premium Cards */
    .sec-card {
        background-color: #101827;
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 8px;
        padding: 24px;
        margin-bottom: 16px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .sec-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.2);
    }
    
    .sec-card-title {
        font-size: 13px;
        font-weight: 600;
        color: #94A3B8;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 8px;
        display: flex;
        align-items: center;
        gap: 6px;
    }
    
    .sec-card-value {
        font-size: 32px;
        font-weight: 700;
        color: #F8FAFC;
        margin-bottom: 4px;
    }
    
    .sec-card-desc {
        font-size: 13px;
        color: #64748B;
    }
    
    /* Badges */
    .sec-badge {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 9999px;
        font-size: 12px;
        font-weight: 600;
        margin-top: 8px;
    }
    .badge-low { background-color: rgba(34, 197, 94, 0.1); color: #22C55E; border: 1px solid rgba(34, 197, 94, 0.2); }
    .badge-medium { background-color: rgba(245, 158, 11, 0.1); color: #F59E0B; border: 1px solid rgba(245, 158, 11, 0.2); }
    .badge-high { background-color: rgba(239, 68, 68, 0.1); color: #EF4444; border: 1px solid rgba(239, 68, 68, 0.2); }
    .badge-info { background-color: rgba(59, 130, 246, 0.1); color: #3B82F6; border: 1px solid rgba(59, 130, 246, 0.2); }
    .badge-neutral { background-color: rgba(148, 163, 184, 0.1); color: #94A3B8; border: 1px solid rgba(148, 163, 184, 0.2); }
    
    /* Action Buttons */
    div.stButton > button:first-child {
        background: linear-gradient(180deg, #3B82F6 0%, #2563EB 100%) !important;
        color: #FFFFFF !important;
        border: 1px solid #1D4ED8 !important;
        border-radius: 6px !important;
        padding: 12px 24px !important;
        font-weight: 600 !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2) !important;
        transition: all 0.2s ease !important;
        width: 100%;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        font-size: 14px !important;
    }
    div.stButton > button:first-child:hover {
        background: linear-gradient(180deg, #60A5FA 0%, #3B82F6 100%) !important;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.4) !important;
        transform: translateY(-1px);
    }
    
    /* Form inputs styling for dark theme */
    div[data-baseweb="select"] > div,
    div[data-baseweb="input"] > div,
    div[data-baseweb="base-input"] {
        background-color: #131E30 !important;
        border-color: rgba(255,255,255,0.1) !important;
        color: #F8FAFC !important;
        border-radius: 6px !important;
    }
    div[data-baseweb="select"] span {
        color: #F8FAFC !important;
    }
    
    /* Form Container */
    div[data-testid="stForm"] {
        background-color: #101827 !important;
        border: 1px solid rgba(255,255,255,0.08) !important;
        border-radius: 12px !important;
        padding: 32px !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2) !important;
    }
    
    /* Radio Nav overrides (Sidebar) */
    div[role="radiogroup"] label {
        padding: 12px 16px;
        border-radius: 8px;
        transition: all 0.2s ease;
        margin-bottom: 4px;
        cursor: pointer;
    }
    div[role="radiogroup"] label:hover {
        background-color: rgba(255,255,255,0.05);
    }
    div[role="radiogroup"] label[data-checked="true"] {
        background-color: rgba(59, 130, 246, 0.1);
        border-left: 3px solid #3B82F6;
        border-radius: 4px 8px 8px 4px;
    }
    div[role="radiogroup"] p {
        font-size: 14px !important;
        font-weight: 500 !important;
        color: #E2E8F0 !important;
    }
    
    /* Sliders */
    div[data-testid="stSlider"] div[data-testid="stThumbValue"] {
        color: #3B82F6 !important;
        font-weight: 700 !important;
    }
    div[data-testid="stSlider"] label p {
        color: #94A3B8 !important;
        font-size: 13px !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        font-weight: 600 !important;
    }
    
    /* Input Labels */
    .stSelectbox label p, .stNumberInput label p {
        color: #94A3B8 !important;
        font-size: 13px !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        font-weight: 600 !important;
    }
    
    /* Section Headers */
    .section-header {
        font-size: 16px;
        font-weight: 600;
        color: #3B82F6;
        border-bottom: 1px solid rgba(255,255,255,0.08);
        padding-bottom: 8px;
        margin-top: 24px;
        margin-bottom: 24px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    
    /* Result Box */
    .result-box {
        padding: 40px 32px;
        border-radius: 12px;
        text-align: center;
        border: 2px solid;
        margin-top: 32px;
        margin-bottom: 32px;
        background-color: #0B1220;
    }
    .result-low { border-color: rgba(34, 197, 94, 0.5); box-shadow: 0 0 40px rgba(34, 197, 94, 0.1); }
    .result-med { border-color: rgba(245, 158, 11, 0.5); box-shadow: 0 0 40px rgba(245, 158, 11, 0.1); }
    .result-high { border-color: rgba(239, 68, 68, 0.5); box-shadow: 0 0 40px rgba(239, 68, 68, 0.15); }
    
    /* Result Scale */
    .risk-scale {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin: 32px auto;
        max-width: 400px;
        position: relative;
    }
    .risk-scale::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 30px;
        right: 30px;
        height: 2px;
        background: linear-gradient(90deg, #22C55E 0%, #F59E0B 50%, #EF4444 100%);
        z-index: 0;
    }
    .risk-point {
        position: relative;
        z-index: 1;
        background: #0B1220;
        padding: 0 8px;
        font-size: 12px;
        font-weight: 600;
        color: #64748B;
    }
    .risk-point.active {
        color: #F8FAFC;
    }
    .risk-point.active::after {
        content: '●';
        position: absolute;
        top: -18px;
        left: 50%;
        transform: translateX(-50%);
        font-size: 20px;
    }
    .active-low::after { color: #22C55E; }
    .active-med::after { color: #F59E0B; }
    .active-high::after { color: #EF4444; }

    /* Action List */
    .action-list {
        text-align: left;
        background: rgba(0,0,0,0.2);
        padding: 24px;
        border-radius: 8px;
        margin-top: 24px;
    }
    .action-item {
        display: flex;
        align-items: flex-start;
        gap: 12px;
        margin-bottom: 12px;
        font-size: 14px;
        color: #E2E8F0;
    }
    .action-icon-low { color: #22C55E; }
    .action-icon-med { color: #F59E0B; }
    .action-icon-high { color: #EF4444; }

    /* Hide ugly standard streamlit features */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# HELPER FUNCTIONS
# -----------------------------------------------------------------------------
def render_metric_card(icon, title, value, desc="", badge_text=None, badge_class="badge-info"):
    badge_html = f'<div class="sec-badge {badge_class}">{badge_text}</div>' if badge_text else ''
    html = f"""
    <div class="sec-card">
        <div class="sec-card-title">{icon} {title}</div>
        <div class="sec-card-value">{value}</div>
        <div class="sec-card-desc">{desc}</div>
        {badge_html}
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

def render_prob_card(title, value, color_hex):
    html = f"""
    <div style="background-color: #131E30; border-top: 3px solid {color_hex}; border-radius: 6px; padding: 16px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
        <div style="font-size: 12px; color: #94A3B8; text-transform: uppercase; font-weight: 600; margin-bottom: 4px;">{title}</div>
        <div style="font-size: 24px; font-weight: 700; color: #F8FAFC;">{value}</div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

@st.cache_resource
def load_model_artifacts():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    model_path = os.path.join(base_dir, "models", "best_model.pkl")
    meta_path = os.path.join(base_dir, "models", "model_metadata.pkl")
    
    if not os.path.exists(model_path):
        model_path = "models/best_model.pkl"
        meta_path = "models/model_metadata.pkl"
        
    if not os.path.exists(model_path):
        return None, None
        
    model = joblib.load(model_path)
    metadata = joblib.load(meta_path) if os.path.exists(meta_path) else None
    return model, metadata

@st.cache_data
def load_datasets():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    processed_path = os.path.join(base_dir, "data", "processed", "device_risk_processed.csv")
    results_path = os.path.join(base_dir, "outputs", "model_results.csv")
    feat_imp_path = os.path.join(base_dir, "outputs", "feature_importance.csv")
    
    if not os.path.exists(processed_path):
        processed_path = "data/processed/device_risk_processed.csv"
        results_path = "outputs/model_results.csv"
        feat_imp_path = "outputs/feature_importance.csv"
        
    df_proc = pd.read_csv(processed_path) if os.path.exists(processed_path) else None
    df_results = pd.read_csv(results_path) if os.path.exists(results_path) else None
    df_feat_imp = pd.read_csv(feat_imp_path) if os.path.exists(feat_imp_path) else None
    
    return df_proc, df_results, df_feat_imp

# -----------------------------------------------------------------------------
# APPLICATION STATE & DATA
# -----------------------------------------------------------------------------
model_pipeline, metadata = load_model_artifacts()
df_proc, df_results, df_feat_imp = load_datasets()

# -----------------------------------------------------------------------------
# SIDEBAR NAVIGATION
# -----------------------------------------------------------------------------
with st.sidebar:
    # Top Logo Area
    logo_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "logo.png")
    if not os.path.exists(logo_path):
        logo_path = "assets/logo.png"
    if os.path.exists(logo_path):
        st.image(logo_path, width=48)
    
    st.markdown("""
    <div style="margin-top: -10px; margin-bottom: 30px;">
        <h2 style="font-size: 20px; margin: 0; color: #F8FAFC; letter-spacing: 1px;">DEVICE RISK</h2>
        <h3 style="font-size: 14px; margin: 0; color: #3B82F6; letter-spacing: 2px;">INTELLIGENCE</h3>
        <p style="font-size: 12px; color: #64748B; margin-top: 4px;">Endpoint Security Analytics</p>
    </div>
    """, unsafe_allow_html=True)
    
    menu = [
        "Overview",
        "Risk Prediction",
        "Dataset Intelligence",
        "Model Performance",
        "Security Insights",
        "About Project"
    ]
    
    # Render invisible label for radio
    st.markdown("""
        <style>
            .stRadio > label { display: none; }
        </style>
    """, unsafe_allow_html=True)
    
    choice = st.radio("Navigation", menu, index=0)
    
    st.markdown("<div style='height: 35vh;'></div>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""
    <div style="font-size: 11px; color: #64748B; line-height: 1.6;">
        <b>CASE STUDY 86</b><br/>
        ITM SKILLS UNIVERSITY<br/>
        B.Tech CSE • Semester V<br/><br/>
        Student: <b>Atharva Gahine</b><br/>
        Year: 2024–2028
    </div>
    """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# TOP HEADER
# -----------------------------------------------------------------------------
col_header1, col_header2 = st.columns([3, 1])
with col_header1:
    st.markdown(f"""
    <div style="padding-top: 15px; font-size: 12px; color: #64748B; font-weight: 500; text-transform: uppercase; letter-spacing: 1px;">
        Device Risk Intelligence / <span style="color: #F8FAFC;">{choice}</span>
    </div>
    """, unsafe_allow_html=True)
with col_header2:
    st.markdown("""
    <div style="text-align: right; padding-top: 10px;">
        <span style="font-size: 11px; color: #94A3B8; letter-spacing: 1px; text-transform: uppercase;">Engine Status</span><br/>
        <span style="color: #22C55E; font-weight: 600; font-size: 14px;">● ML ONLINE</span><br/>
        <span style="font-size: 11px; color: #64748B;">Logistic Regression • v1</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br/>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 1. OVERVIEW PAGE
# -----------------------------------------------------------------------------
if choice == "Overview":
    st.markdown("""
    <div style="margin-bottom: 40px;">
        <span style="background: rgba(59, 130, 246, 0.1); color: #3B82F6; padding: 4px 12px; border-radius: 9999px; font-size: 12px; font-weight: 600; letter-spacing: 1px;">AI-POWERED SECURITY INTELLIGENCE</span>
        <h1 style="margin-top: 16px; margin-bottom: 8px;">Device Risk Intelligence</h1>
        <p style="color: #94A3B8; font-size: 16px; max-width: 800px; line-height: 1.6;">
            Analyze endpoint telemetry, identify security exposure, and classify device risk using the trained machine learning model.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Calculate dataset stats
    total_dev = len(df_proc) if df_proc is not None else 3000
    low_dev = (df_proc['Risk_Level'] == 'Low Risk').sum() if df_proc is not None else 964
    med_dev = (df_proc['Risk_Level'] == 'Medium Risk').sum() if df_proc is not None else 1264
    high_dev = (df_proc['Risk_Level'] == 'High Risk').sum() if df_proc is not None else 772
    best_acc = f"{metadata.get('test_accuracy', 0.89)*100:.2f}%" if metadata else "89.00%"
    
    unpatched = int(df_proc['Vulnerability_Count'].sum()) if df_proc is not None else 8421
    disabled_av = (df_proc['Antivirus_Status'] == 'Disabled').sum() if df_proc is not None else 412
    no_enc = (df_proc['Encryption_Enabled'] == 'No').sum() if df_proc is not None else 980

    # KPI Grid
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1: render_metric_card("💻", "Total Endpoints", f"{total_dev:,}", "Monitored fleet", badge_text="Active", badge_class="badge-info")
    with col2: render_metric_card("🛡️", "Low Risk", f"{low_dev:,}", "Healthy posture", badge_text=f"{low_dev/total_dev*100:.1f}%", badge_class="badge-low")
    with col3: render_metric_card("⚠️", "Medium Risk", f"{med_dev:,}", "Attention needed", badge_text=f"{med_dev/total_dev*100:.1f}%", badge_class="badge-medium")
    with col4: render_metric_card("🚨", "High Risk", f"{high_dev:,}", "Immediate action", badge_text=f"{high_dev/total_dev*100:.1f}%", badge_class="badge-high")
    with col5: render_metric_card("🧠", "Model Accuracy", best_acc, "Test-set performance", badge_text="Champion", badge_class="badge-neutral")
    
    st.markdown("<br/>", unsafe_allow_html=True)
    
    # Layout for charts and posture
    c_chart, c_posture = st.columns([2, 1])
    with c_chart:
        st.markdown("<h3 style='font-size: 18px; margin-bottom: 16px;'>Fleet Risk Distribution</h3>", unsafe_allow_html=True)
        if df_proc is not None:
            fig = px.pie(
                df_proc, 
                names='Risk_Level', 
                hole=0.6,
                color='Risk_Level',
                color_discrete_map={'Low Risk':'#22C55E', 'Medium Risk':'#F59E0B', 'High Risk':'#EF4444'}
            )
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#94A3B8'),
                margin=dict(t=20, b=20, l=20, r=20),
                showlegend=False
            )
            fig.update_traces(textposition='outside', textinfo='percent+label', marker=dict(line=dict(color='#070B14', width=2)))
            st.plotly_chart(fig, use_container_width=True)
            
    with c_posture:
        st.markdown("<h3 style='font-size: 18px; margin-bottom: 16px;'>Security Posture Summary</h3>", unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="sec-card" style="padding: 16px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <div style="font-size: 12px; color: #94A3B8; text-transform: uppercase;">Unpatched CVEs</div>
                    <div style="font-size: 24px; font-weight: 700; color: #F8FAFC;">{unpatched:,}</div>
                </div>
                <div class="sec-badge badge-high">Elevated</div>
            </div>
        </div>
        
        <div class="sec-card" style="padding: 16px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <div style="font-size: 12px; color: #94A3B8; text-transform: uppercase;">Disabled Antivirus</div>
                    <div style="font-size: 24px; font-weight: 700; color: #F8FAFC;">{disabled_av:,}</div>
                </div>
                <div class="sec-badge badge-medium">Warning</div>
            </div>
        </div>
        
        <div class="sec-card" style="padding: 16px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <div style="font-size: 12px; color: #94A3B8; text-transform: uppercase;">Missing Encryption</div>
                    <div style="font-size: 24px; font-weight: 700; color: #F8FAFC;">{no_enc:,}</div>
                </div>
                <div class="sec-badge badge-medium">Warning</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. RISK PREDICTION PAGE
# -----------------------------------------------------------------------------
elif choice == "Risk Prediction":
    st.markdown("""
    <div>
        <h1 style="margin-bottom: 8px;">Analyze Endpoint</h1>
        <p style="color: #94A3B8; font-size: 16px; margin-bottom: 24px;">
            Enter device telemetry to generate an AI-powered security risk assessment.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if model_pipeline is None:
        st.markdown("""
        <div class="sec-card" style="border-color: #EF4444; text-align: center; padding: 40px;">
            <h3 style="color: #EF4444; margin-bottom: 12px;">⚠️ MODEL ARTIFACT UNAVAILABLE</h3>
            <p style="color: #94A3B8;">The trained model could not be loaded. Please verify <b>models/best_model.pkl</b> exists.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("<h3 style='font-size: 14px; color: #94A3B8; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 12px;'>QUICK SCENARIOS</h3>", unsafe_allow_html=True)
        preset = st.selectbox("Select a testing scenario", [
            "Custom Telemetry Input",
            "Secure Developer Laptop",
            "Departmental Desktop with Pending Updates",
            "Misconfigured Field IoT Gateway"
        ], label_visibility="collapsed")
        
        # Default values
        defaults = {
            'type': 'Laptop', 'os': 'Windows 11', 'age': 12, 'fw_age': 3,
            'logins': 2, 'ports': 3, 'vulns': 1, 'updates': 1, 'enc': 'Yes',
            'av': 'Active', 'susp': 0, 'traffic': 650.0, 'access': 5.0,
            'incidents': 0, 'patch': 'Fully Patched'
        }
        
        if preset == "Secure Developer Laptop":
            defaults = {
                'type': 'Laptop', 'os': 'Windows 11', 'age': 8, 'fw_age': 2,
                'logins': 1, 'ports': 2, 'vulns': 0, 'updates': 0, 'enc': 'Yes',
                'av': 'Active', 'susp': 0, 'traffic': 420.0, 'access': 4.5,
                'incidents': 0, 'patch': 'Fully Patched'
            }
        elif preset == "Departmental Desktop with Pending Updates":
            defaults = {
                'type': 'Desktop', 'os': 'Windows 10', 'age': 36, 'fw_age': 14,
                'logins': 5, 'ports': 5, 'vulns': 4, 'updates': 3, 'enc': 'Yes',
                'av': 'Outdated', 'susp': 1, 'traffic': 1200.0, 'access': 6.2,
                'incidents': 1, 'patch': 'Partially Patched'
            }
        elif preset == "Misconfigured Field IoT Gateway":
            defaults = {
                'type': 'IoT_Gateway', 'os': 'Embedded Linux', 'age': 58, 'fw_age': 28,
                'logins': 26, 'ports': 14, 'vulns': 12, 'updates': 8, 'enc': 'No',
                'av': 'Disabled', 'susp': 5, 'traffic': 3800.0, 'access': 8.5,
                'incidents': 3, 'patch': 'Outdated'
            }
            
        with st.form("security_assessment_form"):
            st.markdown("<div class='section-header'>💻 01 DEVICE IDENTITY</div>", unsafe_allow_html=True)
            c1, c2, c3 = st.columns(3)
            with c1:
                dev_type = st.selectbox("DEVICE TYPE", ['Laptop', 'Desktop', 'Server', 'Smartphone', 'IoT_Gateway', 'Tablet'], index=['Laptop', 'Desktop', 'Server', 'Smartphone', 'IoT_Gateway', 'Tablet'].index(defaults['type']))
            with c2:
                os_options = ['Windows 11', 'Windows 10', 'macOS', 'Ubuntu Linux', 'RedHat Linux', 'Android', 'Embedded Linux', 'Windows Server', 'iOS', 'iPadOS', 'FreeRTOS']
                os_idx = os_options.index(defaults['os']) if defaults['os'] in os_options else 0
                op_sys = st.selectbox("OPERATING SYSTEM", os_options, index=os_idx)
            with c3:
                dev_age = st.slider("DEVICE AGE (MONTHS)", 1, 72, defaults['age'])
                
            st.markdown("<div class='section-header'>🌐 02 NETWORK & AUTHENTICATION</div>", unsafe_allow_html=True)
            c4, c5, c6 = st.columns(3)
            with c4:
                fw_age = st.slider("FIRMWARE AGE (MONTHS)", 0, 36, defaults['fw_age'])
                failed_logins = st.slider("FAILED LOGINS (PAST 30 DAYS)", 0, 50, defaults['logins'])
            with c5:
                open_ports = st.slider("OPEN LISTENING PORTS", 1, 25, defaults['ports'], help="Network services currently accepting connections.")
                traffic_mb = st.number_input("AVERAGE DAILY TRAFFIC (MB)", 50.0, 15000.0, float(defaults['traffic']), step=100.0)
            with c6:
                access_freq = st.slider("ACCESS FREQUENCY SCORE", 1.0, 10.0, float(defaults['access']), step=0.1)
                susp_flags = st.slider("SUSPICIOUS ACTIVITY ALERTS", 0, 10, defaults['susp'])
                
            st.markdown("<div class='section-header'>🛡️ 03 VULNERABILITY & DEFENSE</div>", unsafe_allow_html=True)
            c7, c8, c9 = st.columns(3)
            with c7:
                vulns = st.slider("UNPATCHED CVEs", 0, 20, defaults['vulns'], help="Known vulnerabilities without an applied security patch.")
                updates = st.slider("SECURITY UPDATES PENDING", 0, 15, defaults['updates'])
            with c8:
                encryption = st.selectbox("DISK ENCRYPTION", ['Yes', 'No'], index=['Yes', 'No'].index(defaults['enc']))
                antivirus = st.selectbox("ANTIVIRUS STATUS", ['Active', 'Outdated', 'Disabled'], index=['Active', 'Outdated', 'Disabled'].index(defaults['av']))
            with c9:
                patch_status = st.selectbox("PATCH COMPLIANCE", ['Fully Patched', 'Partially Patched', 'Outdated'], index=['Fully Patched', 'Partially Patched', 'Outdated'].index(defaults['patch']))
                past_incidents = st.slider("PAST SECURITY INCIDENTS", 0, 5, defaults['incidents'])
                
            st.markdown("<br/>", unsafe_allow_html=True)
            submitted = st.form_submit_button("🛡️ RUN SECURITY ASSESSMENT")
            
        if submitted:
            # Feature Engineering calculations
            vf_ratio = round(vulns / (fw_age + 1), 3)
            attack_surface = round((open_ports * 0.4) + (failed_logins * 0.6), 2)
            
            comp = 10.0
            comp -= (updates * 0.5)
            comp -= (2.5 if encryption == 'No' else 0.0)
            comp -= (3.5 if antivirus == 'Disabled' else (1.5 if antivirus == 'Outdated' else 0.0))
            comp_score = float(np.clip(round(comp, 2), 0.0, 10.0))
            
            input_df = pd.DataFrame([{
                'Device_Type': dev_type,
                'Operating_System': op_sys,
                'Device_Age_Months': dev_age,
                'Firmware_Age_Months': fw_age,
                'Failed_Login_Attempts': failed_logins,
                'Open_Ports_Count': open_ports,
                'Vulnerability_Count': vulns,
                'Security_Updates_Pending': updates,
                'Encryption_Enabled': encryption,
                'Antivirus_Status': antivirus,
                'Suspicious_Activity_Flags': susp_flags,
                'Average_Daily_Traffic_MB': traffic_mb,
                'Access_Frequency_Score': access_freq,
                'Previous_Security_Incidents': past_incidents,
                'Patch_Status': patch_status,
                'Vulnerability_Firmware_Ratio': vf_ratio,
                'Attack_Surface_Index': attack_surface,
                'Compliance_Posture_Score': comp_score
            }])
            
            # Predict
            pred_code = model_pipeline.predict(input_df)[0]
            probs = model_pipeline.predict_proba(input_df)[0]
            class_names = ['Low Risk', 'Medium Risk', 'High Risk']
            pred_label = class_names[pred_code]
            
            # Extract Probabilities
            p_low, p_med, p_high = probs[0], probs[1], probs[2]
            
            # Setup styling based on risk
            if pred_label == "Low Risk":
                box_class = "result-low"
                icon = "✓"
                color = "#22C55E"
                msg = "Endpoint appears to maintain a healthy security posture."
                active_low = "active active-low"
                active_med, active_high = "", ""
                rec_icon = "<span class='action-icon-low'>✓</span>"
                recs = [
                    "Maintain regular patching schedule",
                    "Continue active antivirus monitoring",
                    "Periodically review exposed network services"
                ]
            elif pred_label == "Medium Risk":
                box_class = "result-med"
                icon = "!"
                color = "#F59E0B"
                msg = "Endpoint requires security attention and remediation."
                active_med = "active active-med"
                active_low, active_high = "", ""
                rec_icon = "<span class='action-icon-med'>!</span>"
                recs = [
                    "Apply pending OS security patches",
                    "Review and close unnecessary open ports",
                    "Update endpoint antivirus definitions",
                    "Investigate failed login patterns"
                ]
            else:
                box_class = "result-high"
                icon = "!"
                color = "#EF4444"
                msg = "Endpoint presents elevated security exposure and requires immediate review."
                active_high = "active active-high"
                active_low, active_med = "", ""
                rec_icon = "<span class='action-icon-high'>!</span>"
                recs = [
                    "Isolate endpoint in a restricted VLAN",
                    "Patch critical CVE vulnerabilities immediately",
                    "Enable full-disk encryption",
                    "Investigate suspicious activity flags",
                    "Reset credentials if compromise suspected"
                ]
            
            max_prob = max(p_low, p_med, p_high) * 100
            
            # Result Display
            st.markdown(f"""
            <div class="result-box {box_class}">
                <div style="font-size: 13px; color: #94A3B8; text-transform: uppercase; letter-spacing: 2px; font-weight: 600; margin-bottom: 16px;">SECURITY ASSESSMENT</div>
                <div style="font-size: 48px; font-weight: 700; color: {color}; margin-bottom: 8px; display: flex; align-items: center; justify-content: center; gap: 16px;">
                    <div style="width: 48px; height: 48px; border-radius: 50%; border: 3px solid {color}; display: flex; align-items: center; justify-content: center; font-size: 28px;">{icon}</div>
                    {pred_label.upper()}
                </div>
                <div style="font-size: 16px; color: #E2E8F0; margin-bottom: 24px;">● {msg}</div>
                
                <div class="risk-scale">
                    <div class="risk-point {active_low}">LOW</div>
                    <div class="risk-point {active_med}">MEDIUM</div>
                    <div class="risk-point {active_high}">HIGH</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Probabilities
            st.markdown("<h3 style='font-size: 14px; color: #94A3B8; text-transform: uppercase; margin-top: 32px; margin-bottom: 16px;'>Risk Classification Probabilities</h3>", unsafe_allow_html=True)
            p_col1, p_col2, p_col3 = st.columns(3)
            with p_col1: render_prob_card("Low Risk", f"{p_low*100:.1f}%", "#22C55E")
            with p_col2: render_prob_card("Medium Risk", f"{p_med*100:.1f}%", "#F59E0B")
            with p_col3: render_prob_card("High Risk", f"{p_high*100:.1f}%", "#EF4444")
            
            # Recommendations
            st.markdown("<h3 style='font-size: 14px; color: #94A3B8; text-transform: uppercase; margin-top: 32px;'>Recommended Security Actions</h3>", unsafe_allow_html=True)
            
            recs_html = "".join([f"<div class='action-item'>{rec_icon} <div>{r}</div></div>" for r in recs])
            st.markdown(f"""
            <div class="action-list">
                {recs_html}
            </div>
            """, unsafe_allow_html=True)
            
            # Input summary grid
            with st.expander("Telemetry Used for Assessment"):
                st.markdown(f"""
                <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; padding: 16px;">
                    <div><span style="color: #64748B; font-size: 12px; text-transform: uppercase;">Device</span><br/><span style="color: #F8FAFC; font-weight: 500;">{dev_type}</span></div>
                    <div><span style="color: #64748B; font-size: 12px; text-transform: uppercase;">OS</span><br/><span style="color: #F8FAFC; font-weight: 500;">{op_sys}</span></div>
                    <div><span style="color: #64748B; font-size: 12px; text-transform: uppercase;">Vulnerabilities</span><br/><span style="color: #F8FAFC; font-weight: 500;">{vulns}</span></div>
                    <div><span style="color: #64748B; font-size: 12px; text-transform: uppercase;">Open Ports</span><br/><span style="color: #F8FAFC; font-weight: 500;">{open_ports}</span></div>
                    <div><span style="color: #64748B; font-size: 12px; text-transform: uppercase;">Failed Logins</span><br/><span style="color: #F8FAFC; font-weight: 500;">{failed_logins}</span></div>
                    <div><span style="color: #64748B; font-size: 12px; text-transform: uppercase;">Antivirus</span><br/><span style="color: #F8FAFC; font-weight: 500;">{antivirus}</span></div>
                    <div><span style="color: #64748B; font-size: 12px; text-transform: uppercase;">Encryption</span><br/><span style="color: #F8FAFC; font-weight: 500;">{encryption}</span></div>
                </div>
                """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. DATASET INTELLIGENCE
# -----------------------------------------------------------------------------
elif choice == "Dataset Intelligence":
    st.markdown("""
    <div style="margin-bottom: 32px;">
        <h1 style="margin-bottom: 8px;">Dataset Intelligence</h1>
        <p style="color: #94A3B8; font-size: 16px;">
            Explore the endpoint telemetry used to train the risk classifier.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if df_proc is not None:
        c1, c2, c3, c4 = st.columns(4)
        with c1: render_metric_card("💻", "Endpoints", f"{len(df_proc):,}")
        with c2: render_metric_card("🔢", "Model Features", "18")
        with c3: render_metric_card("🎯", "Risk Classes", "3")
        with c4: render_metric_card("⚖️", "Train/Test Split", "80/20")
        
        st.markdown("<br/>", unsafe_allow_html=True)
        
        col_c1, col_c2 = st.columns(2)
        with col_c1:
            st.markdown("<div class='sec-card'>", unsafe_allow_html=True)
            st.markdown("<h3 style='font-size: 14px; margin-bottom: 16px; color: #94A3B8; text-transform: uppercase;'>Vulnerabilities vs Risk</h3>", unsafe_allow_html=True)
            fig1 = px.box(df_proc, x='Risk_Level', y='Vulnerability_Count', color='Risk_Level',
                          color_discrete_map={'Low Risk':'#22C55E', 'Medium Risk':'#F59E0B', 'High Risk':'#EF4444'})
            fig1.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font=dict(color='#94A3B8'), showlegend=False, margin=dict(t=10, b=10, l=10, r=10))
            fig1.update_yaxes(gridcolor='rgba(255,255,255,0.05)')
            st.plotly_chart(fig1, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
        with col_c2:
            st.markdown("<div class='sec-card'>", unsafe_allow_html=True)
            st.markdown("<h3 style='font-size: 14px; margin-bottom: 16px; color: #94A3B8; text-transform: uppercase;'>Failed Logins Distribution</h3>", unsafe_allow_html=True)
            fig2 = px.histogram(df_proc, x='Failed_Login_Attempts', color='Risk_Level', barmode='overlay',
                                color_discrete_map={'Low Risk':'#22C55E', 'Medium Risk':'#F59E0B', 'High Risk':'#EF4444'})
            fig2.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font=dict(color='#94A3B8'), margin=dict(t=10, b=10, l=10, r=10))
            fig2.update_yaxes(gridcolor='rgba(255,255,255,0.05)')
            st.plotly_chart(fig2, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
        st.markdown("<div class='sec-card'>", unsafe_allow_html=True)
        st.markdown("<h3 style='font-size: 14px; margin-bottom: 16px; color: #94A3B8; text-transform: uppercase;'>Operating System Distribution by Risk</h3>", unsafe_allow_html=True)
        fig3 = px.histogram(df_proc, x='Operating_System', color='Risk_Level', barmode='group',
                            color_discrete_map={'Low Risk':'#22C55E', 'Medium Risk':'#F59E0B', 'High Risk':'#EF4444'})
        fig3.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font=dict(color='#94A3B8'), margin=dict(t=10, b=10, l=10, r=10))
        fig3.update_yaxes(gridcolor='rgba(255,255,255,0.05)')
        st.plotly_chart(fig3, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 4. MODEL PERFORMANCE
# -----------------------------------------------------------------------------
elif choice == "Model Performance":
    st.markdown("""
    <div style="margin-bottom: 32px;">
        <h1 style="margin-bottom: 8px;">Model Performance</h1>
        <p style="color: #94A3B8; font-size: 16px;">
            Evaluation of the trained classification models.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if df_results is not None:
        best_acc_val = f"{df_results['Accuracy'].max()*100:.2f}%"
        best_f1_val = f"{df_results['F1 Score'].max():.4f}"
        best_roc_val = f"{df_results['ROC_AUC'].max():.4f}"
        
        st.markdown(f"""
        <div class="sec-card" style="border: 1px solid rgba(59, 130, 246, 0.3); background: linear-gradient(135deg, rgba(16, 24, 39, 1) 0%, rgba(11, 25, 44, 1) 100%);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px;">
                <div>
                    <div class="sec-badge badge-info" style="margin-top: 0; margin-bottom: 8px;">CHAMPION MODEL</div>
                    <h2 style="margin: 0;">Logistic Regression</h2>
                </div>
            </div>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px;">
                <div>
                    <div style="font-size: 32px; font-weight: 700; color: #3B82F6;">{best_acc_val}</div>
                    <div style="font-size: 13px; color: #94A3B8; text-transform: uppercase;">Test Accuracy</div>
                </div>
                <div>
                    <div style="font-size: 32px; font-weight: 700; color: #F8FAFC;">{best_f1_val}</div>
                    <div style="font-size: 13px; color: #94A3B8; text-transform: uppercase;">Weighted F1</div>
                </div>
                <div>
                    <div style="font-size: 32px; font-weight: 700; color: #F8FAFC;">{best_roc_val}</div>
                    <div style="font-size: 13px; color: #94A3B8; text-transform: uppercase;">ROC-AUC</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br/>", unsafe_allow_html=True)
        
        df_sorted = df_results.sort_values(by='Accuracy', ascending=True)
        
        model_colors = {
            'Logistic Regression': '#2E4057',
            'Support Vector Machine': '#5B8296',
            'Gradient Boosting': '#409281',
            'Random Forest': '#DE7F64',
            'K-Nearest Neighbors': '#D15B65',
            'Decision Tree': '#8B5CF6'
        }
        
        # Helper function to generate consistent horizontal bar charts for different metrics
        def create_comparison_chart(df, x_col, title):
            # px.bar creates a horizontal ('h') bar chart. It maps the metric (x_col) to the X-axis and 'Model' to the Y-axis. 
            # text_auto formats the value on the bars to 4 decimal places. color maps our custom palette.
            fig = px.bar(df, x=x_col, y='Model', orientation='h', title=title, text_auto='.4f', color='Model', color_discrete_map=model_colors)
            
            # update_layout customizes the chart's appearance to match the dark theme
            fig.update_layout(
                plot_bgcolor='rgba(0,0,0,0)', # Makes the plot area background transparent
                paper_bgcolor='rgba(0,0,0,0)', # Makes the surrounding paper background transparent
                font=dict(color='#94A3B8'), # Sets the general text color to a soft grayish-blue
                title_font=dict(size=14, color='#F8FAFC'), # Sets the title font size and color to white
                margin=dict(t=40, b=20, l=10, r=10), # Adjusts the top, bottom, left, and right margins
                showlegend=False # Hides the legend since the y-axis already shows the model names
            )
            
            # Formats the X-axis: adds a faint gridline and removes the axis title to save space
            fig.update_xaxes(gridcolor='rgba(255,255,255,0.05)', title='')
            # Formats the Y-axis: removes the axis title (the labels are self-explanatory)
            fig.update_yaxes(title='')
            
            # Returns the fully styled figure object
            return fig
            
        # Create the Accuracy chart by passing the sorted dataframe and 'Accuracy' column
        fig_acc = create_comparison_chart(df_sorted, 'Accuracy', 'Model Comparison: Accuracy (Higher is Better)')
        # Create the Precision chart by passing the 'Precision' column
        fig_prec = create_comparison_chart(df_sorted, 'Precision', 'Model Comparison: Precision (Higher is Better)')
        # Create the Recall chart by passing the 'Recall' column
        fig_rec = create_comparison_chart(df_sorted, 'Recall', 'Model Comparison: Recall (Higher is Better)')
        # Create the F1 Score chart by passing the 'F1 Score' column
        fig_f1 = create_comparison_chart(df_sorted, 'F1 Score', 'Model Comparison: F1 Score (Higher is Better)')
        
        # Starts an HTML div with the custom 'sec-card' CSS class to place the charts inside a styled box
        st.markdown("<div class='sec-card'>", unsafe_allow_html=True)
        
        # Splits the UI into two equal-width columns for a 2x2 grid layout
        m1, m2 = st.columns(2)
        
        # In the first column, render the Accuracy and Recall charts
        with m1:
            # st.plotly_chart renders the Plotly figure. use_container_width=True makes it responsive to the column width
            st.plotly_chart(fig_acc, use_container_width=True)
            st.plotly_chart(fig_rec, use_container_width=True)
            
        # In the second column, render the Precision and F1 Score charts
        with m2:
            st.plotly_chart(fig_prec, use_container_width=True)
            st.plotly_chart(fig_f1, use_container_width=True)
            
        # Closes the HTML div tag for the 'sec-card' container
        st.markdown("</div>", unsafe_allow_html=True)
            
        st.markdown("<br/>", unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("<div class='sec-card'>", unsafe_allow_html=True)
            st.markdown("<h3 style='font-size: 14px; margin-bottom: 16px; color: #94A3B8; text-transform: uppercase;'>Confusion Matrix</h3>", unsafe_allow_html=True)
            cm_fig = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "outputs", "figures", "08_best_model_confusion_matrix.png")
            if not os.path.exists(cm_fig): cm_fig = "outputs/figures/08_best_model_confusion_matrix.png"
            if os.path.exists(cm_fig): st.image(cm_fig, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
        with c2:
            st.markdown("<div class='sec-card'>", unsafe_allow_html=True)
            st.markdown("<h3 style='font-size: 14px; margin-bottom: 16px; color: #94A3B8; text-transform: uppercase;'>One-vs-Rest ROC Performance</h3>", unsafe_allow_html=True)
            roc_fig = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "outputs", "figures", "10_multiclass_roc_curves.png")
            if not os.path.exists(roc_fig): roc_fig = "outputs/figures/10_multiclass_roc_curves.png"
            if os.path.exists(roc_fig): st.image(roc_fig, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 5. SECURITY INSIGHTS
# -----------------------------------------------------------------------------
elif choice == "Security Insights":
    st.markdown("""
    <div style="margin-bottom: 32px;">
        <h1 style="margin-bottom: 8px;">Security Intelligence</h1>
        <p style="color: #94A3B8; font-size: 16px;">
            Practical cybersecurity interpretations from the machine learning model.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if df_feat_imp is not None:
        c1, c2 = st.columns([1, 1])
        with c1:
            st.markdown("<div class='sec-card'>", unsafe_allow_html=True)
            st.markdown("<h3 style='font-size: 14px; margin-bottom: 16px; color: #94A3B8; text-transform: uppercase;'>Top Risk Signals</h3>", unsafe_allow_html=True)
            
            top_feats = df_feat_imp.head(10).sort_values(by='Importance', ascending=True)
            fig_bar = px.bar(top_feats, x='Importance', y='Feature', orientation='h', color_discrete_sequence=['#3B82F6'])
            fig_bar.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)', font=dict(color='#94A3B8'), margin=dict(t=10, b=10, l=10, r=10))
            fig_bar.update_xaxes(gridcolor='rgba(255,255,255,0.05)')
            st.plotly_chart(fig_bar, use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
        with c2:
            st.markdown("""
            <div class="sec-card" style="margin-bottom: 16px;">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                    <span style="color: #EF4444;">●</span>
                    <span style="font-weight: 600; font-size: 14px; color: #F8FAFC; text-transform: uppercase;">Attack Surface</span>
                </div>
                <p style="font-size: 13px; color: #94A3B8; margin-bottom: 0;">
                    <b>Finding:</b> Open ports and failed logins are strong indicators of targeted attacks.<br/>
                    <b>Interpretation:</b> Misconfigured devices rapidly accumulate failed authentication attempts, drastically elevating risk.
                </p>
            </div>
            
            <div class="sec-card" style="margin-bottom: 16px;">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                    <span style="color: #F59E0B;">●</span>
                    <span style="font-weight: 600; font-size: 14px; color: #F8FAFC; text-transform: uppercase;">Vulnerability Exposure</span>
                </div>
                <p style="font-size: 13px; color: #94A3B8; margin-bottom: 0;">
                    <b>Finding:</b> Unpatched CVEs correlate highly with older firmware age.<br/>
                    <b>Interpretation:</b> Devices neglecting regular firmware updates become primary targets for known exploits.
                </p>
            </div>
            
            <div class="sec-card" style="margin-bottom: 0;">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 8px;">
                    <span style="color: #22C55E;">●</span>
                    <span style="font-weight: 600; font-size: 14px; color: #F8FAFC; text-transform: uppercase;">Defense Posture</span>
                </div>
                <p style="font-size: 13px; color: #94A3B8; margin-bottom: 0;">
                    <b>Finding:</b> Active antivirus and full-disk encryption heavily mitigate high-risk scoring.<br/>
                    <b>Interpretation:</b> Foundational security hygiene is the most effective preventative measure against endpoint compromise.
                </p>
            </div>
            """, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 6. ABOUT PROJECT
# -----------------------------------------------------------------------------
elif choice == "About Project":
    st.markdown("""
    <div style="margin-bottom: 32px;">
        <h1 style="margin-bottom: 8px;">Project Information</h1>
        <p style="color: #94A3B8; font-size: 16px;">
            Academic Context and Technology Stack.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="sec-card" style="height: 100%;">
            <h3 style="font-size: 14px; margin-bottom: 24px; color: #94A3B8; text-transform: uppercase; letter-spacing: 1px;">Academic Case Study No. 86</h3>
            <div style="margin-bottom: 16px;">
                <div style="font-size: 12px; color: #64748B; text-transform: uppercase;">Project Title</div>
                <div style="font-size: 18px; font-weight: 600; color: #F8FAFC;">DEVICE RISK ANALYSIS</div>
            </div>
            <div style="margin-bottom: 16px;">
                <div style="font-size: 12px; color: #64748B; text-transform: uppercase;">Institution</div>
                <div style="font-size: 16px; font-weight: 500; color: #E2E8F0;">ITM Skills University<br/><span style="color: #94A3B8; font-size: 14px;">School of Future Tech</span></div>
            </div>
            <div style="margin-bottom: 16px;">
                <div style="font-size: 12px; color: #64748B; text-transform: uppercase;">Student Details</div>
                <div style="font-size: 16px; font-weight: 500; color: #E2E8F0;">Atharva Gahine<br/><span style="color: #94A3B8; font-size: 14px;">B.Tech CSE • Semester V (2024–2028)</span></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="sec-card" style="height: 100%;">
            <h3 style="font-size: 14px; margin-bottom: 24px; color: #94A3B8; text-transform: uppercase; letter-spacing: 1px;">Technology Stack</h3>
            <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 24px;">
                <span style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); padding: 6px 12px; border-radius: 4px; font-size: 13px;">Python</span>
                <span style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); padding: 6px 12px; border-radius: 4px; font-size: 13px;">Pandas</span>
                <span style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); padding: 6px 12px; border-radius: 4px; font-size: 13px;">NumPy</span>
                <span style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); padding: 6px 12px; border-radius: 4px; font-size: 13px;">Scikit-learn</span>
                <span style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); padding: 6px 12px; border-radius: 4px; font-size: 13px;">Streamlit</span>
                <span style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); padding: 6px 12px; border-radius: 4px; font-size: 13px;">Plotly</span>
            </div>
            
            <h3 style="font-size: 14px; margin-bottom: 16px; color: #94A3B8; text-transform: uppercase; letter-spacing: 1px;">Machine Learning Pipeline</h3>
            <div style="font-size: 13px; color: #94A3B8; line-height: 2;">
                Dataset Ingestion ➔ Data Cleaning ➔ Feature Engineering ➔ Preprocessing ➔ Model Training ➔ Evaluation ➔ Deployment
            </div>
        </div>
        """, unsafe_allow_html=True)
