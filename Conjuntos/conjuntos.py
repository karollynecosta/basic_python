"""
Conjuntos se referem a Teoria dos Conjuntos da Matematica

- em python, chamados de SETS
    1 - nao possuem valores duplicados, se tiver, sao ignorados
    2 - nao possuem valores ordenados
    3 - elementos nao sao acessados via indice, ou seja, sets nao sao indexados.
    4 - qualquer tipo de dado 
    5 - mutaveis

- Indicados para é necessário armazenar elementos sem se importar com a ordem, nem precisar de chave/valor.
- Referenciados com {}
- Diferencas entre Conjuntos(SETS) e Mapas(DICT):
    1 - Dict tem chave valor
    2 - Conjunto tem apenas valores
"""
conjunto1 = set({1, 2, 3, 4, 4, 6})

print(conjunto1)
print(type(conjunto1))

conjunto2 = {1, 1, 3, 4, 6}
print(conjunto2)

# Encontrar elemento no conjunto
if 3 in conjunto1:
    print(f'Numero 3 encontrado')
else:
    print(f'Numero 3 nao encontrado')

# Iterar
for valor in conjunto2:
    print(valor)

# Casos de uso
# Formulario para preenchimento de dados de visitante, lista de cidades em Python, pois listas aceitam novos elementos+repeticao

cidades = ['BH', 'Macapa', 'Santana', 'Santana']
print(cidades)  # retorna todas as cidades
print(len(cidades))  # retorna quantidade de cidades cadastradas
print(len(set(cidades)))  # retorna a quantidade de cidades sem repeticao

# Adicionando elementos em um conjunto
conjunto2.add(5)
print(conjunto2)

# Remover elementos
conjunto2.remove(1)  # nao é Indice, é o valor mesmo, nao retorna valor
conjunto2.discard(5)
print(conjunto2)

# copiando um conjunto para outro
s = {1, 2, 3}
# deep copy - cria um clone separado
novo = s.copy()
print(novo)

# shallow copy - duas variaveis com o mesmo valores e mesmas operacoes alocadas, se soma em 1, soma no outro tb
novo2 = s
novo2.add(5)
print(novo2)
print(s)

# remover todos os itens do conjunto
s.clear()
print(s)

# metodos matematicos
# 2 conjuntos - um com estudantes de python e outro com de React
est_py = {'Karol', 'Teixeira', 'Weslei'}
est_react = {'Marcos', 'Karol'}
# Precisamos gerar um conj com nomes de estudantes UNICOS
# Solucao 1 = union
unicos = est_py.union(est_react)
print(unicos)
# Solucao 2 =  com caractere pipe |
unicos2 = est_py | est_react
print(unicos2)

# Gerar um conj de estudantes que estao em AMBOS os cursos
#Sol1 = intersection
ambos = est_react.intersection(est_py)
print(ambos)
# Sol2 = &
ambos2 = est_py & est_react
print(ambos2)

# Gerar um conj de quem nao esta no outro curso
pythonista = est_py.difference(est_react)
print(pythonista)

reacteiros = est_react.difference(est_py)
print(reacteiros)

# Soma, maior valor, valor minimo, tamanho
x = {5, 6, 7, 8, 9}
print(sum(x))
print(max(x))
print(min(x))
print(len(x))
