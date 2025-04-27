from behave import *
from features.impl import petstore

@given('que eu tenha uma lista de usuários para criar')
def step_impl(context):
    context.usuarios = [{ 
        "id":1,
        "username":"usuario_behave",
        "firstName":"Behave",
        "lastName":"Tester",
        "email":"teste@tester.com",
        "password":"123456",
        "phone":"5123436577",
        "userStatus": 1
        }]

@when('eu enviar uma requisição POST para criar os usuários')
def step_impl(context):
    context.resposta = petstore.criar_usuario(context.usuarios)

@then('o código de status da resposta deve ser 200')
def step_impl(context):
    context.resposta.status_code == 200, f"Esperado 200, mas obtido {context.resposta.status_code}"

@then('a mensagem de resposta deve ser "ok"')
def step_impl(context):
    corpo = context.resposta.json()
    assert corpo["message"] == "ok", f"Esperado mensagem 'ok', mas obtido {corpo['message']}"

@given('que eu tenha um nome de usuário existente')
def step_impl(context):
    context.nome_usuario = "usuario_behave"

@when('eu enviar uma requisição GET para obter o usuário')
def step_impl(context):
    context.resposta = petstore.obter_usuario(context.nome_usuario)

@then('a resposta deve conter os detalhes do usuário')
def step_impl(context):
    dados_usuario = context.resposta.json()
    assert dados_usuario["username"] == context.nome_usuario, f"Esperado username {context.nome_usuario}, mas obtido {dados_usuario['username']}"

@when('eu enviar uma requisição PUT para atualizar o usuário')
def step_impl(context):
    usuario_atualizado = {
        "id":1,
        "username":context.nome_usuario,
        "firstName":"NomeAtualizado",
        "lastName":"LatnameAtualizado",
        "email":"testeatuali@tester.com",
        "password":"654321",
        "phone":"509876333363",
        "userStatus": 1
    }
    context.resposta = petstore.atualizar_usuario(context.nome_usuario, usuario_atualizado)

@when('eu enviar uma requisição DELETE para excluir o usuário')
def step_impl(context):
    context.resposta = petstore.excluir_usuario(context.nome_usuario)