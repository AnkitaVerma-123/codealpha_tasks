import pandas as pd
import numpy as np

# ==========================================
# 1. LOAD DATASET
# ==========================================

df = pd.read_csv("sales_data.csv")

print("=" * 60)
print("EXPLORATORY DATA ANALYSIS (EDA)")
print("=" * 60)


# ==========================================
# 2. MEANINGFUL QUESTIONS
# ==========================================

print("\n1. MEANINGFUL QUESTIONS")
print("-" * 40)

print("Q1. Which category has the highest sales?")
print("Q2. Which region generates the highest sales?")
print("Q3. Which product has the highest sales?")
print("Q4. Which month has the highest and lowest sales?")
print("Q5. Is there any unusual or abnormal sales value?")
print("Q6. Is there any missing or duplicate data?")
print("Q7. Is quantity related to sales?")


# ==========================================
# 3. DATA STRUCTURE
# ==========================================

print("\n2. DATA STRUCTURE")
print("-" * 40)

print("Number of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Rows:")
print(df.head())


# ==========================================
# 4. DATASET INFORMATION
# ==========================================

print("\n3. DATASET INFORMATION")
print("-" * 40)

df.info()


# ==========================================
# 5. DESCRIPTIVE STATISTICS
# ==========================================

print("\n4. DESCRIPTIVE STATISTICS")
print("-" * 40)

print(df.describe())


# ==========================================
# 6. MISSING VALUES
# ==========================================

print("\n5. MISSING VALUES")
print("-" * 40)

missing_values = df.isnull().sum()

print(missing_values)

if missing_values.sum() == 0:
    print("RESULT: No missing values found.")
else:
    print("RESULT: Missing values are present.")


# ==========================================
# 7. DUPLICATE RECORDS
# ==========================================

print("\n6. DUPLICATE RECORDS")
print("-" * 40)

duplicate_count = df.duplicated().sum()

print("Duplicate Rows:", duplicate_count)

if duplicate_count == 0:
    print("RESULT: No duplicate records found.")
else:
    print("RESULT: Duplicate records found.")


# ==========================================
# 8. CHECK INVALID VALUES
# ==========================================

print("\n7. DATA VALIDATION")
print("-" * 40)

print("Negative Quantity:", (df["Quantity"] < 0).sum())
print("Negative Sales:", (df["Sales"] < 0).sum())
print("Negative Profit:", (df["Profit"] < 0).sum())

if (
    (df["Quantity"] < 0).sum() == 0
    and (df["Sales"] < 0).sum() == 0
    and (df["Profit"] < 0).sum() == 0
):
    print("RESULT: No negative/invalid numeric values found.")
else:
    print("RESULT: Invalid numeric values found.")


# ==========================================
# 9. CATEGORY ANALYSIS
# ==========================================

print("\n8. SALES BY CATEGORY")
print("-" * 40)

category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

print(category_sales)

print("\nHighest Sales Category:")
print(category_sales.idxmax(), "=", category_sales.max())


# ==========================================
# 10. REGION ANALYSIS
# ==========================================

print("\n9. SALES BY REGION")
print("-" * 40)

region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

print(region_sales)

print("\nHighest Sales Region:")
print(region_sales.idxmax(), "=", region_sales.max())


# ==========================================
# 11. PRODUCT ANALYSIS
# ==========================================

print("\n10. TOP PRODUCTS")
print("-" * 40)

product_sales = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)

print(product_sales)

print("\nBest Selling Product:")
print(product_sales.idxmax(), "=", product_sales.max())


# ==========================================
# 12. MONTHLY SALES
# ==========================================

print("\n11. MONTHLY SALES")
print("-" * 40)

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

df["Month_Number"] = df["Order_Date"].dt.month

df["Month"] = df["Order_Date"].dt.strftime("%B")

monthly_sales = (
    df.groupby(["Month_Number", "Month"])["Sales"]
    .sum()
    .sort_index()
)

