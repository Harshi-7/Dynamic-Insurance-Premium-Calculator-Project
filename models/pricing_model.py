# models/pricing_model.py

"""
Premium Pricing Model

Calculates a base insurance premium using:
- Risk score
- Vehicle type
- Policy type

Optionally returns detailed breakdown for transparency.
"""

def calculate_base_premium(risk_score, row, verbose=False):
    explanation = {}

    # Start with a base amount
    base_amount = 5000

    # --- Vehicle Type Multiplier ---
    vehicle_multipliers = {
        "bike": 1.0,
        "car": 1.2,
        "SUV": 1.4,
        "truck": 1.6
    }

    vehicle_type = row["vehicle_type"]
    vehicle_factor = vehicle_multipliers.get(vehicle_type, 1.2)
    explanation["vehicle_type"] = f"{vehicle_type} (x{vehicle_factor})"

    # --- Policy Type Multiplier ---
    policy_multipliers = {
        "basic": 1.0,
        "premium": 1.3,
        "family": 1.5
    }

    policy_type = row["policy_type"]
    policy_factor = policy_multipliers.get(policy_type, 1.0)
    explanation["policy_type"] = f"{policy_type} (x{policy_factor})"

    # --- Risk Score Factor ---
    # For every risk point, add 5% to the base
    risk_factor = 1 + (risk_score * 0.05)
    explanation["risk_score_factor"] = f"Risk score {risk_score} → x{round(risk_factor, 2)}"

    # --- Final Base Premium Calculation ---
    premium = base_amount * vehicle_factor * policy_factor * risk_factor
    premium = round(premium, 2)

    if verbose:
        explanation["base_premium"] = premium
        return premium, explanation

    return premium
