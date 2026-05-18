from flask import Flask, redirect, render_template_string
app = Flask(__name__)
bibliotecas = {
    "flask": ("Flask", "Eliana", "Aplicação web com rotas.", "http://127.0.0.1:5010"),
    "jinja": ("Jinja", "Eliana", "Python enviando dados para HTML.", "http://127.0.0.1:5011"),
    "django": ("Django", "Mohamed", "Framework robusto explicado de forma didática.", "http://127.0.0.1:5012"),
    "fastapi": ("FastAPI", "Mohamed", "API rápida com resposta JSON.", "http://127.0.0.1:5004"),
    "selenium": ("Selenium", "Pauliane", "Automação de navegador.", "http://127.0.0.1:5005"),
    "streamlit": ("Streamlit", "Pauliane", "Dashboard interativo.", "http://localhost:8501"),
    "requests": ("Requests", "Rafael", "Requisições HTTP.", "http://127.0.0.1:5001"),
    "beautifulsoup": ("BeautifulSoup", "Rafael", "Extração de HTML.", "http://127.0.0.1:5002"),
}
HTML = """<!DOCTYPE html><html><head><meta charset='UTF-8'><title>Esquadrão 5</title><style>*{box-sizing:border-box}body{margin:0;min-height:100vh;font-family:Arial;background:radial-gradient(circle at top,rgba(224,160,80,.22),transparent 35%),#050816;color:#f4f4f4;padding:40px}.voltar{position:fixed;top:26px;left:26px;background:#e0a050;color:#111;padding:12px 18px;border-radius:10px;text-decoration:none;font-weight:bold}.card{width:92%;max-width:720px;margin:55px auto;background:#141b24;border:1px solid #d99545;border-radius:18px;padding:36px;box-shadow:0 0 30px rgba(217,149,69,.35)}h1{color:#e0a050;text-align:center;text-transform:uppercase}p{line-height:1.6}label{display:block;margin-top:14px;color:#e8c38f;font-weight:bold}input,select,textarea{width:100%;padding:13px;border-radius:9px;border:1px solid #303744;background:#080c14;color:white;font-weight:bold}button{width:100%;margin-top:20px;padding:14px;border:none;border-radius:10px;background:#e0a050;color:#111;font-weight:bold;cursor:pointer}.resultado{margin-top:24px;border:1px solid #2ecc71;border-radius:12px;padding:20px;background:#0d1118}.resultado h2{color:#2ecc71}</style><style>.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:20px;max-width:1100px;margin:auto}.box{background:#141b24;border:1px solid #d99545;border-radius:16px;padding:24px}.box h2{color:#e0a050;margin:0}.box small{color:#2ecc71;font-weight:bold}.box a{display:block;text-align:center;margin-top:18px;background:#e0a050;color:#111;padding:12px;border-radius:9px;text-decoration:none;font-weight:bold}.topo{text-align:center;margin:35px auto}.topo h1{font-size:48px}</style></head><body><div class='topo'><h1>ESQUADRÃO 5</h1><h2>OS ARQUITETOS WEB</h2><p>Versão resumida • didática • AO VIVO</p></div><div class='grid'>{% for chave,item in bibliotecas.items() %}<div class='box'><h2>{{item[0]}}</h2><small>{{item[1]}}</small><p>{{item[2]}}</p><a href='/abrir/{{chave}}'>Rodar ao vivo</a></div>{% endfor %}</div></body></html>"""
@app.route('/')
def home(): return render_template_string(HTML,bibliotecas=bibliotecas)
@app.route('/abrir/<nome>')
def abrir(nome): return redirect(bibliotecas[nome][3])
if __name__=='__main__': app.run(debug=True, port=5000)
