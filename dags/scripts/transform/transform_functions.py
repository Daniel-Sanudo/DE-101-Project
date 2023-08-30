def transform_data():
    import pandas as pd
    import glob
    import os

    directory_path = "data/products/"
    csv_files = glob.glob(directory_path + "*.csv")

    if len(csv_files) == 0:
        return f"no_files found in {os.getcwd()}/data/product/"

    else:
        # Read the files into dataframes
        dfs = [pd.read_csv(f) for f in csv_files]

        # Combine the list of dataframes
        df = pd.concat(dfs, ignore_index=True)

        # Create Fact Table
        fact_table = df[['UID', 'cloudProdID', 'productID', 'shortID',
                        'colorNum', 'fullPrice', 'currentPrice', 'sale', 'rating']]
        fact_table.columns = fact_table.columns.str.upper()

        # Create Product Dimension Table
        product_dimension = df[['UID', 'title', 'subtitle', 'category', 'type', 'customizable', 'ExtendedSizing', 'inStock', 'ComingSoon', 'BestSeller', 'Excluded',
                                'GiftCard', 'Jersey', 'Launch', 'MemberExclusive', 'NBA', 'NFL', 'Sustainable', 'label', 'prebuildId', 'prod_url', 'currency', 'channel', 'short_description']]
        product_dimension = product_dimension.drop_duplicates().reset_index(drop=True)
        product_dimension.columns = product_dimension.columns.str.upper()

        # Create Color Dimension Table
        color_dimension = df[['UID', 'color-ID', 'color-Description', 'color-FullPrice', 'color-CurrentPrice', 'color-Discount',
                            'TopColor', 'color-BestSeller', 'color-InStock', 'color-MemberExclusive', 'color-New', 'color-Label', 'color-Image-url']]
        color_dimension = color_dimension.drop_duplicates().reset_index(drop=True)
        color_dimension.columns = color_dimension.columns.str.upper()

        # Write DataFrames to csv files
        fact_table.to_csv('data/cleaned/ProductSalesFact.csv', index=False)
        product_dimension.to_csv('data/cleaned/ProductDetailsDimension.csv', index=False)
        color_dimension.to_csv('data/cleaned/ColorDetailsDimension.csv', index=False)
        
        return f"files successfully written to {os.getcwd()}/data/cleaned/"