# Energy Dignity Index (EDI) for India

## Overview

The Energy Dignity Index (EDI) is a multidimensional framework designed to measure whether people have access to energy in a manner that supports a dignified life.

Traditional indicators such as electrification rates only answer the question:

> "Does a household have an electricity connection?"

EDI attempts to answer a broader question:

> "Can people afford, access, and use energy reliably and equitably to improve their quality of life?"

The index combines six dimensions of energy dignity:

* Availability
* Affordability
* Reliability
* Quality
* Cleanliness
* Equity

---

## Methodology

### 1. Sample Dataset

This project uses sample Rajasthan district data to derive PCA-based weights.

| District | Availability | Affordability | Reliability | Quality | Cleanliness | Equity |
| -------- | -----------: | ------------: | ----------: | ------: | ----------: | -----: |
| Jaipur   |           98 |            88 |          95 |      84 |          40 |     90 |
| Jodhpur  |           96 |            78 |          85 |      75 |          35 |     82 |
| Udaipur  |           94 |            70 |          80 |      72 |          45 |     80 |
| Barmer   |           91 |            60 |          70 |      55 |          30 |     75 |
| Dholpur  |           89 |            55 |          65 |      50 |          28 |     70 |

---

## 2. Conversion of Raw Data to 0–100 Scale

Users can either use the sample data or enter their own raw data.

The following transformations convert raw values into standardized scores out of 100.

### Availability

Percentage of households with electricity access.

Example:

97% households electrified

Availability Score = 97

---

### Affordability

Measured using electricity expenditure as a percentage of household income.

Assumptions:

* Best case: 1% of income
* Worst case: 10% of income

Formula:

Affordability Score = 100 × (10 − X) / 9

where X is electricity expenditure as a percentage of income.

Example:

Electricity burden = 4%

Affordability Score

= 100 × (10 − 4) / 9

= 66.7

Higher scores indicate more affordable energy.

---

### Reliability

Measured using average electricity supply hours per day.

Formula:

Reliability Score = (Supply Hours / 24) × 100

Example:

20 hours/day

Reliability Score

= (20 / 24) × 100

= 83.3

---

### Quality

Measured using the number of modern energy services available.

The project assumes five indicators:

* Fan
* Refrigerator
* Television
* Internet
* Computer

Formula:

Quality Score = (Appliances Used / 5) × 100

Example:

3 appliances used

Quality Score

= (3 / 5) × 100

= 60

---

### Cleanliness

Measured using the percentage of households using clean cooking fuels.

Examples include:

* LPG
* PNG
* Electricity

Example:

65% households use clean fuels

Cleanliness Score = 65

---

### Equity

Measured using the rural–urban energy gap.

Formula:

Equity Score = 100 − Gap

Example:

Rural–urban gap = 12%

Equity Score

= 100 − 12

= 88

Higher scores indicate more equitable energy access.

---

## 3. Principal Component Analysis (PCA)

The project uses PCA to derive objective weights for the six dimensions.

### Step 1

Standardize the data:

z = (x − μ) / σ

where:

* x = observed value
* μ = mean
* σ = standard deviation

---

### Step 2

Construct the covariance matrix.

---

### Step 3

Compute the first principal component.

PC₁ = a₁X₁ + a₂X₂ + a₃X₃ + a₄X₄ + a₅X₅ + a₆X₆

where:

* X₁ = Availability
* X₂ = Affordability
* X₃ = Reliability
* X₄ = Quality
* X₅ = Cleanliness
* X₆ = Equity

---

### Step 4

Convert PCA loadings into weights.

Weightᵢ = |Loadingᵢ| / Σ|Loading|

The resulting weights sum to 1.

Indicators contributing more to the variation across districts receive larger weights.

---

## 4. Energy Dignity Index Calculation

The final EDI score is calculated using a weighted sum.

EDI

= Availability × Weight₁

* Affordability × Weight₂
* Reliability × Weight₃
* Quality × Weight₄
* Cleanliness × Weight₅
* Equity × Weight₆

The final EDI score ranges from 0 to 100.

Higher scores indicate greater energy dignity.

---

## 5. Interpretation of EDI

| EDI Score | Interpretation            |
| --------- | ------------------------- |
| 85–100    | Very High Energy Dignity  |
| 70–84.99  | High Energy Dignity       |
| 55–69.99  | Moderate Energy Dignity   |
| 40–54.99  | Low Energy Dignity        |
| Below 40  | Severe Energy Deprivation |

---

## 6. Diagnostic Output

In addition to the overall EDI score, the program identifies the weakest dimensions.

Example:

EDI: 78.4 (High Energy Dignity)

Weakest Areas:

• Cleanliness (42.0)

• Quality (60.0)

This helps policymakers identify priority areas requiring intervention rather than relying solely on a single aggregate score.

---

## Features

* Uses PCA-derived weights.
* Accepts both sample and custom data.
* Converts raw indicators into standardized 0–100 scores.
* Generates an Energy Dignity Index (EDI).
* Classifies EDI into interpretable categories.
* Highlights the weakest dimensions of energy dignity.

---

## Installation

Install dependencies using:

pip install -r requirements.txt

Run the application:

python3 main.py

---

## Future Improvements

* Integration with official Indian government datasets.
* District-level visualization dashboards.
* Population-weighted state and national EDI.
* Interactive maps of India.
* Export results to CSV and PDF reports.
