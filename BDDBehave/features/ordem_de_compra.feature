# language: pt
Funcionalidade: Efetuar ordem de compra

  Cenário: Efetuar uma ordem de compra na petstore
    Dado que o usuário selecionou o animal desejado na petstore
    Então o sistema valida se a ordem de pedido foi armazenada corretamente

  Cenário: Buscar um ordem de compra existente pelo id
    Dado que o pedido com id 4 existe
    Quando eu busco o pedido pelo id 4
    E apresenta o status de resposta com 200
    Então o corpo da resposta deve conter o id 4