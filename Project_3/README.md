# Exploratory data analysis. Preparing data for model training.

One of the company's problems is dishonest hotels that inflate their ratings. One way to detect such hotels is to build a model that predicts the hotel's rating. If the model's predictions differ significantly from the actual results, the hotel may be acting dishonestly and should be investigated.

# Model building stages:

1. Data cleaning.
2. Data exploration (visualization quality, presence of ideas, hypotheses, and comments).
3. Feature generation.
4. Feature selection.
5. Feature transformation.
6. Solution quality assessment: MAPE metric result.

# Additional Materials:
The initial dataset can be downloaded [here](https://www.kaggle.com/competitions/sf-booking/data)

The initial version of the dataset contains 17 fields with the following information:
- hotel_address — hotel address;
- review_date — date the reviewer posted the review;
- average_score — average hotel score, calculated based on the latest comment over the past year;
- hotel_name — hotel name;
- reviewer_nationality — reviewer's country;
- negative_review — negative review the reviewer gave the hotel;
- review_total_negative_word_counts — total number of words in a negative review;
- positive_review — positive review the reviewer gave the hotel;
- review_total_positive_word_counts — total number of words in a positive review.
- reviewer_score — the rating the reviewer gave the hotel based on their experience;
- total_number_of_reviews_reviewer_has_given — the number of reviews reviewers have given in the past;
- total_number_of_reviews — the total number of valid reviews for the hotel;
- tags — the tags the reviewer gave the hotel;
- days_since_review — the number of days between the inspection date and the cleaning date;
- additional_number_of_scoring — some guests simply rated the service but did not leave a review. This number indicates how many valid ratings there are without verification.
- lat — the hotel's latitude;
- lng — the hotel's longitude.
