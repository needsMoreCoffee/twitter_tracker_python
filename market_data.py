import pandas_datareader as pdr
%matplotlib

# pip install matplotlib
# pip install python-tk
# apt-get install python-tk

df = pdr.get_data_yahoo('BTCUSD=X')
df.info
df['Close'].plot(grid=True, figsize=(8,5))
