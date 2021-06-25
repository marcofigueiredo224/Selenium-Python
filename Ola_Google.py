from selenium import webdriver
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Chrome()
navegador.get ('https://www.google.com/?gws_rd=ssl')

pesquisar = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
inputPesquisar = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[2]/center/input[1]'

pesquisarElement = navegador.find_element_by_xpath(pesquisar).send_keys('Olá Google')
inputPesquisarElement = navegador.find_element_by_xpath(inputPesquisar).click()
