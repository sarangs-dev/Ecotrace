"""Data models for Personal Carbon Footprint Calculator."""

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass(frozen=True)
class TransportationInput:
    """User transportation activity data in kilometers per month."""
    car_km: float = 0.0
    bus_km: float = 0.0
    train_km: float = 0.0
    flight_km: float = 0.0


@dataclass(frozen=True)
class ElectricityInput:
    """User electricity consumption in kWh per month."""
    kwh_per_month: float = 0.0


@dataclass(frozen=True)
class FoodInput:
    """User dietary preference key."""
    diet_type: str = "balanced"  # Options: meat_heavy, balanced, vegetarian, vegan


@dataclass(frozen=True)
class UserLifestyleInput:
    """Container for all user lifestyle inputs."""
    transportation: TransportationInput
    electricity: ElectricityInput
    food: FoodInput


@dataclass(frozen=True)
class CategoryFootprint:
    """Calculated footprint breakdown for a single category."""
    category_name: str
    emissions_kg_co2e: float
    percentage_share: float = 0.0


@dataclass(frozen=True)
class TotalFootprintReport:
    """Overall monthly footprint calculation summary."""
    category_breakdowns: Dict[str, CategoryFootprint]
    total_kg_co2e: float
    highest_emitting_category: str
    disclaimer: str = (
        "Educational estimate only. Calculations are based on generalized "
        "regional emission factors and assumptions."
    )
