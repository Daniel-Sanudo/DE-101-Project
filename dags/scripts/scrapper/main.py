import datetime

from scripts.scrapper.nikescrapi import NikeScrAPI
from scripts.scrapper.sales_generator import SalesGenerator

def run_scrapper(max_pages, day_count, min_sales, max_sales):
    
    print(f"""#########
    Loading job with the following parameters:
    max_pages={max_pages}
    day_count={day_count}
    min_sales={min_sales}
    max_sales={max_sales}
    #########""")

    # NOTE: for production set max_pages = 200
    nikeAPI = NikeScrAPI(max_pages=max_pages, path='data/products')
    df = nikeAPI.getData()

    # Sales generator
    gen = SalesGenerator(nike_df=df, min_sales=min_sales, max_sales=max_sales)

    end = datetime.datetime.now()
    start = end - datetime.timedelta(days=day_count)
    gen.generate_interval(start=start, end=end)