"""
LISTAS 
Representadas por []
São mutáveis
"""
lista = [1, 15, 12, 18, 19, 22]

# contar quantas vezes aparece o numero/string X na lista
numero12 = lista.count(12)
print(f"Contador: {numero12}")

# adicionar elementos em lista
"""
para adicionar, é necessário o APPEND
"""
lista.append(23)  # somente 1 item
print(lista)

lista.append([77, 88])  # adc uma lista dentro da lista

# MELHOR PRATICA PARA NUMEROS, adiciona da unitariamente na lista
lista.extend([99, 83, 67])
print(lista)

# Inserir em uma posicao específica,  insert(posicao_index, numero_adc)
lista2 = [0, 1, 2, 3, 4]
lista2.insert(2, 88)
print(lista2)

# modos de adicionar listas em listas
lista3 = lista + lista2
lista.extend(lista2)

# inverter uma lista com reverse ou slice(string)
lista2.reverse()
print(lista2[::-1])

# copiar uma lista
lista3 = lista.copy()

# quantos objetos existem // tamanho da lista = LEN // SOMA TOTAL
print(len(lista2))

# remover o último elemento da lista= POP, ele retorna esse elemento retirado, pop(index_retirado)
# se não tiver numero no index selecionado, retornara IndexError.
print(lista2)
lista2.pop()
print(lista2)
lista2.pop(1)
print(lista2)

# limpar toda  alista CLEAR
lista2.clear()

# Converter string em lista = SPLIT, separa os elementos pelos espaços entre elas ou por virgulas usando split(',')
curso = 'programacao em python com geek'
print(curso)
curso = curso.split()
print(curso)

# Converter Lista em STRING = ' '.join(lista_exemplo), pega a lista + coloca espaco +converte em string
curso2 = ['Prog', 'Python', 'Essencial']
curso2 = ' '.join(curso2)
print(curso2)

lista5 = [26, 18, 22]
# Iterando sobre listas (repetir um conjunto de instrucoes finita vezes = for.. in..:)
for elemente in lista5:
    print(elemente)


# acesso aos elementos de forma indexada
#          0            1         2
cores = ['vermelho', 'branco', 'preto', 'vermelho']
print(cores[0])
# retorna o ultimo,no caso preto. Indice negativo = circulo, onde o final de um elemento esta ligado ao inicio da lista
print(cores[-1])

# loops
for cor in cores:
    print(f'Temos essas cores: {cor}')

# gerar indice = ENUMERATE
for indice, cor in enumerate(cores):
    print(indice, cor)

# encontrar o indice de um elemento na lista = INDEX
print(cores.index('preto'))

# busca dentro de um range específico, index(numero_para_encontrar, posicao_index_comeco, posicao_index_final)
print(cores.index('vermelho', 1,  4))

# slicing é lista[inicio:fim:passo], filtrar uma lista a partir de um index
lista7 = [1, 2, 3, 4]
print(lista7[1:])  # inicia no indice 1 e vai ate o final
print(lista7[:2])  # de 0 até o index 2 - 1
print(lista7[1::2])  # comecou no index 1, vai ate o final, de 2  em 2
print(lista7[::2])  # comecou no index 0, vai ate o final, de 2  em 2

# invertendo valores em lista =  REVERSE
nomes = ['Maria', 'joao']
nomes.reverse()
print(nomes)

# Transformar lista em Tupla
tupla = tuple(lista7)
print(tupla)
print(type(tupla))

# Desempacotamento de listas, numero de variaveis tem que ser = ao numero de elementos da lista
nome1, nome2 = nomes
print(nome1)
print(nome2)

# Copiando de lista para outra(Shallow copy e Deep Copy)
# Deep Copy // copia profunda, quando se copia inteiramente uma lista, criando uma nova independente
lista8 = [1, 2, 3]
deep_lista = lista8.copy()
print(deep_lista)
deep_lista.append(4)

# Shallow Copy
# copia e vira só uma lista, onde qualquer modificação afeta as 2 listas ao mesmo tempo
shallow = lista8
shallow.append(5)
print(lista8)
print(shallow)


# Soma*, Valor Maximo*, Valor Mínimo*, Tamanho
# * Se os valores forem reais ou inteiros
print(sum(lista7))  # soma
print(max(lista7))  # maximo valor
print(min(lista7))  # minimo valor da lista
print(len(lista7))  # tamanho total da lista
