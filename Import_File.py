from selenium import webdriver
from selenium.webdriver.common.keys import Keys

## Navegador
navegador = webdriver.Chrome()
navegador.get('https://demoqa.com/upload-download')

## ELEMENTOS 
inputFiles = 'form-control-file'

## FIND ELEMEMT
navegador.find_element_by_class_name(inputFiles).send_keys('C:/Users/user/OneDrive/Documentos/Drivers/aleatorio.png')