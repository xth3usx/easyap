# -*- coding: utf-8 -*-
import signal
import subprocess
import platform
import time
import pyfiglet
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from art import text2art

# Encerrando processos do chromedriver ou navegador chrome
def close_chrome_processes():
    if platform.system() == "Windows":
        # Comandos para Windows
        subprocess.run(["taskkill", "/F", "/IM", "chrome.exe"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(["taskkill", "/F", "/IM", "chromedriver.exe"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    else:
        # Comandos para Linux/Unix
        subprocess.run(["pkill", "-f", "chrome"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(["pkill", "-f", "chromedriver"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

close_chrome_processes()

# Criando texto estilizado
sti_art = pyfiglet.figlet_format("STI", font="slant")

# Exibindo o texto estilizado
print(sti_art)

# Capturando informações do usuário
def gerar_identificador():
    while True:
        numero = input("Digite o número do AP: ")

        if 1 <= len(numero) <= 3 and numero.isdigit():
            numero_formatado = numero.zfill(4)
            
            while True:
                headless = input("Deseja rodar o script em modo headless? (s/n): ").strip().lower()
                if headless == "s":
                    break
                elif headless == "n":
                    break
                else:
                    print("Entrada inválida. Por favor, digite 's' para sim ou 'n' para não.")
            
            # Preparar as informações para retorno
            etiqueta = f"Etiqueta: AP{numero_formatado}"
            ssid1 = f"Identificação SSID Gerência: Gerência{numero_formatado}-Acesso_restrito"
            ssid2 = f"Gerência{numero_formatado}-Acesso_restrito"
            novo_ip = f"NOVO IP Gerência: 172.24.108.{int(numero)}"
            nome_completo_ap = f"Nome completo do AP: ap{numero_formatado}"
      
            return numero, etiqueta, ssid1, ssid2, novo_ip, nome_completo_ap
        else:
            print("Erro: O número do AP deve ter entre 1 e 3 dígitos. Tente novamente.")

numero, etiqueta, ssid1, ssid2, novo_ip, nome_completo_ap = gerar_identificador()

# Impressão de infomações básicas de configuração
print(etiqueta)
print(ssid1)
print(novo_ip)
print(nome_completo_ap)
print("Aguarde, o ambiente está sendo configurado...")

# IP
oct1 = 172
oct2 = 24
oct3 = 108
oct4 = numero

# Máscara de Sub-rede:
mask1 = 255
mask2 = 255
mask3 = 254
mask4 = 0

# Gateway
gtw1 = 172
gtw2 = 24
gtw3 = 108
gtw4 = 1

# DNS Primário
dns1_1 = 200
dns1_2 = 20
dns1_3 = 0
dns1_4 = 18

# DNS Primário
dns2_1 = 200
dns2_2 = 20
dns2_3 = 10
dns2_4 = 17

# Converte o número para string e separa os dígitos
oct4_str = str(oct4)
digit1 = oct4_str[0]  # Primeiro dígito
digit2 = oct4_str[1] if len(oct4_str) > 1 else ""  # Segundo dígito (se existir)
digit3 = oct4_str[2] if len(oct4_str) > 2 else ""  # Terceiro dígito (se existir)

# Mapea os dígitos para as teclas do teclado numérico
num_pad_mapping = {
    "0": Keys.NUMPAD0,
    "1": Keys.NUMPAD1,
    "2": Keys.NUMPAD2,
    "3": Keys.NUMPAD3,
    "4": Keys.NUMPAD4,
    "5": Keys.NUMPAD5,
    "6": Keys.NUMPAD6,
    "7": Keys.NUMPAD7,
    "8": Keys.NUMPAD8,
    "9": Keys.NUMPAD9,
}

# Configura o serviço para o ChromeDriver
servico = Service(ChromeDriverManager().install())

# Configura o Chrome para rodar em modo headless
options = webdriver.ChromeOptions()
#options.add_argument('--headless')  # Executa o navegador em modo headless
options.add_argument('--disable-gpu')  # Desabilita a GPU (opcional, melhora a compatibilidade)
options.add_argument('--start-maximized')  # Maximiza a janela ao iniciar
options.add_argument("force-device-scale-factor=0.5")
options.add_argument("high-dpi-support=1")
options.add_argument('--no-sandbox')  # Desabilita o sandboxing, necessário em alguns ambientes
options.add_argument('--disable-dev-shm-usage')  # Usa /tmp em vez de /dev/shm para armazenamento de compartilhamento de memória (evita problemas de espaço em memória compartilhada)
options.add_argument('--disable-extensions')  # Desabilita extensões, que podem interferir
options.add_argument('--disable-infobars')  # Desabilita a barra de informações "Chrome is being controlled by automated test software"
options.add_argument('--log-level=3')  # Configura o Chrome para suprimir a maioria dos logs

# Inicializa o navegador em modo headless
navegador = webdriver.Chrome(service=servico, options=options)

service_log_path = "chromedriver.log"  # Caminho para salvar os logs do ChromeDriver

start_time = time.time()
start_local_time = time.localtime(start_time)
print(f"Início: {time.strftime('%H:%M:%S', start_local_time)}")

try:
    navegador.get('http://192.168.0.1/')
    print("URL 192.168.0.1 acessada com sucesso.")

    time.sleep(0.2)

    WebDriverWait(navegador, 2).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="pc-setPwd-new"]'))
    ).send_keys('123456')
    print("Senha preenchida com sucesso no primeiro campo.")

    time.sleep(0.2)

    WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="pc-setPwd-confirm"]'))
    ).send_keys('123456')
    print("Senha preenchida com sucesso no segundo campo.")

    time.sleep(0.2)

    element = WebDriverWait(navegador, 40).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="pc-setPwd-btn"]'))
    )
    element.click()
    print("Botão 'Vamos Começar' acionado.")

    time.sleep(0.2)

    element = WebDriverWait(navegador, 40).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="advanced"]/span[2]'))
    )
    element.click()
    print("Menu superior 'Avançado' acionado.")

    time.sleep(0.2)

    element = WebDriverWait(navegador, 40).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="menuTree"]/li[10]/a/span[2]'))
    )
    element.click()
    print("Menu lateral 'Ferramentas de Sistema' acionado.")

    time.sleep(0.2)

    element = WebDriverWait(navegador, 40).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="menuTree"]/li[10]/ul/li[6]/a'))
    )
    element.click()
    print("Submenu 'Administração' acionado.")

    time.sleep(0.2)

    element = WebDriverWait(navegador, 50).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="remote-management-div"]/div[2]/form/div[1]/label[2]/span[1]'))
    )
    element.click()
    print("Gerenciamento Remoto foi habilitado.")

    time.sleep(0.2)

    element = WebDriverWait(navegador, 50).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="remote-https-div"]/label[2]/span[1]'))
    )
    element.click()
    print("Gerenciamento Remoto HTTPS foi desabilitado.")

    time.sleep(0.2)

    element = WebDriverWait(navegador, 50).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="t_save3"]'))
    )
    element.click()
    print("Primeiro salvar acionado.")

    time.sleep(0.2)

    element = WebDriverWait(navegador, 40).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div[10]/form/div[1]/label[2]/span[1]'))
    )
    element.click()
    print("Ping ICMP Remoto ativado.")

    time.sleep(0.2)

    element = WebDriverWait(navegador, 50).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="t_save4"]'))
    )
    element.click()
    print("Segundo salvar acionado.")

    time.sleep(0.2)

    print("Tentando acessar 192.168.0.1 ...")
    navegador.get('http://192.168.0.1/')
    print("Acesso à 192.168.0.1 realizado novamente com sucesso.")

    time.sleep(0.2)

    element = WebDriverWait(navegador, 40).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="advanced"]/span[2]'))
    )
    element.click()
    print("Menu superior 'Avançado' acionado.")

    time.sleep(0.2)

    element = WebDriverWait(navegador, 40).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="menuTree"]/li[10]/a/span[2]'))
    )
    element.click()
    print("'Ferramentas de Sistema' acionado.")

    time.sleep(0.2)

    element = WebDriverWait(navegador, 200).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="menuTree"]/li[4]/a/span[2]'))
    )
    element.click()
    print("Menu 'Wireless' acionado.")

    time.sleep(0.2)

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="menuTree"]/li[4]/ul/li[5]/a/span'))
    )
    element.click()  # Configurações Avançadas
    print("Submenu 'Configurações Avançadas' acionado.")

    time.sleep(0.2)

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div[5]/form/div/label[2]/span[1]'))
    )
    element.click()  # WPS
    print("'WPS' habilitado.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="wpsSave"]'))
    )
    element.click()  # Salvar 
    print("Alterações salvas com sucesso.")

    time.sleep(0.2)

    element = WebDriverWait(navegador, 200).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="menuTree"]/li[4]/a/span[2]'))
    )
    element.click()
    print("Menu 'Wireless' acionado.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 40).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="menuTree"]/li[10]/a/span[2]'))
    )
    element.click()
    print("'Ferramentas de Sistema' acionado.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="access_div_2g"]/div/label[2]/span[1]'))
    )
    element.click()  # Permite Convidados Acessarem Minha Rede Local
    print("Opção 'Convidados Acessarem Minha Rede Local' habilitado.")

    time.sleep(0.2)    

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="vap0_2g"]/div[1]/label[2]/span[1]'))
    )
    element.click()  # Habilitar SSID 1
    print("'SSID 1' habilitado.")

    time.sleep(0.2)      

    element = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ssid_vap0_2g"]'))
    )
    element.clear()  # Apagar texto SSID 
    print("Texto de SSID 1 removido.")

    time.sleep(0.2)      

    element = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ssid_vap0_2g"]'))
    )
    element.send_keys(ssid2)  # Coloca texto SSID de gerência
    print("Texto SSID de gerência adcionado.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 50).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="mssidSave_2g"]'))
    ).click()
    print("Alterações salvas com sucesso.")

    time.sleep(0.2)   
    
    print("Tentando acessar 192.168.0.1 ...")
    navegador.get('http://192.168.0.1/')
    print("Acesso à 192.168.0.1 realizado novamente com sucesso.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 40).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="advanced"]/span[2]'))
    )
    element.click()
    print("Menu superior 'Avançado' acionado.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 40).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="menuTree"]/li[10]/a/span[2]'))
    )
    element.click()
    print("Menu lateral 'Ferramentas de Sistema' acionado.")

    time.sleep(0.2)

    element = WebDriverWait(navegador, 200).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="menuTree"]/li[4]/a/span[2]'))
    )
    element.click()
    print("Menu lateral 'Wireless' acionado.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="menuTree"]/li[4]/ul/li[5]/a/span'))
    )
    element.click()  # Configurações Avançadas
    print("Submenu 'Configurações Avançadas' acionado.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="secArea_vap0_2g"]/div[1]/label[3]/span[1]'))
    )
    element.click()  # WPA/WPA2 Pessoal
    print("'WPA/WPA2 Pessoal' habilitado.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="secArea_vap0_2g"]/div[1]/label[3]/span[1]'))
    )
    element.click()  
    print("Versão 'WPA/WPA2' acionado.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="hideWpaSec_vap0_2g"]/div[2]/label[4]/span[1]'))
    )
    element.click()  
    print("'Criptografia' acionado.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="passwd_vap0_2g"]'))
    )
    element.send_keys('123dsadsa')  # Coloca texto SSID de gerência
    print("Senha de SSID de gerência adcionado com sucesso.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 50).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="mssidSave_2g"]'))
    ).click()
    print("Alterações salvas com sucesso.")

    time.sleep(0.2)   

    print("Tentando acessar 192.168.0.1 ...")
    navegador.get('http://192.168.0.1/')
    print("Acesso à 192.168.0.1 realizado novamente com sucesso.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 40).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="advanced"]/span[2]'))
    )
    element.click()
    print("'Avançado' acionado com sucesso.")

    time.sleep(0.2)

    element = WebDriverWait(navegador, 40).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="menuTree"]/li[10]/a/span[2]'))
    )
    element.click()
    print("'Ferramentas de Sistema' acionado com sucesso.")

    time.sleep(0.2)

    element = WebDriverWait(navegador, 200).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="menuTree"]/li[4]/a/span[2]'))
    )
    element.click()
    print("Menu 'Wireless' acionado.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="menuTree"]/li[4]/ul/li[1]/a/span'))
    )
    element.click()  # Configurações Avançadas
    print("'Configurações Wireless' acessado com sucesso.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ssid"]'))
    )
    element.clear()  # Apagar texto SSID
    print("SSID 2G removido com sucesso.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ssid"]'))
    )
    element.send_keys('eduroam') # Colocar SSID texto "eduroam"
    print("Texto SSID 'eduroam' adcionado.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="_sec"]/div/div[1]'))
    )
    element.click()  # Segurança 
    print(" Menu suspenso sobre 'Segurança' acionado.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//li[contains(text(), "Sem Segurança")]'))
    )
    element.click() # Sem Segurança
    print("Habilitado 'Sem Segurança'.")

    time.sleep(0.2)    

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="save"]/span'))
    )
    element.click()  # Salvar
    print("Alterações salvas com sucesso...")

    time.sleep(0.2)   

    print("Tentando acessar 192.168.0.1 ...")
    navegador.get('http://192.168.0.1/')
    print("Página acessada com sucesso.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 40).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="advanced"]/span[2]'))
    )
    element.click()
    print("'Avançado' acionado com sucesso.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 40).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="menuTree"]/li[10]/a/span[2]'))
    )
    element.click()
    print("Ferramentas de Sistema' acionado com sucesso.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 200).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="menuTree"]/li[4]/a/span[2]'))
    )
    element.click()
    print("Menu 'Wireless' acionado.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="menuTree"]/li[4]/ul/li[1]/a/span'))
    )
    element.click()  # Configurações Avançadas
    print("Configurações Wireless acessada com sucesso.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="load_5g"]'))
    )
    element.click()  # 5GHz
    print("5G acessado.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ssid"]'))
    )
    element.clear()  # Apagar texto SSID   
    print("SSID 5G removido com sucesso.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ssid"]'))
    )
    element.send_keys('eduroam') # Colocar SSID texto "eduroam"
    print("Texto SSID 'eduroam' colocado.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="_sec"]/div/div[1]'))
    )
    element.click()  # Segurança
    print(" Menu suspenso sobre 'Segurança' acionado.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//li[contains(text(), "Sem Segurança")]'))
    )
    element.click() # Sem Segurança
    print("Habilitado 'Sem Segurança'.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="save"]/span'))
    )
    element.click()  # Salvar
    print("Alterações salvas com sucesso.")

    time.sleep(0.2)   

    print("Tentando acessar 192.168.0.1 ...")
    navegador.get('http://192.168.0.1/')
    print("Página acessada com sucesso.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 40).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="advanced"]/span[2]'))
    )
    element.click()
    print("'Avançado' acionado com sucesso.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 40).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="menuTree"]/li[10]/a/span[2]'))
    )
    element.click()
    print("'Ferramentas de Sistema' acionado com sucesso.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="menuTree"]/li[3]/a/span[2]'))  # Rede
    )
    element.click()  
    print("Rede.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="menuTree"]/li[3]/ul/li[1]/a/span')) # Internet
    )
    element.click()  
    print("Internet.")
    
    time.sleep(3)

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="wanBody"]/tr[2]/td[5]/span[2]')) # Apagando Interface WAN
    )
    element.click()  
    print("Interface WAN.")

    time.sleep(3)

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="alert-container"]/div/div[4]/div/div[2]/div/div[2]/button')) # Apagando Interface WAN
    )
    element.click()  
    print("Confirmado apagar Interface WAN.")

    time.sleep(3)

    print("Tentando acessar 192.168.0.1 ...")
    navegador.get('http://192.168.0.1/')
    print("Página acessada com sucesso.")

    time.sleep(0.2)

    element = WebDriverWait(navegador, 40).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="advanced"]/span[2]'))
    )
    element.click()
    print("'Avançado' acionado com sucesso.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 40).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="menuTree"]/li[10]/a/span[2]'))
    )
    element.click()
    print("'Ferramentas de Sistema' acionado com sucesso.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="menuTree"]/li[3]/a/span[2]'))  # Rede
    )
    element.click()  
    print("Rede.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="menuTree"]/li[3]/ul/li[1]/a/span')) # Internet
    )
    element.click()  
    print("Internet.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="addItem"]/div/div[2]')) # Adicionar
    )
    element.click()  
    print("Adicionar.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="_link_type"]/div/div[1]')) # IP dinamico para ponte
    )
    element.click()  
    print("IP dinamico para ponte.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//li[contains(text(), "Ponte")]'))
    )
    element.click() 
    print("Ponte ativado.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="eth-cfg"]/div[2]/label[2]/span[1]')) # VLAN habilitado
    )
    element.click()  
    print("VLAN 3500 habilitado.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="eth-vlan-id"]')) # Texo "3500" colocado 
    )
    element.send_keys("3500") 
    print("Texo '3500'.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="saveConnBtn"]/span')) # Salvar
    )
    element.click()   
    print("Alterações salvas com sucesso.")

    time.sleep(0.2)
     
    print("Tentando acessar 192.168.0.1 ...")
    navegador.get('http://192.168.0.1/')
    print("Página acessada com sucesso.")

    time.sleep(0.2)       

    element = WebDriverWait(navegador, 40).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="advanced"]/span[2]'))
    )
    element.click()
    print("'Avançado' acionado com sucesso.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 40).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="menuTree"]/li[10]/a/span[2]'))
    )
    element.click()
    print("'Ferramentas de Sistema' acionado com sucesso.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="menuTree"]/li[3]/a/span[2]'))  # Rede
    )
    element.click()  
    print("Rede.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="menuTree"]/li[3]/ul/li[1]/a/span')) # Internet
    )
    element.click()  
    print("Internet.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="addItem"]/div/div[2]')) # Adicionar
    )
    element.click()  
    print("Adicionar.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="_link_type"]/div/div[1]')) # IP estático
    )
    element.click()  
    print("IP dinâmico para estático.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//li[contains(text(), "IP Estático")]'))
    )
    element.click() 
    print("IP Estático ativado.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="eth-cfg"]/div[2]/label[2]/span[1]')) # VLAN habilitado
    )
    element.click()  
    print("VLAN 3501 habilitado.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="eth-vlan-id"]')) # Texo "3501" colocado 
    )
    element.send_keys("3501") 
    print("Texo '3501'.")

    time.sleep(0.2)   

    # Endereço IP

    element = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="eth-vlan-id"]'))
    )
    element.send_keys(Keys.TAB) 
    print("TAB IP.")

    time.sleep(0.2)

    element = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ip_basic_v4"]/div[1]/div/div[1]/input[1]')) 
    )
    element.send_keys(Keys.NUMPAD1 + Keys.NUMPAD7 + Keys.NUMPAD2)
    print(f"Inserido{oct1}")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ip_basic_v4"]/div[1]/div/div[1]/input[2]'))
    )
    element.send_keys(Keys.NUMPAD2 + Keys.NUMPAD4 + Keys.TAB) 
    print(f"Inserido{oct2}")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ip_basic_v4"]/div[1]/div/div[1]/input[3]'))
    )
    element.send_keys(Keys.NUMPAD1 + Keys.NUMPAD0 + Keys.NUMPAD8) 
    print(f"Inserido{oct3}")

    time.sleep(0.2) 

    element = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ip_basic_v4"]/div[1]/div/div[1]/input[4]'))
    )
    element.send_keys(oct4) 
    print(f"Inserido{oct4}")

    time.sleep(0.2) 

    element = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ip_basic_v4"]/div[1]/div/div[1]/input[4]'))
    )
    element.send_keys(Keys.TAB) 
    print("TAB pressionado.")    

    time.sleep(0.2)

    # Máscara de Sub-rede

    element = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ip_basic_v4"]/div[2]/div/div[1]/input[1]'))
    )
    element.send_keys(mask1) 
    print(f"Inserido {mask1}.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ip_basic_v4"]/div[2]/div/div[1]/input[2]'))
    )
    element.send_keys(mask2) 
    print(f"Inserido {mask2}.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ip_basic_v4"]/div[2]/div/div[1]/input[3]'))
    )
    element.send_keys(mask3) 
    print(f"Inserido {mask3}.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ip_basic_v4"]/div[2]/div/div[1]/input[4]'))
    )
    element.send_keys(mask4) 
    print(f"Inserido {mask4}.")

    time.sleep(0.2)  

    element = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ip_basic_v4"]/div[2]/div/div[1]/input[4]'))
    )
    element.send_keys(Keys.TAB) 
    print("TAB pressionado.")  

    time.sleep(0.2)   
    # Gateway

    element = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ip_basic_v4"]/div[3]/div/div[1]/input[1]'))
    )
    element.send_keys(gtw1) 
    print(f"Inserido {gtw1}.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ip_basic_v4"]/div[3]/div/div[1]/input[2]'))
    )
    element.send_keys(gtw2) 
    print(f"Inserido {gtw2}.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ip_basic_v4"]/div[3]/div/div[1]/input[3]'))
    )
    element.clear() 
    print(f"Removido texto.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ip_basic_v4"]/div[3]/div/div[1]/input[3]'))
    )
    element.send_keys(gtw3) 
    print(f"Inserido {gtw3}.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ip_basic_v4"]/div[3]/div/div[1]/input[4]'))
    )
    element.send_keys(gtw4) 
    print(f"Inserido {gtw4}.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ip_basic_v4"]/div[3]/div/div[1]/input[4]'))
    )
    element.send_keys(Keys.TAB) 
    print("TAB pressionado.")  

    time.sleep(0.2)
       
    # DNS Primário

    element = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ip_basic_v4"]/div[4]/div/div[1]/input[1]'))
    )
    element.send_keys(dns1_1) 
    print(f"Inserido {dns1_1}.")

    time.sleep(0.2) 

    element = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ip_basic_v4"]/div[4]/div/div[1]/input[2]'))
    )
    element.send_keys(dns1_2) 
    print(f"Inserido {dns1_2}.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ip_basic_v4"]/div[4]/div/div[1]/input[3]'))
    )
    element.send_keys(dns1_3) 
    print(f"Inserido {dns1_3}.")

    time.sleep(0.2) 

    element = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ip_basic_v4"]/div[4]/div/div[1]/input[4]'))
    )
    element.send_keys(dns1_4) 
    print(f"Inserido {dns1_4}.")

    time.sleep(0.2)

    element = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ip_basic_v4"]/div[4]/div/div[1]/input[4]'))
    )
    element.send_keys(Keys.TAB) 
    print(f"TAB pressionado.")

    time.sleep(0.2)

    # DNS Secundário

    element = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ip_basic_v4"]/div[5]/div/div[1]/input[1]'))
    )
    element.send_keys(dns2_1) 
    print(f"Inserido {dns2_1}.")

    time.sleep(0.2)

    element = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ip_basic_v4"]/div[5]/div/div[1]/input[2]'))
    )
    element.send_keys(dns2_2) 
    print(f"Inserido {dns2_2}.")

    time.sleep(0.2)

    element = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ip_basic_v4"]/div[5]/div/div[1]/input[3]'))
    )
    element.send_keys(dns2_3) 
    print(f"Inserido {dns2_3}.")

    time.sleep(0.2)

    element = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ip_basic_v4"]/div[5]/div/div[1]/input[4]'))
    )
    element.send_keys(dns2_4) 
    print(f"Inserido {dns2_4}.")

    time.sleep(0.2)

    element = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ip_basic_v4"]/div[5]/div/div[1]/input[4]'))
    )
    element.send_keys(Keys.TAB) 
    print("TAB pressionado.")

    time.sleep(0.2)

    # Avançado

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="ipoeClick"]'))
    )
    element.click()  
    print("Avançado.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="ip_adv_v4"]/div[1]/label[2]/span[1]'))
    )
    element.click()  
    print("Desmarcar NAT.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="saveConnBtn"]'))
    )
    element.click()  
    print("Alterações salvas com sucesso.")

    time.sleep(0.2)   

    print("Tentando acessar 192.168.0.1 ...")
    navegador.get('http://192.168.0.1/')
    print("Página acessada com sucesso.")

    time.sleep(0.2)

    element = WebDriverWait(navegador, 40).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="advanced"]/span[2]'))
    )
    element.click()
    print("'Avançado' acionado com sucesso.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 40).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="menuTree"]/li[10]/a/span[2]'))
    )
    element.click()
    print("'Ferramentas de Sistema' acionado com sucesso.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="menuTree"]/li[3]/a/span[2]'))  # Rede
    )
    element.click()  
    print("Rede.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="menuTree"]/li[3]/ul/li[3]/a/span')) # Interface de Agrupamento
    )
    element.click()  
    print("Interface de Agrupamento.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="add"]/div/span')) # Adicionar
    )
    element.click()  
    print("Adicionar.")

    time.sleep(0.2)   

    element = WebDriverWait(navegador, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="groupName"]')) # Adicionar um Novo Grupo
    )
    element.send_keys("desabilitados") 
    print("Adicionar um Novo Grupo.")

    time.sleep(0.2)

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="lanTableTd"]/div[1]/label/span[1]')) # LAN1
    )
    element.click()
    print("LAN1 marcado.")

    time.sleep(0.2)

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="lanTableTd"]/div[2]/label/span[1]')) # LAN2
    )
    element.click()
    print("LAN2 marcado.")

    time.sleep(0.2)

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="lanTableTd"]/div[3]/label/span[1]')) # LAN3
    )
    element.click()
    print("LAN3 marcado.")

    time.sleep(0.2)

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="lanTableTd"]/div[4]/label/span[1]')) # LAN4
    )
    element.click()
    print("LAN4 marcado.")

    time.sleep(0.2)

    element = WebDriverWait(navegador, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div[2]/form/div[3]/label/span[1]')) # Habilitar Isolamento de Grupo
    )
    element.click()
    print("'Isolamento de Grupo' habilitado.")

    time.sleep(0.2)

    # Horário de término
    end_time = time.time()
    end_local_time = time.localtime(end_time)
    print(f"Término: {time.strftime('%H:%M:%S', end_local_time)}")

    # Tempo gasto
    total_time = end_time - start_time
    print(f"Tempo total gasto: {total_time:.2f} segundos")

    print("Tentando acessar 192.168.0.1 ...")
    navegador.get('http://192.168.0.1/')
    print("Página acessada com sucesso.")
    print("Aguarde, gerando html...")

    # Criando uma página HTML para exibir no navegador
    end_time = time.time()
    total_time = end_time - start_time
    minutes, seconds = divmod(int(total_time), 60)
    formatted_time = f"{minutes} minutos e {seconds} segundos"

    # Preparar os dados para serem copiados de uma vez, separados por tabulações (\t)
    dados_para_copiar = f"{etiqueta}\t{ssid1}\t{novo_ip}\t{nome_completo_ap}"

    html_content = f"""
    <html>
    <head>
        <title>Configuração Concluída</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                color: #333;
                display: flex;
                justify-content: center;
                align-items: center;  /* Centralizar a div no centro da tela */
                height: 100vh;
                margin: 0;
                zoom: 1.8;  /* Zoom de 180% */
            }}
            .container {{
                background-color: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
                text-align: left;
                max-width: 800px;
                margin: auto;
                position: relative;  /* Para ajuste do posicionamento */
                top: -50px;  /* Subir a div em relação ao centro da tela */
            }}
            h1 {{
                color: #4CAF50;
                text-align: center;
            }}
            p {{
                font-size: 16px;
                margin: 10px 0;
            }}
            a {{
                display: inline-block;
                margin-top: 5px;
                padding: 10px 20px;
                background-color: #4CAF50;
                color: #fff;
                text-decoration: none;
                border-radius: 5px;
                text-align: center;
                cursor: pointer;
            }}
            a:hover {{
                background-color: #45a049;
            }}
            .highlight {{
                font-size: 18px;
                font-weight: bold;
                color: #FF5733;
                margin-top: 20px;
                text-align: center;
            }}
            .step-number {{
                display: inline-block;
                width: 25px;
                height: 25px;
                border-radius: 50%;
                background-color: #4CAF50;
                color: white;
                text-align: center;
                line-height: 25px;
                margin-right: 10px;
            }}
        </style>
        <script>
            function copyToClipboard(text) {{
                navigator.clipboard.writeText(text).then(function() {{
                    alert('Dados copiados: ' + text);
                }}, function(err) {{
                    alert('Erro ao copiar dados: ' + err);
                }});
            }}
        </script>
    </head>
    <body>
        <div class="container">
            <h1>Configuração Concluída com Sucesso!</h1>
            <p><span class="step-number">1</span> Desconectar o cabo da porta LAN.</p>
            <p><span class="step-number">2</span> Conectar o cabo com acesso à internet na porta WAN.</p>
            <p><span class="step-number">3</span> Para concluir a última etapa, clique no botão abaixo para copiar a URL:</p>
            <a href="javascript:void(0);" onclick="copyToClipboard('http://172.24.108.{int(numero)}')">Copiar URL</a>
            <hr>
            <p>Clique no botão abaixo para copiar os dados:</p>
            <a href="javascript:void(0);" onclick="copyToClipboard('{dados_para_copiar}')">Copiar Dados para Planilha</a>
            <div class="highlight">Tempo Gasto: {formatted_time}</div>
        </div>
    </body>
    </html>
    """

    # Injetando o conteúdo HTML diretamente no navegador
    navegador.execute_script(f"document.write({repr(html_content)});")

finally:
    print("O navegador já pode ser fechado.")
    time.sleep(60)   
    navegador.quit()
    print("Navegador fechado.")