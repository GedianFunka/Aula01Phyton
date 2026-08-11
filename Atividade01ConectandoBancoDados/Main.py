import mysql.connector
from Config import DB_CONFIG

def criar_tabela():
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cliente(
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL,
                telefone VARCHAR(15)
        )
        """)

        conexao.commit()
        print("Tabela criada com sucesso!")

    except mysql.connector.Error as error:
        print(f"Erro: {error}")

    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def cadastrar_cliente(nome, email, telefone):
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO cliente (nome, email, telefone) VALUES (%s, %s, %s)
        """, (nome, email, telefone))

        conexao.commit()
        print(f"Cliente '{nome}' criado com sucesso!")

    except mysql.connector.Error as error:
        print(f"Erro ao cadastrar cliente: {error}")

    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def listar_clientes():
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM cliente ORDER BY nome")
        for p in cursor.fetchall():
            print(f"{p[0]} | {p[1]} | {p[2]} | {p[3]}")
    except mysql.connector.Error as error:
        print(f"Erro ao listar clientes: {error}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def buscar_cliente(termo):
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM cliente WHERE nome LIKE %s ORDER BY nome",
                       (f"%{termo}%",))
        for p in cursor.fetchall():
            print(f"{p[0]} | {p[1]} | {p[2]} | {p[3]}")
    except mysql.connector.Error as error:
        print(f"Erro ao buscar cliente: {error}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def atualizar_email(id, novo_email):
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute("UPDATE cliente SET email = %s WHERE id = %s",
                       (novo_email, id))
        conexao.commit()
        print(f"Email atualizado com sucesso!")

    except mysql.connector.Error as error:
        print(f"Erro ao atualizar email: {error}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def deletar_cliente(id):
    conexao = None
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM cliente WHERE id = %s",
                       (id,))
        conexao.commit()
        print(f"Cliente com ID {id} deletado com sucesso!")

    except mysql.connector.Error as error:
        print(f"Erro ao deletar cliente: {error}")
    finally:
        if conexao and conexao.is_connected():
            conexao.close()

def menu():
    criar_tabela()
    while True:
        print("\n===== SISTEMA DE CLIENTES =====")
        print("1 - Cadastrar cliente")
        print("2 - Listar clientes")
        print("3 - Buscar cliente")
        print("4 - Atualizar email")
        print("5 - Deletar cliente")
        print("0 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            telefone = input("Telefone: ")
            cadastrar_cliente(nome, email, telefone)
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            termo = input("Buscar por nome: ")
            buscar_cliente(termo)
        elif opcao == "4":
            cid = int(input("ID do cliente: "))
            novo_email = input("Novo email: ")
            atualizar_email(cid, novo_email)
        elif opcao == "5":
            cid = int(input("ID do cliente: "))
            deletar_cliente(cid)
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()