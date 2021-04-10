# -*- coding: utf-8 -*-
"""
Project 2 Main Method

Created on Wed Mar 31 18:56:57 2021

@authors: Shane Kramer and Ted Brown
"""

import pandas as pd
import matplotlib.pyplot as plt
import load_fred_data
import load_index_data
import util
import time


def load_data_deprecated():

    nasdaq_frame, sp500_frame, djii_frame = load_index_data.get_normalized_index_data()

    nasdaq_frame = nasdaq_frame.rename(columns={"Date": "DATE"})
    nasdaq_frame.DATE = pd.to_datetime(nasdaq_frame.DATE)

    sp500_frame = sp500_frame.rename(columns={"Date": "DATE"})
    sp500_frame.DATE = pd.to_datetime(nasdaq_frame.DATE)

    djii_frame = djii_frame.rename(columns={"Date": "DATE"})
    djii_frame.DATE = pd.to_datetime(nasdaq_frame.DATE)

    case_shiller_10_city_frame = load_fred_data.get_norm_cse10_data()
    case_shiller_10_city_frame.DATE = pd.to_datetime(case_shiller_10_city_frame.DATE)

    util.generate_scatterplot("NASDAQ", nasdaq_frame, case_shiller_10_city_frame)
    util.generate_scatterplot("SP500", sp500_frame, case_shiller_10_city_frame)
    util.generate_scatterplot("DJIA", djii_frame, case_shiller_10_city_frame)

    nasdaq_frame_norm = util.normalize_dataframe(nasdaq_frame, "Adj Close")
    case_shiller_norm = util.normalize_dataframe(
        case_shiller_10_city_frame, "SPCS10RSA"
    )
    util.generate_lineplot("NASDAQ", nasdaq_frame_norm, case_shiller_norm)


def load_data():
    df = util.load_all_data_from_sql()
    ndf = df[["IXIC_ADJCLOSE", "DJI_ADJCLOSE", "GSPC_ADJCLOSE", "SPCS10RSA"]].dropna()
    ndf = util.normalize_columns(ndf, ndf.columns)

    return ndf


def main():
    """
    Main Loop
    :return:
    :rtype:
    """

    ndf = load_data()

    SPCS10RSA_BEGIN_DATE = "1987-01-01"
    DJII_BEGIN_DATE = "1992-02-01"
    END_DATE = "2021-01-01"
    SPCS_BUBBLE_BEGIN = "1997-08-01"
    SPCS_BUBBLE_END = "2009-01-01"

    cmap = sns.color_palette("vlag")

    # Analyze all indices vs. housing from 1992-2021
    # =============================================================
    nndf = util.normalize_columns(ndf, ndf.columns)
    corr = nndf.corr()

    print("----------------------------------------------------------------")
    print(" ====== Analyzing all indices vs. housing from 1992-2021 =======")
    print("----------------------------------------------------------------")
    print(" ")
    print("Correlation of Indices to Home Values:")
    print(corr)

    mask = np.tril(np.ones_like(corr, dtype=bool))
    util.generate_heatmap(mask, cmap, corr)

    # Analyze all indices vs. housing from 1992-2021
    util.generate_ts_plot(
        nndf,
        SPCS_BUBBLE_BEGIN,
        SPCS_BUBBLE_END,
        "Normalized Values",
        "Stock Market Indicies and the Housing Bubble " "(1992.02.01-2021.02.01)",
    )

    # Analyze all indices vs. housing from 1992-1997
    # =============================================================
    pre_bubble_df = ndf.loc[:SPCS_BUBBLE_BEGIN]
    corr = pre_bubble_df.corr()

    print(" ")
    print("----------------------------------------------------------------")
    print(" ====== Analyzing all indices vs. housing from 1992-1997 =======")
    print("----------------------------------------------------------------")
    print(" ")
    print("Correlation of Indices to Home Values pre-bubble:")
    print(" ")
    print(corr)
    print(" ")

    mask = np.tril(np.ones_like(corr, dtype=bool))
    util.generate_heatmap(mask, cmap, corr)

    util.generate_ts_plot(
        pre_bubble_df,
        None,
        None,
        "Normalized Values",
        "Pre-Bubble Stock Market Indicies vs. Case Shiller "
        "10 City (1992.02.01-1997.08.01)",
    )

    # Analyze all indices vs. housing from 1997-2009
    bubble_df = ndf.loc[SPCS_BUBBLE_BEGIN:SPCS_BUBBLE_END]
    corr = bubble_df.corr()

    print(" ")
    print("----------------------------------------------------------------")
    print(" ====== Analyzing all indices vs. housing from 1997-2009 =======")
    print("----------------------------------------------------------------")
    print(" ")
    print("Correlation of Indices to Home Values during bubble:")
    print(" ")
    print(corr)

    mask = np.tril(np.ones_like(corr, dtype=bool))
    util.generate_heatmap(mask, cmap, corr)

    util.generate_ts_plot(
        bubble_df,
        None,
        None,
        "Normalized Values",
        "Bubble Stock Market Indicies vs. Case Shiller 10 "
        "City (1997.08.01-2009.01.01)",
    )

    # Analyze all indices vs. housing from 2009-2021
    post_bubble_df = ndf.loc[SPCS_BUBBLE_END:]
    corr = post_bubble_df.corr()

    print(" ")
    print("----------------------------------------------------------------")
    print(" ====== Analyzing all indices vs. housing from 2009-2021 =======")
    print("----------------------------------------------------------------")
    print(" ")
    print("Correlation of Indices to Home Values during bubble:")
    print(" ")
    print(corr)

    mask = np.tril(np.ones_like(corr, dtype=bool))
    util.generate_heatmap(mask, cmap, corr)

    util.generate_ts_plot(
        post_bubble_df,
        None,
        None,
        "Normalized Values",
        "Post-Bubble Stock Market Indicies vs. Case Shiller "
        "10 City (2009.01.01-2021.01.01)",
    )

    # Scatterplots ...
    # Scatterplot Nasdaq vs. Case Shiller 1992-2021
    util.generate_norm_scatterplot(
        ndf,
        "IXIC_ADJCLOSE",
        "SPCS10RSA",
        "Nasdaq Close",
        "Case Shiller 10 City Composite (Index)",
        "Nasdaq vs. Case Shiller 10 City "
        "Composite (normalized - 1992.02.01-2021.01.01)",
    )

    # Scatterplot S&P500 vs. Case Shiller 1992-2021
    util.generate_norm_scatterplot(
        ndf,
        "GSPC_ADJCLOSE",
        "SPCS10RSA",
        "S&P500 Close",
        "Case Shiller 10 City Composite (Index)",
        "S&P500 vs. Case Shiller 10 City "
        "Composite (normalized - 1992.02.01-2021.01.01)",
    )

    # Scatterplot DJII vs. Case Shiller 1992-2021
    util.generate_norm_scatterplot(
        ndf,
        "DJI_ADJCLOSE",
        "SPCS10RSA",
        "DJII Close",
        "Case Shiller 10 City Composite (Index)",
        "DJII vs. Case Shiller 10 City "
        "Composite (normalized - 1992.02.01-2021.01.01)",
    )


if __name__ == "__main__":
    main()
