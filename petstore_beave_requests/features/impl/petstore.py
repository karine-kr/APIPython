import requests

URL = "https://petstore.swagger.io/v2"

def criar_usuario(lista_usuarios):
    url=f"{URL}/user/createWithList"
    return requests.post(url, json=lista_usuarios)

def obter_usuario(nome_usuario):
    url=f"{URL}/user/{nome_usuario}"
    return requests.get(url)

def atualizar_usuario(nome_usuario, dados_usuario):
    url=f"{URL}/user/{nome_usuario}"
    return requests.put(url, json=dados_usuario)

def excluir_usuario(nome_usuario):
    url=f"{URL}/user/{nome_usuario}"
    return requests.delete(url)