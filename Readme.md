# Dynamic Insurance Premium Calculator

A modular, rule-based system that calculates personalized, risk-adjusted, and market-aware insurance premiums. This tool uses demographic, health, and policy-related risk factors to simulate real-world actuarial logic and generate transparent, explainable insurance quotes.

---

## 📌 Problem Statement

Design a system that calculates personalized insurance premiums based on real-time risk factors and market conditions. The system should:

- Balance competitive pricing with profitability
- Simulate realistic risk assessment
- Adjust premiums based on market volatility

---

## ✅ Features

- **Risk Scoring**: Calculates a composite risk score per applicant  
- **Dynamic Pricing**: Premiums adjusted based on market trends and policy type  
- **Detailed Explanations**: Transparent output for every quote  
- **Batch Mode**: Processes multiple applicants from a CSV file  
- **Modular Architecture**: Separated logic for risk, pricing, market, and quote generation

---

## 🧠 Skills Demonstrated

| Area | Description |
|------|-------------|
| **AI/ML Concepts** | Rule-based modeling, pricing optimization, market simulation |
| **Critical Thinking** | Balancing fair pricing with business profitability |
| **Problem Solving** | Handles multi-variable pricing, risk volatility |
| **Clean Architecture** | Applicant data → risk profiling → pricing → adjustment → quote |
| **Deliverable** | Ready-to-run tool with clear breakdown and saved results |

---

## 📂 Project Structure

```
Dynamic-Insurance-Premium-Calculator-Project/
├── app.py                      # Main script
├── data/
│   └── insurance_dataset.csv    # Input CSV dataset
├── output/
│   └── insurance_quotes.txt     # Output file
├── models/
│   ├── risk_model.py
│   ├── pricing_model.py
│   └── market_adjuster.py
├── utils/
│   ├── quote_generator.py
│   └── preprocessing.py
└── README.md
```

---

## ⚙️ How to Run

### Prerequisites

- Python 3.8+
- `pandas` installed (`pip install pandas`)

### Running the app

```bash
python app.py
```

Quotes for applicants will be:
- Displayed in the terminal
- Saved to `output/insurance_quotes.txt`

---

## 🔄 Workflow

1. Load applicant data (`insurance_dataset.csv`)
2. Clean and validate inputs
3. Assess risk using rule-based logic
4. Calculate base premium based on policy and risk score
5. Adjust price for current market conditions
6. Generate and save final quote

---

## 📋 Sample Output (Simplified)

```
QUOTE FOR APPLICANT #1
-------------------------------
Vehicle Type: truck
Policy Type: basic
Final Premium: ₹14,771.95

Risk Score: 16.42
Base Premium: ₹14,568.00
Market Adjustment: +₹203.95

→ Final Quote: ₹14,771.95
-------------------------------
```

---

## 📁 Data Format

Sample input CSV (`data/insurance_dataset.csv`) columns:

```csv
age, bmi, smoker, accident_history, credit_score, region_risk_score, driving_experience, vehicle_type, policy_type
25, 32.5, yes, 2, poor, 0.45, 2, car, premium
```

---

## Notes

- This project is based on a **rule-based model**. Risk assessment and premium calculations follow predefined logic and weighted conditions. This approach ensures transparency, control, and ease of understanding—especially important in insurance-related systems.

- The logic is implemented using modular Python scripts without the use of machine learning. This design makes it easier to audit and adjust rules as needed.

- Technologies used include Python and pandas for data processing.

- The structure is extendable and can support ML models like regression or decision trees in future versions.

- All data used for testing is synthetic and created for demonstration purposes only.