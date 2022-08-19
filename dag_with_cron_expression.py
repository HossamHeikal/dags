from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
        'owner': 'user',
        'retries': 5,
        'retry_delay': timedelta(minutes = 5)

        }

with DAG(
        default_args = default_args,
        dag_id = "dag_with_cron_expression_v05",
        start_date=datetime(2022, 7, 3),
        schedule_interval = '0 3 * * tue,fri'

        )as dag:
    task1 = BashOperator(
            task_id = 'task1',
            bash_command = "echo dag woth cron expression"

            )
    task1
