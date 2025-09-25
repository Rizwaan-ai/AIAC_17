import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

def preprocess_iot_sensor_data(input_csv, output_csv=None):
    # Read the IoT sensor data
    df = pd.read_csv(input_csv)
    # Handle missing values using forward fill
    df = df.fillna(method='ffill')
    # Remove sensor drift using rolling mean (window=5, can be adjusted)
    for col in ['temperature', 'humidity']:
        if col in df.columns:
            df[col + '_detrended'] = df[col] - df[col].rolling(window=5, min_periods=1, center=True).mean()
    # Normalize readings using standard scaling (on detrended columns)
    scaler = StandardScaler()
    for col in ['temperature_detrended', 'humidity_detrended']:
        if col in df.columns:
            df[col + '_scaled'] = scaler.fit_transform(df[[col]])
    # Encode categorical sensor IDs
    if 'sensor_id' in df.columns:
        le = LabelEncoder()
        df['sensor_id_encoded'] = le.fit_transform(df['sensor_id'])
    # Select relevant columns for anomaly detection
    output_cols = []
    if 'timestamp' in df.columns:
        output_cols.append('timestamp')
    if 'sensor_id_encoded' in df.columns:
        output_cols.append('sensor_id_encoded')
    for col in ['temperature_scaled', 'humidity_scaled']:
        if col in df.columns:
            output_cols.append(col)
    structured_df = df[output_cols]
    print(structured_df.head())
    if output_csv:
        structured_df.to_csv(output_csv, index=False)
    return structured_df

if __name__ == "__main__":
    preprocess_iot_sensor_data('iot_sensor.csv', 'iot_sensor_preprocessed.csv')
