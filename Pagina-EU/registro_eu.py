
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


# ubicacion de registo 
driver.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[1]/div[2]/div/div/div/div[1]/a[2]').click()
time.sleep(4)
driver.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[1]/div[2]/div/div/div/div[3]/div/section[2]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[1]/div[2]/div/div/div/div[3]/div/form/div[1]/div/input').click()
mail = driver.find_element_by_class_name('Input__input__1t40v')
mail.send_keys("correo@gmail.com")
driver.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[1]/div[2]/div/div/div/div[3]/div/form/div[2]/div/input').click()
passw = driver.find_element_by_css_selector("input[type='password']")
passw.send_keys("CLAVE123456789")

# condiciones - 1
driver.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[1]/div[2]/div/div/div/div[3]/div/form/label[1]/span[2]/span').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[1]/div[2]/div/div/div/div[3]/div/form/label[1]/span[2]').click()
time.sleep(2)
# condiciones - 2
driver.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[1]/div[2]/div/div/div/div[3]/div/form/label[2]/span[2]/span').click()

driver.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[1]/div[2]/div/div/div/div[3]/div/form/button').click()
#boton crear cuenta
driver.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[1]/div[2]/div/div/div/div[3]/div/form/label[1]/span[1]').click()
driver.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[1]/div[2]/div/div/div/div[3]/div/form/button').click()


