import os
import sqlite3 as sql
import pandas as pd


def main():
    filenames = (
        "CPIAUCSL.csv",  # CPI
        "DGS10.csv",  # 10 Treasury Constant Maturity Rate
        "JHDUSRGDPBR.csv",
        "MORTGAGE30US.csv",
        "OBMMIJUMBO30YF.csv",
        "RECPROUSM156N.csv",
        "UMCSENT.csv",
        "RSAHORUSQ156S.csv",
        "SPCS10RSA.csv",
        "CSUSHPISA.csv",
    )
    FRED_DIR = "fred_data"
    dframes = []
    for fname in filenames:
        df = pd.read_csv(os.path.join(FRED_DIR, fname), encoding="utf8")
        df.DATE = pd.to_datetime(df.DATE)
        dframes.append(df)

    final_data = pd.merge(dframes[0], dframes[1], how="outer", on="DATE",)
    i = 2
    while i < len(dframes):
        final_data = final_data.merge(dframes[i], how="outer", on="DATE",)
        if i > len(dframes) - 1:
            break
        i = i + 1


if __name__ == "__main__":
    main()
