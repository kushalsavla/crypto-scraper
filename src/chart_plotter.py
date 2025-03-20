import plotly.graph_objects as go
import pandas as pd
import streamlit as st
from data_fetcher import chart_data



def plot_chart(selected_coin_name, selected_currency):
    data = chart_data(selected_coin_name, selected_currency)
    # # plotting candlestick data using plotly with timestamp as x-axis and price as y-axis with open, high, low, close values. the price is on y-axis and timestamp on x-axis but x axis marks only the date and not the time large size chart
    # # Create the line chart
    fig = go.Figure(data=[go.Scatter(
        x = data['Date'],
        y = data['Price'],
        mode = 'lines',
        name='Price',
        line=dict(color='blue')
    )])
    
    fig.update_layout(
        title=f'{selected_coin_name} Price Chart (1 Year)',
        xaxis_title='Date',
        yaxis_title=f'Price ({selected_currency.upper()})',
        xaxis_rangeslider_visible=True,
        yaxis=dict(
            autorange=True,
            fixedrange=False
        ),
        template='plotly_dark',
        height=600,
        width=1800
    )

    return fig