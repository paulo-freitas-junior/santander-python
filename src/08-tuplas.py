'''
Curso: Santander - Python
Programa: tuplas.py
2026
'''
# Uma tupla é uma estrutura de dados IMUTÁVEL E ORDENADA que permite armazenar uma coleção de elementos. 
# Os elementos de uma tupla são encerrados entre parênteses (), separados por vírgulas. 
# Ao contrário das listas, as tuplas são imutáveis, o que significa que não podem ser modificadas uma vez criadas. 
# Não se pode adicionar, eliminar ou alterar elementos em uma tupla existente.
# As tuplas são úteis quando você precisa armazenar uma coleção de elementos que não devem ser modificados, como coordenadas ou dados de configuração.


# TUPLAS

ponto = (3,4)
print(ponto[0])     # 3
print(ponto[1])     # 4


# MÉTODOS DE TUPLAS

minha_tupla = (1,2,3,4,5,6,7,8,9)

# count(elemento): devolve o número de vezes que um elemento aparece na tupla. 
print(minha_tupla.count(3))    # 1

# index(elemento): devolve o índice da primeira aparição de um elemento na tupla. Opcionalmente, pode-se especificar o início e fim da busca. 
print(minha_tupla.index(5))    # Índice 4

# len(tupla): embora não seja um método de tupla propriamente dito, esta função incorporada devolve o comprimento da tupla.
