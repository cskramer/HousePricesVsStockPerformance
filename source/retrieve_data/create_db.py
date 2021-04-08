import os
import sqlite3
import pandas as pd
import numpy as np


def fix_index_frames(df, idx_name):
    """
    Combining Stock Indicies in the same data frame with the same columns
    require that columns be renamed.
    Date,Open,High,Low,Close,Adj Close,Volume
    :param df: index data from yahoo finance.
    :type df: pandas data frame
    :param idx_name: prefix to append to the index columns
    :type idx_name: string
    :return: copy of the modified dataframe
    :rtype: pandas data frame
    """
    df = df.rename(
        columns={
            "Date": "DATE",
            "Open": idx_name + "_" + "OPEN",
            "High": idx_name + "_" + "HIGH",
            "Low": idx_name + "_" + "LOW",
            "Close": idx_name + "_" + "CLOSE",
            "Adj Close": idx_name + "_" + "ADJCLOSE",
            "Volume": idx_name + "_" + "VOLUME",
        }
    )
    df.DATE = pd.to_datetime(df.DATE)
    return df.copy()


def main():
    """
    Generate an sqlite database from a pandas table.
    :return:
    :rtype:
    """
    FRED_DIR = "../../data/fred_data"
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
    )

    dframes = []
    for fname in fred_filenames:
        df = pd.read_csv(os.path.join(FRED_DIR, fname), encoding="utf8")
        df.DATE = pd.to_datetime(df.DATE)
        df = df.replace(".", np.nan)
        df.iloc[:, 1] = df.iloc[:, 1].astype("float64")
        dframes.append(df)

    all_fred_df = pd.merge(dframes[0], dframes[1], how="outer", on="DATE",)
    i = 2
    while i < len(dframes):
        all_fred_df = all_fred_df.merge(dframes[i], how="outer", on="DATE",)
        if i > len(dframes) - 1:
            break
        i = i + 1

    INDEX_DIR = os.path.join("../../data/index_data", "yahooApi")
    DJI_FILENAME = "djii_1m.csv"
    IXIC_FILENAME = "nasdaq_1m.csv"
    GSPC_FILENAME = "sp500_1m.csv"

    dji_frame = pd.read_csv(os.path.join(INDEX_DIR, DJI_FILENAME), encoding="utf8")
    dji_frame = fix_index_frames(dji_frame, "DJI")

    ixic_frame = pd.read_csv(os.path.join(INDEX_DIR, IXIC_FILENAME), encoding="utf8")
    ixic_frame = fix_index_frames(ixic_frame, "IXIC")

    gspc_frame = pd.read_csv(os.path.join(INDEX_DIR, GSPC_FILENAME), encoding="utf8")
    gspc_frame = fix_index_frames(gspc_frame, "GSPC")

    all_index_df = pd.merge(ixic_frame, dji_frame, how="outer", on="DATE")
    all_index_df = all_index_df.merge(gspc_frame, how="outer", on="DATE")

    complete_df = pd.merge(all_fred_df, all_index_df, how="outer", on="DATE")
    complete_df.sort_values("DATE")
    complete_df = complete_df.set_index("DATE")

    DB_DIR = "../../data/db"
    DB_NAME = "alldata.db"
    con = sqlite3.connect(os.path.join(DB_DIR, DB_NAME))
    cur = con.cursor()
    complete_df.to_sql("all_data", con, if_exists="replace", index=True)
    con.commit()
    con.close()


if __name__ == "__main__":
    main()
