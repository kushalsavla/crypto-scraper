# Cryptocurrency Data Scraper

This project is a Streamlit web application that allows users to scrape and visualize cryptocurrency data using the CoinGecko API. Users can select from a dropdown of available cryptocurrencies ordered by trading volume and view a candlestick chart of the selected coin's historical price data.

## Project Structure

```
crypto-scraper
├── src
│   ├── app.py            # Main entry point of the Streamlit application
│   ├── data_fetcher.py   # Functions to interact with the CoinGecko API
│   ├── chart_plotter.py  # Functions to create candlestick charts
│   └── utils.py          # Utility functions for data formatting and error handling
├── requirements.txt      # List of dependencies
└── README.md             # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd crypto-scraper
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the Streamlit application:
   ```
   streamlit run src/app.py
   ```

## Features

- Dropdown menu to select from a list of cryptocurrencies ordered by trading volume.
- Display of a candlestick chart for the selected cryptocurrency.
- Options for different time intervals: 1m, 5m, 15m, 30m, 45m, 1h, 4h, 8h, 1d, 7d, 15d, 1M, 6M, 1y.

## Usage Guidelines

- After running the application, select a cryptocurrency from the dropdown.
- Choose the desired time interval for the candlestick chart.
- The chart will update to reflect the selected cryptocurrency's historical price data.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.