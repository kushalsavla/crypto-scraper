def format_price_data(price_data):
    # Function to format price data for charting
    formatted_data = []
    for timestamp, price in price_data:
        formatted_data.append({
            'time': timestamp,
            'price': price
        })
    return formatted_data

def handle_api_error(response):
    # Function to handle API errors
    if response.status_code != 200:
        raise Exception(f"API Error: {response.status_code} - {response.text}")

def convert_timestamp_to_datetime(timestamp):
    # Function to convert Unix timestamp to datetime
    from datetime import datetime
    return datetime.fromtimestamp(timestamp)