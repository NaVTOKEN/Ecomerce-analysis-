from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess

def run_etl():
    subprocess.run(["python", "/path/to/etl/main.py"])

default_args = {
    "owner": "data_engineer",
    "start_date": datetime(2024, 1, 1),
    "retries": 1
}

dag = DAG(
    "ecommerce_etl_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False
)

etl_task = PythonOperator(
    task_id="run_etl",
    python_callable=run_etl,
    dag=dag
)

etl_task
