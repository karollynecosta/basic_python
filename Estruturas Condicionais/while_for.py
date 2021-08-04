# Iterando listas com while
carrinho = []
produto = ''

# se o usuário digitar sair,  ira para o for
while produto != 'sair':
    print("Adicione um produto ou digite 'sair': ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)
