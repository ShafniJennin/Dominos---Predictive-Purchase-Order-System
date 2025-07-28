import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
sales = pd.read_csv("data/sales_data.csv")
ingredients = pd.read_csv("data/ingredient_data.csv")

# Convert Date to datetime
sales['Date'] = pd.to_datetime(sales['Date'])

# Basic EDA
print(sales.info())
print(sales.describe())
print(sales['Pizza'].value_counts())

# Sales over time
daily_sales = sales.groupby('Date')['Quantity'].sum().reset_index()

plt.figure(figsize=(12,6))
sns.lineplot(data=daily_sales, x='Date', y='Quantity')
plt.title("Daily Pizza Sales")
plt.show()

# Save cleaned dataset
sales.to_csv("data/cleaned_sales_data.csv", index=False)
