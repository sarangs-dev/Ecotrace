"""CLI interface module for Personal Carbon Footprint Calculator."""

import sys
from typing import Sequence
from src.models import (
    ElectricityInput,
    FoodInput,
    TotalFootprintReport,
    TransportationInput,
    UserLifestyleInput,
)
from src.validators import validate_menu_choice, validate_non_negative_float

DIVIDER = "=" * 64
SUB_DIVIDER = "-" * 64


def print_divider(char: str = "="):
    print(char * 64)


def prompt_float(prompt_text: str, field_name: str) -> float:
    """Prompt user until a valid non-negative float is provided."""
    while True:
        try:
            raw_val = input(prompt_text)
            return validate_non_negative_float(raw_val, field_name)
        except ValueError as err:
            print(f"  [!] Invalid Input: {err}")


def prompt_choice(prompt_text: str, valid_choices: Sequence[str]) -> str:
    """Prompt user until a valid menu choice is selected."""
    while True:
        try:
            raw_val = input(prompt_text)
            return validate_menu_choice(raw_val, valid_choices)
        except ValueError as err:
            print(f"  [!] Invalid Selection: {err}")


def display_header():
    """Print application welcome header."""
    print_divider("=")
    print("      PERSONAL CARBON FOOTPRINT CALCULATOR (SDG 13)")
    print("        Estimate & Reduce Your Personal Carbon Footprint")
    print_divider("=")
    print()


def collect_user_lifestyle_input() -> UserLifestyleInput:
    """Collect lifestyle data from CLI prompts for all MVP categories."""
    print_divider("-")
    print(" 1. TRANSPORTATION ACTIVITY (Estimated monthly km)")
    print_divider("-")
    car_km = prompt_float("  Enter distance travelled by CAR (km/month): ", "Car Distance")
    bus_km = prompt_float("  Enter distance travelled by BUS (km/month): ", "Bus Distance")
    train_km = prompt_float("  Enter distance travelled by TRAIN (km/month): ", "Train Distance")
    flight_km = prompt_float("  Enter distance travelled by FLIGHT (km/month): ", "Flight Distance")

    print()
    print_divider("-")
    print(" 2. ELECTRICITY CONSUMPTION")
    print_divider("-")
    kwh = prompt_float("  Enter monthly electricity usage (kWh/month): ", "Electricity Usage")

    print()
    print_divider("-")
    print(" 3. DIETARY HABITS")
    print_divider("-")
    print("  Select your primary dietary style:")
    print("   [1] Meat-heavy (high red meat consumption)")
    print("   [2] Balanced (average meat & plant diet)")
    print("   [3] Vegetarian (no meat, includes dairy/eggs)")
    print("   [4] Vegan (100% plant-based)")

    choice = prompt_choice("  Enter choice (1-4): ", ["1", "2", "3", "4"])
    diet_map = {
        "1": "meat_heavy",
        "2": "balanced",
        "3": "vegetarian",
        "4": "vegan",
    }
    diet_type = diet_map[choice]

    return UserLifestyleInput(
        transportation=TransportationInput(
            car_km=car_km, bus_km=bus_km, train_km=train_km, flight_km=flight_km
        ),
        electricity=ElectricityInput(kwh_per_month=kwh),
        food=FoodInput(diet_type=diet_type),
    )


def display_footprint_report(report: TotalFootprintReport):
    """Display formatted table showing category breakdowns and total footprint."""
    print()
    print_divider("=")
    print("                    FOOTPRINT CALCULATION RESULTS")
    print_divider("=")
    print(f" {'Category':<20} | {'Emissions (kg CO2e)':<20} | {'Share (%)':<10}")
    print_divider("-")

    for cat_name, b in report.category_breakdowns.items():
        print(f" {cat_name:<20} | {b.emissions_kg_co2e:>18.2f} | {b.percentage_share:>8.1f}%")

    print_divider("-")
    print(f" {'TOTAL ESTIMATED MONTHLY FOOTPRINT':<20} | {report.total_kg_co2e:>18.2f} kg CO2e")
    print_divider("=")
    print(f" Largest Emission Driver: {report.highest_emitting_category}")
    print(f" Disclaimer: {report.disclaimer}")
    print_divider("=")
    print()


def display_ai_recommendations(recommendation_text: str):
    """Display AI-generated action plan and recommendations."""
    print_divider("=")
    print("              AI-POWERED PERSONALIZED RECOMMENDATIONS")
    print_divider("=")
    print(recommendation_text)
    print_divider("=")
    print()
