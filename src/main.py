"""Main entry point for Personal Carbon Footprint Calculator CLI application."""

import sys
from src.ai_service import generate_recommendations
from src.cli import (
    collect_user_lifestyle_input,
    display_ai_recommendations,
    display_footprint_report,
    display_header,
)
from src.engine import calculate_footprint


def main():
    """Run the Personal Carbon Footprint Calculator end-to-end workflow."""
    try:
        display_header()
        print("Please answer the following prompts about your monthly activity.\n")

        # Step 1: Collect user input with validation
        user_input = collect_user_lifestyle_input()

        # Step 2: Perform deterministic calculation
        print("\nCalculating estimated carbon footprint...")
        report = calculate_footprint(user_input)

        # Step 3: Display category breakdown and total estimate
        display_footprint_report(report)

        # Step 4: Generate and display AI-powered personalized recommendations
        print("Generating AI recommendations based on your highest emission categories...")
        recommendations = generate_recommendations(report)
        display_ai_recommendations(recommendations)

        print("Thank you for using the Personal Carbon Footprint Calculator!")

    except KeyboardInterrupt:
        print("\n\nSession cancelled by user. Goodbye!")
        sys.exit(0)
    except Exception as err:
        print(f"\n[!] An error occurred: {err}")
        sys.exit(1)


if __name__ == "__main__":
    main()
