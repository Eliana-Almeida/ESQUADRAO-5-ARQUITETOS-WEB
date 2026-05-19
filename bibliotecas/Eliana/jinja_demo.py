# Importa Flask para criar servidor web e Jinja para renderizar dados no HTML
from flask import Flask, request, render_template_string

# Cria aplicação Flask
app = Flask(__name__)

# HTML com variáveis Jinja: {{produto}}, {{status}} e {{resultado}}
HTML = """<html><head><meta charset='UTF-8'><title>Jinja ao Vivo</title></head><body style='background:#050816;color:white;font-family:Arial;padding:40px'><h1 style='color:#e0a050'>Jinja ao Vivo</h1><p>Jinja conecta o Python ao HTML usando variáveis dinâmicas.</p><form method='POST'><label>Produto</label><input name='produto' value='{{produto}}' style='width:100%;padding:12px'><label>Status</label><input name='status' value='{{status}}' style='width:100%;padding:12px'><button style='width:100%;padding:14px;background:#e0a050;border:none;font-weight:bold'>Executar ao vivo</button></form>{% if resultado %}<div style='margin-top:20px;border:1px solid #2ecc71;padding:20px'><h2>Resultado processado pelo Jinja</h2><p><b>Produto:</b> {{produto}}</p><p><b>Status:</b> {{status}}</p></div>{% endif %}</body></html>"""

# Rota principal: GET abre a página, POST recebe dados do formulário
@app.route('/', methods=['GET','POST'])
def home():
    # Valores iniciais enviados para o HTML
    produto = 'Sistema Web'
    status = 'Disponível'
    resultado = False

    # Se o formulário for enviado, captura os dados digitados
    if request.method == 'POST':
        produto = request.form.get('produto')
        status = request.form.get('status')
        resultado = True

    # Renderiza o HTML e injeta as variáveis do Python na página
    return render_template_string(HTML, produto=produto, status=status, resultado=resultado)

# Executa servidor local na porta 5011
if __name__ == '__main__':
    app.run(debug=True, port=5011)