import pandas as pd
import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer

def clean_review_text(text):
    """Lowercase and remove HTML tags from review text."""
    if pd.isnull(text):
        return ""
    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)
    # Lowercase
    return text.lower()

def preprocess_movie_reviews(input_csv='movie_reviews-1.csv', output_csv=None):
    # Load data
    df = pd.read_csv(input_csv)
    before_summary = {
        "num_rows": len(df),
        "num_missing_ratings": df['rating'].isnull().sum(),
        "rating_min": df['rating'].min(),
        "rating_max": df['rating'].max(),
        "sample_reviews": df['review_text'].head(3).tolist()
    }

    # Clean review text
    df['review_text_clean'] = df['review_text'].apply(clean_review_text)

    # Handle missing ratings: fill with median
    median_rating = df['rating'].median()
    df['rating_filled'] = df['rating'].fillna(median_rating)

    # Normalize ratings to 0-1
    df['rating_normalized'] = df['rating_filled'] / 10.0

    # TF-IDF encoding
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(df['review_text_clean'])
    tfidf_feature_names = tfidf.get_feature_names_out()
    tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=[f"tfidf_{w}" for w in tfidf_feature_names])

    # Concatenate TF-IDF features with main DataFrame
    df_final = pd.concat([df.reset_index(drop=True), tfidf_df.reset_index(drop=True)], axis=1)

    after_summary = {
        "num_rows": len(df_final),
        "num_missing_ratings": df_final['rating_filled'].isnull().sum(),
        "rating_min": df_final['rating_normalized'].min(),
        "rating_max": df_final['rating_normalized'].max(),
        "sample_clean_reviews": df_final['review_text_clean'].head(3).tolist(),
        "tfidf_feature_count": tfidf_df.shape[1]
    }

    print("=== BEFORE CLEANING ===")
    for k, v in before_summary.items():
        print(f"{k}: {v}")
    print("\n=== AFTER CLEANING ===")
    for k, v in after_summary.items():
        print(f"{k}: {v}")

    # Save cleaned dataset if requested
    if output_csv:
        df_final.to_csv(output_csv, index=False)
    return df_final

# Example usage and test cases
if __name__ == "__main__":
    # Run preprocessing
    cleaned_df = preprocess_movie_reviews('movie_reviews-1.csv', 'movie_reviews_cleaned.csv')

    # --- Test Cases ---
    # 1. Check that all review_text_clean are lowercase and have no HTML tags
    assert all('<' not in txt and txt == txt.lower() for txt in cleaned_df['review_text_clean']), "Text cleaning failed"

    # 2. Check that there are no missing values in rating_filled
    assert cleaned_df['rating_filled'].isnull().sum() == 0, "Missing ratings not filled"

    # 3. Check that all normalized ratings are between 0 and 1
    assert cleaned_df['rating_normalized'].between(0, 1).all(), "Ratings not normalized to 0-1"

    print("\nAll test cases passed.")


