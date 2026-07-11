import pandas as pd

from backend.config import EVENT_DATA


def load_events():

    df = pd.read_csv(EVENT_DATA)

    df["Date"] = pd.to_datetime(df["Date"])

    return df