import pandas as pd

from backend.config import BRENT_DATA


def load_price_data():

    df = pd.read_csv(BRENT_DATA)

    df["Date"] = pd.to_datetime(df["Date"])

    return df