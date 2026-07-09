import pandas as pd

from src.preprocessing import (
    remove_duplicates,
    create_price_features
)



def test_remove_duplicates():

    df = pd.DataFrame({

        "Price":[10,10,20]

    })


    result = remove_duplicates(df)


    assert len(result)==2




def test_create_price_features():

    df = pd.DataFrame({

        "Price":[10,12,15]

    })


    result=create_price_features(df)


    assert "Price_Change" in result.columns

    assert "Rolling_Mean_30" in result.columns