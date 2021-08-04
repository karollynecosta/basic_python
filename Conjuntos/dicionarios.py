"""
Dicionarios // DIC

1 - Sao colecoes do tipo chave/valor
chave [cachorro,gato,rato]
valor [1,2,3]
2 - Representados por {'':''}
3 - chave/valor podem ser qualquer tipo(int, string), podendo ser misturados
4 - as buscas ocorrem sempre pela CHAVE
5 - não existem chaves repetidas

- Dict é Ideal para lógicas como e-commerce:
    + pois com listas/tuplas teriamos que saber qual o indice de cada informação do produto
    + com dicionarios facilmente é adicionado e removido elementos do carrinho, tendo certeza sobre cada informação.
- Em algumas linguagens, dicionarios sao conhecidos por Mapas.
- Tuplas sao um bom exemplo para serem usadas como chave.
- iteravel = pode ser manipulada
"""

# Criação de dicionario
dic_paises = {'br': 'Brasil', 'mcp': 'Macapa'}
print(dic_paises)

paises = dict(br='Brasil', mcp='Macapa', rj='Rio')
print(paises)
print(type(paises))

# Acessando elementos via chave/key, se nao existir retorna KeyError, para nao cair nesse erro(try..except..continue)
print(paises['br'])

# Acessando elementos via GET - Recomendada, se nao existir, retorna none
print(paises.get('mcp'))

russia = paises.get('ru')
if russia:
    print(f'Encontrei a tal da {russia}')
else:
    print('Não Encontrei a tal da russia')

# Nos casos que o objeto nao existir, retornará 'Nao encontrado'
valor_padrao = paises.get('mcp', 'Não encontrado')

# Adicionando elementos no dicionário
receita = {'jan': 100, 'fev': 50,  'mar': 200}
print(f'Voce possui: {receita}')

receita['abr'] = 211  # Forma mais comum de adição
print(f'Agora possui: {receita}')

novo_dado = {'mai': 222}
receita.update(novo_dado)  # receita.update({'mai':222}), mesma coisa
print(receita)

# Atualizando dados em um dict, semelhando ao método de adição
receita['abr'] = 300
print(receita)

# Removendo dado de um dic, necessário informar um key válida,
remov = receita.pop('mai')  # mais usada, retorna o valor removido
print(remov)
print(receita)

del receita['abr']  # nao retorna o valor removido
print(receita)

# ecommerce
carrinho = []  # lista vazia

prod1 = {'nome': 'Coleira', 'qtd': 1, 'valor': 10.00}  # dicionario de produtos
prod2 = {'nome': 'Raçao', 'qtd': 1, 'valor': 25.50}

carrinho.append(prod1)
carrinho.append(prod2)
print(carrinho)

# metodos
dir({})  # lista todos os metodos disponiveis

d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

# limpar o dict
# d.clear()
# print(d)

# copiar um dicionario para outro
novo_dict = d.copy()  # deep copy, cria um novo dicionario

novo_dict['d'] = 5
print(d)
print(novo_dict)

# MAPAS -> Dicionarios {}
# Iterar sobre dict
receita2 = {'jan': 200, 'fev': 350,  'mar': 4200}

for key in receita2:
    print(key)  # somente a chave
    print(receita2[key])  # somente o valor
    print(f'Em {key} recebi R$ {receita2[key]}')  # chave e valor

# Acessando as chaves / keys
print(receita2.keys())

for chave in receita2.keys():
    print(chave)

# Acessando os valores
print(receita2.values())

# Desempacotamento de dicionarios
print(receita2.items())
for chave, valor in receita2.items():
    print(f'chave={chave} e valor={valor}')

# Soma
print(sum(receita2.values()))
# Valor Maximo
print(max(receita2.values()))
# Valor Min
print(min(receita2.values()))
# Tamanho total
print(len(receita2))
