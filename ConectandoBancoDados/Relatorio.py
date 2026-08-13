import mysql.connector
from Config import DB_CONFIG

def total_produtos():
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute("SELECT COUNT(*) FROM produtos")
        total_produtos = cursor.fetchone()[0]
        print(f"Total de produtos cadastrados: {total_produtos}")

    except mysql.connector.Error as error:
        print(f"Erro ao calcular total de produtos: {error}")

    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def valor_total_estoque():
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute("SELECT SUM(preco * quantidade) FROM produtos")
        valor_total_estoque = cursor.fetchone()[0]
        if valor_total_estoque is None:
            valor_total_estoque = 0.0
        print(f"Valor total do estoque: R${valor_total_estoque:.2f}")

    except mysql.connector.Error as error:
        print(f"Erro ao calcular valor total do estoque: {error}")

    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def produto_mais_caro():
    conexao =None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute("SELECT nome, preco FROM produtos ORDER BY preco DESC LIMIT 1")
        produto_mais_caro = cursor.fetchone()[0]
        print(f"O produto mais caro é: {produto_mais_caro}")

    except mysql.connector.Error as error:
        print(f"Erro ao buscar produto mais caro: {error}")

    finally:
        if conexao and conexao.is_connected():
            conexao.close()