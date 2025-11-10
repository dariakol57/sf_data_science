# Hotel Reviews EDA & Feature Engineering
## Project Overview

This repository contains an [exploratory data analysis (EDA)](https://github.com/dariakol57/sf_data_science/blob/main/Project_3/EDA_hotels.ipynb) and feature engineering project on hotel reviews. The goal is to preprocess hotel review data, extract meaningful features from text and categorical columns, and prepare the dataset for machine learning models (Random Forest Regressor).

## Key objectives include:

- Cleaning and encoding categorical features (hotel names, reviewer nationality, tags, etc.)

- Extracting numerical features from text (e.g., sentiment scores from reviews)

- Handling missing values and outliers

- Feature engineering for improved model performance

- Preparing train/test splits for predictive modeling

## Dataset

The dataset contains information about hotel reviews, including:

- reviewer_score: numerical rating given by the reviewer

- reviewer_nationality: nationality of the reviewer

- hotel_name and hotel_address

- tags: list of tags describing the stay (e.g., "Leisure trip", "Stayed 2 nights")

- positive_review and negative_review texts

- days_since_review and year

- additional_number_of_scoring, average_score, total_number_of_reviews, and other numerical features

**The dataset was cleaned, encoded, and enriched with derived features such as:**

- Sentiment scores from review texts (positive_score, negative_score)

- Extracted information from tags: nights, trip type, traveler type, pet, room_type, room_description, view

- Latitude and longitude of reviewer nationality with missing value handling

## Project Structure

├── notebooks/

│   └── hotel_reviews_EDA.ipynb   # Main Jupyter notebook with full EDA and feature engineering

├── data/

│   ├── raw/                      # Original dataset

│   └── processed/                # Cleaned and feature-engineered dataset

├── scripts/

│   └── feature_engineering.py    # Feature engineering functions

├── output/

│   └── submission_pred.csv       # Sample model predictions

├── README.md                     # This file

└── requirements.txt              # Required Python packages

## EDA & Feature Engineering

The notebook contains:

1) Data Cleaning:

+ Removing duplicates and irrelevant columns

+ Parsing tags and reviews

+ Handling missing geographical coordinates

2) Feature Extraction:

+ Sentiment analysis using NLTK VADER for positive_review and negative_review

+ Extracting nights stayed, trip type, traveler type, pet, room info, view, etc. from tags

+ Creating binary and ordinal features for categorical columns

3) Geolocation Processing:

+ Filling missing reviewer nationality coordinates from a predefined dictionary or geocoding

+ Creating flags for missing coordinates

4) Outlier Handling & Scaling:

- Identifying numerical outliers using Tukey’s method

- Optional scaling or normalization for numerical features

5) Exploratory Analysis:

- Correlation heatmaps

- Distribution plots of numeric features

- Checking outliers and missing value distributions

## Modeling

Random Forest Regressor is used for predicting reviewer_score.

Performance metrics include:

- Mean Absolute Percentage Error (MAPE)

- Mean Absolute Error (MAE)

- Root Mean Squared Error (RMSE)

- R² score

## Observations:

Missing coordinates replaced with median can introduce noise; added missing flag to mitigate this

Interaction features and log transformations may improve model performance

Some less informative features were dropped to reduce noise

## Usage

Clone the repository:

git clone https://github.com/yourusername/hotel-reviews-eda.git
cd hotel-reviews-eda


Install dependencies:

pip install -r requirements.txt


Open the notebook notebooks/hotel_reviews_EDA.ipynb and run all cells to reproduce the analysis.

### Requirements

Python 3.8+

pandas

numpy

matplotlib

seaborn

scikit-learn

nltk

category_encoders

geopy

collections (Counter)

### Notes

Random Forests do not handle NaNs directly. Missing numeric values are filled with median, with missing flags to retain information.

Reviewer nationality geolocation may contain approximations; missing or ambiguous entries are flagged.

Feature engineering from tags is customized to extract meaningful stay information (trip type, nights, room type, pets, etc.).

### License

This project is licensed under the MIT License – see the LICENSE
 file for details.

### Additional Materials:
The initial dataset can be downloaded [here](https://www.kaggle.com/competitions/sf-booking/data)

