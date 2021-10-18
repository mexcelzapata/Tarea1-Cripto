import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#/usr/local/bin/chromedriver
path = '/usr/local/bin/chromedriver'

#conexion con la pagina web 
driver = webdriver.Chrome(path)
time.sleep(1)
driver.get("https://www.8-bits.cl/index.php?route=account/login")
time.sleep(2)

# ingreso a traves de la pagina
driver.find_element_by_xpath('//*[@id="input-email"]').click()
time.sleep(1)

mail=driver.find_element_by_id('input-email')
time.sleep(1)
mail.send_keys("mexcelzapata@gmail.com")
time.sleep(1)
password = driver.find_element_by_id('input-password')
password.send_keys("12345678")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="content"]/div/div/div[2]/form/input').click()
time.sleep(4)

password = driver.find_element_by_id('input-password')
password.clear()
password.send_keys("1234567111111")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="content"]/div/div/div[2]/form/input').click()
time.sleep(4)

password = driver.find_element_by_id('input-password')
password.clear()
password.send_keys("11111")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="content"]/div/div/div[2]/form/input').click()
time.sleep(4)

password = driver.find_element_by_id('input-password')
password.clear()
password.send_keys("1")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="content"]/div/div/div[2]/form/input').click()

time.sleep(4)

password = driver.find_element_by_id('input-password')
password.clear()
password.send_keys("12")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="content"]/div/div/div[2]/form/input').click()

time.sleep(4)

password = driver.find_element_by_id('input-password')
password.clear()
password.send_keys("666666666")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="content"]/div/div/div[2]/form/input').click()



