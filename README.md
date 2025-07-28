# 🍕 Dominos - Predictive Purchase Order System

## 🧠 Objective
To build a predictive system that forecasts future pizza sales and automatically generates a purchase order for ingredients. This project is designed to help Dominos optimize inventory, reduce waste, and streamline its supply chain.

---

## 🏢 Domain
Food Service Industry

---

## 🚀 Skills You Will Learn
- Data Cleaning and Preprocessing  
- Exploratory Data Analysis (EDA)  
- Time Series Forecasting  
- Predictive Modeling  
- Business Decision Making  
- Real-world Data Science Application  

---

## 📌 Problem Statement
Dominos wants to improve its ordering system by predicting future pizza sales and generating a corresponding ingredient purchase order. This system should minimize waste, prevent stockouts, and ensure ingredient availability by leveraging historical sales data and recipe information.

---

## 💼 Business Use Cases
- **Inventory Management**: Maintain optimal stock levels based on demand forecasts.
- **Cost Reduction**: Lower expenses due to overstocking and spoilage.
- **Sales Forecasting**: Inform promotional and staffing decisions.
- **Supply Chain Optimization**: Reduce delays and improve procurement efficiency.

---

## 🔧 Approach

### 🔹 1. Data Preprocessing and Exploration
- Handle missing data, remove inconsistencies, format columns.
- Perform outlier detection and correction.
- Visualize data trends, seasonality, and anomalies.

### 🔹 2. Sales Prediction
- Feature Engineering: Add date-based features (month, day, weekday), holidays, promotions, etc.
- Model Selection: Choose suitable forecasting models (e.g., ARIMA, SARIMA, Prophet, LSTM, Regression).
- Model Evaluation: Use **Mean Absolute Percentage Error (MAPE)** to assess accuracy.

### 🔹 3. Purchase Order Generation
- Forecast pizza sales for the next week.
- Multiply forecasted sales by ingredient quantities per pizza type.
- Create a clean, structured purchase order for the procurement team.

---

## 📊 Datasets Used

### 📁 Sales Data
- Fields: Date, Pizza Type, Quantity Sold, Price, Category, Ingredients

### 📁 Ingredient Data
- Fields: Pizza Type, Ingredient, Quantity Needed

> Dataset Links:  
> 🔗 Sales Dataset [Your Link]  
> 🔗 Ingredient Dataset [Your Link]

---

## 🛠️ Tools & Technologies
- Python (Pandas, NumPy, Scikit-learn, Statsmodels)
- Matplotlib / Seaborn
- Forecasting Libraries: ARIMA, Prophet, LSTM (optional)
- Jupyter Notebook
- Git & GitHub

---

## 📈 Results

- Accurate forecasting of pizza sales using SARIMA and Prophet models with MAPE < 10%.
- Sales trend visualizations revealed weekly and monthly demand cycles.
- A dynamic purchase order generated based on forecasted sales and recipe mappings.
- Reduced manual effort and enhanced reliability of the procurement process.

---

## 🔍 Conclusion

The **Dominos Predictive Purchase Order System** demonstrates how historical data and predictive modeling can optimize business operations. By forecasting demand and automating purchase order generation, Dominos can ensure ingredient availability while reducing excess inventory. The modular structure allows integration with real-time systems and future scalability.

---

## 🚧 Future Improvements

- **Real-Time Forecasting**: Integrate APIs for live sales tracking and rolling forecasts.
- **Model Ensemble**: Combine multiple models for improved prediction accuracy.
- **Inventory Reconciliation**: Add actual stock levels for smart order adjustments.
- **Vendor Integration**: Link purchase order output directly to supplier systems.
- **Mobile Dashboard**: Create a lightweight UI for store managers to review forecasts and orders.
- **Holiday/Promotion Adjustment**: Dynamically adjust forecasts based on calendar events or campaigns.

---

## 📂 Project Deliverables

- ✅ Cleaned & processed datasets  
- ✅ EDA report with visual insights  
- ✅ Trained forecasting model with performance metrics  
- ✅ Automated ingredient-level purchase order  
- ✅ GitHub repository with source code  
- ✅ Project report with methodology & business impact  

---
