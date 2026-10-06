"""
Script to generate the Enterprise Device Security & Risk Profile Dataset.
Specifically created for academic demonstration (Case Study No. 86 - ITM SKILLS UNIVERSITY).
Dataset Name: Enterprise Device Security & Risk Profile Dataset (Academic Benchmark)
Author: Atharva Gahine (B.Tech CSE Semester V)
"""

import numpy as np
import pandas as pd
import os

def generate_device_risk_dataset(n_samples=3000, random_state=42):
    np.random.seed(random_state)
    
    # 1. Device Identifiers
    device_ids = [f"DEV-{1000 + i}" for i in range(n_samples)]
    
    # 2. Device Types
    device_types = ['Laptop', 'Desktop', 'Server', 'Smartphone', 'IoT_Gateway', 'Tablet']
    p_dev = [0.35, 0.20, 0.12, 0.18, 0.10, 0.05]
    chosen_types = np.random.choice(device_types, size=n_samples, p=p_dev)
    
    # 3. Operating System depending on device type
    os_list = []
    for dt in chosen_types:
        if dt in ['Laptop', 'Desktop']:
            os_list.append(np.random.choice(['Windows 11', 'Windows 10', 'macOS', 'Ubuntu Linux'], p=[0.40, 0.35, 0.15, 0.10]))
        elif dt == 'Server':
            os_list.append(np.random.choice(['Ubuntu Linux', 'RedHat Linux', 'Windows Server'], p=[0.45, 0.40, 0.15]))
        elif dt == 'Smartphone':
            os_list.append(np.random.choice(['Android', 'iOS'], p=[0.70, 0.30]))
        elif dt == 'IoT_Gateway':
            os_list.append(np.random.choice(['Embedded Linux', 'FreeRTOS'], p=[0.85, 0.15]))
        else: # Tablet
            os_list.append(np.random.choice(['Android', 'iPadOS', 'Windows 11'], p=[0.55, 0.35, 0.10]))
            
    # 4. Device Age (Months): 1 to 72 months
    device_age_months = np.random.randint(1, 73, size=n_samples)
    
    # 5. Firmware Age (Months): 0 to 36 months, correlated with device age
    firmware_age_months = np.clip((device_age_months * 0.4 + np.random.normal(2, 4, size=n_samples)).astype(int), 0, 36)
    
    # 6. Failed Login Attempts (past 30 days): Poisson distribution
    failed_logins = np.random.poisson(lam=3.5, size=n_samples)
    # inject occasional brute-force spikes
    spike_idx = np.random.choice(n_samples, size=int(0.08 * n_samples), replace=False)
    failed_logins[spike_idx] += np.random.randint(10, 35, size=len(spike_idx))
    failed_logins = np.clip(failed_logins, 0, 50)
    
    # 7. Open Ports Count: typical devices have 1-5, servers 5-15, misconfigured have more
    open_ports = []
    for dt in chosen_types:
        if dt == 'Server':
            open_ports.append(np.random.randint(4, 18))
        elif dt == 'IoT_Gateway':
            open_ports.append(np.random.randint(1, 10))
        else:
            open_ports.append(np.random.randint(1, 7))
    open_ports = np.array(open_ports)
    # random misconfiguration
    misconf_idx = np.random.choice(n_samples, size=int(0.06 * n_samples), replace=False)
    open_ports[misconf_idx] += np.random.randint(5, 14, size=len(misconf_idx))
    
    # 8. Vulnerability Count (CVEs)
    # Older firmware & unpatched devices have more
    vuln_base = (firmware_age_months / 6.0) + np.random.exponential(scale=1.5, size=n_samples)
    vulnerability_count = np.clip(vuln_base.astype(int), 0, 20)
    
    # 9. Security Updates Pending
    updates_pending = np.clip(np.random.poisson(lam=1.8, size=n_samples) + (firmware_age_months // 6), 0, 15)
    
    # 10. Encryption Enabled: Yes / No
    # Servers & mobile often encrypted, IoT rarely
    encryption = []
    for dt in chosen_types:
        if dt == 'IoT_Gateway':
            encryption.append(np.random.choice(['Yes', 'No'], p=[0.25, 0.75]))
        elif dt in ['Laptop', 'Smartphone']:
            encryption.append(np.random.choice(['Yes', 'No'], p=[0.75, 0.25]))
        else:
            encryption.append(np.random.choice(['Yes', 'No'], p=[0.65, 0.35]))
    encryption = np.array(encryption)
    
    # 11. Antivirus / Endpoint Protection Status: Active, Outdated, Disabled
    antivirus = np.random.choice(['Active', 'Outdated', 'Disabled'], size=n_samples, p=[0.68, 0.20, 0.12])
    
    # 12. Suspicious Activity Flags (Network anomaly count): 0 to 10
    suspicious_flags = np.random.poisson(lam=0.6, size=n_samples)
    susp_spike = np.random.choice(n_samples, size=int(0.07 * n_samples), replace=False)
    suspicious_flags[susp_spike] += np.random.randint(2, 7, size=len(susp_spike))
    suspicious_flags = np.clip(suspicious_flags, 0, 10)
    
    # 13. Average Daily Network Traffic (MB)
    traffic_mb = []
    for dt in chosen_types:
        if dt == 'Server':
            traffic_mb.append(np.random.gamma(shape=5, scale=1200))
        elif dt in ['Laptop', 'Desktop']:
            traffic_mb.append(np.random.gamma(shape=3, scale=500))
        elif dt == 'IoT_Gateway':
            traffic_mb.append(np.random.gamma(shape=2, scale=150))
        else:
            traffic_mb.append(np.random.gamma(shape=2, scale=350))
    traffic_mb = np.clip(np.round(traffic_mb, 1), 50.0, 15000.0)
    
    # 14. Access Frequency Score (1.0 to 10.0)
    access_freq = np.clip(np.round(np.random.normal(5.5, 2.0, size=n_samples), 1), 1.0, 10.0)
    
    # 15. Previous Security Incidents (0 to 5)
    past_incidents = np.random.choice([0, 1, 2, 3, 4], size=n_samples, p=[0.65, 0.20, 0.09, 0.04, 0.02])
    
    # 16. Patch Status: Fully Patched, Partially Patched, Outdated
    patch_status = []
    for upd in updates_pending:
        if upd == 0:
            patch_status.append('Fully Patched')
        elif upd <= 3:
            patch_status.append(np.random.choice(['Fully Patched', 'Partially Patched'], p=[0.3, 0.7]))
        elif upd <= 6:
            patch_status.append(np.random.choice(['Partially Patched', 'Outdated'], p=[0.6, 0.4]))
        else:
            patch_status.append('Outdated')
    patch_status = np.array(patch_status)
    
    # 17. Calculated Composite Security Risk Score based on standard NIST/CIS vulnerability criteria
    # Latent score calculation:
    score = (
        vulnerability_count * 4.2 +
        updates_pending * 2.8 +
        failed_logins * 1.5 +
        suspicious_flags * 5.0 +
        open_ports * 1.2 +
        (firmware_age_months / 36.0) * 12.0 +
        (device_age_months / 72.0) * 6.0 +
        past_incidents * 6.5 +
        (encryption == 'No') * 10.0 +
        (antivirus == 'Disabled') * 16.0 +
        (antivirus == 'Outdated') * 8.0 +
        (patch_status == 'Outdated') * 10.0 +
        (patch_status == 'Partially Patched') * 4.0 +
        np.random.normal(0, 4.5, size=n_samples) # realistic noise & unobserved factors
    )
    
    # Categorization into 3 tiers based on realistic risk percentiles:
    # ~32% Low Risk, ~42% Medium Risk, ~26% High Risk
    p32 = np.percentile(score, 32)
    p74 = np.percentile(score, 74)
    risk_level = []
    for s in score:
        if s <= p32:
            risk_level.append('Low Risk')
        elif s <= p74:
            risk_level.append('Medium Risk')
        else:
            risk_level.append('High Risk')
            
    df = pd.DataFrame({
        'Device_ID': device_ids,
        'Device_Type': chosen_types,
        'Operating_System': os_list,
        'Device_Age_Months': device_age_months,
        'Firmware_Age_Months': firmware_age_months,
        'Failed_Login_Attempts': failed_logins,
        'Open_Ports_Count': open_ports,
        'Vulnerability_Count': vulnerability_count,
        'Security_Updates_Pending': updates_pending,
        'Encryption_Enabled': encryption,
        'Antivirus_Status': antivirus,
        'Suspicious_Activity_Flags': suspicious_flags,
        'Average_Daily_Traffic_MB': traffic_mb,
        'Access_Frequency_Score': access_freq,
        'Previous_Security_Incidents': past_incidents,
        'Patch_Status': patch_status,
        'Risk_Level': risk_level
    })
    
    # Add realistic raw imperfections to demonstrate academic data cleaning:
    # 1. Realistic Missing values (~1.5% - 2.5% in 3 columns)
    nan_idx1 = np.random.choice(n_samples, size=45, replace=False)
    df.loc[nan_idx1, 'Average_Daily_Traffic_MB'] = np.nan
    
    nan_idx2 = np.random.choice(n_samples, size=35, replace=False)
    df.loc[nan_idx2, 'Firmware_Age_Months'] = np.nan
    
    nan_idx3 = np.random.choice(n_samples, size=25, replace=False)
    df.loc[nan_idx3, 'Patch_Status'] = np.nan
    
    # 2. Add 12 duplicate rows at the end to demonstrate duplicate handling
    dups = df.sample(12, random_state=101)
    df = pd.concat([df, dups], ignore_index=True)
    
    # 3. Minor casing variation in Antivirus_Status (e.g., 'active', 'ACTIVE' vs 'Active')
    case_idx = np.random.choice(n_samples, size=15, replace=False)
    df.loc[case_idx[:8], 'Antivirus_Status'] = 'active'
    df.loc[case_idx[8:], 'Antivirus_Status'] = 'ACTIVE'
    
    return df

if __name__ == "__main__":
    df = generate_device_risk_dataset(n_samples=3000, random_state=42)
    os.makedirs("data/raw", exist_ok=True)
    raw_path = "data/raw/device_risk_raw.csv"
    df.to_csv(raw_path, index=False)
    print(f"Generated raw dataset saved to: {raw_path}")
    print(f"Shape: {df.shape}")
    print("Class distribution:")
    print(df['Risk_Level'].value_counts())
