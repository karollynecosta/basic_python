"""
Funções
Conceito: São pequenos partes de código que realizam tarefas específicas
          São inerentes a linguagem, ex.: print(), len(),  max(), min(), count()
          Pode ou não receber entrada de dados e retornar uma saída de dados
          úteis para executar procedimentos similares por repetidas vezes
          1 função = 1 tarefa. Do simple! DRY(Don't Repeat Yourself)
ex: def nome_func(parametros_entrada):
        bloco_da_func

Padrões: nome_func -> SEMPRE letra minuscula, se for composto, usar _
         parametros_entrada -> Opcionais, +1 é separado por virgulas
         bloco_da_func -> Corpo da função, onde o processamento ocorre.
         para  utilização: nome_func()
"""
# func integrada(built-in)
cores = ['vermelho', 'azul', 'preto']
print(cores)

cores.append('branco')

# ex de funcao sem parametro de entrada


def diz_oi():
    print('oi!')


diz_oi()
