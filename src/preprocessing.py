import pandas as pd
import numpy as np

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

    try:

        required = [
            "Price"
        ]

        for col in required:

            if col not in df.columns:
                raise KeyError(
                    f"Missing column {col}"
                )


        df=df.copy()


        if (df["Price"] <= 0).any():

            raise ValueError(
                "Price contains zero or negative values"
            )


        df["Log_Price"] = np.log(
            df["Price"]
        )


        df["Price_Change"] = (
            df["Price"]
            .diff()
        )


        df["Log_Return"] = (
            df["Log_Price"]
            .diff()
        )


        df["Rolling_Volatility"] = (
            df["Log_Return"]
            .rolling(
                window=30
            )
            .std()
        )


        return df


    except Exception as e:

        raise RuntimeError(
            f"Feature creation failed: {e}"
        )



def prepare_model_data(
        df,
        column="Price"
):

    try:

        if column not in df.columns:

            raise KeyError(
                f"{column} missing"
            )


        data = (
            df[column]
            .dropna()
            .values
        )


        if len(data) < 50:

            raise ValueError(
                "Not enough observations for Bayesian model"
            )


        return data


    except Exception as e:

        raise RuntimeError(
            f"Model data preparation failed: {e}"
        )