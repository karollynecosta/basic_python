"""
Funções com Retorno

Para retornar valores, utilizamos a palvra: return dentro do bloco de função

return: Finaliza a função, ou seja, saí da execução da função
        existens diferentes returns
        Pode-se retornar qualquer tipo de dado e até mesmo multiplos valores

Erros comuns: geralmente codificação desnecessária
"""
from random import random


def quadrado_de_7():
    return 7*7


resposta = quadrado_de_7()
print(resposta)

# Exemplo do padrao de uso


def diz_oi():
    print('estou sendo executado antes do retorno')
    return 'Olá,  '
    print('não consigo ser executado após o retorno')


print(diz_oi())


# diferentes retornos


def nova_func():
    var = False
    if var:
        return 4
    elif var is None:
        return 33
    return 'ap'


print(nova_func())

# return de multiplos valores


def another_func():
    return 2, 3, 4


print(another_func())


def jogar_moeda():
    # gera um numero pseudo-randomico entre -0-1
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'  # nao precisa do else em funcoes simples


print(jogar_moeda())
