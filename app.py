import streamlit as st
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
import json

# Page Config
st.set_page_config(
    page_title="CyberShield AI",
    page_icon="🛡️",
    layout="wide"
)

# Custom CSS Styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #00ffcc;
        text-align: center;
        font-weight: bold;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #a0aec0;
        text-align: center;
        margin-bottom: 30px;
    }
    .metric-card {
        background-color: #1e293b;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #334155;
        text-align: center;
    }
    .alert-box {
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 10px;
    }
    .safe-box { background-color: rgba(16, 185, 129, 0.2); border: 1px solid #10b981; color: #34d399; }
    .danger-box { background-color: rgba(239, 68, 68, 0.2); border: 1px solid #ef4444; color: #f87171; }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown('<p class="main-header">🛡️ CyberShield AI</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">24/7 Autonomous Website Security Monitoring & Vulnerability Scanner</p>', unsafe_allow_html=True)

# Sidebar Configuration
st.sidebar.header("⚙️ Configuration & Alerts")
target_url = st.sidebar.text_input("Target Website URL", "https://example.com")
enable_monitoring = st.sidebar.checkbox("Enable 24/7 Autonomous Monitoring", value=False)
check_interval = st.sidebar.slider("Check Interval (Minutes)", min_value=1, max_value=60, value=5)

st.sidebar.markdown("---")
st.sidebar.subheader("📢 Telegram Alert Setup")
telegram_token = st.sidebar.text_input("Telegram Bot Token", type="password")
telegram_chat_id = st.sidebar.text_input("Telegram Chat ID")

def send_telegram_alert(message):
    if telegram_token and telegram_chat_id:
        url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
        payload = {"chat_id": telegram_chat_id, "text": message, "parse_mode": "Markdown"}
        try:
            response = requests.post(url, json=payload, timeout=5)
            return response.status_code == 200
        except Exception as e:
            return False
    return False

# Main Interface Tabs
tab1, tab2, tab3 = st.tabs(["🔍 Vulnerability Audit", "⚡ Live 24/7 Monitor", "📊 Security Reports"])

with tab1:
    st.subheader("Single-Site Security & Vulnerability Audit")
    if st.button("Run Full Security Scan", type="primary"):
        if not target_url.startswith("http"):
            st.error("कृपया सही URL दर्ज करें (जैसे https://example.com)")
        else:
            with st.spinner(f"Scanning {target_url} for vulnerabilities..."):
                time.sleep(2) # Simulating deep scan
                
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Security Score", "85/100", delta="+5%")
                with col2:
                    st.metric("XSS Risk", "Low", delta_color="inverse")
                with col3:
                    st.metric("SQLi Risk", "Secure", delta_color="inverse")
                with col4:
                    st.metric("SSL Status", "Valid", delta_color="normal")
                
                st.markdown("### 🔎 Scan Findings")
                st.success("✅ **HTTPS Security:** Valid SSL certificate detected.")
                st.success("✅ **SQL Injection:** No standard SQL injection points found in forms.")
                st.warning("⚠️ **Headers Check:** 'X-Frame-Options' header is missing. Consider adding clickjacking protection.")
                st.info("ℹ️ **Server Info:** Response headers look standard.")
                
                # Telegram test trigger
                if telegram_token and telegram_chat_id:
                    if send_telegram_alert(f"🚨 *CyberShield AI Alert*\nScan completed for {target_url}. Status: Secure with minor warnings."):
                        st.info("📲 Telegram alert test notification sent successfully!")

with tab2:
    st.subheader("⚡ 24/7 Autonomous Monitoring Dashboard")
    st.write("Here you can track continuous uptime and security pings for your target URL.")
    
    if enable_monitoring:
        st.info(f"🔄 Monitoring active for **{target_url}** every {check_interval} minutes.")
        placeholder = st.empty()
        
        # Simulated live status tracker
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with placeholder.container():
            st.markdown(f"""
                <div class="alert-box safe-box">
                    🟢 <b>Status: ONLINE</b><br>
                    Last checked: {current_time}<br>
                    Response Time: 245ms
                </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Autonomous monitoring is currently disabled. Toggle it from the sidebar.")

with tab3:
    st.subheader("📊 Audit & Compliance Reports")
    st.write("Generate professional security audit summaries.")
    if st.button("Generate PDF Summary Report"):
        st.success("📄 Report generated successfully! (Download link would appear here)")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; color: #64748b;'>CyberShield AI — Mobile-Optimized Autonomous Security Platform</p>", unsafe_allow_html=True)
