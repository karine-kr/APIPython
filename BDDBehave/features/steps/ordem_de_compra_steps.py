from behave import *
from features.impl.ordem_de_compra import OrdemDeCompra
     
     
@given(u'que o usuário selecionou o animal desejado na petstore')
def step_impl(context):
    context.api = OrdemDeCompra()
    context.api.id = 4
    context.api.petId = 2
    context.api.quantidade = 10
    

@when(u'a ordem de compra é registrada')
def step_impl(context):
    context.api.post_criar_uma_nova_ordem()


@then(u'o sistema valida se a ordem de pedido foi armazenada corretamente')
def step_impl(context):
    data = context.api.response.json()
    assert context.api.status_code == 200
    assert data["id"] == context.api.id
    assert data["petId"] == context.api.petId
    assert data["quantity"] == context.api.quantidade
    assert data["status"] == "placed"
    assert data["complete"] is True


@given(u'que existe um pedido cadastrado anteriormente')
def step_impl(context):
    context.api = OrdemDeCompra()
    context.api.id = 4


@when(u'buscar o pedido pelo id')
def step_impl(context):
    context.api.get_buscar_ordem_pelo_id(context.api.id)
    assert context.api.status_code == 200


@then(u'o sistema deve retornar a ordem de compra existente')
def step_impl(context):
    data = context.api.response.json()
    assert data["id"] == context.api.id
