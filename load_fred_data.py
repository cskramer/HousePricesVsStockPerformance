# -*- coding: utf-8 -*-
"""
Gets housing (Fre) csv files for analysis

Created on Wed Mar 31 18:56:57 2021

@authors: Shane Kramer and Ted Brown
"""

import os
import pandas as pd
import util

def get_fred_data():
    fred_dir = "fred_data"
    cpi_file = os.path.join(fred_dir, "CPIAUCSL.csv")
    treasure_10_file = os.path.join(fred_dir, "DGS10.csv")
    recession_dates_file = os.path.join(fred_dir, "JHDUSRGDPBR.csv")
    mortgage_30_file = os.path.join(fred_dir, "MORTGAGE30US.csv")
    jumbo_mortgage_30_file = os.path.join(fred_dir, "OBMMIJUMBO30YF.csv")
    recession_prob_file = os.path.join(fred_dir, "RECPROUSM156N.csv")
    case_shiller_10_city_file = os.path.join(fred_dir, "SPCS10RSA.csv")
    consumer_sentiment_file = os.path.join(fred_dir, "UMCSENT.csv")
    home_ownership_rate_file = os.path.join(fred_dir, "RSAHORUSQ156S.csv")

    cpi_frame = util.load_data(cpi_file)
    treasury_10_frame = util.load_data(treasure_10_file)
    recession_dates_frame = util.load_data(recession_dates_file)
    mortgage_30_frame = util.load_data(mortgage_30_file)
    jumbo_mortgage_30_frame = util.load_data(jumbo_mortgage_30_file)
    recession_prob_frame = util.load_data(recession_prob_file)
    case_shiller_10_city_frame = util.load_data(case_shiller_10_city_file)
    consumer_sentiment_frame = util.load_data(consumer_sentiment_file)
    home_ownership_rate_frame = util.load_data(home_ownership_rate_file)

    complete_fred_data = pd.concat(
        [
            case_shiller_10_city_frame,
            home_ownership_rate_frame,
            cpi_frame,
            consumer_sentiment_frame,
            treasury_10_frame,
            mortgage_30_frame,
            jumbo_mortgage_30_frame,
            recession_prob_frame,
            recession_dates_frame,
        ],
        axis=0,
        join="outer",
        ignore_index=False,
        keys=None,
        levels=None,
        names=None,
    )

    return case_shiller_10_city_frame

