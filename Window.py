from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

navegador = webdriver.Chrome()
navegador.get('https://demoqa.com/browser-windows')

btnTab = 'tabButton' 
btnWindow = 'windowButton'

btnTabElement = navegador.find_element_by_id(btnTab)
btnWindowElement = navegador.find_element_by_id(btnWindow)

btnTabElement.click()

print(navegador.current_window_handle)
print(navegador.window_handles)

sleep(1.5)
navegador.switch_to_window(
    navegador.window_handles[0]
)
sleep(1.5)

btnWindowElement.click()

print(navegador.window_handles)

navegador.switch_to_window(
    navegador.switch_to_window[2]
)