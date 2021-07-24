from selenium import webdriver
from credentials import username, password
import time

path = "D://Python/Instagram Login/chromedriver.exe"

driver = webdriver.Chrome(executable_path=path)
driver.get("https://www.instagram.com/accounts/login/")

time.sleep(5)

driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[1]/div/label/input').send_keys(username)

driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[2]/div/label/input').send_keys(password)

driver.find_element_by_css_selector('button[type=submit]').click()

time.sleep(5)

driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div').click()
