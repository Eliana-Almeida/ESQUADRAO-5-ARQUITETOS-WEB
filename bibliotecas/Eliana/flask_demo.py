# Importa ferramentas necessárias do Flask
# Flask cria o servidor web
# request captura dados enviados pelo formulário
# render_template_string renderiza HTML diretamente no Python
from flask import Flask, request, render_template_string


# Cria a aplicação Flask
app = Flask(__name__)


# Define toda a estrutura visual da página HTML
# Aqui ficam o layout, estilos CSS e componentes visuais
HTML = """<!DOCTYPE html><html><head><meta charset='UTF-8'><title>Flask ao Vivo</title><style>*{box-sizing:border-box}body{margin:0;min-height:100vh;font-family:Arial;background:radial-gradient(circle at top,rgba(224,160,80,.22),transparent 35%),#050816;color:#f4f4f4;padding:40px}.voltar{position:fixed;top:26px;left:26px;background:#e0a050;color:#111;padding:12px 18px;border-radius:10px;text-decoration:none;font-weight:bold}.card{width:92%;max-width:720px;margin:55px auto;background:#141b24;border:1px solid #d99545;border-radius:18px;padding:36px;box-shadow:0 0 30px rgba(217,149,69,.35)}h1{color:#e0a050;text-align:center;text-transform:uppercase}p{line-height:1.6}label{display:block;margin-top:14px;color:#e8c38f;font-weight:bold}input,select,textarea{width:100%;padding:13px;border-radius:9px;border:1px solid #303744;background:#080c14;color:white;font-weight:bold}button{width:100%;margin-top:20px;padding:14px;border:none;border-radius:10px;background:#e0a050;color:#111;font-weight:bold;cursor:pointer}.resultado{margin-top:24px;border:1px solid #2ecc71;border-radius:12px;padding:20px;background:#0d1118}.resultado h2{color:#2ecc71}</style></head><body><a class='voltar' href='http://127.0.0.1:5000'>← Voltar ao Portal</a><div class='card'><h1>Flask ao Vivo</h1><p>Flask cria páginas web com Python, rotas e respostas no navegador.</p><form method='POST'><label>Nome</label><input name='nome' value='{{nome}}'><label>Curso</label><input name='curso' value='{{curso}}'><button>Executar ao vivo</button></form>{% if resultado %}<div class='resultado'><h2>Resultado processado pelo Python</h2><p><b>Nome:</b> {{nome}}</p><p><b>Curso:</b> {{curso}}</p><p>O Flask recebeu dados pela rota e respondeu em HTML.</p></div>{% endif %}</div></body></html>"""


# Cria a rota principal da aplicação
# GET abre a página
# POST envia dados do formulário para o Python
@app.route('/', methods=['GET','POST'])
def home():

    # Define valores iniciais exibidos na tela
    nome='Eliana'
    curso='Python Web'
    resultado=False

    # Verifica se o usuário clicou no botão do formulário
    if request.method=='POST':

        # Captura os dados enviados pelo navegador
        nome=request.form.get('nome')
        curso=request.form.get('curso')

        # Ativa a exibição do resultado processado
        resultado=True

    # Renderiza o HTML e envia os dados processados para a página
    return render_template_string(
        HTML,
        nome=nome,
        curso=curso,
        resultado=resultado
    )


# Verifica se o arquivo está sendo executado diretamente
if __name__=='__main__':

    # Executa o servidor Flask localmente na porta 5010
    app.run(debug=True, port=5010)