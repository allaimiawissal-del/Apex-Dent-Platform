"""
ApexDent - Dental Ecosystem Platform
Entry point for the Streamlit application.
"""
import streamlit as st
from config import APP_CONFIG
from utils.auth import AuthManager
from utils.session import init_session
from components.navigation import render_navbar, render_sidebar
from components.theme import inject_theme
from pages.landing import render_landing
from pages.patient_dashboard import render_patient_dashboard
from pages.dentist_dashboard import render_dentist_dashboard
from pages.lab_dashboard import render_lab_dashboard
from pages.auth_page import render_login, render_register


def main():
    st.set_page_config(
        page_title=APP_CONFIG["app_name"],
        page_icon="🦷",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={"About": f"# {APP_CONFIG['app_name']} v{APP_CONFIG['version']}"}
    )

    inject_theme()
    init_session()

    auth = AuthManager()
    user = st.session_state.get("user")
    page = st.session_state.get("page", "landing")

    # ── Unauthenticated routes ────────────────────────────────────────────────
    if not user:
        render_navbar(authenticated=False)
        if page == "login":
            render_login(auth)
        elif page == "register":
            render_register(auth)
        else:
            render_landing()
        return

    # ── Authenticated routes ──────────────────────────────────────────────────
    role = user.get("role")
    render_navbar(authenticated=True, user=user)
    render_sidebar(role=role)

    if role == "patient":
        render_patient_dashboard()
    elif role == "dentist":
        render_dentist_dashboard()
    elif role == "lab":
        render_lab_dashboard()
    else:
        st.error("Unknown role. Please contact support.")
        if st.button("Logout"):
            auth.logout()


if __name__ == "__main__":
    main()
