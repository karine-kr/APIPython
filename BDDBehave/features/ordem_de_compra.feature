# language: pt
Funcionalidade: Efetuar ordem de compra

  Cenário: Efetuar uma ordem de compra na petstore
    Dado que o usuário selecionou o animal desejado na petstore
    Quando a ordem de compra é registrada
    Então o sistema valida se a ordem de pedido foi armazenada corretamente

  Cenário: Buscar um ordem de compra existente pelo id
    Dado que existe um pedido cadastrado anteriormente
    Quando buscar o pedido pelo id
    Então o sistema deve retornar a ordem de compra existente