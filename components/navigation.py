"""
navigation.py – Top navbar and role-aware sidebar.
"""
import streamlit as st
from config import ROLES

def render_navbar(authenticated: bool = False, user: dict | None = None) -> None:
    col1, col2, col3 = st.columns([1, 4, 2])
    with col1:
        st.markdown('<span class="apex-logo-text">🦷 ApexDent</span>', unsafe_allow_html=True)
    with col3:
        if not authenticated:
            c1, c2 = st.columns(2)
            with c1:
                if st.button("Login", key="nav_login"):
                    st.session_state["page"] = "login"
                    st.rerun()
            with c2:
                if st.button("Register", key="nav_register"):
                    st.session_state["page"] = "register"
                    st.rerun()
        else:
            role_info = ROLES.get(user.get("role", ""), {})
            st.markdown(
                f'<div style="text-align:right;color:var(--apex-muted);font-size:0.85rem;">'
                f'{role_info.get("icon","👤")} <strong style="color:var(--apex-text)">'
                f'{user["name"]}</strong><br/>'
                f'<span style="color:var(--apex-accent);font-size:0.75rem">'
                f'{role_info.get("label","")}</span></div>',
                unsafe_allow_html=True,
            )
    st.divider()


def render_sidebar(role: str) -> None:
    role_info = ROLES.get(role, {})
    pages = role_info.get("pages", [])

    with st.sidebar:
        st.markdown(
            f'<div style="padding:1rem 0 0.5rem;">'
            f'<span class="apex-logo-text">🦷 ApexDent</span><br/>'
            f'<span style="color:var(--apex-muted);font-size:0.8rem;">'
            f'{role_info.get("label","")}</span></div>',
            unsafe_allow_html=True,
        )
        st.divider()

        page_labels = {
            "home":         ("🏠", "Dashboard"),
            "search":       ("🔍", "Find Dentists"),
            "appointments": ("📅", "Appointments"),
            "ai_assistant": ("🤖", "AI Assistant"),
            "ratings":      ("⭐", "Ratings"),
            "profile":      ("👤", "My Profile"),
            "lab_connect":  ("🔗", "Lab Network"),
            "analytics":    ("📊", "Analytics"),
            "orders":       ("📦", "Orders"),
            "ai_inbox":     ("🤖", "AI Inbox"),
        }

        current = st.session_state.get("page", "home")
        for page_id in pages:
            icon, label = page_labels.get(page_id, ("•", page_id.title()))
            is_active = current == page_id
            if st.button(f"{icon} {label}", key=f"nav_{page_id}",
                         use_container_width=True,
                         type="primary" if is_active else "secondary"):
                st.session_state["page"] = page_id
                st.rerun()

        st.divider()
        if st.button("🚪 Logout", use_container_width=True, type="secondary"):
            for key in ["user", "page", "subpage"]:
                st.session_state.pop(key, None)
            st.rerun()
