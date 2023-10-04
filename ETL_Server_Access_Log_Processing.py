# Practice Exercise


# Importing the libraries
# Task 1: Create the imports block.
from airflow import DAG
from datetime import timedelta
from airflow.utils.dates import days_ago
from airflow.operators.bash_operator import BashOperator


# Task 2: Create the DAG Arguments block. You can use the default settings
default_args = {
    'owner': 'Charmaine Vinarta',
    'start_date': days_ago(0),
    'email': ['ramesh@somemail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


# Task 3: Create the DAG definition block. The DAG should run daily.
dag = DAG(
    'ETL_Server_Access_Log_Processing',
    default_args = default_args,
    description = 'ETL Server Access Log Processing',
    schedule_interval = timedelta(days=1)
)


# Task 4: Create the download task, define
download = BashOperator(
    task_id = 'download',
    bash_command = 'wget "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Build%20a%20DAG%20using%20Airflow/web-server-access-log.txt"',
    dag = dag,
)



# Task 5: Create the extract task.
# define the task 'extract'
extract = BashOperator(
    task_id = 'extract',
    bash_command = 'cut -f1,4 -d"#" web-server-access-log.txt > /home/project/airflow/dags/extracted.txt',
    dag = dag,
)


# Task 6: Create the transform task.
# define the task 'transform'

transform = BashOperator(
    task_id='transform',
    bash_command='tr "[a-z]" "[A-Z]" < /home/project/airflow/dags/extracted.txt > /home/project/airflow/dags/capitalized.txt',
    dag=dag,
)


# Task 7: Create the load task.
# define the task 'load'

load = BashOperator(
    task_id='load',
    bash_command='zip log.zip capitalized.txt' ,
    dag=dag,
)


# Task 8: Create the task pipeline block.
# task pipeline

download >> extract >> transform >> load


# ask 9: Submit the DAG.
#  cp ETL_Server_Access_Log_Processing.py $AIRFLOW_HOME/dags


# Task 10. Verify if the DAG is submitted
# airflow dags list
# airflow dags list|grep "ETL_Server_Access_Log_Processing"
# airflow tasks list ETL_Server_Access_Log_Processing