from statsmodels.tsa.stattools import adfuller

def dataset_overview(df):
    """
    Return basic dataset information.
    """

    overview = {

        "rows": df.shape[0],

        "columns": df.shape[1],

        "column_names": list(df.columns),

        "missing_values":
            df.isnull().sum().to_dict(),

        "duplicates":
            df.duplicated().sum()

    }


    return overview




def summary_statistics(df):
    """
    Generate descriptive statistics.
    """

    return df.describe()




def price_range(df):

    result = {

        "minimum_price":
            df["Price"].min(),

        "maximum_price":
            df["Price"].max(),

        "average_price":
            df["Price"].mean()

    }


    return result


def adf_test(Log_Return, name):
    result = adfuller(Log_Return.dropna())
    print(f'\n--- Augmented Dickey-Fuller Test for {name} ---')
    print(f'ADF Statistic: {result[0]:.4f}')
    print(f'P-value: {result[1]:.4f}')
    print('Critical Values:')
    for key, value in result[4].items():
        print(f'    {key}: {value:.4f}')

    if result[1] <= 0.05:
        print('Result: Reject H0 (Series is stationary)')
    else:
        print('Result: Fail to reject H0 (Series is non-stationary)')

  