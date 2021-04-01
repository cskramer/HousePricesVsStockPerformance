import pandas as pd
import load_fred_data
import load_index_data
import util

def main():
    
    # Pull in normalized market data
    nasdaq_frame, sp500_frame, djii_frame = load_index_data.get_index_data()
    
    nasdaq_frame = nasdaq_frame.rename(columns={"Date": "DATE"})    
    nasdaq_frame.DATE = pd.to_datetime(nasdaq_frame.DATE)
    
    sp500_frame = sp500_frame.rename(columns={"Date": "DATE"})    
    sp500_frame.DATE = pd.to_datetime(nasdaq_frame.DATE)
    
    djii_frame =  djii_frame.rename(columns={"Date": "DATE"})    
    djii_frame.DATE = pd.to_datetime(nasdaq_frame.DATE)
    
    # Retrieve and process case_shiller data
    case_shiller_10_city_frame = load_fred_data.get_fred_data()
    
    case_shiller_10_city_frame.DATE = pd.to_datetime(case_shiller_10_city_frame.DATE)
    
    util.generate_scatterplot("NASDAQ", nasdaq_frame, case_shiller_10_city_frame)
    util.generate_scatterplot("SP500", sp500_frame, case_shiller_10_city_frame)
    util.generate_scatterplot("Dow Jones Industrial Average", djii_frame, case_shiller_10_city_frame)

if __name__ == "__main__":
    main()
