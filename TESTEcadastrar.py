from selenium import webdriver
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Chrome()
navegador.get ('https://srbarriga.herokuapp.com/login')

cadastrar = '//*[@id="bs-example-navbar-collapse-1"]/ul/li[2]/a' #XPATH
nome = 'nome' #ID
email = 'email' #ID
senha = 'senha'
cadastro = 'body > div.jumbotron.col-lg-4 > form > input' #SELECTOR

cadastrarElement = navegador.find_element_by_xpath(cadastrar).click()
nomeElement = navegador.find_element_by_id(nome).send_keys('Marco Figueiredo')
emailElement = navegador.find_element_by_id(email).send_keys('email22@gmail.com')
senhaElement = navegador.find_element_by_id(senha).send_keys('30820025')
cadastroElement = navegador.find_element_by_css_selector(cadastro).click()

# Caso de Teste Cadastro
# Dado que acesso a página de cadastro
# Quando submeto meu cadastro com nome, email e senha
# Então recebo uma mensagem de usuário cadastrado.