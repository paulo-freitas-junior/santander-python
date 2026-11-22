'''
Curso: Santander - Python
Programa: loops.py
2026
'''
# LOOPS
#=======

# FOR - O loop for é utilizado para iterar sobre uma sequência (como uma lista, uma tupla ou uma string) ou qualquer objeto iterável.

frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(fruta)


# WHILE - O loop while é utilizado para repetir um bloco de código enquanto uma condição for verdadeira

contador = 0
while contador < 5:
    print(contador)
    contador += 1


# Exemplo 1 - Usando FOR
print ("Números de 1 a 5 multiplicados por 2 usando loop FOR")
for numero in range (1,6):
    print (numero * 2)


# Exemplo 2 - Usando WHILE
print ("Numeros de 1 a 5 multiplicados por 2 usando loop WHILE")
contador = 1
while contador <= 5:
    print (contador * 2)
    contador += 1


# CONTROLE DE LOOPS
#===================

# BREAK - A instrução break é utilizada para sair prematuramente de um loop, independentemente da condição.

contador = 0
while True:
    print(contador)
    contador += 1

    if contador == 5:
        break


# CONTINUE - A instrução continue é utilizada para pular o restante do bloco de código dentro de um loop e passar para a próxima iteração.

for i in range (10):
    if i % 2 == 0:
        continue
    print(i)


# PASS - A instrução pass é uma operação nula que não faz nada. 
# É utilizada como um marcador de posição quando uma instrução é sintaticamente necessária, mas nenhuma ação é desejada

for i in range (5):
    pass
