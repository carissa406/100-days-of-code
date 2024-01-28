#import the packages
import requests
from bs4 import BeautifulSoup
import pandas as pd

STOCKS = ['F','GLAD','HRZN','AGNC','PSEC','KMI']
stock_matrix = [['Name', 'Close', 'Div%']]


for stock_name in STOCKS:
    URL = f'https://www.marketwatch.com/investing/stock/{stock_name}'

    response = requests.get(URL)
    webpage = response.text
    soup = BeautifulSoup(webpage, 'html.parser')

    #------ this is what we just did ---------#
    need = []

    for li_tag in soup.find_all('ul', class_ ='list list--kv list--col50'):
        for span_tag in li_tag.find_all('li', class_ ='kv__item'):
            value = span_tag.find('span', class_='primary').text
            need.append(value)

    div_yield = need[10]

    want = []
    for td in soup.find_all('tr', class_='table__row'):
        value = td.find('td', class_='table__cell u-semi')
        want.append(value)

    previous_close = want[7].text
    #-----------------------------------------#

    row_of_data = [stock_name, previous_close, div_yield]

    stock_matrix.append(row_of_data)


df = pd.DataFrame(stock_matrix[1:],columns=stock_matrix[0])

df.to_csv('C:/Users/hicks/Documents/GitHub/100-days-of-code/Day 59/stocks.csv', index=False)