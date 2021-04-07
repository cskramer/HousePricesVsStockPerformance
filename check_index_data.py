import os
import numpy as np
import pandas as pd

INDEX_DIR = os.path.join("index_data", "yahooApi")
index_filenames = (
    "djii_1m.csv",
    "nasdaq_1m.csv",
    "sp500_1m.csv",
)

index_descriptions = (
    """
    S&P 500 (^DJI)
    Source: Yahoo! Finance 
    Columns: Date (YYYY-MM-DD), Open (float64), High (float64), Low (float64), Close (float64), Adj Close (float64)
    Units:  USD
    Frequency:  Monthly, First Day of the Month 
    """,
    """
    S&P 500 (^IXIC)
    Source: Yahoo! Finance 
    Columns: Date (YYYY-MM-DD), Open (float64), High (float64), Low (float64), Close (float64), Adj Close (float64)
    Units:  USD
    Frequency:  Monthly, First Day of the Month 
    """,
    """
    S&P 500 (^GSPC)
    Source: Yahoo! Finance 
    Columns: Date (YYYY-MM-DD), Open (float64), High (float64), Low (float64), Close (float64), Adj Close (float64)
    Units:  USD
    Frequency:   Monthly, First Day of the Month 
    """,
)


def main():
    global INDEX_DIR
    global index_filenames
    dframes = []
    for fname in index_filenames:
        df = pd.read_csv(os.path.join(INDEX_DIR, fname), encoding="utf8")
        df = df.rename(columns={"Date": "DATE",})
        df.DATE = pd.to_datetime(df.DATE)
        df = df.set_index("DATE")
        dframes.append(df)

    i = 0
    while i < len(dframes):
        print("*" * 120)
        print(index_descriptions[i], end="")
        print("")
        print(dframes[i].head())
        print("")
        print(dframes[i].describe())
        print("")
        print("Number of Columns: ", len(dframes[i].columns))
        print("Are any values Missing:\n", dframes[i].isnull().any())
        print("")
        print("Check the Types: ", dframes[i].dtypes)
        print("")
        print("Check Index:\n", dframes[i].index)
        i = i + 1


if __name__ == "__main__":
    main()
