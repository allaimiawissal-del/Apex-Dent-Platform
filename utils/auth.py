"""
auth.py – Role-based authentication manager.
Wraps session state so the rest of the app never touches st.session_state directly.
"""
import streamlit as st
from utils.database import verify_password, create_user


class AuthManager:

    def login(self, email: str, password: str) -> tuple[bool, str]:
        """Validate credentials and populate session. Returns (success, message)."""
        user = verify_password(email, password)
        if not user:
            return False, "Invalid email or password."
        st.session_state["user"] = user
        st.session_state["page"] = "home"
        return True, f"Welcome back, {user['name']}!"

    def logout(self) -> None:
        for key in ["user", "page", "subpage"]:
            st.session_state.pop(key, None)
        st.rerun()

    def register(self, name: str, email: str, password: str, role: str) -> tuple[bool, str]:
        if len(password) < 6:
            return False, "Password must be at least 6 characters."
        user = create_user(name, email, password, role)
        if not user:
            return False, "An account with this email already exists."
        st.session_state["user"] = user
        st.session_state["page"] = "home"
        return True, f"Account created! Welcome, {name}."

    @staticmethod
    def require_role(*roles: str):
        """Guard – call at the top of a page to enforce RBAC."""
        user = st.session_state.get("user")
        if not user or user.get("role") not in roles:
            st.error("🔒 Access denied.")
            st.stop()

    @staticmethod
    def current_user() -> dict | None:
        return st.session_state.get("user")
