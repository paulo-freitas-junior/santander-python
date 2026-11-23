'''
Curso: Santander - Python
Programa: tratamentoErros.py
2026
'''

# ERROS DE SINTAXE ( SyntaxError )
# Ocorre quando o código não segue as regras de sintaxe do Python, como esquecer dois pontos após uma declaração de função ou um loop.
# Exemplo
'''
def minha_funcao()      # falta dois pontos no final ":"
    print('olá')

'''

# ERRO DE NOME ( NameError )
# Ocorre quando se faz referência a uma variável ou função que não foi definida.
# Exemplo
'''
print()     # Variável não definida no print 
'''

# ERRO DO TIPO ( TypeError )
# Ocorre quando se realiza uma operação com tipos de dados incompatíveis, como tentar somar um número e uma string.
# Exemplo
'''
resultado = (5 + "10")
'''

# ERRO DE ÍNDICE ( IndexError )
# Ocorre quando se tenta acessar um índice fora do intervalo válido de uma lista ou sequência.
# Exemplo
'''
lista = [1,2,3]
print(lista[3])     # Índice 3 não existe na lista [0,1,2] são os índices
'''
