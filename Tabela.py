import sqlite3
from sqlite3 import Error

def ConexaoBanco():
    caminho="C:\\Users\\usuario\\OneDrive\\Área de Trabalho\\Tabela de contatos\\Contatos.db"
    conn = None
    try:
        conn =sqlite3.connect(caminho)
    except Error as er:
        print(er)
    return conn

vcon = ConexaoBanco()

def query(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as er:
        print(er)
    finally:
        print("Registrado")
        conexao.close()

def consultar(conexao,sql):
    c=conexao.cursor()
    c.execute(sql)
    res=c.fetchall()
    return res

def deletar(conexao, sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Contato removido")

def atualizar(conexao, sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Contato atualizado")

def inserir(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Contato registrado")
    except Error as er:
        print(er)

def menu():
    while True:
        print("=====BEM VINDO=====")
        print('''1 - Inserir Contato
    2 - Consultar Contato
    3 - Atualizar Contato
    4 - Deletar Contato
    5 - Sair''')
        escolha = input("Disque o numero para escolha:")
        if escolha == "1":
            Inserircontato()
        if escolha == "2":
            Consultarcontato()
        if escolha == "3":
            Atualizarcontato()
        if escolha == "4":
            Deletarcontato()
        elif escolha == "5":
            print("Obrigado por ter acessada")
            break
            
def Inserircontato():
    Nome = input("Digite o nome do contato: ")
    Numero = input("Digite o numero do contato: ")
    vsql = "INSERT INTO Contatos (Nome, Telefone) VALUES ('"+Nome+"','"+Numero+"')"
    inserir(vcon,vsql)

def Consultarcontato():
    CNome = input("Digite o nome do contato que quer consultar: ")
    vsql = "SELECT * FROM Contatos WHERE Nome LIKE '"+CNome+"'"
    res = consultar(vcon,vsql)
    for r in res:
        print("Id:{0:_<3}, Nome:{1:_<15}, Telefone:{2:_<12}".format(r[0],r[1],r[2]))

def Atualizarcontato():
    id = input("Qual id do contato que deseja mudar: ")
    r = consultar(vcon,"SELECT * FROM Contatos WHERE Id Like '"+id+"'")
    rnome =r[0][1]
    rnumero =r[0][2]
    NNome = input("Digite o nome do contato: ")
    NNumero = input("Digite o numero do contato: ")
    if(len(NNome)==0):
        NNome=rnome
    if(len(NNumero)==0):
        NNumero=rnumero
    vsql = "UPDATE Contatos SET Nome = '"+NNome+"', Telefone = '"+NNumero+"' WHERE Id Like '"+id+"'"
    query(vcon,vsql)

def Deletarcontato():
    id = input("Qual id do contato que deseja deletar: ")
    vsql = "DELETE FROM Contatos WHERE Id Like'"+id+"'"
    deletar(vcon,vsql)

menu()