'''
Curso: Santander - Python
Programa:excecoes.py
2026
'''

# MANEJO DE EXCEÇÕES
# O manejo de exceções nos permite capturar e lidar com erros de maneira controlada utilizando as declarações try, except e opcionalmente finally.


# TRY
# O bloco try contém o código que pode gerar uma exceção. 
# Se ocorrer uma exceção dentro do bloco try, o fluxo de execução é transferido para o bloco except correspondente.

try:
    # Código que pode gerar uma exceção
    resultado = (10/0)  # Divisão por zero
    print(resultado)
except ZeroDivisionError:
    print('Erro: Divisão por Zero')


# EXCEPT
# O bloco except especifica o tipo de exceção que se deseja capturar e lidar. 
# Você pode ter múltiplos blocos except para lidar com diferentes tipos de exceções.
try:
    # código que pode gerar a exceção
    resultado = (10/"2")  # teste com tipos de dados diferentes
    print(resultado)
except ZeroDivisionError:
    print("Erro: Divisão por Zero")
except ValueError:
    print("Erro: Valor Inválido")
except TypeError:
    print("Erro: Tipos de dados inválidos para execução")


# FINALLY
# O bloco finally é opcional e é executado SEMPRE, independentemente de ter ocorrido uma exceção ou não.
# É comumente utilizado para realizar tarefas de limpeza ou liberação de recursos.
try:
    # código que pode gerar a exceção
    arquivo = open("arquivo.txt", "r")  # "r" modo de leitura apenas ready
    print(arquivo.read())
except FileNotFoundError:
    print("Erro: Arquivo não encontrado")
finally:
    arquivo.close() # fecha o arquivo sempre, mesmo se ocorrer a exceção


# EXCEÇÕES PERSONALIZADAS
# Além das exceções incorporadas no Python, você também pode criar suas próprias exceções personalizadas. 
# Isso é útil quando deseja lidar com situações específicas do seu programa.
# Para criar uma exceção personalizada, você deve criar uma classe que herde da classe base Exception ou de uma de suas subclasses.
def calculo_positivo():
    numero1 = 10
    numero2 = 20
    calculo = (numero1 - numero2)
    if calculo < numero1:
        raise Exception("Resultado é negativo! Menor que Numero 1")
try:
    calculo_positivo()
except Exception as e:
    print(f'Erro: {str(e)}')


'''
O tratamento de erros e exceções é uma parte fundamental da programação em Python.
Permite lidar com situações inesperadas de maneira controlada e evitar que seu programa trave ou pare abruptamente.
'''
