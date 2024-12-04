import pandas as pd

def parse_stock_data(json_data):
    timestamps = json_data['chart']['result'][0]['timestamp']
    close_prices = json_data['chart']['result'][0]['indicators']['quote'][0]['close']
    data = pd.DataFrame({'Date': pd.to_datetime(timestamps, unit='s'), 'Close': close_prices})
    return data