#import the packages, using selenium cause I learned it last, still fresh in brains
from selenium import webdriver
from selenium.webdriver.common.by import By

#sorry, I like google chrome so... :p this is for connecting to the website with chrome
chrome_options = webdriver.ChromeOptions()

#you can put all ur stock codes in a list and then iterate through them with a for loop
#STOCK_CODES = ["TSLA", "NOK", "VALE"]
#for stock in STOCK_CODES:
#   driver.get(https://www.google.com/finance/quote/{stock})
#   stock_data = driver.find_elements(By.CSS_SELECTOR, value='div.P6K39c')
#   previous_close = stock_data[0].text
#   dividend_yield = stock_data[6].text

#I will use just one for now
STOCK_CODE = "F:NYSE"

driver = webdriver.Chrome(options=chrome_options)
#put it inside an f string in case you ever want to change the variable
driver.get(f"https://www.google.com/finance/quote/{STOCK_CODE}")

#finding each item in that block that has all the data you want.
stock_data = driver.find_elements(By.CSS_SELECTOR, value='div.P6K39c')

#the first item in the list is the previous close amt
previous_close = stock_data[0].text
#the sixth item is the dividend yield
dividend_yield = stock_data[6].text

print(previous_close)
print(dividend_yield)
