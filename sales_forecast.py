from prophet import Prophet
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned sales data
df = pd.read_csv("data/cleaned_sales_data.csv")

# Aggregate daily sales
forecast_data = df.groupby('Date')['Quantity'].sum().reset_index()
forecast_data.columns = ['ds', 'y']

# Initialize and fit model
model = Prophet()
model.fit(forecast_data)

# Predict next 7 days
future = model.make_future_dataframe(periods=7)
forecast = model.predict(future)

# Plot forecast
model.plot(forecast)
plt.title("7-Day Pizza Sales Forecast")
plt.show()

# Save predictions
forecast[['ds', 'yhat']].tail(7).to_csv("data/weekly_forecast.csv", index=False)
