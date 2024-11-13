from airflow import DAG
from airflow.decorators import task
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airlfow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import os,requests


dag_owner = 'ProjectIE'

default_args = {'owner': dag_owner,
        'depends_on_past': False,
        'retries': 2,
        'retry_delay': timedelta(minutes=5)
        }

with DAG(dag_id='Download from Kaggle',
        default_args=default_args,
        description='Down load and extract into Postgres DB',
        start_date=datetime(2024,11,7),
        schedule_interval='',
        catchup=False,
        tags=['']
)as dag:

    bash_task_down = BashOperator(
        task_id="Download source data from kaggle",
        bash_command='curl -L -o ~/Downloads/archive.zip\https://www.kaggle.com/api/v1/datasets/download/shubhambathwal/flight-price-prediction',
        # env: Optional[Dict[str, str]] = None,
        # output_encoding: str = 'utf-8',
        # skip_exit_code: int = 99,
    )
    python_task_extract_into_DB = PythonOperator(
        task_id='Extract_into_DB',
        python_callable=lambda: print('Hi from python operator'),
        # op_kwargs: Optional[Dict] = None,
        # op_args: Optional[List] = None,
        # templates_dict: Optional[Dict] = None
        # templates_exts: Optional[List] = None
    )

    PostgresHook_hook = PostgresHook(

    )
    PostgresOperator_task = PostgresOperator(
        task_id='PostgresOperator_task',
        postgres_conn_id='postgres_default',
        database=None,
        runtime_parameters=None,
    )



    bash_task_down