from datetime import datetime
import subprocess
import sys

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator


default_args = {
    "owner": "zaki",
}


# ======================================================
# LOAD API
# ======================================================

def run_load_api():

    # Supaya Python bisa menemukan folder /opt/airflow/project
    sys.path.insert(0, "/opt/airflow/project")

    from elt.load_api import load_api_to_bronze

    load_api_to_bronze()


# ======================================================
# DBT RUN
# ======================================================

def run_dbt():

    subprocess.run(
        [
            "dbt",
            "run",
            "--profiles-dir",
            "/opt/airflow/project/dbt/profiles",
        ],
        cwd="/opt/airflow/project/dbt/api_project",
        check=True,
    )


# ======================================================
# DBT TEST
# ======================================================

def test_dbt():

    subprocess.run(
        [
            "dbt",
            "test",
            "--profiles-dir",
            "/opt/airflow/project/dbt/profiles",
        ],
        cwd="/opt/airflow/project/dbt/api_project",
        check=True,
    )


# ======================================================
# DAG
# ======================================================

with DAG(
    dag_id="api_pipeline",
    default_args=default_args,
    start_date=datetime(2026, 8, 1),
    schedule="0 8 * * *",
    catchup=False,
    tags=["API", "ELT"],
) as dag:

    load_api = PythonOperator(
        task_id="load_api",
        python_callable=run_load_api,
    )

    dbt_run = PythonOperator(
        task_id="dbt_run",
        python_callable=run_dbt,
    )

    dbt_test = PythonOperator(
        task_id="dbt_test",
        python_callable=test_dbt,
    )

    load_api >> dbt_run >> dbt_test