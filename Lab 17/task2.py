import pandas as pd
import numpy as np
# Load the financial data
df = pd.read_csv('financial_data.csv')
# Convert 'date' column to datetime and sort
if 'date' in df.columns:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df = df.sort_values('date').reset_index(drop=True)

# Fill missing values in 'closing_price' and 'volume'
for col in ['closing_price', 'volume']:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
        df[col] = df[col].ffill().bfill()
# Generate lag features: 1-day and 7-day returns
if 'closing_price' in df.columns:
    df['return_1d'] = df['closing_price'].pct_change(1)
    df['return_7d'] = df['closing_price'].pct_change(7)
# Log-normalize the 'volume' column
if 'volume' in df.columns:
    df['volume_log'] = np.log1p(df['volume'])
# Outlier detection for 'closing_price' using IQR
if 'closing_price' in df.columns:
    Q1 = df['closing_price'].quantile(0.25)
    Q3 = df['closing_price'].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df['closing_price_outlier'] = (df['closing_price'] < lower) | (df['closing_price'] > upper)
# Display the first few rows of the processed DataFrame
print(df.head())

df.to_csv('financial_data_preprocessed.csv', index=False)
