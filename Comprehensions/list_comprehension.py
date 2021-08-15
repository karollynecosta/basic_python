"""
List Comprehension

- Ao utilizar, é possível gerar novas listas com dados processados a partir de outro iterável
- Pode ser adicionado estruturas condicionais

Sintaxe: [dado for dado in iteravel]

Primeira parte: for numero in numeros
Segunda parte: numero * 10 (o que será feito)
"""
numeros = [1, 2, 3]  # global

# para cada numero na lista de numeros, multiplique x10 esses numeros
res = [numero * 10 for numero in numeros]

print(res)

# List Comprehension X Loop

# loop
numeros_dobrados = []
for numero in numeros:
    numeros_dobrados.append(numero * 2)
print(numeros_dobrados)

# list comp
print([numero * 2 for numero in numeros])

nome = 'Barto'
print([letra.upper() for letra in nome])

# colocando  somente a primeira letra em maiusculo
amigos = ['maria', 'joao', 'apolo']
print([amigo.title() for amigo in amigos])

# verificando se os valores sao corretos com o tipo
print([bool(valor) for valor in numeros])

# transformando int em string
print([str(numero) for numero in numeros])

# estruturas condicionais
# qualquer numero par modulo de 2 é 0, em python 0 é FALSE. Not False == True
pares = [numero for numero in numeros if not numero % 2]
print(f'Numeros pares existentes: {pares}')

impar = [numero for numero in numeros if numero % 2]
print(f'Numeros impares existentes: {impar}')

testando = [numero * 2 if not numero % 2 else numero / 2 for numero in numeros]
print(testando)
