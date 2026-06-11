"""
theme.py – ApexDent design system: Blue/Dark aesthetic.
Call inject_theme() once from app.py after set_page_config().
"""
import streamlit as st

def inject_theme():
    st.markdown("""
    <style>
    /* ── Design Tokens ────────────────────────────────────────────── */
    :root {
      --apex-bg: #070d14;
      --apex-surface: #0d1b2a;
      --apex-surface-2: #112236;
      --apex-border: #1a3250;
      --apex-accent: #00a8ff;
      --apex-accent-glow: rgba(0, 168, 255, 0.18);
      --apex-text: #e0eaf6;
      --apex-muted: #7a9bbf;
      --apex-font: 'Inter', sans-serif;
    }

    /* ── Base ─────────────────────────────────────────────────────── */
    .stApp { background-color: var(--apex-bg) !important; }

    /* ── Sidebar ──────────────────────────────────────────────────── */
    [data-testid="stSidebar"] {
      background-color: var(--apex-surface) !important;
      border-right: 1px solid var(--apex-border) !important;
    }

    /* ── Buttons ──────────────────────────────────────────────────── */
    .stButton > button {
      background: linear-gradient(135deg, #0073b1 0%, var(--apex-accent) 100%) !important;
      color: #fff !important;
      border-radius: 10px !important;
      border: none !important;
    }

    /* ── Inputs ─────────────────────────────────────────────── */
    .stTextInput > div > div > input {
      background-color: var(--apex-surface-2) !important;
      border: 1px solid var(--apex-border) !important;
      color: var(--apex-text) !important;
    }
    </style>
    """, unsafe_allow_html=True)
