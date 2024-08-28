
# Configuração Automática do Roteador Wireless TP-Link AC750

Este projeto oferece um script em Python que automatiza a configuração inicial do Roteador Wireless TP-Link AC750, utilizando o Selenium WebDriver. Com a capacidade de configurar diversos aspectos do roteador, como SSIDs, senhas, DHCP, IPs estáticos, entre outros, o script é projetado para otimizar significativamente o tempo de configuração, garantindo maior eficiência e consistência no processo, além de reduzir eventuais falhas durante a configuração.

## ⚙️ Requisitos

Para utilizar este script, certifique-se de ter os seguintes componentes instalados em seu ambiente:

- **Python 3.8 ou superior**
- **Selenium**
- **ChromeDriver**

## 🚀 Instalação

#### Windows:

1. **Instalar o Python 3.11.5**:
   - Abra o PowerShell e execute o comando abaixo para baixar e instalar o Python automaticamente:
   ```powershell
   Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe -OutFile python-installer.exe
   Start-Process -FilePath "python-installer.exe" -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -Wait
   ```

2. **Garantir que o pip está instalado e atualizado**:
   ```powershell
   python -m ensurepip --upgrade
   ```

3. **Instalar as dependências (Selenium e ChromeDriver Auto Installer)**:
   ```powershell
   pip install selenium
   pip install webdriver-manager
   pip install pyfiglet
   pip install art
   pip install chromedriver-autoinstaller
   ```

### Linux:

1. **Instalar o Python 3.11.5**:
   - Abra o terminal e execute os seguintes comandos para baixar, compilar e instalar o Python 3.11.5:

   ```bash
   sudo apt update
   sudo apt install -y build-essential libssl-dev zlib1g-dev libncurses5-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

   wget https://www.python.org/ftp/python/3.11.5/Python-3.11.5.tgz
   tar -xvf Python-3.11.5.tgz
   cd Python-3.11.5
   ./configure --enable-optimizations
   make -j "$(nproc)"
   sudo make altinstall
   ```

2. **Garantir que o pip está instalado e atualizado**:
   ```bash
   python3 -m ensurepip --upgrade
   python3 -m pip install --upgrade pip
   ```

3. **Instalar as dependências (Selenium e ChromeDriver Auto Installer)**:
   ```bash
   python3 -m pip install selenium
   python3 -m pip install webdriver-manager
   python3 -m pip install pyfiglet
   python3 -m pip install art
   python3 -m pip install chromedriver-autoinstaller


### Configurando o Ambiente

Antes de executar o script, certifique-se de que todos os navegadores Chrome estejam fechados. Isso é necessário para garantir que o Selenium WebDriver possa iniciar e controlar o navegador sem interrupções.

## 📦 Downloads Diretos

Se preferir, você pode baixar os arquivos diretamente nos formatos comprimidos:

- [Baixar como ZIP](https://github.com/xth3usx/easyap/archive/refs/tags/v1.0.0.zip)
- [Baixar como .tar.gz](https://github.com/xth3usx/easyap/archive/refs/tags/v1.0.0.tar.gz)


## 🗂 Estrutura do Projeto

A estrutura do projeto está organizada da seguinte forma:

- **easyAC750.py**: Script principal de automação.
- **config.py**: Arquivo de configuração contendo parâmetros ajustáveis.
- **utils.py**: Funções auxiliares para processamento de IPs e máscaras de sub-rede.
- **html.py**: Responsável pela geração dinâmica de uma página HTML que confirma a conclusão da instalação do dispositivo, exibindo informações detalhadas sobre o processo finalizado, como IP, MAC e tempo gasto.

## 🛠 Uso

Para executar o script e iniciar o processo de automação da configuração do roteador, utilize o seguinte comando:

```bash
python easyAC750.py
```

O script realizará todas as configurações necessárias via interface web do roteador, conforme as definições especificadas no arquivo `config.py`.

## 📋 Log

As configurações aplicadas pelo script são registradas em um arquivo de log (`log.txt`). Este log é útil para auditorias e para acompanhar as alterações realizadas durante o processo de configuração.