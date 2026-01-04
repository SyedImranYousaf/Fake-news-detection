import streamlit as st
from theme import init_theme, theme_toggle, apply_theme

st.set_page_config(
    page_title="Fake News Detection AI",
    page_icon="📰",
    layout="wide"
)

init_theme()
theme_toggle()
apply_theme()


st.markdown("""
<h1 style="text-align:center;">📰 Fake News Detection AI Platform</h1>
<p style="text-align:center;">Explainable AI • NLP • ML Dashboard</p>
""", unsafe_allow_html=True)

st.divider()
st.info("⬅️ Use the sidebar to navigate pages")
