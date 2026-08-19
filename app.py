import os
import pandas as pd
import streamlit as st
from ai.diagnosis import diagnose_case
from checker.checker import run_checks

st.set_page_config(page_title="NetSage AI",page_icon="🌐",layout="wide")
CASES="data/cases.csv"; REVIEWS="data/reviews.csv"

@st.cache_data
def load_cases(): return pd.read_csv(CASES)

cases=load_cases()
if "reviews" not in st.session_state:
    st.session_state.reviews=pd.read_csv(REVIEWS).to_dict("records") if os.path.exists(REVIEWS) else []

st.title("🌐 NetSage AI")
st.caption("AI-assisted Cisco troubleshooting with mandatory human review")

t1,t2,t3=st.tabs(["🔎 Diagnose","📊 Dashboard","🛡️ Responsible AI"])

with t1:
    mode=st.radio("Input mode",["Dataset case","Custom case"],horizontal=True)
    if mode=="Dataset case":
        cid=st.selectbox("Select case",cases.case_id.tolist())
        r=cases[cases.case_id==cid].iloc[0]
        symptom,topology,output,expected=r.symptom,r.topology_note,r.show_output,r.expected_fault
    else:
        cid="CUSTOM"
        symptom=st.text_area("Symptom")
        topology=st.text_area("Topology note")
        output=st.text_area("Show-command output")
        expected="Unknown"
    st.info(symptom)
    st.write("**Topology:**",topology)
    st.code(output,language="text")
    if st.button("Run NetSage Diagnosis",type="primary"):
        st.session_state.last=(diagnose_case(symptom,topology,output,expected),
                               run_checks(symptom,topology,output),expected,cid)
    if "last" in st.session_state:
        d,checks,expected,cid=st.session_state.last
        cols=st.columns(4)
        cols[0].metric("Confidence",f"{d['confidence']:.0%}")
        cols[1].metric("OSI Layer",d["osi_layer"])
        cols[2].metric("Severity",d["severity"])
        cols[3].metric("Concept",d["concept"])
        st.subheader("AI Diagnosis")
        st.write("**Root Cause:**",d["root_cause"])
        st.write("**Evidence:**")
        for e in d["evidence"]: st.write("•",e)
        st.write("**Next Command:**"); st.code(d["next_command"])
        st.write("**Fix Steps:**")
        for x in d["fix_steps"]: st.write("•",x)
        st.subheader("Deterministic Rule Checker")
        st.json(checks)
        st.warning("Human review is mandatory. No configuration is automatically changed.")
        decision=st.radio("Human decision",["Accepted","Edited","Rejected"],horizontal=True)
        comment=st.text_area("Reviewer comment")
        if st.button("Save Review"):
            rec={"case_id":cid,"ai_root_cause":d["root_cause"],"human_decision":decision,
                 "reviewer_comment":comment,"expected_fault":expected}
            st.session_state.reviews.append(rec)
            pd.DataFrame(st.session_state.reviews).to_csv(REVIEWS,index=False)
            st.success("Review saved.")

with t2:
    reviews=pd.DataFrame(st.session_state.reviews)
    a,b,c,d=st.columns(4)
    a.metric("Total Cases",len(cases))
    b.metric("Reviews",len(reviews))
    accepted=int((reviews.human_decision=="Accepted").sum()) if len(reviews) else 0
    c.metric("Accepted",accepted)
    d.metric("Agreement",f"{accepted/len(reviews):.1%}" if len(reviews) else "0%")
    st.subheader("Cases by Issue Type")
    st.bar_chart(cases.concept.value_counts())
    st.subheader("Cases by Severity")
    st.bar_chart(cases.severity.value_counts())
    if len(reviews):
        st.subheader("Human Review Decisions")
        st.bar_chart(reviews.human_decision.value_counts())
        st.dataframe(reviews,use_container_width=True)

with t3:
    st.subheader("Responsible AI")
    st.write("Every diagnosis requires human Accept/Edit/Reject review.")
    st.write("The system never directly executes Cisco configuration changes.")
    st.write("AI evidence must be grounded in supplied case data.")
    if len(st.session_state.reviews):
        st.dataframe(pd.DataFrame(st.session_state.reviews),use_container_width=True)
