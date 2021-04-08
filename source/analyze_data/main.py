# -*- coding: utf-8 -*-
"""
Project 2 Main Method

Created on Wed Mar 31 18:56:57 2021

@authors: Shane Kramer and Ted Brown
"""

import pandas as pd
import load_fred_data
import load_index_data
import util

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
    
    nasdaq_frame_norm = util.normalize_dataframe(nasdaq_frame, 'Adj Close')
    case_shiller_norm = util.normalize_dataframe(case_shiller_10_city_frame, 'SPCS10RSA')
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
    corr = ndf.corr()
    
    SPCS10RSA_BEGIN_DATE = "1987-01-01"
    DJII_BEGIN_DATE = "1992-02-01"
    END_DATE = "2021-01-01"
    SPCS_BUBBLE_BEGIN = "1997-08-01"
    SPCS_BUBBLE_END = "2009-01-01"
    
    pre_bubble_df = ndf.loc[:SPCS_BUBBLE_BEGIN]
    bubble_df = ndf.loc[SPCS_BUBBLE_BEGIN:SPCS_BUBBLE_END]
    post_bubble_df = ndf.loc[SPCS_BUBBLE_END:]
    
    # slicing on an index 
    # mask = np.tril(np.ones_like(corr, dtype=bool))
    # cmap = sns.color_palette("Blues", as_cmap=True)
    # util.generate_heatmap(mask, cmap, corr)
    
    #util.generate_scatterplot("NASDAQ", nasdaq_frame, case_shiller_10_city_frame)
    #util.generate_scatterplot("SP500", sp500_frame, case_shiller_10_city_frame)
    #util.generate_scatterplot("DJIA", djii_frame, case_shiller_10_city_frame)
    
    #util.generate_lineplot("NASDAQ", nasdaq_frame_norm, case_shiller_norm)


if __name__ == "__main__":
    main()
