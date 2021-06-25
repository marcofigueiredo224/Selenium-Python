from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import choice

lista_de_selector = ['tree-node > ol > li > ol > li:nth-child(1) > span > label > span.rct-title', 
'#tree-node > ol > li > ol > li:nth-child(2) > span > label > span.rct-title',
'#tree-node > ol > li > ol > li:nth-child(3) > span > label > span.rct-title']

## Navegador
navegador = webdriver.Chrome()
navegador.get('https://demoqa.com/checkbox')

# ELEMENTOS 
btnView = '#tree-node > ol > li > span > button' #SELECTOR

# FIND ELEMENTS
elementoSelecionado = choice(lista_de_selector)
btnViewElement = navegador.find_element_by_css_selector(btnView).click()
btnSelecionado = navegador.find_element_by_css_selector(elementoSelecionado).click()

