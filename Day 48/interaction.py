from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page/")

# #articles = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
# articles = driver.find_element(By.CSS_SELECTOR, value = "#articlecount a")
# #print(articles.text)

# #articles.click()
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# # all_portals.click()

# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python", Keys.ENTER)

driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")

last_name.send_keys("Hicks")
first_name.send_keys("Carissa")
email.send_keys("hicks.Carissa@Gmail.com")

submit = driver.find_element(By.CSS_SELECTOR, value="form button")
submit.click()