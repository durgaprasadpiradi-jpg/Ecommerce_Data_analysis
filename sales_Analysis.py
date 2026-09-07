import pandas as pd

# Load dataset
df = pd.read_excel("data/sales_data.xlsx")

print("\n========== DATASET OVERVIEW ==========")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n========== FIRST 5 ROWS ==========")
print(df.head())

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# Convert date column
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# KPI calculations
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order_ID"].nunique()
total_quantity = df["Quantity"].sum()
average_order_value = total_sales / total_orders

print("\n========== KEY PERFORMANCE INDICATORS ==========")
print(f"Total Sales       : ${total_sales:,.2f}")
print(f"Total Profit      : ${total_profit:,.2f}")
print(f"Total Orders      : {total_orders}")
print(f"Total Quantity    : {total_quantity}")
print(f"Average Order Value: ${average_order_value:,.2f}")

# Category analysis
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

print("\n========== SALES BY CATEGORY ==========")
print(category_sales)

# Region analysis
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

print("\n========== SALES BY REGION ==========")
print(region_sales)

# Product analysis
product_sales = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)

print("\n========== TOP 10 PRODUCTS ==========")
print(product_sales.head(10))

# Monthly analysis
df["Month"] = df["Order_Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Sales"].sum()

print("\n========== MONTHLY SALES ==========")
print(monthly_sales)

print("\n========== ANALYSIS COMPLETED ==========")