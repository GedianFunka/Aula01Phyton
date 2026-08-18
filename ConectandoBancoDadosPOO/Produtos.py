from Config import DB_CONFIG
from Models import Produto
import mysql.connector

def cadastrar_produto(produto: Produto):
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO produtos ( nome, preco, quantidade, categoria) VALUES (%s, %s, %s, %s)",
            produto.converter_tupla()
        )
        conexao.commit()
        print(f"Produto {produto.nome} cadastrado!")

    except mysql.connector.Error as error:
        print(f"Erro ao cadastrar: {error}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def listar_produto():
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM produtos ORDER BY nome")
        return [Produto.reverte_tupla(linha) for linha in cursor.fetchall()]
    except mysql.connector.Error as error:
        print(f"Erro ao cadastrar: {error}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def buscar_produto():
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute(  "SELECT * FROM produtos WHERE nome LIKE %s ORDER BY nome",
            (f"%{termo}%",))
        return [Produto.reverte_tupla(linha) for linha in cursor.fetchall()]

    except mysql.connector.Error as error:
        print(f"Erro ao cadastrar: {error}")

    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def atualizar_preco(id_produto, novo_preco):
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute(
            "UPDATE produtos SET preco = %s WHERE id = %s",
            (novo_preco, id_produto)
        )
        conexao.commit()
        if cursor.rowcount > 0:
            print("Preço atualizado com sucesso.")
        else:
            print(f"Produto com id {id_produto} não encontrado.")
    except mysql.connector.Error as erro:
        print(f"Erro ao atualizar: {erro}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def excluir_produto(id_produto):
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute("SELECT nome FROM produtos WHERE id = %s", (id_produto,))
        produto = cursor.fetchone()
        if not produto:
            print(f"Produto com id {id_produto} não encontrado.")
            return
        cursor.execute("DELETE FROM produtos WHERE id = %s", (id_produto,))
        conexao.commit()
        print(f"Produto '{produto[0]}' excluído com sucesso.")
    except mysql.connector.Error as erro:
        print(f"Erro ao excluir: {erro}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()