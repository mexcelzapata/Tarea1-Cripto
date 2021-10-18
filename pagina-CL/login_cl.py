import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#/usr/local/bin/chromedriver
path = '/usr/local/bin/chromedriver'

def login():
	#conexion con pagina web
	driver = webdriver.Chrome(path)
	time.sleep(1)
	driver.get("https://www.8-bits.cl/index.php?route=account/login")
	time.sleep(2)
	
	#registro de mail 
	driver.find_element_by_xpath('//*[@id="input-email"]').click()
	time.sleep(1)

	mail=driver.find_element_by_id('input-email')
	time.sleep(1)
	mail.send_keys("mexcelzapata@gmail.com")
	time.sleep(1)

	#registro de password 
	password = driver.find_element_by_id('input-password')
	password.send_keys("66bef2f4f9")
	time.sleep(1)
	driver.find_element_by_xpath('//*[@id="content"]/div/div/div[2]/form/input').click()


if __name__ == "__main__":
    
    login()

