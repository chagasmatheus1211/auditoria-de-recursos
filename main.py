# -*- coding: utf-8 -*-

def calcular_orcamento(dados, *ignorar, **kwargs):

    total = 0

    taxa = kwargs.get("taxa_cambio", 1)
    moeda = kwargs.get("moeda_destino", "BRL")

    for chave, valor in dados.items():

        if chave in ignorar:
            continue

        if type(valor) == dict:
            total += calcular_orcamento(valor, *ignorar)

        else:
            total += valor

    total = total * taxa

    return total

empresa = {

    "TI": {
        "Infraestrutura": 5000,
        "Desenvolvimento": {
            "Backend": 7000,
            "Frontend": 6000
        }
    },

    "RH": {
        "Recrutamento": 3000,
        "Treinamento": 2000
    },

    "Financeiro": 8000
}

resultado = calcular_orcamento(
    empresa,
    "RH",
    moeda_destino="BRL",
    taxa_cambio=1
)

print("Orçamento total:", resultado)
