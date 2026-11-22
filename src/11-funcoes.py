'''
Curso: Santander - Python
Programa: conjuntos.py
2026
'''
# As funções são blocos de código reutilizáveis que nos permitem encapsular tarefas específicas e executá-las quando necessário. 
# As funções nos ajudam a organizar nosso código, evitar a repetição e fazer com que nossos programas sejam mais modulares e fáceis de manter.

def saudacao():
    print ('Olá visitante!')

saudacao()


# PARÂMETROS E ARGUMENTOS

# As funções podem aceitar parâmetros, que são valores que são passados para a função quando ela é chamada. 
# Os parâmetros são especificados dentro dos parênteses na definição da função.
def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Paulo")
saudacao("Elaine")


# VALORES DE RETORNO

# As funções podem retornar valores usando a palavra-chave return. O valor de retorno pode ser usado pelo código que chama a função.
def soma(a,b):
    return (a+b)

resultado = soma(4,6)
print(resultado)    # 10


# FUNÇÕES ANÔNIMAS (LAMBDA)

# Python permite criar funções anônimas ou funções lambda, que são funções sem nome definidas em uma única linha. 
# São comumente usadas para funções pequenas e concisas.
quadrado = lambda x: x ** 2
print(quadrado(5))  # 25


# ESCOPO DAS VARIÁVEIS ( LOCAL X GLOBAL )

# As variáveis definidas dentro de uma função têm um escopo local, o que significa que só são acessíveis dentro da função. 
# Por outro lado, as variáveis definidas fora de qualquer função têm um escopo global e podem ser acessadas de qualquer parte do programa.
def funcao():
    variavel_local = 10
    print(variavel_local)   # acessível APENAS dentro da função (local)


variavel_global = 20

def funcao2():
    print(variavel_global)  # acessível de qualquer lugar (global)


funcao()    # 10
funcao2()   # 20

print(variavel_global)  # 20
# print(variavel_local)   # Gera uma mensagem de ERRO. Variável não está definida nesse escopo.


# DOCUMENTAÇÃO DE FUNÇÕES (docstrings)

# É uma boa prática documentar nossas funções utilizando docstrings. 
# Os docstrings são cadeias de texto que descrevem o propósito, os parâmetros e o valor de retorno de uma função. 
# São colocados imediatamente após a definição da função e são encerrados entre aspas duplas triplas.
def area_retangulo(base,altura):
    '''
    Calcula a área de um retângulo

    Args:
        base (float): A base do retângulo
        altura (float): A altura do retângulo

    Returns:
        float: Área do retângulo.
    '''
    return (base * altura)

print(area_retangulo(3,3))  # 9


# FUNÇÕES COM NÚMERO VARIÁVEL DE ARGUMENTOS

# Python permite definir funções que aceitem um número variável de argumentos. 
# Isso é feito utilizando o operador * antes do nome do parâmetro.
