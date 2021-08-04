nome = 'Karollyne'
lista = [00, 26, 18]
numeros = range(1, 10)

# para cada letra dentro desse iteravel em uma string, imprimi essa letra
for letra in nome:
    print(letra, end='')

# iterando sobre uma lista
for numero in lista:
    print(numero)

# iterando sobre range, o valor final nao e incluso
for numero in range(1, 10):
    print(numero)

# o enumerate coloca um indice para cada valor de nome
for i, v in enumerate(nome):
    print(nome[i])

qtd = int(input('Quantas vezes esse loop ddeve rodar?'))
soma = 0

for n in range(1, qtd+1):
    print(f'Imprimindo {n}')
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma} \U0001F60D')

# ordenando a lista
lista.sort()
print(lista)
