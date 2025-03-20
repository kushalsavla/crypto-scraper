import streamlit as st
from data_fetcher import fetch_coins, fetch_market_data, fetch_description, chart_data
from chart_plotter import plot_chart
import pandas as pd
import pycoingecko as pcg
from datetime import datetime, timedelta
import plotly.graph_objects as go
@st.cache_data
def get_coins():
    return fetch_coins()

current_time = datetime.now()

def end_time():	
    end_time = current_time - datetime.timedelta(days=365)
    return end_time
  

def main():
    
    cg = pcg.CoinGeckoAPI()
    st.title("Cryptocurrency Data Scraper")

    # Fetch the list of coins
    try:
        coins = get_coins()
    except Exception as e:
        st.error(f"Failed to fetch coins: {e}")
        return

    # Create a dropdown menu for selecting a coin
    coin_names = [coin['name'] for coin in coins]
    coin_ids = {coin['name']: coin['id'] for coin in coins}
    selected_coin_name = st.selectbox("Select a cryptocurrency", coin_names)
    selected_coin_id = coin_ids[selected_coin_name]

    # Create a dropdown menu for selecting the currency
    selected_currency = st.selectbox("Select currency", ["usd", "eur", "xau"])
    end_time = current_time - timedelta(days=365) 
    
    # Display the description of the selected coin
    description = fetch_description(selected_coin_id)
    st.markdown("### Description")
    st.write(description)
    
    # Plot the chart
    figure = plot_chart(selected_coin_id, selected_currency)
    st.write(figure)  
    
    # create dataframe of historical prices on daily basis
    data = chart_data(selected_coin_id, selected_currency)
    historical_df = pd.DataFrame(data)
    st.markdown("### Historical Prices (1d interval)")
    st.write(historical_df)
    
    # Create a DataFrame with keys and values columns
    market_data = fetch_market_data(selected_coin_id)
    df = pd.DataFrame(list(market_data.items()), columns=['Keys', 'Values'])
    
    # Extract only the values from the DataFrame
    df['Values'] = df['Values'].apply(lambda x: x[0] if isinstance(x, list) else x)
    
    # Write market data with headings(keys) in one column and values in another column and spread it accross the screen
    st.markdown("### Market Data")
    st.write(df)
 
if __name__ == "__main__":
    main()