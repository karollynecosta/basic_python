"""
Collections - Ordered Dict

Em Dict padrao, a ordem de insercao nao é mantida
O OrderedDict garante a ordem de insercao
"""
from collections import OrderedDict

ord_dict = OrderedDict({'casa': 1, 'apt': 2, 'sobrado': 3, 'fazenda': 4})

for chave, valor in ord_dict.items():
    print(f'chave={chave}:valor={valor}')

odict1 = OrderedDict({'a': 1, 'b': 3})
odict2 = OrderedDict({'b': 1, 'a': 3})

print(odict1 == odict2)  # true ou false? == False, pois nao esta na mesma ordem
