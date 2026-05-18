from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
app = FastAPI()
@app.get('/', response_class=HTMLResponse)
def home():
    return '''<!DOCTYPE html><html><head><meta charset="UTF-8"><title>FastAPI ao Vivo</title><style>body{margin:0;min-height:100vh;background:radial-gradient(circle at top,rgba(224,160,80,.22),transparent 35%),#050816;color:white;font-family:Arial;padding:40px}a{position:fixed;top:26px;left:26px;background:#e0a050;color:#111;padding:12px 18px;border-radius:10px;text-decoration:none;font-weight:bold}.card{max-width:720px;margin:55px auto;background:#141b24;border:1px solid #d99545;border-radius:18px;padding:36px}h1{color:#e0a050;text-align:center}.resultado{border:1px solid #2ecc71;border-radius:12px;padding:20px;background:#0d1118}</style></head><body><a href="http://127.0.0.1:5000">← Voltar ao Portal</a><div class="card"><h1>FASTAPI AO VIVO</h1><p>FastAPI cria APIs rápidas. API é ponte de comunicação entre sistemas.</p><div class="resultado"><h2>Rota funcionando</h2><p>Acesse: <b>http://127.0.0.1:5004/api</b></p></div></div></body></html>'''
@app.get('/api')
def api(): return {'biblioteca':'FastAPI','status':'funcionando','uso':'criar APIs rápidas'}
if __name__=='__main__': uvicorn.run(app, host='127.0.0.1', port=5004)
