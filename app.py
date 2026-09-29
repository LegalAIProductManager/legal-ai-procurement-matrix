import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(layout="wide", page_title="Legal AI Strategic Evaluator")

st.title("🎯 Legal AI Strategic Matchmaker")
st.subheader("Mapping Public Market Capabilities Against Anonymized Enterprise Constraints")

# --- STEP 1: ANONYMIZED CLIENT SELECTION ---
client_profile = st.sidebar.selectbox(
    "Select Client Persona Profile",
    ["Global Infrastructure REIT & Cloud Provider", "AmLaw 50 (Litigation Firm)", "Custom Evaluation"]
)

# --- STEP 2: DYNAMIC PRESETS BASED ON ARCHETYPE ---
if client_profile == "Global Infrastructure REIT & Cloud Provider":
    lease_w = 40; infra_w = 30; research_w = 10; ecosystem_w = 20
    st.sidebar.info("💡 Profile loaded: Optimized for hyper-scale colocation leases, PPA energy compliance, and enterprise CLM flows.")
elif client_profile == "AmLaw 50 (Litigation Firm)":
    lease_w = 10; infra_w = 10; research_w = 50; ecosystem_w = 30
    st.sidebar.info("💡 Profile loaded: Optimized for multi-jurisdiction case law research, citator validation, and motion drafting.")
else:
    lease_w = 25; infra_w = 25; research_w = 25; ecosystem_w = 25

st.sidebar.header("🔧 Customize Dimension Weights (%)")
w_lease = st.sidebar.slider("Hyperscale Lease Operations", 0, 100, lease_w)
w_infra = st.sidebar.slider("Infrastructure & Utility Compliance", 0, 100, infra_w)
w_research = st.sidebar.slider("Deep Litigation Research", 0, 100, research_w)
w_eco = st.sidebar.slider("Ecosystem & CLM Integration", 0, 100, ecosystem_w)

total_weight = w_lease + w_infra + w_research + w_eco
if total_weight != 100:
    st.sidebar.warning(f"⚠️ Total weight must equal 100%. Current: {total_weight}%")

# --- STEP 3: VENDOR BASELINE RATINGS ---
vendors = {
    "Harvey": {"Lease": 7.5, "Infra": 7.0, "Research": 9.5, "Eco": 8.0},
    "Legora": {"Lease": 9.0, "Infra": 8.5, "Research": 7.0, "Eco": 9.0}
}

# --- STEP 4: SCORES CALCULATION WITH BOUNDS SAFETY ---
def calculate_score(vendor_data):
    weighted = (
        (vendor_data["Lease"] * w_lease) +
        (vendor_data["Infra"] * w_infra) +
        (vendor_data["Research"] * w_research) +
        (vendor_data["Eco"] * w_eco)
    ) / 100
    return min(max(round(weighted, 2), 0.0), 10.0)

harvey_final = calculate_score(vendors["Harvey"])
legora_final = calculate_score(vendors["Legora"])

# --- STEP 5: VISUALIZE STRATEGIC FIT METRICS ---
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Harvey Strategic Fit Score", value=f"{harvey_final} / 10")
    st.progress(min(max(harvey_final / 10.0, 0.0), 1.0))
with col2:
    st.metric(label="Legora Strategic Fit Score", value=f"{legora_final} / 10")
    st.progress(min(max(legora_final / 10.0, 0.0), 1.0))

# --- STEP 6: RADAR CHART GENERATION ---
categories = ['Lease Ops', 'Infra/Utility', 'Deep Research', 'Ecosystem Fit']

fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=[vendors["Harvey"]["Lease"], vendors["Harvey"]["Infra"], vendors["Harvey"]["Research"], vendors["Harvey"]["Eco"]],
    theta=categories, fill='toself', name='Harvey Capabilities'
))
fig.add_trace(go.Scatterpolar(
    r=[vendors["Legora"]["Lease"], vendors["Legora"]["Infra"], vendors["Legora"]["Research"], vendors["Legora"]["Eco"]],
    theta=categories, fill='toself', name='Legora Capabilities'
))
fig.add_trace(go.Scatterpolar(
    r=[w_lease/10.0, w_infra/10.0, w_research/10.0, w_eco/10.0],
    theta=categories, mode='lines+markers', name='Client Custom Requirement Profile',
    line=dict(color='red', dash='dash')
))

fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 10])), showlegend=True)
st.plotly_chart(fig, use_container_width=True)

# --- NEW STEP: INFOSEC, PRIVACY, & CLOUD ARCHITECTURE DUE DILIGENCE ---
st.markdown("---")
st.markdown("### 🔒 InfoSec, Privacy, & Cloud Infrastructure Audit")
st.markdown(
    "Evaluating deep data governance parameters required to pass internal corporate InfoSec screening. "
    "This matrix details deployment architecture capabilities and maps critical unaddressed risks:"
)

sec_col1, sec_col2 = st.columns(2)
with sec_col1:
    st.markdown("#### ☁️ Cloud & Data Sovereignty Architecture")
    st.markdown("- **Harvey BYOC / Single-Tenant Support:** Supports highly customized, isolated **dedicated tenant instances** for enterprise deployments to meet strict financial/government client parameters.")
    st.markdown("- **Legora Azure Integration:** Built directly on top of enterprise-grade **Azure OpenAI cloud isolation** infrastructures, leveraging standard corporate Microsoft security perimeters natively.")
    st.markdown("- **Data Retention Rules:** Both platforms guarantee zero-data retention pipelines where zero metadata or transactional files are cached to train base models.")
