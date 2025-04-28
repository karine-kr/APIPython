# language: pt

Funcionalidade: Efetuar automação do login da Petstore

  Cenário: Criar usuários com uma lista
    Dado que eu tenha uma lista de usuários para criar
    Quando eu enviar uma requisição POST para criar os usuários
    Então o código de status da resposta deve ser 200
    E a mensagem de resposta deve ser "ok"

  Cenário: Obter detalhes de um usuário
    Dado que eu tenha um nome de usuário existente
    Quando eu enviar uma requisição GET para obter o usuário
    Então o código de status da resposta deve ser 200
    E a resposta deve conter os detalhes do usuário

  Cenário: Atualizar detalhes de um usuário
    Dado que eu tenha um nome de usuário existente
    Quando eu enviar uma requisição PUT para atualizar o usuário
    Então o código de status da resposta deve ser 200

  Cenário: Excluir um usuário
    Dado que eu tenha um nome de usuário existente
    Quando eu enviar uma requisição DELETE para excluir o usuário
    Então o código de status da resposta deve ser 200