from selenium import webdriver
from selenium.webdriver.common.keys import Keys

## Navegador
navegador = webdriver.Chrome()
navegador.get('https://demoqa.com/text-box')

## Elementos
inputName = '//*[@id="userName"]'  # XPATH
inputEmail = 'userEmail'  # ID
inputAdress = 'currentAddress' #ID
inputPermanent = '//*[@id="permanentAddress"]' #XTPATH
btnSubmit = '#submit' #selector

## FIND ELEMENTS (ENCONTRAR ELEMENTOS NA PASTA)
inputNameElement = navegador.find_element_by_xpath(inputName).send_keys('Marco Figueiredo')
inputEmailElement = navegador.find_element_by_id(inputEmail).send_keys('email@email.com')
inputAdressElement = navegador.find_element_by_id(inputAdress).send_keys('Estrada Automatica, número 2')
inputPermanentElement = navegador.find_element_by_xpath(inputPermanent).send_keys('Estrada Automática, número 3')
btnSubmitElement = navegador.find_element_by_css_selector(btnSubmit).click()







