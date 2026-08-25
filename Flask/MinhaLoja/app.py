from flask import Flask

#Cria a aplicação Flask
app = Flask(__name__)

#Define uma rota
@app.route("/")
def index():
    return "Olá, mundo! O Flask OK."

@app.route("/sobre")
def sobre():
    return "Está página é sobre."

@app.route("/produto")
def produto_lista():
    produtos = ["Camiseta", "Iphone", "CRF"]
    return f"Os produtos cadastrados são: {produtos}"

@app.route("/produto/<int:id>")
def produto(id):
    return f"Exibindo produto com id {id}"

#Inicia o servidor
if __name__ == "__main__":
    app.run(debug = True)