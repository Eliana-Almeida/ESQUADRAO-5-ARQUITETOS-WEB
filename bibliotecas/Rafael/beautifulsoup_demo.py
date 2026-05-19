# Importa Flask para criar servidor web
from flask import Flask, request, render_template_string

# Importa BeautifulSoup para ler HTML
from bs4 import BeautifulSoup

# Cria aplicação Flask
app = Flask(__name__)

# HTML da página com formulário e resultado
HTML = """<html><head><meta charset='UTF-8'><title>BeautifulSoup ao Vivo</title></head><body style='background:#050816;color:white;font-family:Arial;padding:40px'><h1 style='color:#e0a050'>BeautifulSoup ao Vivo</h1><form method='POST'><textarea name='codigo' style='width:100%;height:220px'><html><head><title>Esquadrão 5</title></head><body><h1>Python Web</h1></body></html></textarea><button style='width:100%;padding:14px;background:#e0a050;border:none;font-weight:bold'>Executar ao vivo</button></form>{% if resultado %}<div style='margin-top:20px;border:1px solid #2ecc71;padding:20px'><h2>Título encontrado: {{titulo}}</h2></div>{% endif %}</body></html>"""

# Rota principal: GET abre a página, POST processa o formulário
@app.route('/', methods=['GET','POST'])
def home():
    # Variáveis iniciais
    titulo = ''
    resultado = False

    # Se o usuário clicar no botão, o Python processa o HTML
    if request.method == 'POST':
        codigo = request.form.get('codigo')
        soup = BeautifulSoup(codigo, 'html.parser')
        titulo = soup.title.text if soup.title else 'Sem título'
        resultado = True

    # Devolve a página com o resultado
    return render_template_string(HTML, titulo=titulo, resultado=resultado)

# Executa servidor local na porta 5002
if __name__ == '__main__':
    app.run(debug=True, port=5002)