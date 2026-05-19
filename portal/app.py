# Importa o Flask para criar a aplicação web
# Importa o request para capturar dados enviados pelo formulário
from flask import Flask, request


# Cria a aplicação Flask
app = Flask(__name__)


# Define a rota principal do sistema
# GET abre a página no navegador
# POST envia os dados do formulário para o Python
@app.route("/", methods=["GET", "POST"])
def home():

    # Cria variáveis iniciais vazias
    nome = ""
    cpf = ""
    curso = ""

    # Variável que vai guardar o resultado processado pelo Python
    resultado = ""

    # Verifica se o usuário enviou o formulário
    if request.method == "POST":

        # Captura os dados digitados pelo usuário no navegador
        nome = request.form.get("nome")
        cpf = request.form.get("cpf")
        curso = request.form.get("curso")

        # Monta o resultado que será exibido na tela
        resultado = f"""
        <div class="resultado">
            <h2>Dados recebidos pelo Python</h2>

            <p><strong>Nome:</strong> {nome}</p>
            <p><strong>CPF:</strong> {cpf}</p>
            <p><strong>Curso:</strong> {curso}</p>

            <p>
            O Flask recebeu o formulário,
            processou os dados e devolveu esta resposta
            no navegador.
            </p>
        </div>
        """

    # Retorna a página HTML completa para o navegador
    return f"""
    <!DOCTYPE html>
    <html lang="pt-br">

    <head>
        <meta charset="UTF-8">
        <title>Flask Ao Vivo</title>

        <style>

            body {{
                background: #020617;
                color: white;
                font-family: Arial;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}

            .card {{
                width: 500px;
                background: #0f172a;
                border: 1px solid #f0a84b;
                border-radius: 20px;
                padding: 30px;
                box-shadow: 0 0 30px rgba(240,168,75,0.4);
            }}

            h1 {{
                text-align: center;
                color: #f0a84b;
                font-size: 50px;
            }}

            label {{
                display: block;
                margin-top: 15px;
                color: #f0a84b;
                font-weight: bold;
            }}

            input, select {{
                width: 100%;
                padding: 12px;
                margin-top: 5px;
                border-radius: 8px;
                border: 1px solid #1e293b;
                background: #020617;
                color: white;
            }}

            button {{
                width: 100%;
                padding: 14px;
                margin-top: 20px;
                border: none;
                border-radius: 10px;
                background: #f0a84b;
                color: black;
                font-weight: bold;
                cursor: pointer;
            }}

            .resultado {{
                margin-top: 25px;
                padding: 20px;
                border: 1px solid #00ff99;
                border-radius: 12px;
                background: #020617;
            }}

            .resultado h2 {{
                color: #00ff99;
            }}

        </style>
    </head>

    <body>

        <div class="card">

            <h1>FLASK AO VIVO</h1>

            <p>
            Esta página prova que o Flask está funcionando:
            o usuário preenche o formulário,
            o Python recebe os dados e devolve
            uma resposta dinâmica no navegador.
            </p>

            <form method="POST">

                <label>Nome</label>
                <input
                    type="text"
                    name="nome"
                    placeholder="Digite seu nome completo"
                >

                <label>CPF</label>
                <input
                    type="text"
                    name="cpf"
                    placeholder="000.000.000-00"
                >

                <label>Curso</label>

                <select name="curso">

                    <option>Python para Web</option>
                    <option>Inteligência Artificial</option>
                    <option>Automação</option>
                    <option>Desenvolvimento Web</option>

                </select>

                <button type="submit">
                    Enviar para o Python
                </button>

            </form>

            {resultado}

        </div>

    </body>
    </html>
    """


# Garante que o servidor só execute quando este arquivo for rodado diretamente
if __name__ == "__main__":

    # Executa o Flask em modo debug na porta 5010
    app.run(debug=True, port=5010)