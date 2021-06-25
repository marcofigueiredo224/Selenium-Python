from selenium import webdriver
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Chrome()
navegador.get('https://demoqa.com/alerts')

btnAlert = 'alertButton'
btnConfirm = 'confirmButton'
btnPrompt = 'promtButton'

btnAlertElement = navegador.find_element_by_id(btnPrompt)

## CLICKS 
btnAlertElement.click()

## SWITCH TO
alerta = navegador.switch_to.alert
# Para aceitar = alerta.accept()
alerta.send_keys('Marco Figueiredo')
alerta.accept()

