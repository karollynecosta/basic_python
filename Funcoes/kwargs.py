"""
**kwargs

Por convenção da comunidade é chamado desta forma, mas poderia ser **xis
Parametros extras para as instrucoes, utilizando parametros nomeados, retornando DICT

*args e **kwargs não sao obrigatórios

Em funções, podemos juntar NESTA ORDEM: parametros obrigatórios
                                    *args
                                    parametros default
                                    **kwargs

Para desempacotar um dicionario: **variavel
"""


def cores_fav(**kwargs):
    for pessoa, cor in kwargs.items():  # .items pega os dois valores
        print(f'A cor favorita de {pessoa.title()} é {cor}')
    print(kwargs)


print(cores_fav(marcos='verde', barto='preto'))


def cumprimento_espec(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Cumprimentos pythonicos !'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!!"
    return 'voce nao tem um cumprimento pythonico ainda...'


print(cumprimento_espec())
print(cumprimento_espec(geek='Python'))
print(cumprimento_espec(geek='Golang'))


def funcao_all(idade, nome, *args, solteiro=False, **kwargs):  # ordem padrao
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('solteiro')
    else:
        print('Casado')
    print(kwargs)


print(funcao_all(2, 'Barto', 10, solteiro=True, apelido='Artold'))
