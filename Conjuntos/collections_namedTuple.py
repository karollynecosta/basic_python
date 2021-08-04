"""
Collections - Named Tuple

tuple = (1,2,3) - imutável, acessivel via print(tupla[1])

named_tuple == Tupla nomeadas, sao diferenciadas, onde é especificado nome e parametros

"""
from collections import namedtuple

# nome e parametro
# Declaracao
cachorro = namedtuple('cachorro', 'idade raca nome')
print(cachorro)

gato = namedtuple('gato', 'idade, cor, apelido')

# usando
ray = cachorro(idade=2, raca='Pug', nome='Ray')
print(ray)

# acessand elemento
print(ray[0])
print(ray.nome)
