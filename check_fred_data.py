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
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "https://fred.stlouisfed.org/series/CPILFESL",
)
fred_descriptions = (
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    """CPILFESL 
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
    dframes = []
    for fname in fred_filenames:
        df = pd.read_csv(os.path.join(FRED_DIR, fname), encoding="utf8")
        df.DATE = pd.to_datetime(df.DATE)
        dframes.append(df)

if __name__ == "__main__":
    main()