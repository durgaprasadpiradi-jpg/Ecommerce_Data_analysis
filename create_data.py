import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

products = {
    "Electronics": ["Laptop", "Headphones", "Keyboard", "Mouse", "Monitor"],
    "Furniture": ["Chair", "Desk", "Bookshelf", "Table", "Sofa"],
    "Office Supplies": ["Notebook", "Pen", "Printer Paper", "Stapler", "File Folder"],
    "Accessories": ["Backpack", "Water Bottle", "USB Cable", "Phone Stand", "Wallet"]
}

regions = ["North", "South", "East", "West"]
segments = ["Consumer", "Corporate", "Small Business"]

data = []

start_date = datetime(2025, 1, 1)

for order_id in range(1, 1001):

    category = random.choice(list(products.keys()))
    product = random.choice(products[category])
    region = random.choice(regions)
    segment = random.choice(segments)

    order_date = start_date + timedelta(days=random.randint(0, 364))

    quantity = random.randint(1, 8)
    unit_price = round(random.uniform(10, 500), 2)

    sales = round(quantity * unit_price, 2)
    profit = round(sales * random.uniform(0.05, 0.30), 2)

    data.append([
        order_id,
        order_date,
        category,
        product,
        region,
        segment,
        quantity,
        unit_price,
        sales,
        profit
    ])

df = pd.DataFrame(data, columns=[
    "Order_ID",
    "Order_Date",
    "Category",
    "Product",
    "Region",
    "Customer_Segment",
    "Quantity",
    "Unit_Price",
    "Sales",
    "Profit"
])

df.to_excel("data/sales_data.xlsx", index=False)

print("Dataset created successfully!")
print("Rows:", len(df))
print("File: data/sales_data.xlsx")