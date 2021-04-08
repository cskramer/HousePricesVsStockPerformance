# Great place for junk that I'm not quite sure I want to get rid of

import pandas as pd

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
+# R Values and Rule of Thumb Meanings
+# 0.00-0.19: very weak
+# 0.20-0.39: weak
+# 0.40-0.59: moderate
+# 0.60-0.79: strong
+# 0.80-1.00: very strong.