# -*- coding: utf-8 -*-
"""
Gets index data (Nasdaq, S&P500, DJII) csv files for analysis

Created on Wed Mar 31 18:56:57 2021

@authors: Shane Kramer and Ted Brown
"""
import util
import os 


''' A function used to load index csv data into dataframes
        Out:
            dataframe
'''
def get_index_data():
    # INDEX HISTORY FILES
    market_data = "index_data\yahooApi"
        
    nasdaq_file = os.path.join(market_data, "nasdaq_1m.csv")
    sp500_file = os.path.join(market_data, "sp500_1m.csv")
    djii_file = os.path.join(market_data, "djii_1m.csv")

    # Load 3 index history files into dataframes
    df_nasdaq = util.load_data(nasdaq_file)
    df_sp500 = util.load_data(sp500_file)
    df_djii = util.load_data(djii_file)

    # Get rid of unecessary rows (leaving volume for now)
    df_nasdaq = df_nasdaq.drop(['Open', 'High', 'Low', 'Close'], axis=1)
        
    df_sp500 = df_sp500.drop(['Open', 'High', 'Low', 'Close'], axis=1)
        
    df_djii = df_djii.drop(['Open', 'High', 'Low', 'Close'], axis=1)
    
    return df_nasdaq, df_sp500, df_djii


''' A function used to load index csv data into normalized dataframes
        Out:
            normalized dataframe
'''
def get_normalized_index_data():
    df_nasdaq, df_sp500, df_djii = get_index_data()
    
    df_nasdaq_norm = util.normalize_dataframe(df_nasdaq, "Adj Close")
    df_sp500_norm = util.normalize_dataframe(df_sp500, "Adj Close")
    df_djii_norm = util.normalize_dataframe(df_djii, "Adj Close")
    
    return df_nasdaq_norm, df_sp500_norm, df_djii_norm