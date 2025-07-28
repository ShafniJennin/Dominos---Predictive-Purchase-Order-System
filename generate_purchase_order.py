import pandas as pd

# Load forecast and ingredient data
forecast = pd.read_csv("data/weekly_forecast.csv")
ingredients = pd.read_csv("data/ingredient_data.csv")
sales = pd.read_csv("data/cleaned_sales_data.csv")

# Average pizza proportions (simple estimate by frequency)
pizza_dist = sales['Pizza'].value_counts(normalize=True)

# Estimate total pizzas by type
total_forecast = forecast['yhat'].sum()
pizza_estimates = (pizza_dist * total_forecast).round().astype(int)

# Calculate total ingredients needed
purchase_order = {}

for pizza, qty in pizza_estimates.items():
    pizza_ingredients = ingredients[ingredients['Pizza'] == pizza]
    for _, row in pizza_ingredients.iterrows():
        ingredient = row['Ingredient']
        required_qty = row['Quantity'] * qty
        purchase_order[ingredient] = purchase_order.get(ingredient, 0) + required_qty

# Convert to DataFrame
order_df = pd.DataFrame(purchase_order.items(), columns=['Ingredient', 'Quantity Needed'])
order_df.to_csv("data/final_purchase_order.csv", index=False)

print("✅ Purchase order generated successfully.")
