import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


# -----------------------------
# Sample Rajasthan Data
# -----------------------------
sample_data = pd.DataFrame({
    "District": ["Jaipur", "Jodhpur", "Udaipur", "Barmer", "Dholpur"],
    "Availability": [98, 96, 94, 91, 89],
    "Affordability": [88, 78, 70, 60, 55],
    "Reliability": [95, 85, 80, 70, 65],
    "Quality": [84, 75, 72, 55, 50],
    "Cleanliness": [40, 35, 45, 30, 28],
    "Equity": [90, 82, 80, 75, 70]
})


# -----------------------------
# Derive PCA Weights
# -----------------------------
def calculate_pca_weights(df):
    X = df[[
        "Availability",
        "Affordability",
        "Reliability",
        "Quality",
        "Cleanliness",
        "Equity"
    ]]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    pca = PCA()
    pca.fit(X_scaled)

    loadings = np.abs(pca.components_[0])
    weights = loadings / loadings.sum()

    return dict(zip(X.columns, weights))


# -----------------------------
# Calculate EDI
# -----------------------------
def calculate_edi(scores, weights):
    edi = 0

    for factor in weights:
        edi += scores[factor] * weights[factor]

    return edi


# -----------------------------
# EDI Category
# -----------------------------
def get_category(edi):

    if edi >= 85:
        return "Very High Energy Dignity"

    elif edi >= 70:
        return "High Energy Dignity"

    elif edi >= 55:
        return "Moderate Energy Dignity"

    elif edi >= 40:
        return "Low Energy Dignity"

    else:
        return "Severe Energy Deprivation"


# -----------------------------
# Weakest Areas
# -----------------------------
def weakest_areas(scores):
    sorted_scores = sorted(scores.items(),
                           key=lambda x: x[1])

    return sorted_scores[:2]


# -----------------------------
# Convert User Inputs to 0-100
# -----------------------------
def get_user_scores():

    print("\nEnter Raw Values\n")

    availability = float(
        input("Electricity access (% households): ")
    )

    electricity_burden = float(
        input("Electricity expenditure as % income: ")
    )

    supply_hours = float(
        input("Average electricity supply (hours/day): ")
    )

    appliances = float(
        input("Number of appliances used (0-5): ")
    )

    clean_fuel = float(
        input("Clean cooking fuel adoption (%): ")
    )

    rural_urban_gap = float(
        input("Rural-urban energy gap (%): ")
    )

    # Convert to 0-100

    affordability = max(
        0,
        min(100,
            100 * (10 - electricity_burden) / 9)
    )

    reliability = max(
        0,
        min(100,
            supply_hours / 24 * 100)
    )

    quality = max(
        0,
        min(100,
            appliances / 5 * 100)
    )

    equity = max(
        0,
        min(100,
            100 - rural_urban_gap)
    )

    scores = {
        "Availability": availability,
        "Affordability": affordability,
        "Reliability": reliability,
        "Quality": quality,
        "Cleanliness": clean_fuel,
        "Equity": equity
    }

    return scores


# -----------------------------
# Main Program
# -----------------------------
print("ENERGY DIGNITY INDEX CALCULATOR\n")

print("1. Use Sample Rajasthan Data")
print("2. Enter Your Own Data")

choice = input("\nEnter choice: ")

weights = calculate_pca_weights(sample_data)

print("\nPCA Derived Weights")

for factor, weight in weights.items():
    print(f"{factor:<15}: {weight:.3f}")


if choice == "1":

    print("\nDISTRICT RESULTS\n")

    for _, row in sample_data.iterrows():

        scores = {
            "Availability": row["Availability"],
            "Affordability": row["Affordability"],
            "Reliability": row["Reliability"],
            "Quality": row["Quality"],
            "Cleanliness": row["Cleanliness"],
            "Equity": row["Equity"]
        }

        edi = calculate_edi(scores, weights)

        category = get_category(edi)

        weak = weakest_areas(scores)

        print("-" * 40)
        print(row["District"])

        print(f"EDI: {edi:.1f} ({category})")

        print("\nWeakest Areas:")

        for factor, score in weak:
            print(f"• {factor} ({score:.1f})")

        print()


elif choice == "2":

    scores = get_user_scores()

    edi = calculate_edi(scores, weights)

    category = get_category(edi)

    weak = weakest_areas(scores)

    print("\nRESULT")
    print("-" * 40)

    print(f"EDI: {edi:.1f} ({category})")

    print("\nWeakest Areas:")

    for factor, score in weak:
        print(f"• {factor} ({score:.1f})")

else:
    print("Invalid choice.")