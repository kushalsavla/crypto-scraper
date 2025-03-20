import requests
import pandas as pd
import pycoingecko as pcg
from datetime import datetime, timedelta
import plotly.graph_objects as go

cg = pcg.CoinGeckoAPI()

current_time = datetime.now()

end_time = current_time - timedelta(days=365)

def fetch_coins():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "volume_desc",
        "per_page": 100,
        "page": 1,
        "sparkline": False
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}, {response.text}")
        raise Exception("Error fetching data from CoinGecko API")
 
def fetch_market_data(id):
    cg = pcg.CoinGeckoAPI()
    # get coin market data
    coin_market_data = cg.get_coin_by_id(id)
    # Dropping unnecessary data
    keys_to_remove = [
        'asset_platform_id', 'additional_notices', 'platforms', 'web_slug',
        'detail_platforms', 'categories', 'public_notice', 'localization',
        'preview_listing', 'ico_data'
    ]
    for key in keys_to_remove:
        coin_market_data.pop(key, None)
    
    # lets take coin description highlight the website links in description and remove html tags and print it
    coin_desc = coin_market_data['description']['en'] 
    coin_desc = coin_desc.replace('<a href=', '( ').replace('</a>', ' )').replace('>', ', ')
    
    # Extracting relevant data
    token_id = coin_market_data['id']
    symbol = coin_market_data['symbol']
    name = coin_market_data['name']
    hashing_algorithm = coin_market_data['hashing_algorithm']
    homepage = coin_market_data['links']['homepage']
    whitepaper = coin_market_data['links']['whitepaper']
    genesis_date = coin_market_data['genesis_date']
    market_cap_rank = coin_market_data['market_cap_rank']
    
    current_price = coin_market_data['market_data']['current_price']
    ath = coin_market_data['market_data']['ath']
    ath_date = coin_market_data['market_data']['ath_date']['usd']
    atl = coin_market_data['market_data']['atl']
    atl_date = coin_market_data['market_data']['atl_date']['usd']
    block_time_in_minutes = coin_market_data['block_time_in_minutes']
    market_cap = coin_market_data['market_data']['market_cap']
    fully_diluted_valuation = coin_market_data['market_data']['fully_diluted_valuation']
    total_volume = coin_market_data['market_data']['total_volume']
    high_24h = coin_market_data['market_data']['high_24h']
    low_24h = coin_market_data['market_data']['low_24h']
    price_change_24h = coin_market_data['market_data']['price_change_24h']
    price_change_percentage_24h = coin_market_data['market_data']['price_change_percentage_24h']
    price_change_percentage_7d = coin_market_data['market_data']['price_change_percentage_7d']
    price_change_percentage_14d = coin_market_data['market_data']['price_change_percentage_14d']
    price_change_percentage_30d = coin_market_data['market_data']['price_change_percentage_30d']
    price_change_percentage_60d = coin_market_data['market_data']['price_change_percentage_60d']
    price_change_percentage_200d = coin_market_data['market_data']['price_change_percentage_200d']
    price_change_percentage_1y = coin_market_data['market_data']['price_change_percentage_1y']
    market_cap_change_24h_in_currency = coin_market_data['market_data']['market_cap_change_24h_in_currency']
    market_cap_change_percentage_24h_in_currency = coin_market_data['market_data']['market_cap_change_percentage_24h_in_currency']
    total_supply = coin_market_data['market_data']['total_supply']
    max_supply = coin_market_data['market_data']['max_supply']
    circulating_supply = coin_market_data['market_data']['circulating_supply']
    last_updated = coin_market_data['market_data']['last_updated']
    
    # Creating a DataFrame
    data = {
        'token id': [token_id],
        'symbol': [symbol],
        'name': [name],
        'hashing algorithm': [hashing_algorithm],
        'homepage': [homepage],
        'whitepaper': [whitepaper],
        'genesis date': [genesis_date],
        'market cap rank': [market_cap_rank],
        'current price usd': [current_price['usd']],
        'current price eur': [current_price['eur']],
        'current price xau': [current_price['xau']],
        'ath usd': [ath['usd']],
        'ath eur': [ath['eur']],
        'ath xau': [ath['xau']],
        'ath date': [ath_date],
        'atl usd': [atl['usd']],
        'atl eur': [atl['eur']],
        'atl xau': [atl['xau']],
        'atl date': [atl_date],
        'block time in minutes': [block_time_in_minutes],
        'market cap usd': [market_cap['usd']],
        'market cap eur': [market_cap['eur']],
        'market cap xau': [market_cap['xau']],
        'fully diluted valuation usd': [fully_diluted_valuation['usd']],
        'fully diluted valuation eur': [fully_diluted_valuation['eur']],
        'fully diluted valuation xau': [fully_diluted_valuation['xau']],
        'total volume usd': [total_volume['usd']],
        'total volume eur': [total_volume['eur']],
        'total volume xau': [total_volume['xau']],
        '24h high usd': [high_24h['usd']],
        '24h high eur': [high_24h['eur']],
        '24h high xau': [high_24h['xau']],
        '24h low usd': [low_24h['usd']],
        '24h low eur': [low_24h['eur']],
        '24h low xau': [low_24h['xau']],
        '24h price change': [price_change_24h],
        'price change percentage 24h': [price_change_percentage_24h],
        'price change percentage 7d': [price_change_percentage_7d],
        'price change percentage 14d': [price_change_percentage_14d],
        'price change percentage 30d': [price_change_percentage_30d],
        'price change percentage 60d': [price_change_percentage_60d],
        'price change percentage 200d': [price_change_percentage_200d],
        'price change percentage 1y': [price_change_percentage_1y],
        'market cap change 24h usd': [market_cap_change_24h_in_currency['usd']],
        'market cap change 24h eur': [market_cap_change_24h_in_currency['eur']],
        'market cap change 24h xau': [market_cap_change_24h_in_currency['xau']],
        'market cap change percentage 24h usd': [market_cap_change_percentage_24h_in_currency['usd']],
        'market cap change percentage 24h eur': [market_cap_change_percentage_24h_in_currency['eur']],
        'market cap change percentage 24h xau': [market_cap_change_percentage_24h_in_currency['xau']],
        'total supply': [total_supply],
        'max supply': [max_supply],
        'circulating supply': [circulating_supply],
        'last updated': [last_updated]
    }
    #making dataframe from data with keys in one column and values in another column
    df = pd.DataFrame(data)
    
    return df
    
def fetch_description(id):
    # get coin description
    coin_desc = cg.get_coin_by_id(id)
    coin_desc = coin_desc['description']['en']
    return coin_desc

def chart_data(id, currency):
    #getting historical market chart data
    market_chart_data = cg.get_coin_market_chart_range_by_id(
        id=id,
        vs_currency=currency,
        from_timestamp=int(end_time.timestamp()),
        to_timestamp=int(current_time.timestamp()),
    )
          
    # Extract relevant data and create a DataFrame
    df = pd.DataFrame(market_chart_data['prices'], columns=['Timestamp', 'Price'])
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='ms')
    df['Date'] = pd.to_datetime(df['Timestamp'], unit='ms')
    df = df.set_index('Timestamp')
    
    # Resample data to 1-minute timeframe (if necessary)
    # The API might already provide 1-minute data, but we can
    # ensure it by resampling if required
    df = df.resample('1d').mean().ffill()
    # making dataframe in descending order of time
    df = df.sort_index(ascending=False)
    return df

    