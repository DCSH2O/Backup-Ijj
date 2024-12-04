from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import os
import time
import requests
from faker import Faker

# Função para configurar o driver
def setup_driver():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(executable_path="geckodriver_path", options=options)  # Altere para o caminho correto do geckodriver
    return driver

# Função para realizar o login
def login(driver, email, senha):
    driver.get("https://projetofinal.jogajuntoinstituto.org/")
    
    email_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "email"))
    )
    email_input.send_keys(email)

    senha_input = driver.find_element(By.NAME, "password")
    senha_input.send_keys(senha)

    login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Iniciar sessão')]"))
    )
    login_button.click()

# Função para baixar uma imagem aleatória
def baixar_imagem_aleatoria():
    url_imagem = "https://picsum.photos/200"
    resposta = requests.get(url_imagem)
    caminho_imagem = os.path.join(os.getcwd(), "imagem_aleatoria.jpg")
    with open(caminho_imagem, 'wb') as file:
        file.write(resposta.content)
    return caminho_imagem

# Função para cadastrar um produto
def adicionar_produto(driver, nome_produto, descricao_produto, preco_produto, imagem_path):
    adicionar_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Adicionar')]"))
    )
    adicionar_button.click()

    nome_produto_input = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.NAME, "name"))
    )
    nome_produto_input.send_keys(nome_produto)

    descricao_produto_input = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.NAME, "description"))
    )
    descricao_produto_input.send_keys(descricao_produto)

    preco_input = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.NAME, "price"))
    )
    preco_input.send_keys(preco_produto)

    imagem_input = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.NAME, "image"))
    )
    imagem_input.send_keys(imagem_path)

    submit_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'ENVIAR NOVO PRODUTO')]"))
    )
    submit_button.click()

    # Esperar a lista de produtos ser atualizada
    time.sleep(5)

# Cenários de testes no Behave

@given('que eu esteja na página de login')
def step_impl(context):
    context.driver = setup_driver()
    context.driver.get("https://projetofinal.jogajuntoinstituto.org/")

@when('eu fizer login com meu email e senha')
def step_impl(context):
    email = "dionebraga.work@gmail.com"
    senha = "123456"
    login(context.driver, email, senha)

@when('eu adicionar um produto com nome, descrição, preço e imagem')
def step_impl(context):
    fake = Faker("pt_br")
    nome_produto = fake.word().capitalize()
    descricao_produto = fake.sentence(nb_words=6)
    preco_produto = f"R$ {random.uniform(10, 100):.2f}".replace('.', ',')
    imagem_path = baixar_imagem_aleatoria()
    
    adicionar_produto(context.driver, nome_produto, descricao_produto, preco_produto, imagem_path)

@then('o produto deve ser adicionado com sucesso')
def step_impl(context):
    # Aqui você pode verificar se o produto foi realmente adicionado na lista
    # Exemplo: verificar se o nome do produto está na tela ou em uma lista de produtos
    context.driver.quit()
