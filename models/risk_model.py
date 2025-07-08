# models/risk_model.py

"""
Risk Assessment Engine for Insurance Premium Calculation

This module calculates a comprehensive risk score using:
- Age category
- BMI category
- Smoking status
- Accident history
- Credit score tier
- Region risk score
- Driving experience

Returns:
- Numerical risk score
- (Optional) Explanation dictionary for transparency
"""

def assess_risk(row, verbose=False):
    """
    Assess risk based on applicant data.

    Args:
        row (pd.Series): Applicant data from the dataset.
        verbose (bool): If True, also return detailed breakdown.

    Returns:
        float: Risk score
        dict (optional): Explanation per feature
    """

    explanation = {}

    # --- Age Risk ---
    age = row['age']
    if age < 25:
        age_risk = 3
        explanation['age'] = 'High risk (young drivers)'
    elif age <= 40:
        age_risk = 2
        explanation['age'] = 'Moderate risk'
    elif age <= 60:
        age_risk = 1
        explanation['age'] = 'Low risk'
    else:
        age_risk = 2
        explanation['age'] = 'Slightly elevated risk (elderly)'

    # --- BMI Risk ---
    bmi = row['bmi']
    if bmi < 18.5:
        bmi_risk = 2
        explanation['bmi'] = 'Underweight (health risk)'
    elif 18.5 <= bmi <= 24.9:
        bmi_risk = 0.5
        explanation['bmi'] = 'Healthy BMI'
    elif 25 <= bmi <= 29.9:
        bmi_risk = 1.5
        explanation['bmi'] = 'Overweight'
    else:
        bmi_risk = 3
        explanation['bmi'] = 'Obese (high health risk)'

    # --- Smoker Risk ---
    smoker_risk = 4 if row['smoker'] == 'yes' else 0
    explanation['smoker'] = 'Smoker' if smoker_risk else 'Non-smoker'

    # --- Accident History Risk ---
    accidents = row['accident_history']
    accident_risk = min(accidents * 1.5, 5)  # cap to prevent outlier impact
    explanation['accident_history'] = f'{accidents} accidents'

    # --- Credit Score Risk ---
    credit = row['credit_score']
    if credit >= 750:
        credit_risk = 0.5
        explanation['credit_score'] = 'Excellent credit'
    elif credit >= 650:
        credit_risk = 1.5
        explanation['credit_score'] = 'Good credit'
    elif credit >= 550:
        credit_risk = 3
        explanation['credit_score'] = 'Fair credit'
    else:
        credit_risk = 5
        explanation['credit_score'] = 'Poor credit'

    # --- Region Risk Score (direct use) ---
    region_risk = row['region_risk_score']
    explanation['region_risk_score'] = f'{region_risk:.2f}'

    # --- Driving Experience ---
    experience = row['driving_experience']
    if experience >= 20:
        experience_risk = 0.2
        explanation['driving_experience'] = 'Highly experienced driver'
    elif experience >= 10:
        experience_risk = 0.8
        explanation['driving_experience'] = 'Moderate experience'
    elif experience >= 5:
        experience_risk = 1.5
        explanation['driving_experience'] = 'Low experience'
    else:
        experience_risk = 3
        explanation['driving_experience'] = 'Inexperienced driver'

    # --- Total Score ---
    total_risk_score = round(
        age_risk + bmi_risk + smoker_risk + accident_risk +
        credit_risk + region_risk + experience_risk, 2
    )

    if verbose:
        explanation['total_score'] = total_risk_score
        return total_risk_score, explanation

    return total_risk_score
