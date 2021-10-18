import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#/usr/local/bin/chromedriver
path = '/usr/local/bin/chromedriver'


#conexion con la pagina Web
driver = webdriver.Chrome(path)
time.sleep(1)
driver.get("https://www.8-bits.cl/index.php?route=account/login")
time.sleep(3)

#solicitar recuperacion de la clave con mail del usuario
driver.find_element_by_xpath('//*[@id="content"]/div/div/div[2]/form/a').click()
time.sleep(3) 
driver.find_element_by_xpath('//*[@id="input-email"]').click()
email = driver.find_element_by_id('input-email')
email.send_keys("mexcelzapata@gmail.com")
driver.find_element_by_xpath('//*[@id="content"]/form/div/div[2]/input').click()

driver.get("https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")