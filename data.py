import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler


data = {
    'hours_of_study': [2.5, 5.1, 3.2, 8.5, 3.5, 1.5, 9.2, 5.5, 8.3, 2.7, 7.7, 5.9, 4.5, 3.3, 1.1, 8.9, 2.5, 1.9, 6.1, 7.4, 2.7, 4.8, 3.8, 6.9, 7.8],
    'Scores': [21, 47, 27, 75, 30, 20, 88, 60, 81, 25, 85, 62, 41, 42, 17, 95, 30, 24, 67, 69, 30, 54, 35, 76, 8.6]
}

df = pd.DataFrame(data)

scaler = MinMaxScaler()
normalized_minmax = scaler.fit_transform(df)
df_normalized_minmax = pd.DataFrame(normalized_minmax, columns=df.columns)

scaler = StandardScaler()
normalized_zscore = scaler.fit_transform(df)
df_normalized_zscore = pd.DataFrame(normalized_zscore, columns=df.columns)

normalized_standard = (df - df.mean()) / df.std()

print("Hasil Min-Max Scaling:")
print(df_normalized_minmax)

print("\nHasil Z-score (Standardization):")
print(df_normalized_zscore)

print("\nHasil Standar Normal Baku:")
print(normalized_standard)
