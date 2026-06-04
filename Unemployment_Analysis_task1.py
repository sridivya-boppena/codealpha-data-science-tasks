import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("Unemployment_Rate_upto_11_2020.csv")

# Clean columns
df.columns = df.columns.str.strip()

# Convert Date
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# -------------------------------
# PRINT OUTPUT (IMPORTANT)
# -------------------------------
print("First 5 Rows:\n")
print(df.head())

print("\nDataset Info:\n")
print(df.info())

print("\nSummary Statistics:\n")
print(df.describe())

# -------------------------------
# GRAPH 1
# -------------------------------
df_date = df.groupby('Date')['Estimated Unemployment Rate (%)'].mean().reset_index()

plt.figure(figsize=(10,5))
plt.plot(df_date['Date'], df_date['Estimated Unemployment Rate (%)'], marker='o')

plt.title("Average Unemployment Rate Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -------------------------------
# GRAPH 2
# -------------------------------
plt.figure(figsize=(10,5))
sns.barplot(x='Region', y='Estimated Unemployment Rate (%)', data=df)

plt.title("Unemployment Rate by Region")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()