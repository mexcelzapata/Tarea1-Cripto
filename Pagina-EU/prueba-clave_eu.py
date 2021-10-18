import time, string, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#/usr/local/bin/chromedriver
path = '/usr/local/bin/chromedriver'

# tipo de caracteres
numeros = string.digits #[0-9]
letras = string.ascii_letters #[a-z][A-Z]
arabe =  "؛ڜﭗﺹﻇﻨﻩﻲ"
ascii_letras = "@#~¥§«Æ¼ñÑá^ø=()$þ”ßÐ‡‰―‼⁊‹¢"
script = "₁ⁱₕ₉ₘ₊⁼⁽ₔ⁰"
emoji = "🌝💓😢🙉"

listado = letras + letras + arabe + ascii_letras+ script + emoji
print(listado)

#conexion con la pagina 
driver = webdriver.Chrome(path)
time.sleep(1)
driver.get("https://eu.4game.com/en/signin/")
time.sleep(2)

# iteracion de ingreso 100 veces

for i in range(100):
	mail = driver.find_element_by_class_name('Input__input__1t40v')
	mail.clear()
	time.sleep(1)
	mail.send_keys("mexcelzapata@gmail.com")
	time.sleep(1)

	driver.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[1]/div[2]/div/div/div/div[3]/div/form/div[2]/div/input').click()
	passw = driver.find_element_by_css_selector("input[type='password']")
	passw.clear()
	key = ''.join(random.choice(listado) for j in range (random.randrange(8,20)))
	passw.send_keys(key)
	time.sleep(1)
	print("password:" + key)
	driver.find_element_by_xpath('//*[@id="gatsby-focus-wrapper"]/div/div[1]/div[2]/div/div/div/div[3]/div/form/button').click()
	time.sleep(4)	


