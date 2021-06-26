from os import removedirs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

navegador = webdriver.Chrome()
navegador.get ('https://demoqa.com/webtables')

btnAdd = 'addNewRecordButton' 
FirstName = 'firstName' 
LastName = 'lastName' 
Email = 'userEmail' 
Age = 'age'
Salary = 'salary'
Departament = 'department'
btnSubmit = 'submit'

btnAddElement = navegador.find_element_by_id(btnAdd).click()
FirstNameElement = navegador.find_element_by_id(FirstName).send_keys('Marco')
LastNameElement= navegador.find_element_by_id(LastName).send_keys('Figueiredo')
EmailElement = navegador.find_element_by_id(Email).send_keys('email22@gmail.com')
AgeElemet = navegador.find_element_by_id(Age).send_keys('19')
SalaryElement = navegador.find_element_by_id(Salary).send_keys('2800')
DepartamentElement = navegador.find_element_by_id(Departament).send_keys('Tecnologia da Informação')
btnSubmitElement = navegador.find_element_by_id(btnSubmit).click()


