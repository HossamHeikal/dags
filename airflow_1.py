from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
        'owner': 'user',
        'retries': 5,
        'retry_delay': timedelta(minutes=2)
        }





with DAG(
        dag_id='first_dag_v08',
        default_args=default_args,
        description='This is my first dag to write',
        start_date=datetime(2022, 8, 1, 5),
        schedule_interval = '@daily',
        catchup = False

) as dag:
    task1 = BashOperator(
            task_id='first_task',
            bash_command="echo hello world, this is the first task!"
            )
    task2 = BashOperator(
            task_id='second_task',
            bash_command="echo hey, I am task 2 and I will be running after task1"
            )
    task3= BashOperator(
            task_id= 'third_task',
            bash_command="echo I am task 3 and wil run after task1 at te same time with task2"
            )
#Method 1:    
#task1.set_downstream(task2)
#task1.set_downstream(task3)
#Method2:
#task1 >> task2
#task1 >> task3
#Mothod 3:
task1 >> [task2, task3]
