from behave import *
from features.impl.ordem_de_compra import OrdemDeCompra
     
     
@given(u'que o usuário selecionou o animal desejado na petstore')
def step_impl(context):
    context.api = OrdemDeCompra()
    context.api.id = 4
    context.api.petId = 2
    context.api.quantidade = 10
    context.api.post_criar_uma_nova_ordem()


@then(u'o sistema valida se a ordem de pedido foi armazenada corretamente')
def step_impl(context):
    pass

@given(u'que o pedido com id 4 existe')
def step_impl(context):
    context.api = OrdemDeCompra()
    context.api.id = 4


@when(u'eu busco o pedido pelo id 4')
def step_impl(context):
    context.api = OrdemDeCompra()
    context.api.get_buscar_ordem_pelo_id(4)

@when(f"apresenta o status de resposta com 200")
def step_impl(context):
    assert context.api.status_code == 200

@then(f"o corpo da resposta deve conter o id 4")
def step_impl(context):
    data = context.api.response.json()
    assert data["id"] == 4
