import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

URL = "https://www.amazon.com/dp/B08QXB9BH5/?coliid=I3KQSRWYJ3MOTR&colid=3TE0IFYDRF7I0&ref_=list_c_wl_lv_ov_lig_dp_it&th=1"

headers = {
    "User-Agent":"Defined",
    "Accept-Language":"en-US,en;q=0.9",
}

def get_price():

    response = requests.get(URL, headers = headers)
    webpage = response.text
    soup = BeautifulSoup(webpage, 'lxml')

    try:
        price = soup.find(class_="a-offscreen").get_text()
        price_without_currency = price.split("$")[1]
        price_as_float = float(price_without_currency)
        return price_as_float
    except AttributeError:
        return None
    
price = get_price()

while price is None:
    price = get_price()

print(price)
    
BUY_PRICE = 200
EMAIL = "catentertainers@gmail.com"
PASSWORD = "stsu muqc tbbf mwwu"


if price < BUY_PRICE:
    
    message = f"New price on the icecream maker!"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="hicks.carissa@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )