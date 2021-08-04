"""
Modulo Collection - Counter

Collections -> High-performance Container Datetypes

Counter -> recebe um iteravel como parametro e cria um objeto do tipo Collections Counter, parecido com um dicionário,
            contendo como chave o elemento da lista passada como parametro e como valor a quantidade de ocorrencias desse elemento.
"""
from collections import Counter

# qualquer iteravel
lista = [1, 1, 2, 2, 3, 3, 55, 66, 6, 6]

res = Counter(lista)
print(res)
print(type(res))

# Counter({1: 2, 2: 2, 3: 2, 6: 2, 55: 1, 66: 1})
# Para cada elemento da lista o counter criou uma chave:valor quantidade de ocorrencias

print(Counter('Geek'))

texto = """"Este e um exemplo de texto grande para o Collections Counter feito por alguem que e um exemplo"""
palavras = texto.split()
re = Counter(palavras)
print(re)

# Encontrando as 2 palavras com mais ocorrencia no texto
print(re.most_common(2))
