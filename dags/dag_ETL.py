from airflow import DAG
from airflow.decorators import task
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import os,requests
import pandas as pd
from Data_Transformation import Data_Transformation


def df_to_postgres_direct(df, table_name):
    pg_hook = PostgresHook(postgres_conn_id='postgres_connect_Project')
    engine = pg_hook.get_sqlalchemy_engine()
    
    df.to_sql(
        name=table_name,
        con=engine,
        if_exists='append',  # 'replace' 
        index=False,
        method='multi'  # 
    )

def get_data_as_df(table):
        pg_hook = PostgresHook(postgres_conn_id='postgres_connect_Project')
        df = pg_hook.get_pandas_df(f"SELECT * FROM {table}")
        return df

dag_owner = 'ProjectIE'

default_args = {'owner': dag_owner,
        'depends_on_past': False,
        'retries': 2,
        'retry_delay': timedelta(minutes=5)
        }

with DAG(dag_id='ETL_DATA',
        default_args=default_args,
        description='ETL data from DB, load into DB Postgres',
        start_date=datetime(2024,11,7),
        schedule_interval=None,
        catchup=False,
        tags=['']
)as dag:
    @task
    def Extract_into_DB():
        df_read_economy = get_data_as_df('economy_flight')
        df_read_business = get_data_as_df('business_flight')

        df_gold_data = Data_Transformation(df_read_economy,df_read_business)
        df_to_postgres_direct(df_gold_data,'cleandata_flight')
        print("Success ETL DATA INTO POSTGREDB !!!")

        
        

    

    Extract_into_DB()