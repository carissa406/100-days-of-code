from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3797480953&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")

time.sleep(2)

sign_in = driver.find_element(By.XPATH, value='/html/body/div[1]/header/nav/div/a[2]')
sign_in.click()

email = driver.find_element(By.ID, value='username')
password = driver.find_element(By.ID, value='password')

email.send_keys('hicks.carissa@gmail.com')
password.send_keys('Springfield1!23')

submit = driver.find_element(By.CSS_SELECTOR, value='button')
submit.click()

time.sleep(1)

save = driver.find_element(By.CLASS_NAME, value='jobs-save-button')
save.click()

all_jobs = driver.find_elements(By.CLASS_NAME, value='.job-card-container')
for job in all_jobs:
    try:
        print(job.text)
    except:
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()