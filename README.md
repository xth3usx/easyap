

# Configuração Automática do Roteador Wireless TP-Link AC750

Este repositório contém um script Python para automação da configuração inicial de um Roteador Wireless TP-Link AC750 usando Selenium WebDriver. O script configura múltiplos aspectos do roteador como SSIDs, senhas, DHCP, IPs estáticos e mais, ideal para uso em ambientes corporativos ou residenciais.

## Requisitos

- Python 3.8 ou superior
- Selenium
- ChromeDriver

## Instalação

### Clonando o Repositório

Para clonar o repositório e instalar as dependências, use:

#### No Linux:
```bash
git clone https://github.com/xth3usx/easyap.git
cd easyap
pip install -r requirements.txt

No Windows:

git clone https://github.com/xth3usx/easyap.git
cd easyap
pip install -r requirements.txt

Downloads Diretos

Você também pode baixar os arquivos diretamente em formatos comprimidos:

Baixar como ZIP
Baixar como TAR.GZ

Estrutura do Projeto

O projeto contém:

easyAC750.py: O script principal de automação.
config.py: Arquivo de configuração com parâmetros ajustáveis.
utils.py: Funções auxiliares para processamento de IP e máscaras de sub-rede.
log.txt: Arquivo de log que registra todas as ações realizadas pelo script.
.gitignore: Para excluir arquivos temporários e de log do controle de versão.

Uso

Execute o script com o seguinte comando:
python easyAC750.py

O script automatiza as configurações via interface web do roteador de acordo com as definições do arquivo config.py.



