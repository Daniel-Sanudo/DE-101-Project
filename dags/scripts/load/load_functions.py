def load_data():
    from snowflake.connector.pandas_tools import pd_writer
    from sqlalchemy import create_engine
    import pandas as pd
    import glob
    import os

    # Get connection parameters from .env file
    account_identifier = os.environ["SNOWFLAKE_ACCOUNT"]
    user = os.environ["SNOWFLAKE_USER"]
    password = os.environ["SNOWFLAKE_PASSWORD"]
    database_name = os.environ["SNOWFLAKE_DATABASE"]
    schema_name = 'staging'

    # Create connection string and engine
    conn_string = f"snowflake://{user}:{password}@{account_identifier}/{database_name}/{schema_name}"
    engine = create_engine(conn_string)

    # Get csv file list
    directory_path = "data/cleaned/"
    csv_files = glob.glob(directory_path + "*.csv")
    file_tuples = [(file_path, os.path.splitext(
        os.path.basename(file_path))[0]) for file_path in csv_files]

    # Write the data to Snowflake, using pd_writer to speed up loading
    with engine.connect() as con:
        for file_list in file_tuples:
            print(f'Loading data for table {file_list[1].lower()}')
            pd.read_csv(
                file_list[0],
                index_col=False
            ).to_sql(
                name=file_list[1].lower(),
                con=con,
                if_exists='replace',
                method=pd_writer,
                index=False
            )
