# Airflow pipeline script
# Python script blocks

# python library imports

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
import datetime as dt

# Airflow Pipeline Script DAG Arguments
default_args = {
  'owner': 'me',
  'start_date': dt.datetime(2021, 7, 28),
  'retries': 1,
  'retry_delay': dt.timedelta(minutes=5),
}

# Airflow Pipeline Script DAG definition
dag = DAG('simple_example',
          description='A simple example DAG',
          default_args=default_args,
          schedule_interval=dt.timedelta(seconds=5),
)

# Airflow Pipeline Script Task Definition
task1 = BashOperator(
  task_id='print_hello',
  bash_command='echo "Greetings. The date and time are"',
  dag=dag,
  description='Print a greeting message.',
)

task2 = BashOperator(
  task_id='print_date',
  bash_command='date',
  dag=dag,
  description='Print the current date and time.',
)

# Airflow Pipeline Script Task Pipeline
task1 >> task2  # task one, named 'print hello', will run first, Once 'print hello' runs successfully, task two, or 'print date', will run.
