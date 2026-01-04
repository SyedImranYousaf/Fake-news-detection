import streamlit as st
from theme import init_theme, theme_toggle, apply_theme

init_theme()
theme_toggle()
apply_theme()
st.markdown("## 📄 Project Documentation")

with open("Fake_News_Detection_Project_Report.pdf", "rb") as pdf:
    st.download_button(
        "⬇️ Download Full Project Report (PDF)",
        pdf,
        file_name="Fake_News_Detection_Report.pdf",
        mime="application/pdf"
    )

st.success("This report contains architecture, algorithm, results, and analysis.")
