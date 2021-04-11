import os
import numpy as np
import pandas as pd

FRED_DIR = "fred_data"
fred_filenames = (
    "CPIAUCSL.csv",
    "DGS10.csv",
    "JHDUSRGDPBR.csv",
    "MORTGAGE30US.csv",
    "OBMMIJUMBO30YF.csv",
    "RECPROUSM156N.csv",
    "UMCSENT.csv",
    "RSAHORUSQ156S.csv",
    "SPCS10RSA.csv",
    "CSUSHPISA.csv",
    "CPILFESL.csv",
)
fred_urls = (
    "",
    "https://fred.stlouisfed.org/series/DGS10",
    "https://fred.stlouisfed.org/series/CPIAUCSL",
    "https://fred.stlouisfed.org/series/JHDUSRGDPBR",
    "https://fred.stlouisfed.org/series/MORTGAGE30US",
    "https://fred.stlouisfed.org/series/OBMMIJUMBO30YF",
    "https://fred.stlouisfed.org/series/RECPROUSM156N",
    "https://fred.stlouisfed.org/series/UMCSENT",
    "https://fred.stlouisfed.org/series/RSAHORUSQ156S",
    "https://fred.stlouisfed.org/series/SPCS10RSA",
    "https://fred.stlouisfed.org/series/CSUSHPISA",
    "https://fred.stlouisfed.org/series/CPILFESL",
)
fred_descriptions = (
    """
    DGS10
    10-Year Treasury Constant Maturity Rate
    Source: Board of Governors of the Federal Reserve System (US)  
    Release: H.15 Selected Interest Rates  
    Units:  Percent, Not Seasonally Adjusted
    Frequency:  Daily 
    """,
    """
    CPIAUCSL
    Consumer Price Index for All Urban Consumers: All Items in U.S. City Average
    Source: U.S. Bureau of Labor Statistics  
    Release: Consumer Price Index  
    Units:  Index 1982-1984=100, Seasonally Adjusted
    Frequency:  Monthly 
    """,
    """
    JHDUSRGDPBR
    Dates of U.S. recessions as inferred by GDP-based recession indicator
    Source: Hamilton, James  
    Release: GDP-Based Recession Indicator Index  
    Units:  +1 or 0, Not Seasonally Adjusted
    Frequency:  Quarterly 
    """,
    """
    MORTGAGE30US
    30-Year Fixed Rate Mortgage Average in the United States 
    Source: Freddie Mac  
    Release: Primary Mortgage Market Survey  
    Units:  Percent, Not Seasonally Adjusted
    Frequency:  Weekly, Ending Thursday 
    """,
    """
    OBMMIJUMBO30YF
    30-Year Fixed Rate Jumbo Mortgage Index 
    Source: Optimal Blue  
    Release: Optimal Blue Mortgage Market Indices  
    Units:  Percent, Not Seasonally Adjusted
    Frequency:  Daily 
    """,
    """
    RECPROUSM156N
    Smoothed U.S. Recession Probabilities 
    Source: Chauvet, Marcelle
    Source: Piger, Jeremy Max  
    Release: U.S. Recession Probabilities  
    Units:  Percent, Not Seasonally Adjusted
    Frequency:  Monthly 
    """,
    """
    UMCSENT
    University of Michigan: Consumer Sentiment
    Source: University of Michigan  
    Release: Surveys of Consumers  
    Units:  Index 1966:Q1=100, Not Seasonally Adjusted
    Frequency:  Monthly 
    """,
    """
    RSAHORUSQ156S
    Homeownership Rate for the United States
    Source: U.S. Census Bureau  
    Release: Housing Vacancies and Homeownership  
    Units:  Percent, Seasonally Adjusted
    Frequency:  Quarterly 
    """,
    """
    SPCS10RSA
    S&P/Case-Shiller 10-City Composite Home Price Index 
    Source: S&P Dow Jones Indices LLC  
    Release: S&P/Case-Shiller Home Price Indices  
    Units:  Index Jan 2000=100, Seasonally Adjusted
    Frequency:  Monthly 
    """,
    """
    CSUSHPISA
    S&P/Case-Shiller U.S. National Home Price Index
    Source: S&P Dow Jones Indices LLC  
    Release: S&P/Case-Shiller Home Price Indices  
    Units:  Index Jan 2000=100, Seasonally Adjusted
    Frequency:  Monthly  
    """,
    """
    CPILFESL 
    Consumer Price Index for All Urban Consumers: All Items Less Food and Energy in U.S. City Average
    Source: U.S. Bureau of Labor Statistics  
    Release: Consumer Price Index  
    Units:  Index 1982-1984=100, Seasonally Adjusted
    Frequency:  Monthly
    """,
)


def main():
    global FRED_DIR
    global fred_filenames
    script_dir = os.path.dirname(os.path.realpath(__file__))
    fred_abs_path = os.path.abspath(
        os.path.join(script_dir, "..", "..", "data", FRED_DIR)
    )

    dframes = []
    for fname in fred_filenames:
        df = pd.read_csv(os.path.join(fred_abs_path, fname), encoding="utf8")
        df.DATE = pd.to_datetime(df.DATE)
        df = df.set_index("DATE")
        dframes.append(df)

    i = 0
    while i < len(dframes):
        print("*" * 120)
        print(fred_descriptions[i], end="")
        print(fred_urls[i])
        print("")
        print(dframes[i].head())
        print("")
        print(dframes[i].describe())
        print("")
        print("Number of Columns: ", len(dframes[i].columns))
        print("Are any values Missing: ", bool(dframes[i].isnull().any()[0]))
        # print("Unique Values: ", dframes[i].iloc[,:0].unique())
        print("Check the Types: ", dframes[i].dtypes)
        print("")
        print("Check Index:\n", dframes[i].index)
        i = i + 1


if __name__ == "__main__":
    main()
