# Create a DAG

# import libraries
from datetime import timedelta
# DAG objects
from airflow import DAG
# Operators
from airflow.operators.bash_operator import BashOperator
# utils.dates make scheduling easy
from airflow.utils.dates import days_ago


# Defining DAG arguments

default_args = {
    'owner': 'Ramesh Sannareddy',
    'start_date': days_ago(0),
    'email': ['ramesh@somemail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


# Defining the DAG
dag = DAG(
    'my_first_dag',
    default_args = default_args,
    description = 'My First DAG',
    schedule_interval = timedelta(days=1),
)


# Define the tasks (task1, taks2)

# Defining the first task
extract = BashOperator(
    task_id='extract',
    bash_command='cut -d":" -f1,3,6 /etc/password > /home/project/airflow/dags/extracted-data.txt',
    dag=dag,
)

# Define the second task with a unique 'task_id'
transform_and_load = BashOperator(
    task_id='transform_and_load',
    bash_command='tr ":" "," < /home/project/airflow/dags/extracted-data.txt > /home/project/airflow/dags/transformed-data.csv',
    dag=dag,
)


# task pipeline
extract >> transform_and_load