import pandas as pd
from models.risk_model import assess_risk
from models.pricing_model import calculate_base_premium
from models.market_adjuster import apply_market_conditions
from utils.quote_generator import generate_quote
from utils.preprocessing import clean_row
import os


def get_user_input():
    print("\nPlease enter applicant details:")

    try:
        age = int(input("Age: "))
        sex = input("Sex (male/female/other): ").lower()
        bmi = float(input("BMI: "))
        smoker = input("Smoker? (yes/no): ").lower()
        vehicle_type = input("Vehicle Type (car/bike/truck): ").lower()
        policy_type = input("Policy Type (basic/family/premium): ").lower()
        accident_history = int(input("Number of past accidents: "))
        credit_score = int(input("Credit Score (300-850): "))
        region_risk_score = float(input("Region Risk Score (0.0 - 1.0): "))
        market_volatility_index = float(input("Market Volatility Index (0.0 - 1.0): "))
        driving_experience = int(input("Years of Driving Experience: "))

        row = pd.Series({
            'age': age,
            'sex': sex,
            'bmi': bmi,
            'smoker': smoker,
            'vehicle_type': vehicle_type,
            'policy_type': policy_type,
            'accident_history': accident_history,
            'credit_score': credit_score,
            'region_risk_score': region_risk_score,
            'market_volatility_index': market_volatility_index,
            'driving_experience': driving_experience
        })

        return row
    except Exception as e:
        print(f"Invalid input: {e}")
        return None


def process_applicant(row, index=None):
    try:
        row = clean_row(row)
        risk_score, risk_expl = assess_risk(row, verbose=True)
        base_premium, pricing_expl = calculate_base_premium(risk_score, row, verbose=True)
        final_premium, adjust_expl = apply_market_conditions(base_premium, row, verbose=True)
        quote = generate_quote(row, final_premium, risk_expl, pricing_expl, adjust_expl)

        print(f"\nQuote for Applicant #{index + 1 if index is not None else 'You'}")
        print("-" * 50)
        print(quote)
        print("-" * 50)

        return quote

    except Exception as e:
        print(f"Error processing applicant: {e}")
        return None


def main():
    print("Dynamic Insurance Premium Calculator")
    mode = input("Select mode: (1) CSV Batch Mode (2) Manual Entry Mode → ")

    all_quotes = []

    if mode == "1":
        try:
            df = pd.read_csv("data/insurance dataset.csv")
            print(f"\nLoaded {len(df)} applicant records.")
        except FileNotFoundError:
            print("File not found: data/insurance dataset.csv")
            return

        for index, row in df.iterrows():
            quote = process_applicant(row, index=index)
            if quote:
                all_quotes.append(quote)

            if index == 4:
                break

    elif mode == "2":
        row = get_user_input()
        if row is not None:
            quote = process_applicant(row)
            if quote:
                all_quotes.append(quote)

    else:
        print("Invalid mode selected.")
        return

    if all_quotes:
        os.makedirs("output", exist_ok=True)
        with open("output/insurance_quotes.txt", "w", encoding="utf-8") as f:
            for q in all_quotes:
                f.write(q + "\n" + "-" * 80 + "\n")
        print("\nQuotes saved to output/insurance_quotes.txt")


if __name__ == "__main__":
    main()
