
# Configuração Automática do Roteador Wireless TP-Link AC750

Este projeto oferece um script em Python que automatiza a configuração inicial do Roteador Wireless TP-Link AC750, utilizando o Selenium WebDriver. Com a capacidade de configurar diversos aspectos do roteador, como SSIDs, senhas, DHCP, IPs estáticos, entre outros, o script é projetado para otimizar significativamente o tempo necessário para a configuração e reduzir a possibilidade de erros humanos.

## ⚙️ Requisitos

Para utilizar este script, certifique-se de ter os seguintes componentes instalados em seu ambiente:

- **Python 3.8 ou superior**
- **Selenium**
- **ChromeDriver**

## 🚀 Instalação

### Clonando o Repositório

Siga as instruções abaixo para clonar o repositório e instalar as dependências necessárias:

```bash
git clone https://github.com/xth3usx/easyap.git

```

## 📦 Downloads Diretos

Se preferir, você pode baixar os arquivos diretamente nos formatos comprimidos:

- [Baixar como ZIP](#)
- [Baixar como TAR.GZ](#)

## 🗂 Estrutura do Projeto

A estrutura do projeto está organizada da seguinte forma:

- **easyAC750.py**: Script principal de automação.
- **config.py**: Arquivo de configuração contendo parâmetros ajustáveis.
- **utils.py**: Funções auxiliares para processamento de IPs e máscaras de sub-rede.
- **log.txt**: Arquivo de log que registra todas as ações realizadas pelo script.
- **.gitignore**: Arquivo para excluir arquivos temporários e de log do controle de versão.

## 🛠 Uso

Para executar o script e iniciar o processo de automação da configuração do roteador, utilize o seguinte comando:

```bash
python easyAC750.py
```

O script realizará todas as configurações necessárias via interface web do roteador, conforme as definições especificadas no arquivo `config.py`.

## 📋 Log

As configurações aplicadas pelo script são registradas em um arquivo de log (`log.txt`). Este log é útil para auditorias e para acompanhar as alterações realizadas durante o processo de configuração.

## 🤝 Contribuição

Contribuições são sempre bem-vindas! Se você deseja contribuir com o projeto, siga os passos abaixo:

1. Faça um fork do projeto.
2. Crie uma branch para suas modificações (`git checkout -b minha-feature`).
3. Envie suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. Envie um pull request.