print(monthly_sales)

highest_month = monthly_sales.idxmax()
lowest_month = monthly_sales.idxmin()

print("\nHighest Sales Month:")
print(highest_month)

print("\nLowest Sales Month:")
print(lowest_month)


# ==========================================
# 13. TREND & PATTERN ANALYSIS
# ==========================================

print("\n12. TRENDS, PATTERNS AND ANOMALIES")
print("-" * 40)

print("Highest Monthly Sales:",
      monthly_sales.max())

print("Lowest Monthly Sales:",
      monthly_sales.min())

print("Average Monthly Sales:",
      round(monthly_sales.mean(), 2))

sales_difference = monthly_sales.max() - monthly_sales.min()

print("Difference between highest and lowest monthly sales:",
      sales_difference)


# ==========================================
# 14. OUTLIER DETECTION USING IQR
# ==========================================

print("\n13. OUTLIER DETECTION")
print("-" * 40)

Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df[
    (df["Sales"] < lower_limit) |
    (df["Sales"] > upper_limit)
]

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)

print("Lower Limit:", lower_limit)
print("Upper Limit:", upper_limit)

print("\nNumber of Sales Outliers:", len(outliers))

if len(outliers) == 0:
    print("RESULT: No major sales outliers detected.")
else:
    print("RESULT: Possible sales outliers:")
    print(outliers[["Order_ID", "Product", "Sales"]])


# ==========================================
# 15. CORRELATION ANALYSIS
# ==========================================

print("\n14. CORRELATION ANALYSIS")
print("-" * 40)

correlation = df["Quantity"].corr(df["Sales"])

print("Correlation between Quantity and Sales:",
      round(correlation, 3))

if correlation > 0:
    print("RESULT: Quantity and Sales have a positive relationship.")
elif correlation < 0:
    print("RESULT: Quantity and Sales have a negative relationship.")
else:
    print("RESULT: No linear relationship detected.")


# ==========================================
# 16. HYPOTHESIS TESTING
# ==========================================

print("\n15. HYPOTHESIS TESTING")
print("-" * 40)

print("Hypothesis:")
print("Higher quantity is associated with higher sales.")

print("\nCorrelation value:", round(correlation, 3))

if correlation > 0:
    print("Observation: Higher quantity generally corresponds to higher sales.")
else:
    print("Observation: Higher quantity does not show a positive relationship with sales.")


# ==========================================
# 17. DATA QUALITY SUMMARY
# ==========================================

print("\n16. DATA QUALITY SUMMARY")
print("-" * 40)

print("Total Rows:", len(df))
print("Total Columns:", len(df.columns))
print("Missing Values:", df.isnull().sum().sum())
print("Duplicate Rows:", df.duplicated().sum())

invalid_values = (
    (df["Quantity"] < 0).sum()
    + (df["Sales"] < 0).sum()
    + (df["Profit"] < 0).sum()
)

print("Invalid Numeric Values:", invalid_values)

if (
    df.isnull().sum().sum() == 0
    and df.duplicated().sum() == 0
    and invalid_values == 0
):
    print("\nFINAL RESULT:")
    print("Dataset quality is good for further analysis.")
else:
    print("\nFINAL RESULT:")
    print("Dataset requires cleaning before further analysis.")


# ==========================================
# 18. FINAL EDA INSIGHTS
# ==========================================

print("\n17. FINAL EDA INSIGHTS")
print("-" * 40)

print("1. Highest performing category:",
      category_sales.idxmax())

print("2. Highest performing region:",
      region_sales.idxmax())

print("3. Best selling product:",
      product_sales.idxmax())

print("4. Highest sales month:",
      highest_month)

print("5. Lowest sales month:",
      lowest_month)

print("6. Quantity-Sales correlation:",
      round(correlation, 3))

print("\nEDA ANALYSIS COMPLETED SUCCESSFULLY!")
print("=" * 60)