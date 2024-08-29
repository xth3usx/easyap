# Gerador do HTML de confirmação da conclusão
def gerar_html(ip,mac,ftime):
    html = f"""
            <html>
            <head>
                <title>Configuração concluída com sucesso!</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        background-color: #f4f4f4;
                        color: #333;
                        display: flex;
                        justify-content: center;
                        align-items: flex-start;  /* Alinhar ao topo */
                        height: 100vh;
                        margin: 0;
                        zoom: 1.8;  
                    }}
                    .container {{
                        background-color: #fff;
                        padding: 20px;
                        border-radius: 8px;
                        box-shadow: 0 0 10px rgba(0,0,0,0.1);
                        max-width: 800px;
                        width: 100%;  /* Garantir que o container utilize toda a largura disponível */
                        text-align: center;
                        display: flex;
                        flex-direction: column;
                        align-items: center;
                        margin-top: 20px; /* Menos margem superior para aproximar do topo */
                        margin-bottom: 20px; /* Margem inferior para adicionar espaço no final */
                    }}
                    h1 {{
                        color: #4CAF50;
                        margin-bottom: 20px;
                    }}
                    p {{
                        font-size: 16px;
                        margin: 10px 0;
                        text-align: left;
                        width: 100%;  /* Garantir que o texto ocupe toda a largura do container */
                    }}
                    .card {{
                        background-color: #e0e0e0;
                        border: 1px solid #ddd;
                        border-radius: 8px;
                        padding: 20px;
                        margin: 10px;
                        width: 80%;
                        max-width: 600px;
                        font-size: 20px;
                        font-weight: bold;
                        color: #333;
                        text-align: center;
                        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
                    }}
                    .highlight {{
                        background-color: #FF5733;
                        color: #fff;
                        padding: 20px;
                        border-radius: 8px;
                        margin-top: 20px;
                        width: 80%;
                        max-width: 600px;
                        font-size: 20px;
                        font-weight: bold;
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
                    <h1>Configuração da primeira etapa concluída com sucesso! </h1>
                    <p>Para concluir a última etapa:</p>
                    <p><span class="step-number">1</span> Desconecte o cabo de rede da porta LAN do dispositivo.</p>
                    <p><span class="step-number">2</span> Conecte o cabo de internet à porta WAN do roteador.</p>
                    <p><span class="step-number">2</span> Acesse a página do roteador usando o endereço IP fornecido e, após o login, desative o serviço DHCP.</p>
                    
                    <div class="card">{ip}</div>
                    <div class="card">{mac}</div>
                    <div class="highlight">Tempo Gasto: {ftime}</div>
                </div>
            </body>
            </html>
            """
    return html
  