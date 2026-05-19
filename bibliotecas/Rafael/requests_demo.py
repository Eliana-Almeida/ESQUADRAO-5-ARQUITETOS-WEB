# Importa ferramentas necessárias do Flask
# Flask cria o servidor web
# request captura dados enviados pelo formulário
# render_template_string renderiza HTML diretamente no Python
from flask import Flask, request, render_template_string


# Cria a aplicação Flask
app = Flask(__name__)


# Define toda a estrutura visual da página HTML
# Aqui ficam o layout, estilos CSS e elementos visuais
HTML = """<!DOCTYPE html><html><head><meta charset='UTF-8'><title>Requests ao Vivo</title><style>*{box-sizing:border-box}body{margin:0;min-height:100vh;font-family:Arial;background:radial-gradient(circle at top,rgba(224,160,80,.22),transparent 35%),#050816;color:#f4f4f4;padding:40px}.voltar{position:fixed;top:26px;left:26px;background:#e0a050;color:#111;padding:12px 18px;border-radius:10px;text-decoration:none;font-weight:bold}.card{width:92%;max-width:720px;margin:55px auto;background:#141b24;border:1px solid #d99545;border-radius:18px;padding:36px;box-shadow:0 0 30px rgba(217,149,69,.35)}h1{color:#e0a050;text-align:center;text-transform:uppercase}p{line-height:1.6}label{display:block;margin-top:14px;color:#e8c38f;font-weight:bold}input,select,textarea{width:100%;padding:13px;border-radius:9px;border:1px solid #303744;background:#080c14;color:white;font-weight:bold}button{width:100%;margin-top:20px;padding:14px;border:none;border-radius:10px;background:#e0a050;color:#111;font-weight:bold;cursor:pointer}.resultado{margin-top:24px;border:1px solid #2ecc71;border-radius:12px;padding:20px;background:#0d1118}.resultado h2{color:#2ecc71}</style></head><body><a class='voltar' href='http://127.0.0.1:5000'>← Voltar ao Portal</a><div class='card'><h1>Requests ao Vivo</h1><p>Requests permite conversar com sites e APIs usando requisições HTTP.</p><form method='POST'><label>URL</label><input name='url' value='{{url}}'><button>Executar ao vivo</button></form>{% if resultado %}<div class='resultado'><h2>Resultado processado pelo Python</h2><p><b>URL:</b> {{url}}</p><p><b>Status:</b> {{status}}</p><p>O Python enviou uma requisição e recebeu resposta do servidor.</p></div>{% endif %}</div></body></html>"""


# Cria a rota principal da aplicação
# GET abre a página
# POST envia dados do formulário para o Python
@app.route('/', methods=['GET','POST'])
def home():

    # Importa a biblioteca Requests
    # Requests permite enviar requisições HTTP para sites e APIs
    import requests

    # Define valores iniciais
    url='https://example.com'
    status=''
    resultado=False

    # Verifica se o usuário enviou o formulário
    if request.method=='POST':

        # Captura a URL digitada pelo usuário
        url=request.form.get('url')

        # Tenta acessar o site informado
        try:

            # Envia uma requisição HTTP GET
            # timeout evita travamentos demorados
            status=requests.get(url,timeout=5).status_code

        # Caso ocorra erro de conexão
        except Exception:

            # Exibe mensagem de erro
            status='Erro de conexão'

        # Ativa a exibição do resultado
        resultado=True

    # Renderiza o HTML e envia os dados processados para a página
    return render_template_string(
        HTML,
        url=url,
        status=status,
        resultado=resultado
    )


    return render_template_string(
        HTML,
        url=url,
        status=status,
        resultado=resultado
    )

# Verifica se o arquivo está sendo executado diretamente
if __name__ == '__main__':

    # Executa o servidor Flask localmente na porta 5001
    app.run(debug=False, port=5001)