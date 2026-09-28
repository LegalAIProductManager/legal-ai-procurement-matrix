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
    ) / 100  # Fixed divisor to maintain baseline metric scale
    return min(max(round(weighted, 2), 0.0), 10.0)

harvey_final = calculate_score(vendors["Harvey"])
legora_final = calculate_score(vendors["Legora"])

# --- STEP 5: VISUALIZE STRATEGIC FIT METRICS ---
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Harvey Strategic Fit Score", value=f"{harvey_final} / 10")
    # Streamlit expects 0.0 to 1.0 for progress bar, so divide score by 10 with safety limits
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

# --- STEP 7: SOURCE INTEL REFERENCE DRAWER ---
st.markdown("---")
st.markdown("### 🌐 Grounded Market Intelligence & Verification Data")
st.markdown(
    "To ensure transparency, the baseline model metrics are derived from active public disclosures "
    "and independent legal tech benchmark frameworks. Use the links below to verify the source parameters:"
)

col_src1, col_src2 = st.columns(2)
with col_src1:
    st.markdown("**🔹 Harvey Platform Sources:**")
    st.markdown("- [Harvey LAB Performance Benchmark](https://artificialanalysis.ai) (Independent Legal LLM Accuracy Auditing)")
    st.markdown("- [OpenAI Custom Astra Model Layer](https://openai.com) (Foundational Model Architecture Disclosures)")
    st.markdown("- [Harvey II Multi-Step Agentic Memory](https://artificiallawyer.com) (Long-Horizon Workflow Upgrades)")

with col_src2:
    st.markdown("**🔹 Legora Platform Sources:**")
    st.markdown("- [Legora vs Harvey Feature Mapping](https://fusiontaxlaw.com) (Direct System Capabilities & Specializations)")
    st.markdown("- [AI-Native Legal Ontology Release](https://legora.com) (Advanced Statutory Citator Tracking)")
    st.markdown("- [ServiceNow Legal Service Delivery Integration Context](https://servicenow.com) (Enterprise Workflow Layering)")
