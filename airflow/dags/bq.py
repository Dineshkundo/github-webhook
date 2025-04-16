from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from datetime import datetime

default_args = {
    "start_date": datetime(2023, 1, 1),
}

with DAG(
    dag_id="bq_insert_data",
    schedule_interval=None,
    catchup=False,
    default_args=default_args,
    tags=["bigquery", "insert"],
) as dag:

    insert_data = BigQueryInsertJobOperator(
        task_id="insert_sample_rows",
        configuration={
            "query": {
                "query": """
                    INSERT INTO `adq-get-project.sample_dataset.sample_table` (id, name, created_at)
                    VALUES
                      (1, 'Alice', CURRENT_TIMESTAMP()),
                      (2, 'Bob', CURRENT_TIMESTAMP()),
                      (3, 'Charlie', CURRENT_TIMESTAMP());
                """,
                "useLegacySql": False,
            }
        },
        location="US",  # Set to match your dataset location
        gcp_conn_id="google_cloud_default",
    )

    insert_data

