import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#/usr/local/bin/chromedriver
path = '/usr/local/bin/chromedriver'


#conexion con la pagina 
driver = webdriver.Chrome(path)
time.sleep(1)
driver.get("https://eu.4game.com/en/signin/")
time.sleep(2)

# ingreso de los datos de la cuenta 1
mail = driver.find_element_by_class_name('Input__input__1t40v')
mail.send_keys("mexcelzapata@gmail.com")
driver.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[1]/div[2]/div/div/div/div[3]/div/form/div[2]/div/input').click()
passw = driver.find_element_by_css_selector("input[type='password']")
passw.send_keys("CLAVE")
driver.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[1]/div[2]/div/div/div/div[3]/div/form/button').click()
time.sleep(2)


# ingreso de los datos de la cuenta 2
driver.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[1]/div[2]/div/div/div/div[3]/div/form/div[2]/div/input').click()
passw = driver.find_element_by_css_selector("input[type='password']")
passw.clear()
passw.send_keys("11")
driver.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[1]/div[2]/div/div/div/div[3]/div/form/button').click()
time.sleep(2)


# ingreso de los datos de la cuenta 3
driver.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[1]/div[2]/div/div/div/div[3]/div/form/div[2]/div/input').click()
passw = driver.find_element_by_css_selector("input[type='password']")
passw.clear()
passw.send_keys("11111111")
driver.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[1]/div[2]/div/div/div/div[3]/div/form/button').click()
time.sleep(2)

# ingreso de los datos de la cuenta 3
driver.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[1]/div[2]/div/div/div/div[3]/div/form/div[2]/div/input').click()
passw = driver.find_element_by_css_selector("input[type='password']")
passw.clear()
passw.send_keys("999")
driver.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[1]/div[2]/div/div/div/div[3]/div/form/button').click()
time.sleep(2)