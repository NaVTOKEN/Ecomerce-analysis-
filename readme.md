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

---

## Key Features
- Modular ETL pipeline (extract, transform, load)
- Star schema implementation
- Data normalization & deduplication
- Feature engineering (revenue metrics)
- SQL analytics layer
- Pipeline orchestration ready (Airflow)

---

## Project Structure
```
.
├── data/
├── etl/
├── warehouse/
├── sql/
├── airflow/
├── db/
├── README.md
├── requirements.txt
```

---

## How to Run
```bash
git clone <repo-url>
cd ecommerce-etl
pip install -r requirements.txt
python etl/main.py
```

---

## Sample Analytics Queries
```sql
-- Revenue by Region
SELECT r.region_name, SUM(f.total_amount) AS revenue
FROM fact_sales f
JOIN dim_region r ON f.region_id = r.region_id
GROUP BY r.region_name;

-- Top Products
SELECT p.product_name, SUM(f.quantity) AS total_sold
FROM fact_sales f
JOIN dim_product p ON f.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_sold DESC;
```

---

## Scalability Considerations
- Replace SQLite with PostgreSQL / Redshift
- Use Spark for distributed processing
- Store raw data in S3 (data lake)
- Partition fact table by date

---

## Future Enhancements
- Real-time ingestion using Kafka
- Spark Structured Streaming
- Dashboard (Power BI / Tableau)
- Data quality checks (Great Expectations)

---

Designed and implemented a scalable ETL pipeline with star schema modeling, enabling analytical queries on sales data and simulating real-world data warehouse architecture.

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
