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