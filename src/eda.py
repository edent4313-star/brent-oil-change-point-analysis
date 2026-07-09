def dataset_overview(df):
    """
    Return basic dataset information.
    """

    overview = {

        "rows": df.shape[0],

        "columns": df.shape[1],

        "column_names": list(df.columns),

        "missing_values":
            df.isnull().sum().to_dict(),

        "duplicates":
            df.duplicated().sum()

    }


    return overview




def summary_statistics(df):
    """
    Generate descriptive statistics.
    """

    return df.describe()




def price_range(df):

    result = {

        "minimum_price":
            df["Price"].min(),

        "maximum_price":
            df["Price"].max(),

        "average_price":
            df["Price"].mean()

    }


    return result