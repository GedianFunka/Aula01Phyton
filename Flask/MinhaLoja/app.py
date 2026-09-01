from flask import Flask, render_template

#Cria a aplicação Flask
app = Flask(__name__)

lista = [
        {"id":1, "nome":"CRF 250f", "preco": 31000, "categoria": "motos", "quantidade": 10},
        {"id": 2, "nome": "TTR 230", "preco": 23000, "categoria": "motos", "quantidade": 0},
        {"id": 3, "nome": "MXF 270fi", "preco": 27000, "categoria": "motos", "quantidade": 3},
        {"id": 4, "nome": "KX250X", "preco": 45000, "categoria": "motos", "quantidade": 7},
        {"id": 5, "nome": "KTM450 Six Days", "preco": 100000, "categoria": "motos", "quantidade": 5},
        {"id": 6, "nome": "Husqvarna FC 250", "preco": 95000, "categoria": "motos", "quantidade": 15},
    ]

#Define uma rota
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/produtos")
def produto_lista():
    return render_template("produtos.html", produtos = lista)

@app.route("/catalogo")
def catalogo():
    return render_template("catalogo.html", produtos = lista)

@app.route("/produtos/<int:id>")
def detalhe_produto(id):
    produto = None
    for p in lista:
        if p["id"] == id:
            produto = p
            break
    return render_template("detalhe.html", id = id, produto = produto)

@app.route("/categoria/<nome>")
def categoria(nome):
    return f"Exibindo produtos da categoria {nome}"

#Inicia o servidor
if __name__ == "__main__":
    app.run(debug = True)