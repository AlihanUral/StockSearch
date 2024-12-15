# StockSearch
This project is a web application that allows users to search for stock prices and view historical price charts. By entering a stock symbol (e.g., AAPL for Apple), the app fetches real-time stock information and displays a chart of the stock’s price over the past 6 months.

Features:
	•	Search for stock symbols and view real-time price data.
	•	Display a historical price chart for the selected stock (last 6 months).
	•	User-friendly interface built with Bootstrap.

Technologies Used:
	•	Flask: A lightweight Python web framework for building web applications.
	•	yfinance: A Python library for fetching financial data, such as stock prices.
	•	Matplotlib: A plotting library for creating static, animated, and interactive visualizations in Python.
	•	HTML/CSS: For building the front-end of the application, styled with Bootstrap.

How It Works:
	1.	The user inputs a stock symbol into the search bar (e.g., AAPL, TSLA, GOOG).
	2.	The app fetches the stock information using the yfinance library.
	3.	The current price and a 6-month historical price chart are displayed to the user.
	4.	If an invalid symbol is entered, an error message is shown.
