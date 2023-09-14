import pyodbc
import stdiomask
from datetime import date
date = date.today()

# Informações do banco de dados
dados = (
    "Driver={SQL Server};"
    "Server=DESKTOP-O58J1VV\sqlexpress;"
    "Database=USERS;"
)


print("\nOlá, seja bem-vindo ao meu mundo.\n"),
print("Aperte a tecla ENTER para iniciar."), input()

# Criando menu.
class Menu:
    def __init__(self, options, email, username, senha, senha2):
        self.options = options
        self.email = email
        self.username = username
        self.senha = senha
        self.senha2 = senha2

    def MenuPrincipal(self):
        options = input("> [1] Entrar\n> [2] Registrar\n> [3] Sair\n \nDigite sua opção:")
        return options   

# Criando a função registrar.
    def Registroandlogin(self):
# Abrindo conexão para validar email e usuário e fechando posteriormente.
        connect = pyodbc.connect(dados)
        c = connect.cursor()
        consulta = f"""SELECT * FROM contas"""
        try:
            c.execute(consulta)
            colunas = c.fetchall()
        except pyodbc.DatabaseError as error:
            print(error)
            c.rollback()
        finally:
            connect.close()

        email = str(input("Digite o seu email:"))

# Repetição de limitador de caractere para o email.       
        while len(email):
            if 5 < len(email) < 25:
                for linha in colunas:
                    if (email == linha[0]):
                        print("\nO email já está sendo utilizado.")
                        return Menu.Registroandlogin([])
                    elif email == "":
                        print("\nDigite um email válido.\n")
                        return Menu.Registroandlogin([])
                break
            else:
                print("\nO email deve conter entre 6 e 15 caracteres.")
                return Menu.Registroandlogin([])
            
        username = str(input("Digite seu nome de usuário:"))
# Repetição de limitador de caractere para usuário.
        while len(username):
            if 3 < len(username) < 20:
                for linha in colunas:
                    if (username == linha[1]):
                        print("Usuário já existente.")
                        return Menu.Registroandlogin([])
                    elif username == "":
                        print("\nDigite um usuário válido.\n")
                        return Menu.Registroandlogin([])
            else:
                print("O usuário deve conter entre 6 e 15 caracteres.")
                return Menu.Registroandlogin([])

        senha = stdiomask.getpass(prompt='Senha:', mask='*',) 

# Repetição de limitador de caractere.
        while len(senha):
            if 5 < len(senha) < 16:
                senha2 = stdiomask.getpass(prompt='Senha:', mask='*',)
                if 5 < len(senha2) < 16:
                    break
                else:
                    print("A senha deve conter entre 6 e 15 caracteres.")
                return 
            else:
                print("A senha deve conter entre 6 e 15 caracteres.")
                return 
        if senha2 != senha:
            print("Senhas diferentes, tente novamente.\n")
        else:
            print("Registrado com sucesso.\n")

# Abrindo conexão para inserir dados na tabela e posteriormente encerrando-a.
        connect = pyodbc.connect(dados)
        c = connect.cursor()
        inserir = f"""INSERT INTO contas(email, usuario, senha, data_registro)
        VALUES
        ('{email}', '{username}', '{senha2}', '{date}')"""
        try:
            if senha2 == senha:
                c.execute(inserir)
                c.commit()
        except pyodbc.DatabaseError as error:
            print(error)
            c.rollback()
        finally:
            connect.close()
            return(options)

# Função para buscar login e senha no dba e validar.
    def Searchandlogin(self):
        login = str(input("Login:"))
        senha = stdiomask.getpass(prompt='Senha:', mask='*')

# Abrindo conexão para consultar e validar login e senha e posteriormente encerrando-a.
        connect = pyodbc.connect(dados)
        c = connect.cursor()
        consulta = f"""SELECT *FROM contas"""
        try:
            c.execute(consulta)
            colunas = c.fetchall()
        except pyodbc.DatabaseError as error:
            print(error)
            c.rollback()
        finally:
            connect.close()
        while True:
            for linha in colunas:
                if (login == linha[1] or [0]) and (senha == linha[2]):
                    print("Seja bem-vindo\n Enjoy"), exit()
                    break
            for linha in colunas:
                if (login != linha[1]) and (senha != linha[2]):
                    print("\nUsuário ou senha errados.\n")
                    return


# Repetição para o código funcionar.
while True:
    options = Menu.MenuPrincipal([])
    if options == '2':
        Menu.Registroandlogin([])
    elif options == '1':
        Menu.Searchandlogin([])
    elif options == '3':
        print("Saindo em 3, 2, 1...\nDesconectado.\n")
        exit()
    elif options == "":
        continue



