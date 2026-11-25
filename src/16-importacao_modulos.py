'''
Curso: Santander - Python
Programa:importacao_modulos.py
2026
'''
#Em Python, um módulo é um arquivo que contém definições de funções, classes e variáveis que podem ser utilizadas em outros programas.
# A importação de módulos nos permite acessar a funcionalidade definida em outros arquivos e reutilizar código de maneira eficiente. 
# Além disso, podemos criar nossos próprios módulos para organizar e modularizar nosso código.

import math

numero = int(input(f'Insira o número: '))
raiz_numero = math.sqrt(numero)
print(f'A raiz de {numero} é {raiz_numero}')


# Também podemos importar funções específicas de um módulo utilizando a sintaxe from módulo import função.
from math import sqrt

resultado = sqrt(100)
print(resultado)    # 10


# FUNÇÕES E CLASSES DE MÓDULOS PADRÕES
import random
import datetime

numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio) # Numero aleatório entre 1 e 10

data_atual = datetime.datetime.now()
print(data_atual)

