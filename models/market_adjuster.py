# models/market_adjuster.py

"""
Market Adjuster Module

Applies real-time market and regional risk adjustments to the base premium.
"""

def apply_market_conditions(base_premium, row, verbose=False):
    """
    Adjust the base premium based on market volatility and region risk.

    Args:
        base_premium (float): The base premium before adjustment.
        row (pd.Series): The applicant's data.
        verbose (bool): If True, returns breakdown dictionary.

    Returns:
        float: Final adjusted premium
        dict (optional): Adjustment breakdown
    """

    explanation = {}

    # --- Market Volatility Adjustment ---
    market_vol = row.get("market_volatility_index", 0)
    volatility_factor = market_vol * 0.10
    explanation["market_volatility_index"] = f"{market_vol} (x{round(1 + volatility_factor, 3)})"

    # --- Region Risk Adjustment ---
    region_risk = row.get("region_risk_score", 0)
    region_factor = region_risk * 0.05
    explanation["region_risk_score"] = f"{region_risk} (x{round(1 + region_factor, 3)})"

    # --- Apply Adjustments ---
    adjustment_multiplier = 1 + volatility_factor + region_factor
    final_premium = round(base_premium * adjustment_multiplier, 2)

    if verbose:
        explanation["adjustment_multiplier"] = round(adjustment_multiplier, 3)
        explanation["final_premium"] = final_premium
        return final_premium, explanation

    return final_premium
