import pandas as pd
import sqlite3

df = pd.read_csv("../data/raw_sales.csv")

# Feature engineering
df["total_amount"] = df["price"] * df["quantity"]

# Create dimension tables
dim_product = df[["product_id", "product_name", "category"]].drop_duplicates()
dim_customer = df[["customer_id", "customer_name", "region"]].drop_duplicates()

# Fact table
fact_sales = df[["order_id", "product_id", "customer_id", "quantity", "total_amount"]]

# Load to DB
conn = sqlite3.connect("../db/ecommerce.db")

dim_product.to_sql("dim_product", conn, if_exists="replace", index=False)
dim_customer.to_sql("dim_customer", conn, if_exists="replace", index=False)
fact_sales.to_sql("fact_sales", conn, if_exists="replace", index=False)

conn.close()

print("ETL Completed")
