"""
Módulo Collections - Default Dict

É informado um valor default, podendo utilizar um lambda para isso.
Este valor será utilizado sempre que nao houver um valor definido.
No caso de chave inexistente chamada, a chave será criada e o valor default atribuido == Nao apresenta o keyError

Lambdas == funcoes sem nome, que podem ou nao receber parametros de entrada e retornar valores
"""
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Progamacao em Python'
print(dicionario)
