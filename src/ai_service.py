"""AI service module using Google Gemini API for carbon reduction tips."""

import os
from typing import Optional
from dotenv import load_dotenv
from src.models import TotalFootprintReport

# Load environment variables from .env file
load_dotenv()


def generate_fallback_recommendations(report: TotalFootprintReport) -> str:
    """Generate static fallback recommendations when AI API is unavailable."""
    top = report.highest_emitting_category
    lines = [
        "Note: AI Service is currently unavailable or API key is not configured.",
        "",
        f"Based on your calculated footprint, your highest emitting category is '{top}'.",
        "Here are general recommendations based on standard sustainability best practices:",
    ]

    if top == "Transportation":
        lines.extend([
            " • Walk, cycle, or use public transport for short urban trips.",
            " • Combine multiple errands into a single efficient trip.",
            " • Consider carpooling or choosing fuel-efficient/electric vehicles."
        ])
    elif top == "Electricity":
        lines.extend([
            " • Switch to energy-efficient LED lighting and ENERGY STAR appliances.",
            " • Unplug electronics when not in use to avoid standby power draw.",
            " • Adjust thermostat settings by 1-2 degrees to lower HVAC energy use."
        ])
    elif top == "Food":
        lines.extend([
            " • Incorporate more plant-based meals into your weekly diet.",
            " • Reduce food waste by planning meals and storing food properly.",
            " • Choose locally sourced and seasonal ingredients where possible."
        ])
    else:
        lines.extend([
            " • Audit your monthly energy and travel habits to spot quick savings.",
            " • Focus on small daily habit changes to gradually reduce emissions."
        ])

    return "\n".join(lines)


def generate_recommendations(report: TotalFootprintReport) -> str:
    """Generate personalized carbon reduction recommendations using Gemini API.

    Enforces graceful degradation: if API key is missing or call fails,
    returns static fallback recommendations without raising an exception.
    """
    api_key = os.getenv("GEMINI_API_KEY", "").strip()

    if not api_key or api_key == "your_gemini_api_key_here":
        return generate_fallback_recommendations(report)

    try:
        from google import genai

        client = genai.Client(api_key=api_key)

        prompt = f"""
You are an expert environmental consultant giving practical, friendly carbon footprint reduction advice.

Here is the user's estimated monthly carbon footprint calculation:
- Total Footprint: {report.total_kg_co2e} kg CO2e / month
- Breakdown:
"""
        for cat, b in report.category_breakdowns.items():
            prompt += f"  * {cat}: {b.emissions_kg_co2e} kg CO2e ({b.percentage_share}%)\n"

        prompt += f"""
- Highest Emitting Category: {report.highest_emitting_category}

Task:
Provide 3 concise, practical, high-impact actionable tips to help the user reduce their carbon footprint, focusing especially on their highest emitting category ({report.highest_emitting_category}).
Keep your tone encouraging, direct, and realistic. Do not invent or recalculate any numerical figures.
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        if response and response.text:
            return response.text.strip()
        else:
            return generate_fallback_recommendations(report)

    except Exception as err:
        # Graceful degradation on network timeout, quota limit, invalid key, etc.
        return f"(API Notice: {err})\n\n" + generate_fallback_recommendations(report)
