import pandas as pd

from backend.services.data_service import load_price_data


def get_statistics():
    """
    Calculate summary statistics for Brent oil prices.
    """

    try:

        df = load_price_data()

        stats = {
            "records": len(df),
            "average_price": round(df["Price"].mean(), 2),
            "minimum_price": round(df["Price"].min(), 2),
            "maximum_price": round(df["Price"].max(), 2),
            "median_price": round(df["Price"].median(), 2),
            "std_price": round(df["Price"].std(), 2)
        }

        return stats

    except Exception as e:
        raise RuntimeError(
            f"Statistics calculation failed: {e}"
        )