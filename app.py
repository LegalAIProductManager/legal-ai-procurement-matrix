# --- STEP 9: LIVE CLIENT RFP GENERATION WORKSPACE ---
st.markdown("---")
st.markdown("### 📋 Client Request for Proposal (RFP) Custom Workspace Engine")
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

# --- STEP 10: VERIFICATION SANDBOX & PILOT TEST LOGS ---
st.markdown("---")
st.markdown("### 🧪 Operational Verification Sandbox & Pilot Test Audits")
tab1, tab2, tab3 = st.tabs(["📋 Test 1: Bulk Lease Extraction", "⚡ Test 2: Infrastructure PPA Compliance", "⚙️ Test 3: System Interoperability"])
with tab1:
    st.write("**Scenario Prompt:** Extract metadata from 5 multi-facility colocation leases.")
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
        st.text_area("Custom Legora Execution Notes:", "Clean extraction straight into markdown table formats.", key="l_txt1")

with tab2:
    st.write("**Scenario Prompt:** Cross-reference a Spanish Virtual Power Purchase Agreement (VPPA) draft against active EU CSRD energy metrics.")
    col_t2_h, col_t2_l = st.columns(2)
    with col_t2_h:
        st.markdown("**Harvey Results Log:**")
        st.checkbox("Identified additionality risk clauses", value=True, key="h_t2_1")
        st.checkbox("Zero regulatory hallucinations flagged", value=True, key="h_t2_2")
        st.text_area("Custom Harvey Execution Notes:", "Strong comparative legal synthesis; accurately cited EU directives.", key="h_txt2")
    with col_t2_l:
        st.markdown("**Legora Results Log:**")
        st.checkbox("Identified additionality risk clauses", value=True, key="l_t2_1")
        st.checkbox("Zero regulatory hallucinations flagged", value=False, key="l_t2_2")
        st.text_area("Custom Legora Execution Notes:", "Missed one specific pass-through utility cost clause amendment.", key="l_txt2")

with tab3:
    st.write("**Scenario Prompt:** Track revision edits directly against Outside Counsel Guidelines (OCG) inside the native workspace engine.")
    col_t3_h, col_t3_l = st.columns(2)
    with col_t3_h:
        st.markdown("**Harvey Results Log:**")
        st.checkbox("Executed natively via browser context", value=True, key="h_t3_1")
        st.checkbox("Parsed JSON structure for external tools", value=False, key="h_t3_2")
        st.text_area("Custom Harvey Execution Notes:", "Required custom formatting work to map to standard ServiceNow inputs.", key="h_txt3")
    with col_t3_l:
        st.markdown("**Legora Results Log:**")
        st.checkbox("Executed natively via browser context", value=True, key="l_t3_1")
        st.checkbox("Parsed JSON structure for external tools", value=True, key="l_t3_2")
        st.text_area("Custom Legora Execution Notes:", "Generated a clean data schema ready for instant API push.", key="l_txt3")

# --- STEP 11: SOURCE INTEL REFERENCE DRAWER ---
st.markdown("---")
st.markdown("### 🌐 Grounded Market Intelligence & Verification Data")
col_src1, col_src2 = st.columns(2)
with col_src1:
    st.markdown("**🔹 Harvey Platform Sources:**")
    st.markdown("- [Harvey LAB Performance Benchmark](https://artificialanalysis.ai)")
    st.markdown("- [OpenAI Custom Astra Model Layer](https://openai.com)")
    st.markdown("- [Harvey II Multi-Step Agentic Memory](https://artificiallawyer.com)")
with col_src2:
    st.markdown("**🔹 Legora Platform Sources:**")
    st.markdown("- [Legora vs Harvey Feature Mapping](https://fusiontaxlaw.com)")
    st.markdown("- [AI-Native Legal Ontology Release](https://legora.com)")
    st.markdown("- [ServiceNow Legal Service Delivery Integration Context](https://servicenow.com)")
