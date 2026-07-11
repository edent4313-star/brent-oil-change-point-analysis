from backend.services.data_service import load_price_data


def get_volatility(window=30):

    try:

        df = load_price_data()

        df["RollingVolatility"] = (
            df["Price"]
            .rolling(window)
            .std()
        )

        return df[
            ["Date", "RollingVolatility"]
        ].dropna()

    except Exception as e:

        raise RuntimeError(
            f"Volatility calculation failed: {e}"
        )