import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import date, timedelta

app = Flask(__name__)
app.secret_key = "f7s7hqy8W8HEJQ9JSJiiye8998H"

def init_db():
    conexao = sqlite3.connect("Banco.DB")
    cursor = conexao.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS banco_corretivo(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(50),
            email VARCHAR(50),
            cores VARCHAR(10),
            tamanho INT,
            quantidade INT,
            prazo DATE,
            status VARCHAR(20),
            resposta VARCHAR(100),
            data DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    conexao.commit()
    conexao.close()

init_db()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pedido", methods=["POST"])
def novo_pedido():
    if request.method == "POST":
        nome = request.form.get("nome").capitalize()
        email = request.form.get("email").strip()
        cores = request.form.get("cores").capitalize()
        tamanho = int(request.form.get("tamanho"))
        quantidade = int(request.form.get("quantidade"))
        prazo = request.form.get("prazo")

        tamanhos_permitidos = [2, 4, 6, 8, 10, 12]

        if tamanho not in tamanhos_permitidos:
            flash("O tamanho da paleta deve ser 2, 4, 6, 8, 10 ou 12 cores.")
            return redirect(url_for("index"))

        if quantidade > 5:
            flash("A quantidade máxima é de 5 paletas.")
            return redirect(url_for("index"))

        data_minima = date.today() + timedelta(days=15)

        if date.fromisoformat(prazo) < data_minima:
            flash("O prazo deve ser de no mínimo 15 dias.")
            return redirect(url_for("index"))

        conexao = sqlite3.connect("Banco.DB")
        cursor = conexao.cursor()
        cursor.execute(
            """
            INSERT INTO banco_corretivo (nome, email, cores, tamanho, quantidade, prazo, status) 
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (nome, email, cores, tamanho, quantidade, prazo, "Pendente")
        )
        conexao.commit()
        conexao.close()

        flash("Pedido enviado com sucesso!")
        return redirect(url_for("index"))

USUARIOS = {
    "nome_adm": {"senha": "123"},
}

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        usuario_input = request.form["usuario"].strip().lower()
        senha_input = request.form["senha"]

        if usuario_input in USUARIOS:

            dados = USUARIOS[usuario_input]

            if senha_input == dados["senha"]:
                session["usuario"] = usuario_input
                return redirect(url_for("admin"))

        return render_template("login.html", erro="Usuário ou senha incorretos.")

    return render_template("login.html")

@app.route("/admin")
def admin():

    if "usuario" not in session:
        return redirect(url_for("login"))

    usuario = session["usuario"]

    conexao = sqlite3.connect("Banco.DB")
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, nome, email, cores, tamanho, quantidade, prazo, status, resposta, data
        FROM banco_corretivo
        ORDER BY data DESC
    """)

    pedidos = cursor.fetchall()
    
    conexao.close()

    return render_template("admin.html", usuario=usuario, pedidos=pedidos)

@app.route("/pedido/<int:id>", methods=["GET", "POST"])
def analisar_pedido(id):

    if "usuario" not in session:
        return redirect(url_for("login"))

    conexao = sqlite3.connect("Banco.DB")
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM banco_corretivo WHERE id = ?",
        (id,)
    )

    pedido = cursor.fetchone()

    if request.method == "POST":

        resposta = request.form["resposta"]
        status = request.form["status"]

        cursor.execute(
            "UPDATE banco_corretivo SET status = ?, resposta = ? WHERE id = ?",
            (status, resposta, id)
        )

        conexao.commit()
        conexao.close()

        return redirect(url_for("admin"))

    conexao.close()

    return render_template("analisar.html", pedido=pedido)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)