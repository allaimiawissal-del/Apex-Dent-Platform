"""
session.py – Centralised session-state initialisation.
Call init_session() once at app startup before any page renders.
"""
import streamlit as st

DEFAULTS: dict = {
    "user": None,
    "page": "landing",
    "subpage": None,
    "search_query": "",
    "selected_dentist": None,
    "selected_lab": None,
    "ai_messages": [],
    "lab_ai_messages": [],
    "map_filter": {},
    "notifications": [],
}

def init_session() -> None:
    for key, default in DEFAULTS.items():
        if key not in st.session_state:
            st.session_state[key] = default

def nav(page: str, subpage: str | None = None) -> None:
    """Navigate programmatically without a widget interaction."""
    st.session_state["page"] = page
    st.session_state["subpage"] = subpage
    st.rerun()
