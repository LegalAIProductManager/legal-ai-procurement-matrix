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

# --- NEW STEP: RFI VS RFP VENDOR MATURITY MODULE ---
st.markdown("---")
st.markdown("### 📋 Market Intelligence Discovery (RFI) vs. Selection (RFP)")
st.markdown(
    "How information requests vary between general capability discovery (RFI) and hard contractual binding (RFP). "
    "Review common vs. distinct points both vendors face when responding to enterprise requests:"
)

rfi_col1, rfi_col2 = st.columns(2)
with rfi_col1:
    st.markdown("#### 🤝 Commonly Compelled Items (Shared Baselines)")
    st.markdown("- **Enterprise Data Isolation:** Both vendors are forced to guarantee that no user inputs or tenant lease files are used to train baseline public AI models.")
    st.markdown("- **SOC 2 Type II Compliance:** Basic infrastructure requirement to clear baseline corporate risk screening.")
    st.markdown("- **Native MS Word Add-ins:** Both platforms must provide a sidepanel inside Word where attorneys spend their active workdays.")
with rfi_col2:
    st.markdown("#### ⚡ Distinctly Compelled Items (The Divergence)")
    st.markdown("- **Harvey Customization:** Heavily requested to detail their fine-tuning layers and open-weight custom model costs for firm memory [Mon, Sep 28, 2026].")
    st.markdown("- **Legora Customization:** Heavily pushed on table export limits, cell data structure support, and their exact API mapping schema to ServiceNow Legal tables [Tue, Sep 15, 2026; Mon, Sep 28, 2026].")

# --- NEW STEP: IMPLEMENTATION PLAYBOOK MODULE ---
st.markdown("---")
st.markdown("### ⚙️ Operational Implementation Playbook")
st.markdown("Enterprise software deployments fail without clear technical change management. This framework outlines delivery similarities and functional variances:")

imp_col1, imp_col2 = st.columns(2)
with imp_col1:
    st.markdown("#### 🔄 Shared Implementation Dynamics")
    st.markdown("- **Tenant Architecture Provisioning:** Both require coordinating with corporate IT security teams to establish isolated enterprise spaces (Azure cloud environments or secure cloud buckets).")
    st.markdown("- **Attorney Change Management:** Both require structured training cycles. Attorneys frequently reject plain browser windows and demand intuitive native workspace options.")
with imp_col2:
    st.markdown("#### ⚠️ Divergent Implementation Risks")
    st.markdown("- **Harvey Framework:** Implementation leans heavily on internal context mapping—feeding thousands of firm documents into their system to train the long-horizon agentic memory engine [Mon, Sep 28, 2026].")
    st.markdown("- **Legora Framework:** Implementation is integration-heavy—requiring data engineers to map Legora’s native legal data tables directly onto existing corporate metadata fields and ServiceNow workflows [Tue, Sep 15, 2026; Mon, Sep 28, 2026].")

# --- STEP 7: LIVE CLIENT RFP GENERATION WORKSPACE ---
st.markdown("---")
st.markdown("### 🛠️ Client Request for Proposal (RFP) Custom Workspace Engine")
st.markdown("Customize this module by inserting unique organization requirements to build your quantitative selection template:")

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

# --- STEP 8: VERIFICATION SANDBOX & PILOT TEST LOGS ---
st.markdown("---")
st.markdown("### 🧪 Operational Verification Sandbox & Pilot Test Audits")
tab1, tab2, tab3 = st.tabs(["📋 Test 1: Bulk Lease Extraction", "⚡ Test 2: Infrastructure PPA Compliance", "⚙️ Test 3: System Interoperability"])
with tab1:
    st.write("**Scenario Prompt:** Extract metadata (Megawatt caps, SLA metrics, cross-border indemnity) from 5 multi-facility colocation leases.")
    col_t1_h, col_t1_l = st.columns(2)
    with col_t1_h:
        st.markdown("**Harvey Results Log:**")
        st.checkbox("Accurately converted kW to MW", value=True, key="h_t1_1")
        st.checkbox("Separated cross-border jurisdictions", value=False, key="h_t1_2")
        st.text_area("Custom Harvey Execution Notes:", "Model struggled with multi-column layout on German framework.", key="h_txt1")
    with col_t1_l:
        st.markdown("**Legora Results Log:**")
        st.checkbox("Accurately converted kW to MW", value=True, key="l_t1_1")
        st.checkbox("Separated cross-border jurisdictions", value=True, key="l_t1_2")
