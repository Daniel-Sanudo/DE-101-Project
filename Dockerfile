FROM apache/airflow:2.6.2
USER airflow
RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" tqdm bs4 numpy pandas requests snowflake-connector-python sqlalchemy