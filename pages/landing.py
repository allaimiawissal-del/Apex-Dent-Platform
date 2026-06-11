"""
landing.py – The welcome page for unauthenticated users.
"""
import streamlit as st

def render_landing():
    st.markdown("""
    <div style="text-align: center; padding: 50px 0;">
        <h1 style="font-size: 3rem; color: var(--apex-accent);">Welcome to ApexDent</h1>
        <p style="font-size: 1.2rem; color: var(--apex-muted);">
            Connecting Dentists, Patients, and Labs with AI-powered precision.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("### 👤 For Patients\nFind the best dentists in your area and manage your appointments easily.")
    with col2:
        st.warning("### 🦷 For Dentists\nConnect with specialized labs and manage your digital workflow.")
    with col3:
        st.success("### 🔬 For Labs\nReceive high-precision orders and automate your dispatch with AI.")

    if st.button("Get Started", type="primary"):
        st.session_state["page"] = "register"
        st.rerun()
