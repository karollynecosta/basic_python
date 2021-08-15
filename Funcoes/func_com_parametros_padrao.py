"""
Funcoes com parametror padrão (default parameters)

- Funcoes onde a passagem de parametro seja opcional
- DEVEM sempre estar ao final da declaracao de parametros
- Nos permite ser mais flexiveis nas funcoes
- Evita erros com parametros incorretos
- exemplos mais legíveis

Pode ser usado qualquer tipo de dados
funcoes onde argumentos padrao tem acoes mesmo se o usuario nao passar argumento
"""
# pode ou nao informar a potencia, mas se nao informar, ira ser 2
# exemplo de docstring


def exponencial(numero, potencia=2):
    """
    Funcao que retorna por padrao o quadrado de 'numero' 
    :param potencia: int - este é um parametro padrão, caso nao seja informado algum valor subs, sempre será 2
    :param numero: int - caso não seja informado valor, será o mesmo da potencia
    :return: Retorna o exponencial de numero por potencia
    """
    return numero ** potencia


print(exponencial(2))

# ex de funcao com parametros requeridos, terceiro valor opcional


def soma(num1, num2):
    return num1 + num2


def subtracao(num1, num2):
    return num1 - num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


print(mat(4,  2, subtracao))

# ex com valores padroes


def mostra_info(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Olá instrutor'
    elif nome == 'Geek':
        return 'Pensei que voce era instrutor'
    return f'Olá {nome}'


print(mostra_info())
print(mostra_info(instrutor=True))
print(mostra_info(nome='Apolo'))

# Escopo
# Variaveis globais, nao estao dentro de funcoes e podem ser chamadas em qualquer local. Evitável.
instrutor = 'Geek'
# variaveis locais - dentro da func, se tiver o mesmo nome de uma var global, a local será utilizada

# Funcoes que sao declaradas dentro de funcoes


def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()


print(fora())
