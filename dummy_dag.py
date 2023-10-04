# Creating a dummy DAG with 3 tasks
# Task1 does nothing but sleep for 1 second.
# Task2 sleeps for 2 seconds.
# Task3 sleeps for 3 seconds.

# import libraries

from datetime import timedelta
# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to write tasks!
from airflow.operators.bash_operator import BashOperator
# This makes scheduling easy
from airflow.utils.dates import days_ago

#define DAG arguments
default_args = {
    'owner': 'Charmaine Vinarta',
    'start_date': days_ago(0),
    'email': ['charmainee.vinarta@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

#define DAG
dag = DAG(
    'dummy_dag',
    default_args = default_args,
    description = 'My Dummy Dag',
    schedule_interval = timedelta(minutes = 1),
)

#define tasks 1,2,3

#Task1 does nothing but sleep for 1 second.
task1 = BashOperator(
    task_id = 'taks1',
    bash_command = 'sleep 1',
    dag = dag,
)

# Task2 sleeps for 2 seconds.
task2 = BashOperator(
    task_id = 'task2',
    bash_command = 'sleep 2',
    dag = dag,
)

# Task3 sleeps for 3 seconds.
task3 = BashOperator(
    task_id = 'task3',
    bash_command = 'sleep 3',
    dag = dag,
)

#task pipeline
task1 >> task2 >> task3