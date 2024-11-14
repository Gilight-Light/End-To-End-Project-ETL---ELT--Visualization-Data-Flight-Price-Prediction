from airflow import DAG
from airflow.decorators import task
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airlfow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import os,requests
import pandas as pd


dag_owner = 'ProjectIE'

default_args = {'owner': dag_owner,
        'depends_on_past': False,
        'retries': 2,
        'retry_delay': timedelta(minutes=5)
        }

with DAG(dag_id='ETL DATA ',
        default_args=default_args,
        description='ETL data from DB, load into DB Postgres',
        start_date=datetime(2024,11,7),
        schedule_interval='',
        catchup=False,
        tags=['']
)as dag:

    python_task_extract_into_DB = PythonOperator(
        task_id='Extract_into_DB',
        python_callable=lambda: print('Hi from python operator'),
        # op_kwargs: Optional[Dict] = None,
        # op_args: Optional[List] = None,
        # templates_dict: Optional[Dict] = None
        # templates_exts: Optional[List] = None
    )

    

    python_task_extract_into_DB