"""
Advanced Preprocessing Module

Cleans and validates input data before use in premium prediction pipeline.
"""

import warnings

def clean_row(row):
    """
    Clean and validate a single applicant's row.
    
    Parameters:
        row (pd.Series): Raw applicant data.
    
    Returns:
        pd.Series: Cleaned and validated row.
    """

    # --- Handle missing values with defaults ---
    row['sex'] = str(row.get('sex', 'unknown')).strip().lower()
    row['smoker'] = str(row.get('smoker', 'no')).strip().lower()
    row['vehicle_type'] = str(row.get('vehicle_type', 'car')).strip().lower()
    row['policy_type'] = str(row.get('policy_type', 'basic')).strip().lower()
    row['region'] = str(row.get('region', 'unknown')).strip().lower()

    # --- Numeric Columns with Type & Range Validation ---
    try:
        row['age'] = int(float(row.get('age', 30)))
        if not (18 <= row['age'] <= 100):
            warnings.warn(f"Unusual age: {row['age']}. Resetting to 30.")
            row['age'] = 30
    except:
        row['age'] = 30

    try:
        row['bmi'] = round(float(row.get('bmi', 25.0)), 1)
        if not (10 <= row['bmi'] <= 60):
            warnings.warn(f"Outlier BMI: {row['bmi']}. Resetting to 25.0.")
            row['bmi'] = 25.0
    except:
        row['bmi'] = 25.0

    try:
        row['children'] = int(row.get('children', 0))
        row['children'] = max(0, min(row['children'], 10))  # Cap children between 0-10
    except:
        row['children'] = 0

    try:
        row['accident_history'] = int(row.get('accident_history', 0))
        row['accident_history'] = max(0, min(row['accident_history'], 10))
    except:
        row['accident_history'] = 0

    try:
        row['credit_score'] = int(row.get('credit_score', 700))
        if not (300 <= row['credit_score'] <= 850):
            warnings.warn(f"Unusual credit score: {row['credit_score']}. Resetting to 700.")
            row['credit_score'] = 700
    except:
        row['credit_score'] = 700

    try:
        row['region_risk_score'] = float(row.get('region_risk_score', 0.5))
        row['region_risk_score'] = round(max(0.0, min(row['region_risk_score'], 1.0)), 2)
    except:
        row['region_risk_score'] = 0.5

    try:
        row['market_volatility_index'] = float(row.get('market_volatility_index', 0.3))
        row['market_volatility_index'] = round(max(0.0, min(row['market_volatility_index'], 1.0)), 2)
    except:
        row['market_volatility_index'] = 0.3

    try:
        row['driving_experience'] = int(row.get('driving_experience', 5))
        if not (0 <= row['driving_experience'] <= row['age'] - 16):
            warnings.warn(f"Invalid driving experience: {row['driving_experience']}. Resetting to 5.")
            row['driving_experience'] = 5
    except:
        row['driving_experience'] = 5

    return row
