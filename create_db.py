import sqlite3 as sql
import pandas as pd
import util
import os


def main():
    filenames = ( "CPIAUCSL.csv", "DGS10.csv", "JHDUSRGDPBR.csv", "MORTGAGE30US.csv", "OBMMIJUMBO30YF.csv",
                  "RECPROUSM156N.csv", "UMCSENT.csv", "RSAHORUSQ156S.csv", "SPCS10RSA.csv", "CSUSHPISA.csv")
    FRED_DIR = "fred_data"
    dframes = []
    for fname in filenames:
        df = pd.read_csv(os.path.join(FRED_DIR, fname), encoding="utf8")
        df.DATE =  pd.to_datetime(df.DATE)
        dframes.append(df)

    for df in dframes:
        final_data = pd.merge(
            df[["DATE", "SPCS10RSA"]],
            how="outer",
            on="DATE",
        )



if __name__ == "__main__":
    main()
