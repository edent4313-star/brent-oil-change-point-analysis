import pandas as pd

from src.eda import (
    dataset_overview,
    price_range
)



def test_dataset_overview():

    df=pd.DataFrame({

        "Price":[10,20]

    })


    result=dataset_overview(df)


    assert result["rows"]==2



def test_price_range():

    df=pd.DataFrame({

        "Price":[10,20,30]

    })


    result=price_range(df)


    assert result["minimum_price"]==10

    assert result["maximum_price"]==30