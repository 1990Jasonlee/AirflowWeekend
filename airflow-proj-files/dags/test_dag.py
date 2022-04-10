from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from script import some_script


default_args = {
    'owners': 'airflow',
    'start_date': datetime.today() - timedelta(days=1)
}

with DAG()