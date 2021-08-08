"""
Funcoes com parametror padrão (default parameters)

- Funcoes onde a passagem de parametro seja opcional
- DEVEM sempre estar ao final da declaracao de parametros

funcoes onde argumentos padrao tem acoes mesmo se o usuario nao passar argumento
"""
# pode ou nao informar a potencia, mas se nao informar, ira ser 2


def exponencial(numero, potencia=2):
    return numero ** potencia


print(exponencial(2))
