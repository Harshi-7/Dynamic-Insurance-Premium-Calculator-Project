# utils/quote_generator.py

"""
Quote Generator

Formats the final output shown to users with explanations.
"""

def generate_quote(row, final_premium, risk_expl=None, pricing_expl=None, adjust_expl=None):
    """
    Generates a readable insurance premium quote.

    Args:
        row (pd.Series): Applicant data
        final_premium (float): Final premium after all adjustments
        risk_expl (dict): Risk score explanation
        pricing_expl (dict): Pricing breakdown
        adjust_expl (dict): Market adjustment breakdown

    Returns:
        str: Formatted quote
    """

    name = row.get("name", "Applicant")
    vehicle = row.get("vehicle_type", "N/A")
    policy = row.get("policy_type", "N/A")

    output = []
    output.append(f"Insurance Quote for: {name}")
    output.append(f"Vehicle Type: {vehicle}")
    output.append(f"Policy Type: {policy}")
    output.append(f"Final Premium: ₹{final_premium}")
    output.append("")

    # --- Breakdown Sections ---
    if risk_expl:
        output.append("Risk Assessment Factors:")
        for key, val in risk_expl.items():
            if key != "total_score":
                output.append(f" - {key.replace('_', ' ').title()}: {val}")
        output.append(f" -> Risk Score: {risk_expl.get('total_score', '?')}")
        output.append("")

    if pricing_expl:
        output.append("Base Premium Calculation:")
        for key, val in pricing_expl.items():
            if key != "base_premium":
                output.append(f" - {key.replace('_', ' ').title()}: {val}")
        output.append(f" -> Base Premium: ₹{pricing_expl.get('base_premium', '?')}")
        output.append("")

    if adjust_expl:
        output.append("Market Adjustment Applied:")
        for key, val in adjust_expl.items():
            if key != "final_premium":
                output.append(f" - {key.replace('_', ' ').title()}: {val}")
        output.append(f" -> Adjusted Final Premium: ₹{adjust_expl.get('final_premium', '?')}")
        output.append("")

    output.append("Thank you for choosing our insurance platform.")

    return "\n".join(output)
