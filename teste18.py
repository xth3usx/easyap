# -*- coding: utf-8 -*-

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configura o serviço para o ChromeDriver
servico = Service(ChromeDriverManager().install())

# Inicializa o navegador
navegador = webdriver.Chrome(service=servico)

try:
    print("Tentando acessar a página...")
    navegador.get('http://192.168.0.1/')
    print("Página acessada com sucesso.")

    print("Tentando preencher o campo de senha...")
    WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="pc-setPwd-new"]'))
    ).send_keys('123456')
    print("Senha preenchida com sucesso no primeiro campo.")

    print("Tentando preencher o segundo campo de senha...")
    WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="pc-setPwd-confirm"]'))
    ).send_keys('123456')
    print("Senha preenchida com sucesso no segundo campo.")

    print("Tentando clicar no botão de acesso...")
    WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="pc-setPwd-btn"]'))
    ).click()
    print("Botão de acesso clicado com sucesso.")

    print("Tentando clicar em 'Ferramentas de Sistema'...")
    WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="advanced"]/span[2]'))
    ).click()
    print("'Ferramentas de Sistema' clicado com sucesso.")

    print("Verificando se a seção de 'Administração' está presente...")
    WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="menuTree"]/li[10]/a/span[2]'))
    )
    print("Seção de 'Administração' encontrada.")

    print("Tentando clicar na seção de 'Administração'...")
    WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="menuTree"]/li[10]/a/span[2]'))
    ).click()
    print("Seção de 'Administração' clicada com sucesso.")

    print("Verificando se o Gerenciamento Remoto está habilitado...")
    WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="menuTree"]/li[10]/ul/li[6]/a/span'))
    )
    print("Gerenciamento Remoto encontrado.")

    print("Tentando habilitar o Gerenciamento Remoto...")
    WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="menuTree"]/li[10]/ul/li[6]/a/span'))
    ).click()
    print("Gerenciamento Remoto habilitado com sucesso.")

    print("Verificando se o Gerenciamento Remoto HTTPS está presente...")
    WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="remote-management-div"]/div[2]/form/div[1]/label[2]/span[1]'))
    )
    print("Gerenciamento Remoto HTTPS encontrado.")

    print("Tentando desabilitar o Gerenciamento Remoto HTTPS...")
    WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="remote-management-div"]/div[2]/form/div[1]/label[2]/span[1]'))
    ).click()
    print("Gerenciamento Remoto HTTPS desabilitado com sucesso.")

    print("Verificando se o botão de salvar está presente...")
    WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="remote-https-div"]/label[2]/span[1]'))
    )
    print("Botão de salvar encontrado.")

    print("Tentando clicar no botão de salvar...")
    WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="t_save3"]'))
    ).click()
    print("Botão de salvar clicado com sucesso.")

    print("Verificando se o processo de salvamento foi concluído antes de continuar...")
    WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="t_save3"]'))  # Substitua pelo XPath real do indicador de sucesso
    )
    print("Processo de salvamento concluído.")

    print("Tentando ativar o Ping ICMP Remoto...")
    WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div[10]/form/div[1]/label[2]/span[1]'))
    ).click()
    print("Ping ICMP Remoto ativado com sucesso.")

    print("Verificando se o segundo processo de salvamento foi concluído antes de finalizar...")
    WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="t_save4"]'))  # Substitua pelo XPath real do indicador de sucesso
    )
    print("Segundo processo de salvamento concluído.")

    print("Tentando clicar no botão de salvar novamente...")
    WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="t_save4"]'))
    ).click()
    print("Botão de salvar clicado com sucesso novamente.")
    
    print("Tentando clicar em 'Wireless'...")
    WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="menuTree"]/li[4]/a/span[2]'))
    ).click()
    print("'Wireless' clicado com sucesso.") 
    

finally:
    print("Finalizando o script e fechando o navegador...")
    time.sleep(100)
    navegador.quit()
    print("Navegador fechado.")

