'''
Curso: Santander - Python
Programa: módulo_personalizado.py
2026
'''

import meu_modulo_exemplo

meu_modulo_exemplo.saudar("Paulo")  # Olá, Paulo
resultado = meu_modulo_exemplo.calcular_soma(10,20)
print(f'Resultado da soma é {resultado}')



# ORGANIZAÇÃO DE CÓDIGOS EM MÓDULOS

# À medida que nossos programas crescem em tamanho e complexidade, é uma boa prática organizar nosso código em módulos separados segundo sua funcionalidade. 
# Isso nos permite manter um código mais legível, agrupado em módulos e fácil de manter.

# Por exemplo, podemos CRIAR um módulo operacoes.py que contenha funções relacionadas com operações matemáticas
# E outro módulo utilidades.py que contenha funções de uso geral.

import operacoes
import utilidades

soma = operacoes.somar(10,20)
utilidades.imprimir_mensagem(f'Soma de 1o e 20 é {soma}')

nome = utilidades.obter_nome_usuario()
utilidades.imprimir_mensagem(f'Nome do usuário é: {nome}')
