Project 2
	W200 - Spring 2021

-------------------------------------------------
Problem: 
	Determine the correlation between US stock indices (DJII, Nasdaq, S&P500) to Unites States Housing Data (Standard and Poors)

-------------------------------------------------
Instructions:

	There are parts to this project
	   1. Data retrieval
		  
		  To run: "python source/retrive_data/main.py"
		  
		  Results: 
			 * Fetches and normalizes housing data (Standard and Poors), and 3 US Indices (SP500, DJII, Nasdaq) for the date range of 1992-02-01 (DJII begin date) to 
		   2021-01-01
			 * Store the data above in an SQLite Flat File

	   2. Data analysis

		  To run: "python source/analyze_data/main.py"

		  Results:
			 Generates the following output:
				(Exploratory Phase)
				
					1992.02.01 - 2021.01.01
						text-based Correlation analysis
						Correlation heatmap
						Line Graph for all indices vs Case Shiller Data
					
				(Explanatory Phase)
					Pre-Bubble (1992.02.01 - 1997.08.01)
						text-based Correlation analysis
						Correlation heatmap
						Line Graph for all indices vs Case Shiller Data
						Scatterplot for each index vs housing data
					
					During-Bubble (1997.08.01 - 2009.01.01)
						text-based Correlation analysis
						Correlation heatmap
						Line Graph for all indices vs Case Shiller Data
						Scatterplot for each index vs housing data
						
					After-Bubble (2009.01.01 - 2021.01.01)
						text-based Correlation analysis
						Correlation heatmap
						Line Graph for all indices vs Case Shiller Data
						Scatterplot for each index vs housing data
