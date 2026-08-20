import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales_data.csv")

# Convert Order_Date into date format
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

print("Dataset loaded successfully!")
print(df.head())

# ==========================================
# 1. MONTHLY SALES TREND
# ==========================================

df["Month_Number"] = df["Order_Date"].dt.month
df["Month"] = df["Order_Date"].dt.strftime("%B")

monthly_sales = (
    df.groupby(["Month_Number", "Month"])["Sales"]
    .sum()
    .sort_index()
)

months = monthly_sales.index.get_level_values("Month")
sales_values = monthly_sales.values

plt.figure(figsize=(10, 5))

plt.plot(
    months,
    sales_values,
    marker="o",
    linewidth=2
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Save the graph
plt.savefig("monthly_sales.png", dpi=300)

# Display the graph
plt.show()


# ==========================================
# 2. CATEGORY-WISE SALES
# ==========================================

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))

plt.bar(
    category_sales.index,
    category_sales.values
)

plt.title("Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.xticks(rotation=20)
plt.tight_layout()

# Save the graph
plt.savefig("category_sales.png", dpi=300)

# Display the graph
plt.show()

# ==========================================
# 3. REGION-WISE SALES
# ==========================================

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))

plt.bar(
    region_sales.index,
    region_sales.values
)

plt.title("Region-wise Sales")
plt.xlabel("Region")
plt.ylabel("Total Sales")

plt.tight_layout()

# Save the graph
plt.savefig("region_sales.png", dpi=300)

# Display the graph
plt.show()

# ==========================================
# 4. TOP 10 PRODUCTS BY SALES
# ==========================================

product_sales = (
    df.groupby("Product")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))

plt.barh(
    product_sales.index[::-1],
    product_sales.values[::-1]
)

plt.title("Top 10 Products by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Product")

plt.tight_layout()

# Save the graph
plt.savefig("top_products_sales.png", dpi=300)

# Display the graph
plt.show()

# ==========================================
# 5. PROFIT BY CATEGORY
# ==========================================

category_profit = (
    df.groupby("Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))

plt.bar(
    category_profit.index,
    category_profit.values
)

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Total Profit")

plt.xticks(rotation=20)
plt.tight_layout()

# Save the graph
plt.savefig("profit_by_category.png", dpi=300)

# Display the graph
plt.show()

# ==========================================
# 6. SALES VS PROFIT ANALYSIS
# ==========================================

plt.figure(figsize=(9, 5))

plt.scatter(
    df["Sales"],
    df["Profit"]
)

plt.title("Sales vs Profit Analysis")
plt.xlabel("Sales")
plt.ylabel("Profit")

plt.tight_layout()

# Save the graph
plt.savefig("sales_vs_profit.png", dpi=300)

# Display the graph
plt.show()

# ==========================================
# 7. MONTHLY SALES VS PROFIT
# ==========================================

monthly_analysis = (
    df.groupby(df["Order_Date"].dt.month)[["Sales", "Profit"]]
    .sum()
)

monthly_analysis.index = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

plt.figure(figsize=(10, 5))

plt.plot(
    monthly_analysis.index,
    monthly_analysis["Sales"],
    marker="o",
    label="Sales"
)

plt.plot(
    monthly_analysis.index,
    monthly_analysis["Profit"],
    marker="o",
    label="Profit"
)

plt.title("Monthly Sales vs Profit")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.legend()

plt.xticks(rotation=45)
plt.tight_layout()

# Save the graph
plt.savefig("monthly_sales_vs_profit.png", dpi=300)

# Display the graph
plt.show()

# ============================================================
# DATA STORY / KEY INSIGHTS
# ============================================================

print("\n" + "=" * 50)
print("KEY BUSINESS INSIGHTS")
print("=" * 50)

# 1. Best selling category
category_sales = df.groupby("Category")["Sales"].sum()
best_category = category_sales.idxmax()
best_category_sales = category_sales.max()

print("\n1. BEST CATEGORY:")
print(f"{best_category} generated the highest sales of {best_category_sales:,.0f}.")

# 2. Best performing region
region_sales = df.groupby("Region")["Sales"].sum()
best_region = region_sales.idxmax()
best_region_sales = region_sales.max()

print("\n2. BEST REGION:")
print(f"{best_region} generated the highest sales of {best_region_sales:,.0f}.")

# 3. Best selling product
product_sales = df.groupby("Product")["Sales"].sum()
best_product = product_sales.idxmax()
best_product_sales = product_sales.max()

print("\n3. TOP PRODUCT:")
print(f"{best_product} generated the highest sales of {best_product_sales:,.0f}.")

# 4. Highest sales month
monthly_sales = df.groupby("Month_Number")["Sales"].sum()
highest_month_number = monthly_sales.idxmax()
highest_month_sales = monthly_sales.max()

month_names = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

highest_month = month_names[highest_month_number]

print("\n4. BEST SALES MONTH:")
print(f"{highest_month} had the highest sales of {highest_month_sales:,.0f}.")

# 5. Total sales and profit
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

print("\n5. OVERALL PERFORMANCE:")
print(f"Total Sales  : {total_sales:,.0f}")
print(f"Total Profit : {total_profit:,.0f}")

# 6. Profit margin
profit_margin = (total_profit / total_sales) * 100

print(f"Profit Margin: {profit_margin:.2f}%")

print("\n" + "=" * 50)
print("DATA VISUALIZATION ANALYSIS COMPLETED")
print("=" * 50)