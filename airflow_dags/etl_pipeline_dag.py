from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1
}

dag = DAG('etl_pipeline', default_args=default_args, schedule_interval='@hourly')

ingest_task = BashOperator(
    task_id='data_ingestion',
    bash_command='python3 /path/to/data_ingestion/kafka_consumer.py',
    dag=dag
)

process_task = BashOperator(
    task_id='data_processing',
    bash_command='python3 /path/to/data_processing/spark_processing.py',
    dag=dag
)

load_task = BashOperator(
    task_id='data_loading',
    bash_command='python3 /path/to/data_storage/postgres_loader.py',
    dag=dag
)

ingest_task >> process_task >> load_task
