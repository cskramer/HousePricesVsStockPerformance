# -*- coding: utf-8 -*-
"""
Util methods for project 2

Created on Wed Mar 31 20:20:10 2021

@authors: Shane Kramer and Ted Brown
"""

import pandas as pd
import numpy as np
import seaborn as sns
import yfinance as yf
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler


def load_data(file_name):
    """ A function used to load csv data into dataframes
            In:
                filename (relative path)
            Out:
                dataframe
    """
    df = pd.read_csv(file_name, encoding="utf8")
    return df


def normalize_dataframe(data_frame, column):
    """ A function used to normalize index prices
            In:
                dataframe
            Out:
                normalized dataframe
    """
    df_sklearn = data_frame.copy()
    df_sklearn[column] = MinMaxScaler().fit_transform(
        np.array(df_sklearn[column]).reshape(-1, 1)
    )
    return df_sklearn


def generate_scatterplot(index_name, index_frame, housing_frame):
    """ A function used to generate a scatterplot for housing prices/index data
            In:
                indexName
                indexFrame
                housingFrame
            Out:
                plot
    """
    plotting_data = pd.merge(
        index_frame[["DATE", "Adj Close"]],
        housing_frame[["DATE", "SPCS10RSA"]],
        how="outer",
        on="DATE",
    )

    scatter_chart = plt.figure(figsize=(5, 5))
    ax_scat = scatter_chart.add_subplot(1, 1, 1)

    ax_scat.set_title(index_name + " Close vs. Case Shiller 10 City Composite")
    ax_scat.set_xlabel(index_name + " NASDAQ Close ($)")
    ax_scat.set_ylabel("Case Shiller 10 City Composite (Index)")
    plotting_data = plotting_data.sort_values("SPCS10RSA", ascending=True)
    plt.scatter(plotting_data["Adj Close"], plotting_data["SPCS10RSA"])
    plt.show()

    sns.set_theme(color_codes=True)
    sns.regplot(plotting_data["Adj Close"], plotting_data["SPCS10RSA"])


def getIndexCSVs():
    """
        A function to retrieve montly (period) csv for US Stock indices
            Out:
                csv for each of the three major US indices

        -----------------------------
        Composite ticker information
        -----------------------------
        DJII = ^DJI
        S&P 500 = ^GSPC
        Nasdaq = ^IXIC
    """
    # Download DJII data at 1m intervals
    djii1m_df = yf.download(
        "^DJI", start="1987-01-01", end="2020-01-01", interval="1mo"
    )
    djii1m_df.to_csv("djii_1m.csv")

    # Download S&P500 data at 1m intervals
    sp5001m_df = yf.download(
        "^GSPC", start="1987-01-01", end="2020-01-01", interval="1mo"
    )
    sp5001m_df.to_csv("sp500_1m.csv")

    # Download Nasdaq data at 1m intervals
    nd1m_df = yf.download("^IXIC", start="1987-01-01", end="2020-01-01", interval="1mo")
    nd1m_df.to_csv("nasdaq_1m.csv")
