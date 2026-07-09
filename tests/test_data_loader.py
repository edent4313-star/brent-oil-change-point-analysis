import pandas as pd

from src.data_loader import convert_date_column



def test_convert_date_column():

    data = {

        "Date":
        [
            "01-Jan-2020",
            "02-Jan-2020"
        ],

        "Price":
        [
            60,
            61
        ]

    }


    df = pd.DataFrame(data)


    result = convert_date_column(df)


    assert pd.api.types.is_datetime64_any_dtype(
        result["Date"]
    )