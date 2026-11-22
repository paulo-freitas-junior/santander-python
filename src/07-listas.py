'''
Curso: Santander - Python
Programa: listas.py
2026
'''

# ESTRUTURA DE DADOS
# ==================


# LISTAS - Uma lista é uma estrutura de dados mutável e ordenada que permite armazenar uma coleção de elementos.

frutas = ['maçã','banana','laranja']

# acessando os elementos de uma lista através dos índices
print(frutas[0])    # imprime mação
print(frutas[1])    # imprime banana
print(frutas[2])    # imprime laranja

# acessando os elementos de uma lista por índices negativos
print(frutas[-1])   # imprime laranja
print(frutas[-2])   # imprime banana
print(frutas[-3])   # imprime maçã


# MÉTODOS DE LISTAS

# append(elemento): adiciona um elemento ao final da lista.
frutas = ['maçã','banana','laranja']
frutas.append('pera')
print(frutas)

# insert(indice, elemento): insere um elemento em uma posição específica da lista.
frutas.insert(1, 'uva')
print(frutas)   # inseriu "uva" no índice 1 da lista

# remove(elemento): remove a primeira ocorrência de um elemento na lista.
frutas.remove('banana')
print(frutas)

# pop(indice): remove e retorna o elemento em uma posição específica da lista.
fruta_removida = frutas.pop(2)
print(frutas)
print(fruta_removida)   # laranja

# sort(): ordena os elementos da lista em ordem ascendente.
frutas.sort()
print(frutas)

# reverse(): inverte a ordem dos elementos na lista.
frutas.reverse()
print(frutas)


# LISTAS DE COMPREENSÃO  (list compression)
'''
Criar uma lista baseada em uma sequência existente
nova_lista = [EXPRESSÃO for ELEMENTO in SEQUENCIA if CONDIÇÃO]
'''
numeros = [1,2,3,4,5]
quadrados = [x ** 2 for x in numeros if x % 2 == 0]
print(quadrados)    # [4,16]

