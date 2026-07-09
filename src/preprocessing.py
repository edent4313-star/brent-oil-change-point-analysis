def check_missing_values(df):
    """
    Return missing value summary.
    """

    return df.isnull().sum()



def remove_duplicates(df):
    """
    Remove duplicated rows.
    """

    df = df.copy()

    df = df.drop_duplicates()

    return df



def create_price_features(df):
    """
    Create time series features.
    """

    df = df.copy()


    df["Price_Change"] = (
        df["Price"]
        .diff()
    )


    df["Rolling_Mean_30"] = (
        df["Price"]
        .rolling(window=30)
        .mean()
    )


    return df