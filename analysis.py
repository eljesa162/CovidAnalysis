import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("covid_data.csv")

# Inspect data
print("First 5 rows:")
print(data.head())
print("\nData info:")
print(data.info())
print("\nSummary statistics:")
print(data.describe())

# Clean data (remove missing values)
data = data.dropna()

# Filter data for a single country
country_data = data[data['Country'] == 'Germany']

# Plot daily confirmed cases
plt.figure(figsize=(12,6))
sns.lineplot(x='Date', y='Confirmed', data=country_data)
plt.title("Daily Confirmed COVID-19 Cases in Germany")
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
