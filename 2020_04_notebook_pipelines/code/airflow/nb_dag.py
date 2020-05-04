from datetime import timedelta
from airflow import DAG

from airflow.operators.bash_operator import BashOperator
from airflow.operators.papermill_operator import PapermillOperator
from airflow.utils.dates import days_ago

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": days_ago(2),
    "email": ["airflow@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

dag = DAG(
    "nb_pipeline",
    default_args=default_args,
    description="A simple notebook pipeline DAG",
    schedule_interval=timedelta(days=1),
)

t1 = PapermillOperator(
     task_id="data_ingest",
     dag=dag,
     input_nb="/mnt/airflow/ingest_data.ipynb",
     output_nb="/mnt/airflow/out/ingest_data_out_{{ execution_date }}.ipynb")

t2 = PapermillOperator(
     task_id="data_prep",
     dag=dag,
     input_nb="/mnt/airflow/data_prep.ipynb",
     output_nb="/mnt/airflow/out/data_prep_out_{{ execution_date }}.ipynb")

t3 = PapermillOperator(
     task_id="model_training",
     dag=dag,
     input_nb="/mnt/airflow/model_training.ipynb",
     output_nb="/mnt/airflow/out/model_training_out_{{ execution_date }}.ipynb",
     parameters={"tree_max_depth": 5})

t4 = PapermillOperator(
     task_id="validation",
     dag=dag,
     input_nb="/mnt/airflow/validation.ipynb",
     output_nb="/mnt/airflow/out/validation_out_{{ execution_date }}.ipynb")

t1 >> t2 >> t3 >> t4
