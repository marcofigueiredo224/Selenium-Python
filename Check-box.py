from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


## Navegador
navegador = webdriver.Chrome()
navegador.get('https://demoqa.com/checkbox')

## ELEMENTOS 
home = 'rct-title' #CLASSE
btnView = '#tree-node > ol > li > span > button' #SELECTOR
documentsBtn = '//*[@id="tree-node"]/ol/li/ol/li[2]/span/label/span[3]' #XPATH

## FIND ELEMENTS 
homeElement = navegador.find_element_by_class_name(home).click()
sleep(1)
btnViewElement = navegador.find_element_by_css_selector(btnView).click()
sleep(1)
documentsBtnElement = navegador.find_element_by_xpath(documentsBtn).click()
