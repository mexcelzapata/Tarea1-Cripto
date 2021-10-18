import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#/usr/local/bin/chromedriver
path = '/usr/local/bin/chromedriver'


#conexion con la pagina Web
driver = webdriver.Chrome(path)
time.sleep(1)
driver.get("https://www.8-bits.cl/index.php?route=account/login")
time.sleep(2)

driver.find_element_by_xpath('//*[@id="column-right"]/div/div[2]/ul/li[2]/a').click()
time.sleep(3)

# Registro de los datos el usuario
driver.find_element_by_xpath('//*[@id="input-firstname"]').click()

nombre=driver.find_element_by_id('input-firstname')
nombre.send_keys("CARLOS")	
time.sleep(1)
driver.find_element_by_xpath('//*[@id="input-lastname"]').click()
apellido = driver.find_element_by_id('input-lastname')
apellido.send_keys("CACELI")
time.sleep(1)

driver.find_element_by_xpath('//*[@id="input-city"]').click()
ciudad = driver.find_element_by_id('input-city')
ciudad.send_keys("santiago")
time.sleep(1)

driver.find_element_by_xpath('//*[@id="input-address-1"]').click()
direccion = driver.find_element_by_id('input-address-1')
direccion.send_keys("santiago")


driver.find_element_by_xpath('//*[@id="input-email"]').click()
email = driver.find_element_by_id('input-email')
email.send_keys("correo2@gmail.com")

driver.find_element_by_xpath('//*[@id="input-country"]').click()
driver.find_element_by_xpath('//*[@id="input-country"]/option[8]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="input-zone"]').click()
driver.find_element_by_xpath('//*[@id="input-zone"]/option[5]').click()
driver.find_element_by_xpath('//*[@id="input-zone"]/option[6]').click()
time.sleep(1)

driver.find_element_by_xpath('//*[@id="input-telephone"]').click()
tel = driver.find_element_by_id('input-telephone')
tel.send_keys("123456789")
time.sleep(1)

driver.find_element_by_xpath('//*[@id="input-password"]').click()
passw = driver.find_element_by_id('input-password')
passw.send_keys("a12345678")
time.sleep(1)

driver.find_element_by_xpath('//*[@id="input-confirm"]').click()
passw2 = driver.find_element_by_id('input-confirm')
passw2.send_keys("a12345678")

time.sleep(1)

driver.find_element_by_xpath('//*[@id="content"]/form/div/div/input[1]').click()
driver.find_element_by_xpath('//*[@id="content"]/form/div/div/input[2]').click()

