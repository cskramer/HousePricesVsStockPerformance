# -*- coding: utf-8 -*-
"""
Gets housing (Fred) csv files for analysis

Created on Wed Mar 31 18:56:57 2021

@authors: Shane Kramer and Ted Brown
"""

import os
import util


def get_norm_cse10_data():
    """
    Load Case Shiller 10 City Data from CSV File
    :return: normalized Pandas Dataframe
    """
    fred_dir = "fred_data"
    case_shiller_10_city_file = os.path.join(fred_dir, "SPCS10RSA.csv")
    case_shiller_10_city_frame = util.load_data(case_shiller_10_city_file)
    return util.normalize_dataframe(case_shiller_10_city_frame, "SPCS10RSA")
