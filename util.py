# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 20:20:10 2021

@author: shane
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler 


''' A function used to load csv data into dataframes
        In:
            filename (relative path)
        Out:
            dataframe
'''
def load_data(file_name):
    df = pd.read_csv(file_name, encoding="utf8")
    return df


''' A function used to normalize index prices
        In:
            dataframe 
        Out:
            normalized dataframe
'''
def normalize_dataframe(data_frame, column):
    df_sklearn = data_frame.copy()
    df_sklearn[column] = MinMaxScaler().fit_transform(np.array(df_sklearn[column]).reshape(-1,1))
    return df_sklearn


''' A function used to generate a scatterplot for housing prices/index data
        In:
            indexName
            indexFrame
            housingFrame 
        Out:
            plot
'''
def generate_scatterplot(indexName, indexFrame, housingFrame):
    print("Hello")
    print(indexFrame)
    plotting_data = pd.merge(
        indexFrame[["DATE", "Adj Close"]],
        housingFrame[["DATE", "SPCS10RSA"]],
        how="outer",
        on="DATE",
    )
   
    scatter_chart = plt.figure(figsize=(5, 5))
    ax_scat = scatter_chart.add_subplot(1, 1, 1)
    
    ax_scat.set_title(indexName + " Close vs. Case Shiller 10 City Composite")
    ax_scat.set_xlabel(indexName + " NASDAQ Close ($)")
    ax_scat.set_ylabel("Case Shiller 10 City Composite (Index)")
    plotting_data = plotting_data.sort_values("SPCS10RSA", ascending=True)
    plt.scatter(plotting_data["Adj Close"], plotting_data["SPCS10RSA"])
    plt.show()
    
    sns.set_theme(color_codes=True)
    sns.regplot(plotting_data["Adj Close"], plotting_data["SPCS10RSA"])

