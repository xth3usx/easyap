# Configuração Automática do Roteador Wireless TP-Link AC750

Bem-vindo ao repositório **easyAP**! Este projeto contém um script em Python que automatiza a configuração inicial de um Roteador Wireless TP-Link AC750, utilizando o Selenium WebDriver. O script é capaz de configurar múltiplos aspectos do roteador, como SSIDs, senhas, DHCP, IPs estáticos, entre outros, tornando-o ideal tanto para ambientes corporativos quanto residenciais.

## ⚙️ Requisitos

Para utilizar este script, você precisará dos seguintes componentes instalados em seu ambiente:

- **Python 3.8 ou superior**
- **Selenium**
- **ChromeDriver**

## 🚀 Instalação

### Clonando o Repositório

Siga as instruções abaixo para clonar o repositório e instalar as dependências necessárias:

#### No Linux:
```bash
git clone https://github.com/xth3usx/easyap.git
cd easyap
pip install -r requirements.txt
No Windows:
bash
Copiar código
git clone https://github.com/xth3usx/easyap.git
cd easyap
pip install -r requirements.txt
📦 Downloads Diretos
Se preferir, você pode baixar os arquivos diretamente nos formatos comprimidos:

Baixar como ZIP
Baixar como TAR.GZ
🗂 Estrutura do Projeto
A estrutura do projeto é organizada da seguinte forma:

easyAC750.py: Script principal de automação.
config.py: Arquivo de configuração contendo parâmetros ajustáveis.
utils.py: Funções auxiliares para processamento de IPs e máscaras de sub-rede.
log.txt: Arquivo de log que registra todas as ações realizadas pelo script.
.gitignore: Arquivo para excluir arquivos temporários e de log do controle de versão.
🛠 Uso
Para executar o script e iniciar o processo de automação da configuração do roteador, utilize o seguinte comando:

bash
Copiar código
python easyAC750.py
O script realizará todas as configurações necessárias via interface web do roteador, conforme as definições especificadas no arquivo config.py.

📋 Log
As configurações aplicadas pelo script são registradas em um arquivo de log (log.txt). Este log é útil para auditorias e para acompanhar as alterações realizadas durante o processo de configuração.

🤝 Contribuição
Contribuições são sempre bem-vindas! Se você deseja contribuir com o projeto, siga os passos abaixo:

Faça um fork do projeto.
Crie uma branch para suas modificações (git checkout -b minha-feature).
Envie suas mudanças (git commit -am 'Adiciona nova feature').
Envie um pull request.
📝 Licença
Este projeto é distribuído sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.