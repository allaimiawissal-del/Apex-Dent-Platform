"""
maps.py – Map rendering helpers.
Uses pydeck for rich 3-D layers and falls back to st.map.
"""
import streamlit as st
import pandas as pd
from config import MAP_CONFIG

def render_dentist_map(dentists: list[dict]) -> str | None:
    """Render an interactive map of dentists and return selected ID."""
    if not dentists:
        st.info("No dentists found.")
        return None

    df = pd.DataFrame(dentists)
    # خريطة بسيطة باستخدام Streamlit
    st.map(df.rename(columns={"lat": "latitude", "lon": "longitude"}))

    names = {d["name"]: d["id"] for d in dentists}
    chosen_name = st.selectbox("Select a dentist to view profile", ["— Choose —"] + list(names.keys()))
    return names.get(chosen_name) if chosen_name != "— Choose —" else None

def render_lab_map(labs: list[dict]) -> str | None:
    """Render interactive lab map; return selected lab ID."""
    if not labs:
        st.info("No laboratories found.")
        return None

    df = pd.DataFrame(labs)
    st.map(df.rename(columns={"lat": "latitude", "lon": "longitude"}))
    
    names = {lab["name"]: lab["id"] for lab in labs}
    chosen = st.selectbox("Select a laboratory", ["— Choose —"] + list(names.keys()))
    return names.get(chosen) if chosen != "— Choose —" else None
