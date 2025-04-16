from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG("test", start_date=datetime(2023, 1, 1), schedule_interval=None, catchup=False) as dag:
    task = BashOperator(
        task_id="print_from_git",
        bash_command="echo 'Triggered by GitHub push!'"
    )
