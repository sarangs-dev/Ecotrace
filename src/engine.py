"""Deterministic calculation engine for Personal Carbon Footprint Calculator."""

import json
from pathlib import Path
from typing import Dict, Union

from src.models import (
    CategoryFootprint,
    ElectricityInput,
    FoodInput,
    TotalFootprintReport,
    TransportationInput,
    UserLifestyleInput,
)

DEFAULT_FACTORS_PATH = Path(__file__).resolve().parent.parent / "data" / "emission_factors.json"


def load_emission_factors(file_path: Union[str, Path] = DEFAULT_FACTORS_PATH) -> Dict:
    """Load emission factors configuration from external JSON file.

    Raises:
        FileNotFoundError: If factors file does not exist.
        ValueError: If JSON file is malformed.
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Emission factors file not found at: {path}")

    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as err:
        raise ValueError(f"Malformed JSON in emission factors file: {err}") from err


def calculate_transportation_emissions(
    transport_input: TransportationInput, factors: Dict
) -> float:
    """Calculate monthly transportation carbon emissions in kg CO2e."""
    tfactors = factors.get("transportation", {}).get("factors", {})
    car = transport_input.car_km * tfactors.get("car", 0.170)
    bus = transport_input.bus_km * tfactors.get("bus", 0.080)
    train = transport_input.train_km * tfactors.get("train", 0.040)
    flight = transport_input.flight_km * tfactors.get("flight", 0.250)
    return max(0.0, car + bus + train + flight)


def calculate_electricity_emissions(
    electricity_input: ElectricityInput, factors: Dict
) -> float:
    """Calculate monthly electricity carbon emissions in kg CO2e."""
    efactors = factors.get("electricity", {}).get("factors", {})
    grid_factor = efactors.get("grid_default", 0.450)
    return max(0.0, electricity_input.kwh_per_month * grid_factor)


def calculate_food_emissions(food_input: FoodInput, factors: Dict) -> float:
    """Calculate monthly dietary carbon emissions in kg CO2e."""
    ffactors = factors.get("food", {}).get("factors", {})
    diet_key = food_input.diet_type.lower()
    return max(0.0, ffactors.get(diet_key, ffactors.get("balanced", 140.0)))


def calculate_footprint(
    user_input: UserLifestyleInput,
    factors_file: Union[str, Path] = DEFAULT_FACTORS_PATH,
) -> TotalFootprintReport:
    """Calculate category breakdowns, percentage shares, and total footprint report."""
    factors = load_emission_factors(factors_file)

    transport_emissions = calculate_transportation_emissions(
        user_input.transportation, factors
    )
    electricity_emissions = calculate_electricity_emissions(
        user_input.electricity, factors
    )
    food_emissions = calculate_food_emissions(user_input.food, factors)

    total_kg = transport_emissions + electricity_emissions + food_emissions

    # Calculate percentage share safely
    def calc_share(category_val: float) -> float:
        if total_kg <= 0:
            return 0.0
        return round((category_val / total_kg) * 100, 1)

    breakdowns = {
        "Transportation": CategoryFootprint(
            category_name="Transportation",
            emissions_kg_co2e=round(transport_emissions, 2),
            percentage_share=calc_share(transport_emissions),
        ),
        "Electricity": CategoryFootprint(
            category_name="Electricity",
            emissions_kg_co2e=round(electricity_emissions, 2),
            percentage_share=calc_share(electricity_emissions),
        ),
        "Food": CategoryFootprint(
            category_name="Food",
            emissions_kg_co2e=round(food_emissions, 2),
            percentage_share=calc_share(food_emissions),
        ),
    }

    # Determine highest emitting category
    if total_kg > 0:
        highest_cat = max(
            breakdowns.values(), key=lambda c: c.emissions_kg_co2e
        ).category_name
    else:
        highest_cat = "None"

    return TotalFootprintReport(
        category_breakdowns=breakdowns,
        total_kg_co2e=round(total_kg, 2),
        highest_emitting_category=highest_cat,
    )
