from time import sleep
import selenium
from selenium import webdriver
import random
option = webdriver.ChromeOptions()
option.add_argument("--disable-system-notifications")
option.headless= True
driver=webdriver.Chrome(options=option)
driver.get("https://nick-name.ru/generate/")
while True:
    driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[2]/form/table/tbody/tr[5]/td[2]/input").click()
    link = driver.find_element_by_id("register").get_attribute("href")[37:]
    print(f"Nickname: {link}")

