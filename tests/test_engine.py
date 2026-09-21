"""Unit tests for src/engine.py calculation functions."""

import json
import pytest
from pathlib import Path
from src.models import (
    ElectricityInput,
    FoodInput,
    TransportationInput,
    UserLifestyleInput,
)
from src.engine import (
    calculate_electricity_emissions,
    calculate_food_emissions,
    calculate_footprint,
    calculate_transportation_emissions,
    load_emission_factors,
)

SAMPLE_FACTORS = {
    "transportation": {
        "factors": {"car": 0.170, "bus": 0.080, "train": 0.040, "flight": 0.250}
    },
    "electricity": {"factors": {"grid_default": 0.450}},
    "food": {
        "factors": {
            "meat_heavy": 210.0,
            "balanced": 140.0,
            "vegetarian": 90.0,
            "vegan": 60.0,
        }
    },
}


def test_load_emission_factors():
    factors = load_emission_factors()
    assert "transportation" in factors
    assert "electricity" in factors
    assert "food" in factors


def test_load_emission_factors_missing():
    with pytest.raises(FileNotFoundError):
        load_emission_factors(Path("non_existent_file.json"))


def test_calculate_transportation_emissions():
    trans = TransportationInput(car_km=100, bus_km=50, train_km=0, flight_km=0)
    # 100 * 0.170 + 50 * 0.080 = 17.0 + 4.0 = 21.0
    res = calculate_transportation_emissions(trans, SAMPLE_FACTORS)
    assert res == pytest.approx(21.0)


def test_calculate_electricity_emissions():
    elec = ElectricityInput(kwh_per_month=200)
    # 200 * 0.450 = 90.0
    res = calculate_electricity_emissions(elec, SAMPLE_FACTORS)
    assert res == pytest.approx(90.0)


def test_calculate_food_emissions():
    food_vegan = FoodInput(diet_type="vegan")
    assert calculate_food_emissions(food_vegan, SAMPLE_FACTORS) == 60.0

    food_meat = FoodInput(diet_type="meat_heavy")
    assert calculate_food_emissions(food_meat, SAMPLE_FACTORS) == 210.0

    food_unknown = FoodInput(diet_type="unknown_diet")
    assert calculate_food_emissions(food_unknown, SAMPLE_FACTORS) == 140.0


def test_calculate_footprint_total_and_breakdown():
    user_input = UserLifestyleInput(
        transportation=TransportationInput(car_km=100),  # 17.0
        electricity=ElectricityInput(kwh_per_month=100),  # 45.0
        food=FoodInput(diet_type="vegetarian"),  # 90.0
    )
    # Total = 17 + 45 + 90 = 152.0 kg CO2e
    report = calculate_footprint(user_input)
    assert report.total_kg_co2e == 152.0
    assert report.highest_emitting_category == "Food"
    assert report.category_breakdowns["Food"].emissions_kg_co2e == 90.0
    assert report.category_breakdowns["Food"].percentage_share == pytest.approx(59.2, 0.1)


def test_zero_emissions():
    user_input = UserLifestyleInput(
        transportation=TransportationInput(0, 0, 0, 0),
        electricity=ElectricityInput(0),
        food=FoodInput(diet_type="unknown"),  # falls back to balanced=140
    )
    report = calculate_footprint(user_input)
    assert report.total_kg_co2e == 140.0
