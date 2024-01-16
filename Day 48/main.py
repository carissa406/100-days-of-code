from selenium import webdriver
from selenium.webdriver.common.by import By
import pprint

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
#driver.get("https://mycomfyblouse.com/products/floral-bustier-midriff-waist-shaper-dress?variant=40790929178678")
driver.get("https://www.python.org/")

#price_dollar = driver.find_element(By.ID, value="ProductPrice")
#print(price_dollar.text)
#driver.close() close active tab

# search_bar = driver.find_element(By.NAME, value="q")
# #print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)

# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)

# #using the xpath is easier? 
# #right click it in the inspect, copy, xpath
# downloads_link = driver.find_element(By.XPATH, value='//*[@id="container"]/li[2]/a')
# print(downloads_link.text)

event_times = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')

# for time in event_times:
#     print(time.text)

event_names = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')

# for event in event_names:
#     print(event.text)

events = {}
for n in range(len(event_times)):
    events[n] = {
        "time":event_times[n].text,
        "name":event_names[n].text
    }


pprint.pprint(events)






# events = {k:v for (k,v) in zip(event_times,event_names)}
# print(events)

driver.quit() #close entire browser