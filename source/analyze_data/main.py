# -*- coding: utf-8 -*-
"""
Project 2 Main Method

Created on Wed Mar 31 18:56:57 2021

@authors: Shane Kramer and Ted Brown
"""
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

import util


def load_normalized_data():
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
    script_dir = os.path.dirname(os.path.realpath(__file__))
    output_dir = os.path.abspath(os.path.join(script_dir, "..", "..", "output"))

    raw_df = util.load_all_data_from_sql()
    ndf = load_normalized_data()

    SPCS_BUBBLE_BEGIN = "1997-08-01"
    SPCS_BUBBLE_END = "2009-01-01"

    cmap = sns.color_palette("vlag")

    # Analyze all indices vs. housing from 1992-2021
    # =============================================================
    nndf = util.normalize_columns(ndf, ndf.columns)
    corr = nndf.corr()

    correlation_data_fname = os.path.join(output_dir, "AllCorrelationData.csv")
    heat_map_fname = os.path.join(output_dir, "AllCorrelationHeatmap.png")
    ts_fname = os.path.join(output_dir, "AllDataNormalizedLineGraph.png")

    print("----------------------------------------------------------------")
    print(" ====== Analyzing all indices vs. housing from 1992-2021 =======")
    print("----------------------------------------------------------------")
    print(" ")
    print("Correlation of Indices to Home Values:")
    print(corr)
    print(" ")
    corr.to_csv(
        correlation_data_fname, header=True, encoding="utf-8", line_terminator="\n"
    )

    mask = np.tril(np.ones_like(corr, dtype=bool))
    heat_fig = util.generate_heatmap(
        mask,
        cmap,
        corr,
        "Correlations For Stock Market Indicies and Case Shiller Index\n(1992.02.01-2021.02.01)",
    )
    heat_fig.savefig(heat_map_fname, format="png")

    # Analyze all indices vs. housing from 1992-2021
    ts_fig = util.generate_ts_plot(
        nndf,
        SPCS_BUBBLE_BEGIN,
        SPCS_BUBBLE_END,
        "Normalized Values",
        "Stock Market Indicies and the Housing Bubble " "(1992.02.01-2021.02.01)",
    )
    ts_fig.savefig(ts_fname, format="png")

    # Analyze all indices vs. housing from 1992-1997
    # =============================================================
    pre_bubble_df = ndf.loc[:SPCS_BUBBLE_BEGIN]
    corr = pre_bubble_df.corr()

    correlation_data_fname = os.path.join(output_dir, "PreBubbleCorrelationData.csv")
    heat_map_fname = os.path.join(output_dir, "PreBubbleCorrelationHeatmap.png")
    ts_fname = os.path.join(output_dir, "PreBubbleNormalizedLineGraph.png")

    print(" ")
    print("----------------------------------------------------------------")
    print(" ====== Analyzing all indices vs. housing from 1992-1997 =======")
    print("----------------------------------------------------------------")
    print(" ")
    print("Correlation of Indices to Home Values pre-bubble:")
    print(" ")
    print(corr)
    print(" ")
    corr.to_csv(
        correlation_data_fname, header=True, encoding="utf-8", line_terminator="\n"
    )

    mask = np.tril(np.ones_like(corr, dtype=bool))
    heat_fig = util.generate_heatmap(
        mask,
        cmap,
        corr,
        "Pre-Bubble Correlations For Stock Market Indicies and Case Shiller Index",
    )
    heat_fig.savefig(heat_map_fname, format="png")

    ts_fig = util.generate_ts_plot(
        pre_bubble_df,
        None,
        None,
        "Normalized Values",
        "Pre-Bubble Stock Market Indicies vs. Case Shiller "
        "10 City (1992.02.01-1997.08.01)",
        legend_loc="upper left",
    )
    ts_fig.savefig(ts_fname, format="png")

    # Analyze all indices vs. housing from 1997-2009
    bubble_df = ndf.loc[SPCS_BUBBLE_BEGIN:SPCS_BUBBLE_END]
    corr = bubble_df.corr()

    correlation_data_fname = os.path.join(output_dir, "DuringBubbleCorrelationData.csv")
    heat_map_fname = os.path.join(output_dir, "DuringBubbleCorrelationHeatmap.png")
    ts_fname = os.path.join(output_dir, "DuringBubbleNormalizedLineGraph.png")

    print(" ")
    print("----------------------------------------------------------------")
    print(" ====== Analyzing all indices vs. housing from 1997-2009 =======")
    print("----------------------------------------------------------------")
    print(" ")
    print("Correlation of Indices to Home Values during bubble:")
    print(" ")
    print(corr)
    print(" ")
    corr.to_csv(
        correlation_data_fname, header=True, encoding="utf-8", line_terminator="\n"
    )

    mask = np.tril(np.ones_like(corr, dtype=bool))
    heat_fig = util.generate_heatmap(
        mask,
        cmap,
        corr,
        "Bubble Correlations For Stock Market Indicies and Case Shiller Index",
    )
    heat_fig.savefig(heat_map_fname, format="png")

    ts_fig = util.generate_ts_plot(
        bubble_df,
        None,
        None,
        "Normalized Values",
        "Bubble Stock Market Indicies vs. Case Shiller 10 "
        "City (1997.08.01-2009.01.01)",
        legend_loc="upper left",
    )
    ts_fig.savefig(ts_fname, format="png")

    # Analyze all indices vs. housing from 2009-2021
    post_bubble_df = ndf.loc[SPCS_BUBBLE_END:]
    corr = post_bubble_df.corr()

    correlation_data_fname = os.path.join(output_dir, "PostBubbleCorrelationData.csv")
    heat_map_fname = os.path.join(output_dir, "PostBubbleCorrelationHeatmap.png")
    ts_fname = os.path.join(output_dir, "PostBubbleNormalizedLineGraph.png")

    print(" ")
    print("----------------------------------------------------------------")
    print(" ====== Analyzing all indices vs. housing from 2009-2021 =======")
    print("----------------------------------------------------------------")
    print(" ")
    print("Correlation of Indices to Home Values during bubble:")
    print(" ")
    print(corr)
    print(" ")
    corr.to_csv(
        correlation_data_fname, header=True, encoding="utf-8", line_terminator="\n"
    )

    mask = np.tril(np.ones_like(corr, dtype=bool))
    heat_fig = util.generate_heatmap(
        mask,
        cmap,
        corr,
        "Post-Bubble Correlations For Stock Market Indicies and Case Shiller Index",
    )
    heat_fig.savefig(heat_map_fname, format="png")

    ts_fig = util.generate_ts_plot(
        post_bubble_df,
        None,
        None,
        "Normalized Values",
        "Post-Bubble Stock Market Indicies vs. Case Shiller "
        "10 City (2009.01.01-2021.01.01)",
    )
    ts_fig.savefig(ts_fname, format="png")

    # Scatterplots ...
    # ################       Scatterplot Nasdaq vs. Case Shiller 1992-2021          ################
    scat_plot_fname = os.path.join(output_dir, "NasdaqVsCaseShillerScatterplot.png")
    scat_fig = util.generate_norm_scatterplot(
        ndf,
        "IXIC_ADJCLOSE",
        "SPCS10RSA",
        "Nasdaq Close",
        "Case Shiller 10 City Composite (Index)",
        "Nasdaq vs. Case Shiller 10 City "
        "Composite (normalized - 1992.02.01-2021.01.01)",
    )
    scat_fig.savefig(scat_plot_fname, format="png")

    # Scatterplot S&P500 vs. Case Shiller 1992-2021
    scat_plot_fname = os.path.join(output_dir, "SP500VsCaseShillerScatterplot.png")
    scat_fig = util.generate_norm_scatterplot(
        ndf,
        "GSPC_ADJCLOSE",
        "SPCS10RSA",
        "S&P500 Close",
        "Case Shiller 10 City Composite (Index)",
        "S&P500 vs. Case Shiller 10 City "
        "Composite (normalized - 1992.02.01-2021.01.01)",
    )
    scat_fig.savefig(scat_plot_fname, format="png")

    # Scatterplot DJII vs. Case Shiller 1992-2021
    scat_plot_fname = os.path.join(output_dir, "DJIIVsCaseShillerScatterplot.png")
    scat_fig = util.generate_norm_scatterplot(
        ndf,
        "DJI_ADJCLOSE",
        "SPCS10RSA",
        "DJII Close",
        "Case Shiller 10 City Composite (Index)",
        "DJII vs. Case Shiller 10 City "
        "Composite (normalized - 1992.02.01-2021.01.01)",
    )
    scat_fig.savefig(scat_plot_fname, format="png")

    # ################       Scatterplot Nasdaq vs. Case Shiller Pre-Bubble          ################
    scat_plot_fname = os.path.join(
        output_dir, "NasdaqVsCaseShillerScatterplot_PreBubble.png"
    )
    pre_bubble_normalized = util.normalize_columns(
        raw_df.loc[:SPCS_BUBBLE_BEGIN], raw_df.columns
    )
    scat_fig = util.generate_norm_scatterplot(
        pre_bubble_normalized,
        "IXIC_ADJCLOSE",
        "SPCS10RSA",
        "Nasdaq Close",
        "Case Shiller 10 City Composite (Index)",
        "Nasdaq vs. Case Shiller 10 City "
        "Composite (normalized - Before Housing Bubble)",
    )
    scat_fig.savefig(scat_plot_fname, format="png")

    # Scatterplot S&P500 vs. Case Shiller 1992-2021
    scat_plot_fname = os.path.join(
        output_dir, "SP500VsCaseShillerScatterplot_PreBubble.png"
    )
    scat_fig = util.generate_norm_scatterplot(
        pre_bubble_normalized,
        "GSPC_ADJCLOSE",
        "SPCS10RSA",
        "S&P500 Close",
        "Case Shiller 10 City Composite (Index)",
        "S&P500 vs. Case Shiller 10 City "
        "Composite (normalized - Before Housing Bubble)",
    )
    scat_fig.savefig(scat_plot_fname, format="png")

    # Scatterplot DJII vs. Case Shiller 1992-2021
    scat_plot_fname = os.path.join(
        output_dir, "DJIIVsCaseShillerScatterplot_Bubble.png"
    )
    scat_fig = util.generate_norm_scatterplot(
        pre_bubble_normalized,
        "DJI_ADJCLOSE",
        "SPCS10RSA",
        "DJII Close",
        "Case Shiller 10 City Composite (Index)",
        "DJII vs. Case Shiller 10 City "
        "Composite (normalized - During Housing Bubble)",
    )
    scat_fig.savefig(scat_plot_fname, format="png")

    # ################       Scatterplot Nasdaq vs. Case Shiller Bubble          ################
    scat_plot_fname = os.path.join(
        output_dir, "NasdaqVsCaseShillerScatterplot_Bubble.png"
    )
    bubble_normalized = util.normalize_columns(
        raw_df.loc[SPCS_BUBBLE_BEGIN:SPCS_BUBBLE_END], raw_df.columns
    )
    scat_fig = util.generate_norm_scatterplot(
        bubble_normalized,
        "IXIC_ADJCLOSE",
        "SPCS10RSA",
        "Nasdaq Close",
        "Case Shiller 10 City Composite (Index)",
        "Nasdaq vs. Case Shiller 10 City "
        "Composite (normalized - During Housing Bubble)",
    )
    scat_fig.savefig(scat_plot_fname, format="png")

    # Scatterplot S&P500 vs. Case Shiller 1992-2021
    scat_plot_fname = os.path.join(
        output_dir, "SP500VsCaseShillerScatterplot_Bubble.png"
    )
    scat_fig = util.generate_norm_scatterplot(
        bubble_normalized,
        "GSPC_ADJCLOSE",
        "SPCS10RSA",
        "S&P500 Close",
        "Case Shiller 10 City Composite (Index)",
        "S&P500 vs. Case Shiller 10 City "
        "Composite (normalized - During Housing Bubble)",
    )
    scat_fig.savefig(scat_plot_fname, format="png")

    # Scatterplot DJII vs. Case Shiller 1992-2021
    scat_plot_fname = os.path.join(
        output_dir, "DJIIVsCaseShillerScatterplot_Bubble.png"
    )
    scat_fig = util.generate_norm_scatterplot(
        bubble_normalized,
        "DJI_ADJCLOSE",
        "SPCS10RSA",
        "DJII Close",
        "Case Shiller 10 City Composite (Index)",
        "DJII vs. Case Shiller 10 City "
        "Composite (normalized - During Housing Bubble)",
    )
    scat_fig.savefig(scat_plot_fname, format="png")

    # ################       Scatterplot Nasdaq vs. Case Shiller PostBubble          ################
    scat_plot_fname = os.path.join(
        output_dir, "NasdaqVsCaseShillerScatterplot_PostBubble.png"
    )
    post_bubble_normalized = util.normalize_columns(
        raw_df.loc[SPCS_BUBBLE_END:], raw_df.columns
    )
    scat_fig = util.generate_norm_scatterplot(
        post_bubble_normalized,
        "IXIC_ADJCLOSE",
        "SPCS10RSA",
        "Nasdaq Close",
        "Case Shiller 10 City Composite (Index)",
        "Nasdaq vs. Case Shiller 10 City "
        "Composite (normalized - After Housing Bubble)",
    )
    scat_fig.savefig(scat_plot_fname, format="png")

    # Scatterplot S&P500 vs. Case Shiller 1992-2021
    scat_plot_fname = os.path.join(
        output_dir, "SP500VsCaseShillerScatterplot_PostBubble.png"
    )
    scat_fig = util.generate_norm_scatterplot(
        post_bubble_normalized,
        "GSPC_ADJCLOSE",
        "SPCS10RSA",
        "S&P500 Close",
        "Case Shiller 10 City Composite (Index)",
        "S&P500 vs. Case Shiller 10 City "
        "Composite (normalized - After Housing Bubble)",
    )
    scat_fig.savefig(scat_plot_fname, format="png")

    # Scatterplot DJII vs. Case Shiller 1992-2021
    scat_plot_fname = os.path.join(
        output_dir, "DJIIVsCaseShillerScatterplot_PostBubble.png"
    )
    scat_fig = util.generate_norm_scatterplot(
        post_bubble_normalized,
        "DJI_ADJCLOSE",
        "SPCS10RSA",
        "DJII Close",
        "Case Shiller 10 City Composite (Index)",
        "DJII vs. Case Shiller 10 City "
        "Composite (normalized - After Housing Bubble)",
    )
    scat_fig.savefig(scat_plot_fname, format="png")


if __name__ == "__main__":
    main()
