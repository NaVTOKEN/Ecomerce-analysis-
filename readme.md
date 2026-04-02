
# Scalable E-Commerce ETL Pipeline 🚀

## Overview
Production-style data engineering pipeline simulating an e-commerce analytics system.  
Implements batch ETL, dimensional data modeling, and analytical queries.

---

## Tech Stack
- Python (Pandas)
- SQL (SQLite / PostgreSQL ready)
- Apache Airflow (Orchestration)
- Data Modeling (Star Schema)

---

## Architecture
```
Raw Data → Staging → Transformation → Data Warehouse (Star Schema) → Analytics
```

---

## Data Model (Star Schema)

### Fact Table
- `fact_sales`
  - order_id
  - product_id
  - customer_id
  - date_id
  - quantity
  - total_amount

### Dimension Tables
- `dim_product`
- `dim_customer`
- `dim_date`
- `dim_region`
