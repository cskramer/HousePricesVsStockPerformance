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


def normalize_columns(df, cols):
    """
    Min Max normalize a pandas data frame column in place
    :param df: incoming dataframe with column to be normalized
    :type df: pandas dataframe
    :param cols: list of columns to be renamed
    :type cols: list of column names
    :return: copy of the dataframe with the normalized column
    :rtype: pandas dataframe
    """
    # normalized_df=(df-df.min())/(df.max()-df.min())
    # normalized_df=(df-df.mean())/df.std()
    ldf = df.copy()
    for col_name in cols:
        ldf.loc[:, (col_name)] = (ldf[col_name] - ldf[col_name].min()) / (
            ldf[col_name].max() - ldf[col_name].min()
        )
    return ldf


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


def generate_ts_plot(
    df,
    beg_line,
    end_line,
    p_ylabel,
    p_title,
    legend_loc="lower right",
    yaxis_scale="linear",
):
    """ A function used to generate a scatterplot for housing prices/index data
            In:
                dataframe
                beg_line - Marker for beginning of period of interest
                end_line - Marker for end of period of interest
                ylabel
                title
                                
            Out:
                plot
    """

    df_plot = df.plot(figsize=(8, 5))

    if beg_line is not None:
        df_plot.axvline(x=beg_line)
    if end_line is not None:
        df_plot.axvline(x=end_line)

    df_plot.set_title(p_title)
    df_plot.set_ylabel(p_ylabel)
    df_plot.set_yscale(yaxis_scale)
    df_plot.legend(loc=legend_loc)
    return df_plot.get_figure()


def generate_norm_scatterplot(df, ycol_name, xcol_name, p_xlabel, p_ylabel, p_title):
    """ A function used to generate a scatterplot for housing prices/index data
            In:
                dataframe
                ycol_name
                xcol_name
                xlabel
                ylabel
                title
                                
            Out:
                plot
    """
    f, ax = plt.subplots(figsize=(7, 5))
    #   #sns.set_theme(color_codes=True)
    ax_sb_scat = sns.regplot(df[ycol_name], df[xcol_name], ax=ax)
    ax_sb_scat.set(xlabel=p_xlabel, ylabel=p_ylabel)
    ax_sb_scat.set(title=p_title)
    ax_sb_scat.set(xlim=(0, 1.0))
    ax_sb_scat.set(ylim=(0, 1.0))
    return f


def generate_lineplot(indexName, indexFrame, housingFrame):
    """ A function to generate line plots for normalized housing prices/index data
        # https://stackoverflow.com/questions/43941245/line-plot-with-data-points-in-pandas
        In:
            indexName
            indexFrame
            housingFrame 
        Out:
            plot
    """
    plotting_data = pd.merge(
        indexFrame[["DATE", "Adj Close"]],
        housingFrame[["DATE", "SPCS10RSA"]],
        how="outer",
        on="DATE",
    )

    print(plotting_data)
    df = plotting_data, index = pd.date_range(
        "1/1/1987", len(plotting_data), columns=list("AB")
    )

    lines = df.plot.line(
        linestyle="-", markevery=100, marker="*", markerfacecolor="black"
    )

    # show legend
    # plt.legend()

    # show graph
    # plt.show()


def generate_heatmap(mask, cmap, corr, title):
    """ A function to generate a heatmap of housing and index
        data correlation values
        In:
            mask
            cmap
        Out:
            heatmap plot
    """

    f, ax = plt.subplots(figsize=(8, 8))  # Enlarge to show missing parts of graph
    ax.set_yticks(
        ax.get_yticks().tolist()
    )  # Shut-up a UserWarning from set_yticklabels
    ax.set_yticklabels(labels=ax.get_yticklabels(), va="center")
    ax.set_title(title)
    sns.heatmap(
        corr,
        cmap=cmap,
        square=True,
        linewidths=0.3,
        linecolor="grey",
        cbar=False,
        annot=True,
        annot_kws={"size": 16},
        ax=ax,
        mask=mask,
    )
    return f


def load_all_data_from_sql():
    """
    open the sqlite database created from create_db.py and load it into a dataframe. This represents the raw
    data as it was downloaded.

    :return: copy of a single pandas dataframe with all information for this project indexed and sorted by date
    :rtype: pandas dataframe
    """
    script_dir = os.path.dirname(os.path.realpath(__file__))
    DB_DIR = os.path.abspath(os.path.join(script_dir, "..", "..", "data", "db"))
    DB_NAME = "alldata.db"
    con = sqlite3.connect(os.path.join(DB_DIR, DB_NAME))
    df = pd.read_sql(
        "SELECT * from all_data",
        con,
        parse_dates={"DATE", "%Y-%m-%d"},
        index_col="DATE",
    )

    return df.copy()
