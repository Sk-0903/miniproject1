import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


# Set random seed for reproducibility
np.random.seed(42)


# Generate synthetic sales data
dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
n_days = len(dates)


# Create dataset
data = {
    'Date': dates,
    'Product_A': np.random.randint(20, 100, n_days),
    'Product_B': np.random.randint(15, 80, n_days),
    'Product_C': np.random.randint(5, 50, n_days),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], n_days),
    'Discount': np.random.choice([0, 5, 10, 15, 20], n_days, p=[0.6, 0.2, 0.1, 0.05, 0.05])
}


df = pd.DataFrame(data)


# Calculate total sales and revenue
df['Total_Units'] = df['Product_A'] + df['Product_B'] + df['Product_C']
df['Revenue'] = (df['Product_A'] * 50 + df['Product_B'] * 75 + df['Product_C'] * 100) * (1 - df['Discount']/100)


# Extract time features
df['Month'] = df['Date'].dt.month
df['DayOfWeek'] = df['Date'].dt.dayofweek
df['Quarter'] = df['Date'].dt.quarter


print("="*60)
print("SALES DATA ANALYSIS DASHBOARD")
print("="*60)
print(f"Dataset Shape: {df.shape}")
print(f"Date Range: {df['Date'].min().date()} to {df['Date'].max().date()}")
print(f"Total Revenue: ${df['Revenue'].sum():,.2f}")
print(f"Total Units Sold: {df['Total_Units'].sum():,}")
print("="*60)
