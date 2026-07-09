"""
Data loading utilities for Brent Oil Change Point Project.
"""

from pathlib import Path
import pandas as pd


def load_brent_data(file_path):
    """
    Load Brent oil price dataset.

    Parameters
    ----------
    file_path : str
        Dataset location

    Returns
    -------
    pandas.DataFrame
    """

    try:

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(
                f"Dataset not found: {file_path}"
            )


        df = pd.read_csv(path)


        if df.empty:
            raise ValueError(
                "Dataset is empty"
            )


        required_columns = [
            "Date",
            "Price"
        ]


        missing = set(required_columns) - set(df.columns)


        if missing:
            raise ValueError(
                f"Missing required columns: {missing}"
            )


        return df


    except Exception as e:

        raise RuntimeError(
            f"Error loading Brent dataset: {e}"
        )



def convert_date_column(
        df,
        date_column="Date"
):

    try:

        if date_column not in df.columns:
            raise KeyError(
                f"{date_column} not found"
            )


        df = df.copy()


        df[date_column] = pd.to_datetime(
            df[date_column],
            errors="coerce"
        )


        invalid_dates = df[date_column].isna().sum()


        if invalid_dates > 0:
            raise ValueError(
                f"{invalid_dates} invalid dates found"
            )


        df = df.sort_values(
            date_column
        ).reset_index(drop=True)


        return df


    except Exception as e:

        raise RuntimeError(
            f"Date conversion failed: {e}"
        )