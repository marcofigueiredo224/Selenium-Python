from typing import KeysView
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from time import sleep

navegador = webdriver.Chrome()
navegador.get ('https://www.buscape.com.br/')

inputConcordar = '//*[@id="__next"]/div[2]/div/div[2]/button'
inputBarra = '//*[@id="header"]/div/div/div[3]/div/div[1]/input' #XPATH
btnBuscar = '//*[@id="header"]/div/div/div[3]/div/div[1]/button' #PATH
btnBotao = '//*[@id="orderBy"]' #XPATH
inputMaiorPreco = '//*[@id="orderBy"]/option[3]' #PATH
inputPrecos = '#resultArea > div:nth-child(3) > div > div:nth-child(1) > div.cardBody > div.cardFooter > a' #SELECTOR
inputCep = '//*[@id="zipcode"]' #XPATH
inputCalcular = '//*[@id="__next"]/div[1]/div[3]/div[2]/div/div/section[3]/div[1]/header/div/div[1]/form/button' #XPATH

inputConcordarElement = navegador.find_element_by_xpath(inputConcordar).click()
inputBarraElement = navegador.find_element_by_xpath(inputBarra).send_keys('Celular')
btnBuscarElement = navegador.find_element_by_xpath(btnBuscar).click()
btnBotaoElemet = navegador.find_element_by_xpath(btnBotao).click()
sleep(1)
inputMaiorPrecoElement = navegador.find_element_by_xpath(inputMaiorPreco).click()
sleep(2)
inputPrecosElement = navegador.find_element_by_css_selector(inputPrecos).click()
sleep(1)
inputCepElement = navegador.find_element_by_xpath(inputCep).send_keys('70000000')
sleep(1)
inputCalcularElement = navegador.find_element_by_xpath(inputCalcular).click()