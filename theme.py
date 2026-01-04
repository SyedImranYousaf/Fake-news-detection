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
        .stApp {
            background: linear-gradient(135deg,#020617,#020617);
            color: #e5e7eb;
            transition: all 0.4s ease;
        }
        h1,h2,h3,h4,h5,h6 { color:#38bdf8; }
        p, label, span, div { color:#e5e7eb !important; }
        input, textarea {
            background-color:#020617 !important;
            color:white !important;
        }
        </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(135deg,#f8fafc,#e2e8f0);
            color: #020617;
            transition: all 0.4s ease;
        }
        h1,h2,h3,h4,h5,h6 { color:#1e40af; }
        p, label, span, div { color:#020617 !important; }
        input, textarea {
            background-color:white !important;
            color:#020617 !important;
        }
        </style>
        """, unsafe_allow_html=True)
