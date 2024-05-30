#import the packages
import requests
from bs4 import BeautifulSoup
import pandas as pd

#Google finance uses these codes to search for different stocks, found in the search bar when you search for a stonk in Google Finance
#be careful tho cause the search bar will say STOCK_EXCHANGE:STOCK_TICKER_SYMBOL but in the actual address bar it's reversed.
#make sure to use what appears in the address bar
#you can erase and add the stock names here, it won't mess with anything else
STOCKS = ['F:NYSE', 'FDX:NYSE', 'AAPL:NASDAQ']

#this is where we will save all the stocks we are looping through
stock_matrix = [['Name', 'Close', 'Div%']]

#looping through each stock name
for stock_name in STOCKS:
    URL = f'https://www.google.com/finance/quote/{stock_name}'

    #this is how you use the requests package to connect to any website
    #it usually always looks like this:
    response = requests.get(URL)
    webpage = response.text
    soup = BeautifulSoup(webpage, 'html.parser')
    #the data in that little rectangle (where it says close,day range, etc) on google is located here:
    stock_data = soup.find_all('div', class_='P6K39c')

    #get the first and sixth elements in that list to grab the two things you wanted
    previous_close = stock_data[0].text
    dividend_yield = stock_data[6].text

    #make a list of the complete data you've gathered
    row_of_data = [stock_name, previous_close, dividend_yield]
    #append it to our matrix
    stock_matrix.append(row_of_data)

#Once the matrix is done, we will turn it into a dataframe
#I already put the column names in the matrix when I first made the assignment, so I will make those the column names instead... 
    #if you dont do this it will say 0, 1, 2 etc on the top of each column
df = pd.DataFrame(stock_matrix[1:],columns=stock_matrix[0])

#save the dataframe as a csv file to your compooter
#index=false to not save the indicies of each row... if you erase this,it will say 0, 1, 2 etc on the beginning of each row
#the file name is stocks.csv, change it to whatever and where ever you want it to go.
df.to_csv('C:/Users/wumbus/Documents/stocks.csv', index=False)