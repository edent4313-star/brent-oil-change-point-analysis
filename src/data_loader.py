import pandas as pd
from pathlib import Path


def load_brent_data(file_path):
    """
    Load Brent oil price dataset.

    Parameters
    ----------
    file_path : str
        Path to BrentOilPrices.csv

    Returns
    -------
    pandas.DataFrame
        Loaded dataframe
    """

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {file_path}"
        )

    df = pd.read_csv(file_path)

    return df



def convert_date_column(df, date_column="Date"):
    """
    Convert date column to datetime format.
    """

    df = df.copy()

    df[date_column] = pd.to_datetime(
        df[date_column],
        dayfirst=True
    )

    df = df.sort_values(
        by=date_column
    )

    df.reset_index(
        drop=True,
        inplace=True
    )

    return df