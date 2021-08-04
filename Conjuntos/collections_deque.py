"""
Collections - Deque

É uma lista de alta performance

"""
from collections import deque

deq = deque('geek')
print(deq)

# Add elementos
deq.append('k')
print(deq)

deq.appendleft('a')  # Adiciona no começo
deq.popleft()  # remove o primeiro elemento
