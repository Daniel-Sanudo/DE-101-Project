from datetime import datetime, timedelta
from airflow import DAG
from airflow.models import Variable
from airflow.operators.python_operator import PythonOperator
from scripts.scrapper.main import run_scrapper
from scripts.transform.transform_functions import transform_data
from scripts.load.load_functions import load_data
from scripts.report.create_report_views import create_report


default_args = {
    'owner': 'Daniel Sanudo',
    'depends_on_past': False,
    'start_date': datetime(2023, 8, 18),
    'retries': 3,
    'retry_delay': timedelta(minutes=15),
}

with DAG(
    'nike_data_pipeline', 
    default_args=default_args, 
    schedule='0 4 * * *',
) as dag:

    extraction_task = PythonOperator(
        task_id='extraction_task',
        python_callable=run_scrapper,
        op_kwargs={'max_pages': int(Variable.setdefault('max_pages', 300)),
                   'day_count': int(Variable.setdefault('day_count', 30)),
                   'min_sales': int(Variable.setdefault('min_sales', 0)),
                   'max_sales': int(Variable.setdefault('max_sales', 4)),
                   }
    )

    transform_task = PythonOperator(
        task_id='transform_task',
        python_callable=transform_data,
    )

    load_task = PythonOperator(
        task_id='load_task',
        python_callable=load_data,
    )

    create_report_views = PythonOperator(
        task_id='create_report_views',
        python_callable=create_report
    )


    extraction_task >> transform_task >> load_task >> create_report_views
