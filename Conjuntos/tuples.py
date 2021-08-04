"""
Tuplas
1 - representadas por parenteses ()
2 - são valores imutáveis: toda operação em uma tupla gera uma NOVA tupla.]
3 - podem ser também: tupla = 1,2,3,4
4 - precisa ter mais de 1 elemento, caso contrario, é somente um inteiro. Ou pode ser se adicionar virgula: tupla2 = (4,)
5 - deve ser utilizado tupla quando nao precisamos modificar os dados contidos em uma coleção
6 - sao mais rapidas que listas
7 - mais seguras por conta da imutabilidade
TUPLAS SAO DEFINIDAS PELAS VIRGULAS, NAO PELO PARENTESES
(4) -> não é
(4,) ->é
4, -> é
"""
# tupla dinamica / com range
tupla = tuple(range(11))
# Desempacotamento de tupla
tupla = ('CCA', '101')
escola, sala = tupla
print(escola)
print(sala)

# Metodos para adicao e removao de elementos nao existem nas TUPLAS

tuple2 = (1, 2, 3, 4, 5, 6)
# Soma * inteiros
print(sum(tuple2))
# Valor Max * inteiros
print(max(tuple2))
# Val minimo * inteiros
print(min(tuple2))
# Total Tamanho
print(len(tuple2))

tuple3 = (9, 8, 7, 6)
# Concatenacao de tuplas
concatenacao = (tuple2 + tuple3)

# Verificar se o valor esta na tupla
print(1 in tuple2)

# iterando
for indice, valor in enumerate(tuple2):
    print(indice, valor)

# Contando os elementos dentro de uma tupla = COUNT
print(tuple2.count(1))

# converter string em tupla
curso = tuple('Curso Programacao')

print(tuple3[1])

# Buscando em qual index esta o valor, se nao exister, retorna ValueError
print(tuple3.index(6))

# slicing tupla[inicio:fim:passo]
novocurso = curso  # nao existe shallow copy com tuplas
