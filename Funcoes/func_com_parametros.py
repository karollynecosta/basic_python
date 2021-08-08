"""
Funções com Parametro (de entrada)

Funções que recebem dados par serem processados dentro da mesma.
Fluxo comum:
    entrada ->processamento ->saída
Parametros : variaveis declaradas na def de uma func. A ordem importa.
Argumentos: dados passados  durante a execução de uma func.
            Argumentos nomeados (key arguments): nome_completo(nome=nome, sobrenome=sobrenome) 
                                                 nome_completo(nome='Angelina', sobrenome='Jolie')

Erro comum no 'return': colocar no bloco do for, pois finaliza o loop
"""


def quadrado(numero):
    return numero ** 2


print(quadrado(3))


def cantar_parabens(aniversariante):
    print(f'parabens {aniversariante}')


cantar_parabens('Bea')

# parametros a e s


def soma(a, s):
    return a + s


# argumentos para os parametros
print(soma(1, 2))

# nomeando parametros


def nome_completo(nome, sobrenome):
    return f'Seu nome é: {nome} {sobrenome}'


print(nome_completo('Karol', 'teste'))
