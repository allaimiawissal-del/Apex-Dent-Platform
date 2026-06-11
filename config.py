"""
ApexDent – centralized configuration.
All tuneable values live here; import from this module everywhere.
"""

APP_CONFIG = {
    "app_name": "ApexDent",
    "version": "1.0.0",
    "tagline": "The Future of Dental Care",
    "support_email": "support@apexdent.io",
}

# Roles available in the RBAC system
ROLES = {
    "patient": {
        "label": "Patient",
        "icon": "👤",
        "pages": ["home", "search", "appointments", "ai_assistant", "ratings"],
    },
    "dentist": {
        "label": "Dentist",
        "icon": "🦷",
        "pages": ["home", "profile", "appointments", "lab_connect", "analytics"],
    },
    "lab": {
        "label": "Laboratory",
        "icon": "🔬",
        "pages": ["home", "orders", "profile", "ai_inbox", "analytics"],
    },
}

# Map / geo defaults
MAP_CONFIG = {
    "default_lat": 36.7538,   # Algiers
    "default_lon": 3.0588,
    "default_zoom": 12,
}

# AI Digital Lab settings (mock thresholds)
AI_LAB_CONFIG = {
    "match_weights": {
        "specialization": 0.40,
        "rating": 0.25,
        "turnaround_days": 0.20,
        "price_score": 0.15,
    },
    "min_confidence": 0.65,
}

# Mock JWT secret (replace with env var in production)
SECRET_KEY = "apexdent-secret-change-in-prod"
SESSION_EXPIRE_HOURS = 8
