# Exercise

- **1. To start an Apache Airflow use:**
  ```bash
  start_airflow
  ```
- **2. To list all Dags:**
- Apache airflow gives us some handy command line options to work with.
- list out all the existing DAGs.
  ```bash
  airflow dags list
  ```
- **3. List tasks in a DAG:**
- list out all the tasks in the DAG named `example_bash_operator`.
- Here example_bash_operator is the name of the DAG.
  ```bash
  airflow tasks list example_bash_operator
  ```
- **4. Pause/Unpause a DAG:**
- Pause a Dag
  ```bash
  aiflow dags pause tutorial
  ```
- Unpause a DAG
  ```bash
  airflow dags unpause tutorial
  ```



# Practice Exercises

### Problem 1
- **Task:** List tasks for the DAG `example_branch_labels`.
- **Command:**
  ```bash
  airflow tasks list example_branch_labels
  ```

### Problem 2
- **Task:** Unpause the DAG `example_branch_labels`.
- **Command:**
  ```bash
  airflow unpause dags example_branch_labels
  ```


### Problem 2
- **Task:** Unpause the DAG `example_branch_labels`.
- **Command:**
  ```bash
  airflow pause dags example_branch_labels
  ```
