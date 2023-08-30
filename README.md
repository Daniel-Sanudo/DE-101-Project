# DE-101-Project

Project for DE-101 Course

## Project Objective

The objective of this project is to consume data from the Nike API provided on the nikescrapi.py file, build a data pipeline to insert the API data into a data warehouse, and create a data warehouse structure to store the data. Finally, we will write necessary queries to make reports from the data warehouse.

## User guide

The project requires a .env file created in its root that contains the following snowflake information:
```
SNOWFLAKE_USER=
SNOWFLAKE_PASSWORD=
SNOWFLAKE_ACCOUNT=
SNOWFLAKE_WAREHOUSE=
SNOWFLAKE_DATABASE=
SNOWFLAKE_ROLE=
```

These environmental variables are used in the load and report tasks of the dag to create the staging table where the scrapped information is uploaded. And to create the views that report the relevant results using sql.

Following airflow best practices, all top level code can be found in its dedicated folder inside the scripts dags/scripts directory. 

The dockerfile for airflow also includes the required dependencies to run both the scrapper and the load process. 

The loading is done by splitting the scrapped information into a sales fact table, a product dimension and a color dimension. These are uploaded into snowflake using sqlalchemy and pandas.

The python file that creates the data warehouse is in the dags/scripts/load folder, while the queries to create the reports are in dags/scripts/report.

[scrapper_readme]: ./scrapper/project_requirements.md
[scrapper_folder]: ./scrapper
