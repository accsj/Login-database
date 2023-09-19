# Login-database
Um sistema de login que acessa o banco de dados e faz verificações de registro e autenticação de login.

  O meu objetivo com esse código foi estudar a conexão feita com o banco de dados do SQL Server Management, me certifiquei de fechar a conexão com o banco usando o Try, Except e Finally em todas ocasiões.
- Tem funções como logar, onde o código acessa o banco de dados e após armazenar os dados fecha a conexão, e inicia a procura pelo usuário fornecido ou email (também tem coomo logar com o email)
e valida a senha posteriormente.
- A função de Registro onde deverá ser fornecidos o Email que deve conter entre 20 e 30 caracteres (o código também verifica com o banco de dados se já existe uma conta com esse email),
também deverá ser fornecido um Usuário, onde deve conter entre 4 e 25 caracteres (Também verificando no banco de dados se já existe, mas sem CASE SENSITIVE),
e por último pedirá a senha, onde o código faz uma validação da 2 senha fornecida com a primeira.

PS: Caso a informação seja inválida, nenhuma informação inserida no processo de login, ou o código validar que já existe uma conta com as informações inseridas ele irá reiniciar o processo de registro.

- Opção de sair


Para o código inserir as informações no banco de dados com segurança, eu uso uma Try onde diz que, se "Senha2 == Senha"" deverá executar o comando de inserir as informações no banco de dados.

