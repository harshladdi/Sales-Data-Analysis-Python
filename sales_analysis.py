import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Generate synthetic sales data
# -------------------------------
print("Program started")
np.random.seed(42)  # for consistent results

products = ["Laptop", "Mobile", "Tablet"]
regions = ["North", "South", "East", "West"]

num_records = 30

data = {
    "Day": np.arange(1, num_records + 1),
    "Product": np.random.choice(products, num_records),
    "Region": np.random.choice(regions, num_records),
    "Quantity": np.random.randint(1, 10, num_records),
    "Price": np.random.choice([20000, 30000, 50000], num_records)
}

df = pd.DataFrame(data)

# -------------------------------
# Data Analysis
# -------------------------------

# Calculate total sales using NumPy
df["Total_Sales"] = np.multiply(df["Quantity"], df["Price"])

print("\n--- SALES DATA ---")
print(df.head())

# Product-wise total sales
product_sales = df.groupby("Product")["Total_Sales"].sum()

# Region-wise total sales
region_sales = df.groupby("Region")["Total_Sales"].sum()

# Daily sales trend
daily_sales = df.groupby("Day")["Total_Sales"].sum()

# -------------------------------
# Visualization
# -------------------------------

# Bar Chart: Product Sales
plt.figure()
product_sales.plot(kind="bar")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales Amount")
plt.show()

# Pie Chart: Region Sales
plt.figure()
region_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Sales Distribution by Region")
plt.ylabel("")
plt.show()

# Line Chart: Daily Sales Trend
plt.figure()
plt.plot(daily_sales.index, daily_sales.values, marker='o')
plt.title("Daily Sales Trend")
plt.xlabel("Day")
plt.ylabel("Sales Amount")
plt.show()
print("\nProgram finished successfully")
input("Press Enter to exit...")

