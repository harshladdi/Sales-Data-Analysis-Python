import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("Program started")
np.random.seed(42) 

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

df["Total_Sales"] = np.multiply(df["Quantity"], df["Price"])

print("\n--- SALES DATA ---")
print(df.head())

product_sales = df.groupby("Product")["Total_Sales"].sum()

region_sales = df.groupby("Region")["Total_Sales"].sum()

daily_sales = df.groupby("Day")["Total_Sales"].sum()

plt.figure()
product_sales.plot(kind="bar")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales Amount")
plt.show()

plt.figure()
region_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Sales Distribution by Region")
plt.ylabel("")
plt.show()

plt.figure()
plt.plot(daily_sales.index, daily_sales.values, marker='o')
plt.title("Daily Sales Trend")
plt.xlabel("Day")
plt.ylabel("Sales Amount")
plt.show()
print("\nProgram finished successfully")
input("Press Enter to exit...")


