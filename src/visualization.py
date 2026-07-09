import matplotlib.pyplot as plt



def plot_price_history(df):

    plt.figure(figsize=(14,6))


    plt.plot(
        df["Date"],
        df["Price"]
    )


    plt.title(
        "Historical Brent Oil Prices"
    )


    plt.xlabel(
        "Date"
    )


    plt.ylabel(
        "Price USD/barrel"
    )


    plt.grid(True)


    plt.show()




def plot_price_distribution(df):

    plt.figure(figsize=(10,5))


    plt.hist(
        df["Price"],
        bins=50
    )


    plt.title(
        "Brent Oil Price Distribution"
    )


    plt.xlabel(
        "Price"
    )


    plt.ylabel(
        "Frequency"
    )


    plt.show()




def plot_price_change(df):

    plt.figure(figsize=(14,5))


    plt.plot(
        df["Date"],
        df["Price_Change"]
    )


    plt.title(
        "Daily Brent Oil Price Change"
    )


    plt.xlabel(
        "Date"
    )


    plt.ylabel(
        "Change"
    )


    plt.grid(True)


    plt.show()

def plot_change_point(
        df,
        date
):

    try:

        plt.figure(figsize=(15,6))

        plt.plot(
            df["Date"],
            df["Price"]
        )


        plt.axvline(
            date,
            linestyle="--"
        )


        plt.title(
            "Detected Bayesian Change Point"
        )


        plt.show()


    except Exception as e:

        raise RuntimeError(
            f"Change point plot failed: {e}"
        )
    
def plot_Log_Return_Analysis(df):
    
    try:

        plt.figure(figsize=(14,5))

        plt.plot(
            df["Date"],
            df["Log_Return"]
        )


        plt.title(
            "Daily Log Returns of Brent Oil Prices"
        )


        plt.xlabel(
            "Date"
        )


        plt.ylabel(
            "Log Return"
        )


        plt.grid(True)


        plt.show()
    
    except Exception as e:

        raise RuntimeError(
            f"Log Return Analysis failed: {e}"
        )
    
def plot_rolling_volatility(df):
    
    try:

        plt.figure(figsize=(14,5))

        plt.plot(
            df["Date"],
            df["Rolling_Volatility"]
        )


        plt.title(
            "30-Day Rolling Volatility of Brent Oil Prices"
        )


        plt.xlabel(
            "Date"
        )


        plt.ylabel(
            "Volatility"
        )


        plt.grid(True)


        plt.show()
    
    except Exception as e:

        raise RuntimeError(
            f"Rolling Volatility plot failed: {e}"
        )