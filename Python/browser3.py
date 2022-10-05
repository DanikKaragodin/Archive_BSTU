import time
from selenium import webdriver
option = webdriver.ChromeOptions()
option.add_argument('--proxy-server=178.125.67.104:8080')
browser = webdriver.Chrome(options=option)
browser.get('https://2ip.ru')