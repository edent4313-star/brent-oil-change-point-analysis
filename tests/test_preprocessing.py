import numpy as np
import pandas as pd

from src.preprocessing import (
    remove_duplicates,
    create_price_features,
    prepare_change_point_series
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


def test_prepare_change_point_series_uses_log_scale():

    values = np.array([10, 20, 40])

    result = prepare_change_point_series(values)

    np.testing.assert_allclose(result, np.log(values))