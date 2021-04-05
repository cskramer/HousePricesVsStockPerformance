import os
import pandas as pd
import matplotlib.pyplot as plt
import util


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
    for col_name in cols:
        df[col_name] = (df[col_name] - df[col_name].min()) / (
            df[col_name].max() - df[col_name].min()
        )
    return df.copy()


def main():
    """
    Main Loop
    :return:
    :rtype:
    """

    df = util.load_all_data_from_sql()

    BEGIN_DATE = "1987-01-01"
    END_DATE = "2021-01-01"
    ndf = df[["IXIC_ADJCLOSE", "DJI_ADJCLOSE", "GSPC_ADJCLOSE", "SPCS10RSA"]].dropna()
    ndf = normalize_columns(ndf, ndf.columns)
    corr = ndf.corr()
    # mask = np.tril(np.ones_like(corr, dtype=bool))
    # cmap = sns.color_palette("Blues", as_cmap=True)
    # f, ax = plt.subplots(figsize=(15, 15))
    # sns.heatmap(corr, mask=mask, cmap=cmap, square=True, linewidths=0.5, cbar=False, annot=True)


if __name__ == "__main__":
    main()
