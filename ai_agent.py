"""
ai_agent.py – Digital Lab AI middleware and patient dental assistant.
"""
from __future__ import annotations
import random
from config import AI_LAB_CONFIG
from utils.database import get_all_labs, get_all_dentists

class LabDispatchAI:
    WEIGHTS = AI_LAB_CONFIG["match_weights"]

    def analyze_order(self, order: dict) -> dict:
        labs = get_all_labs()
        urgency = order.get("urgency_days", 7)
        scored = []
        for lab in labs:
            if not lab.get("capacity_available", True): continue
            order_label = f"{order.get('material', '')} {order.get('type', '')}".strip()
            spec_score = self._spec_match(lab["specializations"], order_label)
            rating_norm = lab.get("rating", 0) / 5.0
            turn = lab.get("turnaround_days", 7)
            speed_score = max(0.0, 1.0 - max(0, turn - urgency) / urgency) if urgency else 0.5
            price_score = lab.get("price_score", 0.5)
            total = (self.WEIGHTS["specialization"] * spec_score + 
                     self.WEIGHTS["rating"] * rating_norm + 
                     self.WEIGHTS["turnaround_days"] * speed_score + 
                     self.WEIGHTS["price_score"] * price_score)
            scored.append({**lab, "_score": round(total, 3)})
        scored.sort(key=lambda x: x["_score"], reverse=True)
        return {"best_lab": scored[0] if scored else None, "ranked_labs": scored[:5]}

    @staticmethod
    def _spec_match(specializations: list[str], order_label: str) -> float:
        ol = order_label.lower()
        for spec in specializations:
            if any(w in spec.lower() for w in ol.split()): return 1.0
        return 0.1

class PatientAssistAI:
    def get_response(self, user_message: str) -> str:
        msg = user_message.lower()
        if "dentist" in msg or "find" in msg:
            return self._recommend_dentist_full()
        return "I recommend consulting our verified dentists for a personalized assessment."

    @staticmethod
    def _recommend_dentist_full() -> str:
        dentists = sorted(get_all_dentists(), key=lambda d: d["rating"], reverse=True)[:3]
        lines = "\n".join([f"- **{d['name']}** – ⭐ {d['rating']}" for d in dentists])
        return f"Top-rated dentists on ApexDent:\n\n{lines}"
