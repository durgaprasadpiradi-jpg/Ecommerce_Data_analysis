import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_excel("data/sales_data.xlsx")

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# -------------------------------
# 1. Sales by Category
# -------------------------------

category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/category_sales.png")
plt.close()

# -------------------------------
# 2. Sales by Region
# -------------------------------

region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales ($)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("output/region_sales.png")
plt.close()

# -------------------------------
# 3. Monthly Sales Trend
# -------------------------------

df["Month"] = df["Order_Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(12, 6))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend - 2025")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("output/monthly_sales.png")
plt.close()

print("All charts created successfully!")
print("Charts saved inside the output folder.")