with sec_col2:
    st.markdown("#### ⚠️ Unaddressed Security Risks & Gaps")
    st.markdown("- **The Hidden Sub-Processor Trap:** While foundational data stays isolated, legal apps frequently bounce requests to external sub-processors for optical character recognition (OCR) or document translation. *Audit Requirement: Verify sub-processor logs.*")
    st.markdown("- **Model Drift Integrity:** Automated updates can alter foundational model behavior without prior disclosure. If a security model regresses, it can silently introduce compliance risks into standard contract reviews.")
    st.markdown("- **Prompt Injection Exploitations:** Malicious or poorly formatted third-party contract files uploaded to the systems can trigger prompt injections, forcing the tool to leak adjacent session information.")

# --- STEP 7: MARKET DISCOVERY (RFI) VS SELECTION (RFP) ---
st.markdown("---")
st.markdown("### 📋 Market Intelligence Discovery (RFI) vs. Selection (RFP)")
rfi_col1, rfi_col2 = st.columns(2)
with rfi_col1:
    st.markdown("#### 🤝 Commonly Compelled Items (Shared Baselines)")
    st.markdown("- **Enterprise Data Isolation:** Both vendors guarantee no user inputs are used to train public models.")
    st.markdown("- **SOC 2 Type II Compliance:** Basic requirement to clear baseline corporate risk screening.")
    st.markdown("- **Native MS Word Add-ins:** Both platforms must provide custom sidepanels inside Microsoft Word workspace suites.")
with rfi_col2:
    st.markdown("#### ⚡ Distinctly Compelled Items (The Divergence)")
    st.markdown("- **Harvey Customization:** Heavily requested to detail their fine-tuning layers and open-weight custom model costs for firm memory.")
    st.markdown("- **Legora Customization:** Heavily pushed on table export limits, cell data structure support, and their exact API mapping schema to ServiceNow Legal tables.")

# --- STEP 8: OPERATIONAL IMPLEMENTATION PLAYBOOK ---
st.markdown("---")
st.markdown("### ⚙️ Operational Implementation Playbook")
imp_col1, imp_col2 = st.columns(2)
with imp_col1:
    st.markdown("#### 🔄 Shared Implementation Dynamics")
    st.markdown("- **Tenant Architecture Provisioning:** Requires establishing isolated enterprise environments (Azure cloud spaces or secure buckets) with IT security.")
    st.markdown("- **Attorney Change Management:** Structured training cycles are mandatory to bridge the adoption gap from plain chat bars to native add-in workflows.")
with imp_col2:
    st.markdown("#### ⚠️ Divergent Implementation Risks")
    st.markdown("- **Harvey Framework:** Leans heavily on knowledge management—feeding thousands of corporate files into their systems to map firm memory layers safely.")
    st.markdown("- **Legora Framework:** Leans heavily on integration engineering—requiring data configurations to map native legal tables onto active corporate ServiceNow structures.")

# --- STEP 9: LIVE CLIENT RFP GENERATION WORKSPACE ---
st.markdown("---")
st.markdown("### 🛠️ Client Request for Proposal (RFP) Custom Workspace Engine")
with st.expander("📝 Click to View/Edit Your 10-Question RFP Matrix", expanded=False):
    default_rfp = [
        "Does the system support dedicated cloud tenant isolation to satisfy sovereign customer protocols?",
        "Can the system parse numeric Megawatt (MW) capacity conversions inside legacy PDF lease tables?",
        "What is the system's accuracy rate when extracting out-of-jurisdiction European construction clauses?",
        "Is there a native API connector syncing structured clause outputs straight to ServiceNow schemas?",
        "How does the commercial pricing model adjust for usage tier spikes vs flat seat subscriptions?",
        "Does the platform maintain zero data retention to enforce strict client NDAs?",
        "Can attorneys access model capabilities directly via a native Microsoft Word workspace extension?",
        "What automated parameters flag hallucinated statutes or broken internal document cross-references?",
        "Does the model support localized compliance mapping against EU CSRD sustainability frameworks?",
        "How are multi-step agentic workflows logged inside visible system audit trails?"
    ]
    rfp_scores_h = []
    rfp_scores_l = []
    for i in range(10):
        st.markdown(f"**📍 RFP Requirement #{i+1}**")
        q_text = st.text_input(f"Define Requirement / Question #{i+1}:", value=default_rfp[i], key=f"rfp_q_{i}")
        c1, c2 = st.columns(2)
        with c1:
            h_s = st.slider(f"Harvey Score for Q#{i+1} (1=Fail, 5=Pass)", 1, 5, 4, key=f"rfp_h_s_{i}")
            rfp_scores_h.append(h_s)
        with c2:
            l_s = st.slider(f"Legora Score for Q#{i+1} (1=Fail, 5=Pass)", 1, 5, 4, key=f"rfp_l_s_{i}")
            rfp_scores_l.append(l_s)
        st.markdown("<br>", unsafe_allow_html=True)
    harvey_rfp_avg = round(sum(rfp_scores_h) / 10, 2)
    legora_rfp_avg = round(sum(rfp_scores_l) / 10, 2)
    st.markdown("#### 📊 Dynamic RFP Response Summary")
    st.write(f"**Harvey RFP Evaluation Average:** {harvey_rfp_avg} / 5.0")
    st.write(f"**Legora RFP Evaluation Average:** {legora_rfp_avg} / 5.0")

# --- STEP 10: VERIFICATION SANDBOX & PILOT TEST LOGS ---
