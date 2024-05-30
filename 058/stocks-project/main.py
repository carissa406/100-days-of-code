#import the packages
import requests
from bs4 import BeautifulSoup
import pandas as pd

#STOCKS = ['NASDAQ:TSLA', 'NYSE:VALE', 'NASDAQ:RIVN']
stock_name = 'NASDAQ:TSLA'
stock_matrix = [['Name', 'Close', 'Div%']]

#for stock_name in STOCKS:
URL = f'https://www.google.com/finance/quote/{stock_name}'

response = requests.get(URL)
webpage = response.text
soup = BeautifulSoup(webpage, 'html.parser')

stock_data = soup.find_all('div', class_='P6K39c')

print(stock_data)

# previous_close = stock_data[0].text
# dividend_yield = stock_data[6].text

# row_of_data = [stock_name, previous_close, dividend_yield]

# stock_matrix.append(row_of_data)


# df = pd.DataFrame(stock_matrix[1:],columns=stock_matrix[0])

# print(df)