# -*- coding: utf-8 -*-
"""
Gets housing (Fred) csv files for analysis

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

    #nasdaq_frame.DATE = pd.to_datetime(nasdaq_frame.DATE)
    #case_shiller_10_city_frame.DATE = pd.to_datetime(case_shiller_10_city_frame.DATE)
    #plotting_data = pd.merge(
    #    nasdaq_frame[["DATE", "Close"]],
    #    case_shiller_10_city_frame[["DATE", "SPCS10RSA"]],
    #    how="outer",
    #    on="DATE",
    #)

    #scatter_chart = plt.figure(figsize=(5, 5))
    #ax_scat = scatter_chart.add_subplot(1, 1, 1)
    #ax_scat.set_title("NASDAQ Close vs. Case Shiller 10 City Composite")
    #ax_scat.set_xlabel("NASDAQ Close ($)")
    #ax_scat.set_ylabel("Case Shiller 10 City Composite (Index)")
    #plotting_data = plotting_data.sort_values("SPCS10RSA", ascending=True)
    #plt.scatter(plotting_data["Close"], plotting_data["SPCS10RSA"])
    #plt.show()

    #sns.set_theme(color_codes=True)
    #sns.regplot(plotting_data["Close"], plotting_data["SPCS10RSA"])

    return util.normalize_dataframe(case_shiller_10_city_frame, "SPCS10RSA")

