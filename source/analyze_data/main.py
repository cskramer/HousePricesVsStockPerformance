# -*- coding: utf-8 -*-
"""
Project 2 Main Method

Created on Wed Mar 31 18:56:57 2021

@authors: Shane Kramer and Ted Brown
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

import load_fred_data
import load_index_data
import util


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
