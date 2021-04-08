Project 2
	W200 - Spring 2021
	Ted Brown
	Shane Kramer

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
			 Generates the following graphs:
				(Exploratory Phase)
				Scatterplots for each of the 3 indexes against the housing data
				Line plot for each of the three indexes against housing data (normalized)
				R value heatmap for all 4 datasets
				
				(Explanatory Phase)
				Same set of graphs above, broken down by following date ranges:
					1992-02-01 - 1997-08-01
					1997-08-01 - 2009-01-01
					2009-01-01 - 2021-01-01
				
			Text-based summary
		