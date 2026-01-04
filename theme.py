import streamlit as st

def init_theme():
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = True  

def theme_toggle():
    st.sidebar.markdown("## 🎨 Appearance")
    st.session_state.dark_mode = st.sidebar.toggle(
        "Dark Mode",
        value=st.session_state.dark_mode
    )


def apply_theme():
    if st.session_state.dark_mode:
        st.markdown("""
        <style>
        /* Background & page */
        .stApp { background-color: #020617 !important; color: white !important; transition: all 0.4s ease; }

        /* Headers */
        h1, h2, h3, h4, h5, h6 { color: #38bdf8 !important; }

        /* Paragraphs, labels, spans, divs */
        p, label, span, div, strong { color: white !important; }

        /* Inputs and text areas */
        input, textarea { background-color: #020617 !important; color: white !important; }

        /* Tables text */
        td, th { color: white !important; }

        </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <style>
        /* Background & page */
        .stApp { background-color: #f8fafc !important; color: black !important; transition: all 0.4s ease; }

        /* Headers */
        h1, h2, h3, h4, h5, h6 { color: #1e40af !important; }

        /* Paragraphs, labels, spans, divs */
        p, label, span, div, strong { color: black !important; }

        /* Inputs and text areas */
        input, textarea { background-color: white !important; color: black !important; }

        /* Tables text */
        td, th { color: black !important; }
        </style>
        """, unsafe_allow_html=True)
