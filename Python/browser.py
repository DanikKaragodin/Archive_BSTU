from time import sleep
import selenium
from selenium import webdriver
import random

options = webdriver.ChromeOptions()
# options.binary_location = r"C:\Users\Karagodin\AppData\Local\Programs\Opera GX\launcher.exe"
#driver = webdriver.Chrome(r"C:\Users\Karagodin\AppData\Local\Programs\Python\Python38\operadriver.exe",options=options)
driver=webdriver.Chrome()
driver.get('https://vk.com/afonasijmq') #перейти на сайт
driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div[1]/div/div/form/div[2]/input').send_keys('+375295203457')
driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div[1]/div/div/form/div[4]/input').send_keys('kolit2004')
driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div[1]/div/div/button[1]').click()
sleep(5)
for i in range(10000):
    driver.find_element_by_xpath('/html/body/div[12]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/div/div[1]/aside/div/div[1]/div/a[1]/button').click()
    sleep(2)
    driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div/div[2]/div/div[4]/div[2]').send_keys('Ты был выебан автоматизированным ПО Карагодина')
    driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div/div[2]/div/div[7]/button').click()
    sleep(random.randint(1,5))
driver.save_screenshot('photo.png') #сохранить скриншот
#driver.refresh() #перезагрузка
#driver.quit() #закрыть браузер
