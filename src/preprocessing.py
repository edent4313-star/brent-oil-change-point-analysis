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


def _safe_log(values):
    """
    Apply a log-like transform that preserves the sign of negative values.
    """

    values = np.asarray(values, dtype=float)
    transformed = np.empty_like(values, dtype=float)

    positive_mask = values > 0
    negative_mask = values < 0
    zero_mask = ~(positive_mask | negative_mask)

    transformed[positive_mask] = np.log(values[positive_mask])
    transformed[negative_mask] = -np.log(np.abs(values[negative_mask]) + 1)
    transformed[zero_mask] = 0.0

    return transformed


def prepare_change_point_series(values, transform="log"):
    """
    Transform a numeric series for change-point modeling while preserving
    negative values instead of dropping them.
    """

    values = np.asarray(values, dtype=float)

    if values.ndim != 1:
        values = values.reshape(-1)

    values = values[np.isfinite(values)]

    if len(values) < 2:
        raise ValueError("Need at least two observations")

    if transform == "log":
        return _safe_log(values)

    if transform == "log_return":
        transformed = prepare_change_point_series(values, transform="log")
        return np.diff(transformed)

    raise ValueError(f"Unsupported transform: {transform}")


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


        df["Log_Price"] = _safe_log(
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


        df["Rolling_Mean_30"] = (
            df["Log_Return"]
            .rolling(
                window=30
            )
            .mean()
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