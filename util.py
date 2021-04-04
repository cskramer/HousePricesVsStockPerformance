# -*- coding: utf-8 -*-
"""
Util methods for project 2

Created on Wed Mar 31 20:20:10 2021

@authors: Shane Kramer and Ted Brown
"""
import os
import sqlite3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
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


def load_all_data_from_sql():
    """
    open the sqlite database created from create_db.py and load it into a dataframe. This represents the raw
    data as it was downloaded.
    
    :return: copy of a single pandas dataframe with all information for this project indexed and sorted by date
    :rtype: pandas dataframe
    """
    DB_DIR = "db"
    DB_NAME = "alldata.db"
    con = sqlite3.connect(os.path.join(DB_DIR, DB_NAME))
    df = pd.read_sql(
        "SELECT * from all_data",
        con,
        parse_dates={"DATE", "%Y-%m-%d"},
        index_col="DATE",
    )

    return df.copy()
