from selenium import webdriver
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Chrome()
navegador.get ('https://www.facebook.com/')

inputLogin = 'email' #ID
inputSenha = 'pass' #id
btnEntrar = 'login'
inputLoginElement = navegador.find_element_by_id(inputLogin).send_keys('teste123@gmail.com')
inputSenhaElement = navegador.find_element_by_id(inputSenha).send_keys('******')
btnEntrar = navegador.find_elements_by_name(btnEntrar).click()
