# E-Commerce Sales Data Analysis

## Project Overview

This project analyzes e-commerce sales data for the year 2025 to identify sales trends, profitable categories, regional performance, and top-selling products.

The project demonstrates an end-to-end data analytics workflow using Python, SQL, Excel, and Power BI.

## Tools & Technologies

- Python
- Pandas
- Matplotlib
- Excel
- SQLite / SQL
- Power BI
- Git & GitHub

## Dataset

The dataset contains 1,000 e-commerce orders with information about:

- Order ID
- Order Date
- Category
- Product
- Region
- Customer Segment
- Quantity
- Unit Price
- Sales
- Profit

## Key Performance Indicators

| Metric | Value |
|---|---:|
| Total Sales | $1,146,151.14 |
| Total Profit | $198,720.36 |
| Total Orders | 1,000 |
| Total Quantity | 4,517 |
| Average Order Value | $1,146.15 |

## Key Insights

- Furniture generated the highest sales among all categories.
- South region recorded the highest sales.
- Wallet was the top-selling product by sales.
- July recorded the highest monthly sales.
- The business generated approximately $198.7K in total profit.

## Analysis Performed

### Python Analysis
Used Pandas for data cleaning, aggregation, and analysis.

Used Matplotlib to create:
- Category sales chart
- Regional sales chart
- Monthly sales trend

### SQL Analysis
Used SQLite to analyze:
- Total sales
- Sales by category
- Sales by region
- Top 10 products
- Monthly sales
- Overall profit, quantity, orders, and average order value

### Power BI Dashboard

Created an interactive Power BI dashboard containing:

- Total Sales KPI
- Total Profit KPI
- Total Orders KPI
- Total Quantity KPI
- Average Order Value KPI
- Sales by Category
- Sales by Region
- Monthly Sales Trend
- Top Products

## Project Structure

```text
Ecommerce_Data_Analysis/
│
├── data/
│   ├── sales_data.csv
│   └── sales_data.xlsx
│
├── output/
│   ├── category_sales.png
│   ├── Ecommerce_Sales_Report.xlsx
│   ├── monthly_sales.png
│   └── region_sales.png
│
├── create_data.py
├── sales_analysis.py
├── create_charts.py
├── create_report.py
├── Ecommerce_Sales_Dashboard.pbix
├── E-commerce_Sales.db
└── README.md
Conclusion

This project demonstrates practical data analyst skills including data preparation, exploratory analysis, SQL querying, data visualization, dashboard development, and GitHub project management.
