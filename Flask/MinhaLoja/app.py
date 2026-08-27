from flask import Flask, render_template

#Cria a aplicação Flask
app = Flask(__name__)

#Define uma rota
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/produtos")
def produto_lista():
    lista = [
        {"id":1, "nome":"CRF 250f", "preco": 31000, "categoria": "motos"},
        {"id": 2, "nome": "TTR 230", "preco": 23000, "categoria": "motos"},
        {"id": 3, "nome": "MXF 270fi", "preco": 27000, "categoria": "motos"},
        {"id": 4, "nome": "KX250X", "preco": 45000, "categoria": "motos"},
        {"id": 5, "nome": "KTM450 Six Days", "preco": 100000, "categoria": "motos"},
    ]
    return render_template("produtos.html", produtos = lista)

@app.route("/produtos/<int:id>")
def produtos(id):
    return f"Exibindo produto com id {id}"

#Inicia o servidor
if __name__ == "__main__":
    app.run(debug = True)