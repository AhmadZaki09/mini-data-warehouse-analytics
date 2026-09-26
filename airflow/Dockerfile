FROM apache/airflow:3.3.0

USER root

RUN apt-get update && apt-get install -y build-essential

USER airflow

RUN pip install --no-cache-dir \
    dbt-core \
    dbt-postgres \
    apache-airflow-providers-postgres