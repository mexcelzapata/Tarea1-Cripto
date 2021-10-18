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

#conexion con la pagina Web
driver = webdriver.Chrome(path)
time.sleep(1)
driver.get("https://www.8-bits.cl/index.php?route=account/login")
time.sleep(2)

# iteracion de ingreso 100 veces

for i in range(100):
	mail=driver.find_element_by_id('input-email')
	mail.clear()
	time.sleep(1)
	mail.send_keys("mexcelzapata@gmail.com")
	time.sleep(1)
	password = driver.find_element_by_id('input-password')
	password.clear()
	key = ''.join(random.choice(listado) for j in range (random.randrange(8,20)))
	password.send_keys(key)
	time.sleep(1)
	print("password:" + key)
	driver.find_element_by_xpath('//*[@id="content"]/div/div/div[2]/form/input').click()
	time.sleep(4)	








