# -*- coding: utf-8 -*-
"""
getUSStockIndexHistory.py - Uses yFinance to download US 
        index data at 1m intervals

Created on Tue Mar 30 22:49:59 2021

@author: Shane Kramer, Ted Brown

"""

import yfinance as yf

"""
-----------------------------
 Composite ticker information
-----------------------------
 DJII = ^DJI
 S&P 500 = ^GSPC
 Nasdaq = ^IXIC
"""

# Download DJII data at 1m intervals
djii1m_df = yf.download("^DJI", start="1987-01-01", end="2020-01-01", 
                        interval="1mo")
djii1m_df.to_csv('djii_1m.csv')

# Download S&P500 data at 1m intervals
sp5001m_df = yf.download("^GSPC", start="1987-01-01", end="2020-01-01", 
                         interval="1mo")
sp5001m_df.to_csv('sp500_1m.csv')

# Download Nasdaq data at 1m intervals
nd1m_df = yf.download("^IXIC", start="1987-01-01", end="2020-01-01", 
                      interval="1mo")
nd1m_df.to_csv('nasdaq_1m.csv')