"""Unit tests for src/ai_service.py fallback behavior."""

from src.ai_service import generate_fallback_recommendations, generate_recommendations
from src.models import CategoryFootprint, TotalFootprintReport


def test_fallback_recommendations_transportation():
    report = TotalFootprintReport(
        category_breakdowns={
            "Transportation": CategoryFootprint("Transportation", 100.0, 60.0),
            "Electricity": CategoryFootprint("Electricity", 40.0, 24.0),
            "Food": CategoryFootprint("Food", 26.0, 16.0),
        },
        total_kg_co2e=166.0,
        highest_emitting_category="Transportation",
    )
    fallback = generate_fallback_recommendations(report)
    assert "Transportation" in fallback
    assert "walk, cycle, or use public transport" in fallback.lower()


def test_generate_recommendations_without_key(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    report = TotalFootprintReport(
        category_breakdowns={
            "Electricity": CategoryFootprint("Electricity", 100.0, 100.0),
        },
        total_kg_co2e=100.0,
        highest_emitting_category="Electricity",
    )
    res = generate_recommendations(report)
    assert "Electricity" in res
    assert "AI Service is currently unavailable" in res
