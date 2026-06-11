"""
database.py – Mock data layer.
In production, swap these stores for SQLAlchemy / Supabase / MongoDB calls.
"""
from __future__ import annotations
import hashlib, uuid
from datetime import datetime, date

# ── In-memory stores ──────────────────────────────────────────────────────────
_users: dict[str, dict] = {}
_dentists: dict[str, dict] = {}
_labs: dict[str, dict] = {}
_appointments: list[dict] = []
_lab_orders: list[dict] = []
_ratings: list[dict] = []

def _hash(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

# ── Seed data ─────────────────────────────────────────────────────────────────
def _seed():
    # Patients
    for i, (name, email) in enumerate([("Amina Khaled", "amina@mail.com"), ("Youcef Brahim", "youcef@mail.com")], start=1):
        uid = f"P{i:03d}"
        _users[uid] = {"id": uid, "name": name, "email": email, "password": _hash("password"), "role": "patient", "phone": f"+213 5{i}0 000 00{i}", "created_at": str(date.today())}

    # Dentists
    dentist_data = [
        ("Dr. Karim Meddah", "karim@dent.com", "General Dentistry", 36.7692, 3.0586, 4.8, 3000),
        ("Dr. Soumia Aït", "soumia@dent.com", "Orthodontics", 36.7450, 3.0700, 4.6, 4500),
        ("Dr. Nabil Zerrouki", "nabil@dent.com", "Implantology", 36.7600, 3.0400, 4.9, 6000),
    ]
    for i, (name, email, spec, lat, lon, rating, price) in enumerate(dentist_data, start=1):
        uid = f"D{i:03d}"
        _users[uid] = {"id": uid, "name": name, "email": email, "password": _hash("password"), "role": "dentist", "created_at": str(date.today())}
        _dentists[uid] = {"id": uid, "name": name, "email": email, "specialization": spec, "lat": lat, "lon": lon, "rating": rating, "review_count": 12 + i * 3, "price_dzd": price, "address": f"Clinic {i}, Algiers", "phone": f"+213 5{i}1 111 11{i}", "hours": "08:00 – 17:00", "accepts_new": True, "technologies": ["Digital X-Ray", "CAD/CAM"] if i > 1 else ["Digital X-Ray"], "bio": f"Specialist in {spec} with over {8+i} years of experience."}

    # Laboratories
    lab_data = [
        ("AlgeriaDent Lab", "lab1@lab.com", ["Crowns", "Bridges", "Veneers"], 36.7550, 3.0500, 4.7, 5),
        ("ProthèsePro", "lab2@lab.com", ["Dentures", "Implant Bars", "Splints"], 36.7400, 3.0650, 4.5, 7),
        ("ZirconArt Studio", "lab3@lab.com", ["Zirconia Crowns", "E.max", "Inlays"], 36.7700, 3.0300, 4.9, 4),
    ]
    for i, (name, email, specs, lat, lon, rating, turnaround) in enumerate(lab_data, start=1):
        uid = f"L{i:03d}"
        _users[uid] = {"id": uid, "name": name, "email": email, "password": _hash("password"), "role": "lab", "created_at": str(date.today())}
        _labs[uid] = {"id": uid, "name": name, "email": email, "specializations": specs, "lat": lat, "lon": lon, "rating": rating, "turnaround_days": turnaround, "price_score": round(1 - (i * 0.1), 2), "address": "Lab District, Algiers", "phone": f"+213 2{i}3 456 78{i}", "capacity_available": True, "active_orders": i}

    _appointments.extend([{"id": "APT001", "patient_id": "P001", "dentist_id": "D001", "date": "2026-06-15", "time": "10:00", "status": "confirmed", "reason": "Routine checkup", "notes": ""}])
    _lab_orders.extend([{"id": "ORD001", "dentist_id": "D001", "lab_id": "L001", "type": "Crown", "material": "Zirconia", "tooth": "26", "status": "in_progress", "created_at": "2026-06-01", "due_date": "2026-06-10", "ai_confidence": 0.92, "notes": "Shade A2"}])

_seed()

# ── Public API ────────────────────────────────────────────────────────────────
def get_user_by_email(email: str) -> dict | None:
    for u in _users.values():
        if u["email"] == email: return u
    return None

def verify_password(email: str, password: str) -> dict | None:
    user = get_user_by_email(email)
    if user and user["password"] == _hash(password): return user
    return None

def create_user(name: str, email: str, password: str, role: str) -> dict | None:
    if get_user_by_email(email): return None
    prefix = {"patient": "P", "dentist": "D", "lab": "L"}.get(role, "U")
    uid = f"{prefix}{str(uuid.uuid4())[:6].upper()}"
    user = {"id": uid, "name": name, "email": email, "password": _hash(password), "role": role, "created_at": str(date.today())}
    _users[uid] = user
    return user

def get_all_dentists() -> list[dict]: return list(_dentists.values())
def get_all_labs() -> list[dict]: return list(_labs.values())
def get_appointments(user_id: str, role: str) -> list[dict]:
    key = "patient_id" if role == "patient" else "dentist_id"
    return [a for a in _appointments if a.get(key) == user_id]
