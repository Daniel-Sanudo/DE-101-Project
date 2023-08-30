def create_report():
    import snowflake.connector
    import os

    # Get connection parameters from .env file
    account_identifier = os.environ["SNOWFLAKE_ACCOUNT"]
    user = os.environ["SNOWFLAKE_USER"]
    password = os.environ["SNOWFLAKE_PASSWORD"]
    warehouse = os.environ["SNOWFLAKE_WAREHOUSE"]
    database_name = os.environ["SNOWFLAKE_DATABASE"]
    schema_name = 'prod'

    with snowflake.connector.connect(
        user=user,
        password=password,
        account=account_identifier,
        warehouse=warehouse,
        database=database_name,
        schema=schema_name,
        autocommit=False,
    ) as con:
        # Top 5 sold products
        con.cursor().execute("""
            CREATE OR REPLACE VIEW top_5_sold_products AS (
                select a.productid, count(*) as sales from NIKE_API.STAGING.PRODUCTSALESFACT a 
                INNER JOIN NIKE_API.STAGING.PRODUCTDETAILSDIMENSION b
                ON a.UID = b.uid
                GROUP BY a.productid
                ORDER BY sales DESC
                LIMIT 5
            );
        """)

        # Top 5 sold categories
        con.cursor().execute("""
            CREATE OR REPLACE VIEW top_5_sold_categories AS (
                select b.category, count(*) as sales from NIKE_API.STAGING.PRODUCTSALESFACT a 
                INNER JOIN NIKE_API.STAGING.PRODUCTDETAILSDIMENSION b
                ON a.UID = b.uid
                GROUP BY b.category
                ORDER BY sales DESC
                LIMIT 5
            );
        """)

        # Bottom 5 sold categories
        con.cursor().execute("""
            CREATE OR REPLACE VIEW bottom_5_sold_categories AS (
                select b.category, count(*) as sales from NIKE_API.STAGING.PRODUCTSALESFACT a 
                INNER JOIN NIKE_API.STAGING.PRODUCTDETAILSDIMENSION b
                ON a.UID = b.uid
                GROUP BY b.category
                ORDER BY sales ASC
                LIMIT 5
            );
        """)

        # Top 5 sales by title and subtitle
        con.cursor().execute("""
            CREATE OR REPLACE VIEW top_5_sold_title_and_subtitle AS (
                select b.title, b.subtitle, count(*) as sales from NIKE_API.STAGING.PRODUCTSALESFACT a 
                INNER JOIN NIKE_API.STAGING.PRODUCTDETAILSDIMENSION b
                ON a.UID = b.uid
                GROUP BY b.title, b.subtitle
                ORDER BY sales DESC
                LIMIT 5
            );
        """)

        # Top 3 products by category
        con.cursor().execute("""
            CREATE OR REPLACE VIEW top_5_sold_category_and_product AS (
                select a.productid, b.category, count(*) as sales from NIKE_API.STAGING.PRODUCTSALESFACT a 
                INNER JOIN NIKE_API.STAGING.PRODUCTDETAILSDIMENSION b
                ON a.UID = b.uid
                GROUP BY a.productid, b.category
                ORDER BY sales DESC
                LIMIT 5
            );
        """)
