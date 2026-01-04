import streamlit as st

st.set_page_config(
    page_title="Fake News Detection AI",
    page_icon="📰",
    layout="wide"
)

if "theme" not in st.session_state:
    st.session_state.theme = "dark"

def apply_theme():
    if st.session_state.theme == "dark":
        st.markdown("""
        <style>
        body { background-color:#020617; color:white; }
        .stApp { background: linear-gradient(135deg,#020617,#020617); }
        </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <style>
        body { background-color:#f8fafc; color:black; }
        .stApp { background: linear-gradient(135deg,#f8fafc,#e2e8f0); }
        </style>
        """, unsafe_allow_html=True)

apply_theme()

st.markdown("""
<h1 style='text-align:center; animation: fadeIn 1.5s;'>
📰 Fake News Detection AI Platform
</h1>
<p style='text-align:center; color:gray;'>
Explainable AI • NLP • Machine Learning
</p>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([3,1,3])
with col2:
    if st.button("🌙 Dark / ☀️ Light"):
        st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"
        st.rerun()

st.divider()

st.info("⬅️ Use the sidebar to navigate between pages")
