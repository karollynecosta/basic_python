"""
Entendendo o *args

Parametro especial, necessita começar com arterisco
Coloca os valores extras informados como entrada em uma tupla(imutaveis)
"""


def soma_todos(*args):
    """
    Funcao de soma simples
    retorno em TUPLA
    """
    return sum(args)


print(soma_todos(1))  # tuple(1,)
lista_numeros = [1, 2, 3]
# desempacotando a lista para a tupla somar, utilizando o * para isto
print(soma_todos(*lista_numeros))


def verifica_info(*args):
    if 'Geek' in args and 'Univer' in args:
        return 'Bem vindo Geek'
    return 'Who is you?'


print(verifica_info())
print(verifica_info(1, True, 'Univer', 'Geek'))
print(verifica_info(1, 'Geek', 10))
