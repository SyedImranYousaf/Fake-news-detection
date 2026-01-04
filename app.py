import streamlit as st

st.set_page_config(
    page_title="Fake News Detection AI",
    page_icon="📰",
    layout="wide"
)

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True

st.sidebar.markdown("## 🎨 Appearance")
dark_toggle = st.sidebar.toggle(
    "Dark Mode",
    value=st.session_state.dark_mode
)

st.session_state.dark_mode = dark_toggle

if st.session_state.dark_mode:
    st.markdown("""
    <style>
    body { background-color:#020617; color:white; }
    .stApp {
        background: linear-gradient(135deg,#020617,#020617);
    }
    h1, h2, h3 { color:#38bdf8; }
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
    body { background-color:#f8fafc; color:#020617; }
    .stApp {
        background: linear-gradient(135deg,#f8fafc,#e2e8f0);
    }
    h1, h2, h3 { color:#2563eb; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
<h1 style="text-align:center;">
📰 Fake News Detection AI Platform
</h1>
<p style="text-align:center; color:gray;">
Explainable AI • NLP • Machine Learning
</p>
""", unsafe_allow_html=True)

st.divider()
st.info("⬅️ Use the sidebar to navigate between pages")
