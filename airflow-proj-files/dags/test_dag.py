from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from script import some_script

default_args = {
    'owners': 'airflow',
    'start_date': datetime.today() - timedelta(days=1)
}

with DAG('pokemon_dag', start_date=datetime(2022, 1, 1),
         schedule_interval='@once',
         catchup=False,
         default_args=default_args) as dag:
    task = PythonOperator(
        task_id='pokemon script',
        python_callable=some_script(),
        dag=dag
    )