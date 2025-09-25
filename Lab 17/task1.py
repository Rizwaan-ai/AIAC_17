import pandas as pd
import string
import re
# If nltk is available, use it for stopwords; otherwise, define a basic set
try:
    from nltk.corpus import stopwords
    STOPWORDS = set(stopwords.words('english'))
except:
    STOPWORDS = set([
        'the', 'and', 'is', 'in', 'to', 'of', 'a', 'for', 'on', 'with', 'at', 'by', 'an', 'be', 'this', 'that', 'it', 'from', 'as', 'are', 'was', 'were', 'or', 'but', 'not'
    ])
def clean_text(text):
    if not isinstance(text, str):
        return ""
    # Remove punctuation and special symbols
    text = re.sub(r'[^\w\s]', '', text)
    # Lowercase
    text = text.lower()
    # Remove stopwords
    tokens = text.split()
    tokens = [word for word in tokens if word not in STOPWORDS]
    return ' '.join(tokens)
def clean_social_media_data(df):
    # Remove spam/duplicate posts (exact duplicates in 'post_text')
    df = df.drop_duplicates(subset=['post_text'])
    # Clean post text
    df['clean_text'] = df['post_text'].apply(clean_text)
    # Handle missing values in likes and shares
    for col in ['likes', 'shares']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            df[col] = df[col].fillna(0).astype(int)
    # Convert timestamp to datetime and extract hour, weekday
    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
        df['hour'] = df['timestamp'].dt.hour
        df['weekday'] = df['timestamp'].dt.weekday
    # Optionally, drop rows with invalid timestamps
    df = df.dropna(subset=['timestamp'])
    # Reset index after cleaning
    df = df.reset_index(drop=True)
    return df
# Read the uploaded file
df = pd.read_csv('social_media.csv')
# Clean the data
cleaned_df = clean_social_media_data(df)
# Save the cleaned DataFrame to an Excel file
cleaned_df.to_excel('social_media_cleaned.xlsx', index=False)
print("Excel sheet 'social_media_cleaned.xlsx' has been created with the cleaned data.")
