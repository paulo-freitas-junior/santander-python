'''
Curso: Santander - Python
Programa:entradas_saidas.py
2026
'''

# Em Python, a entrada e saída de dados nos permite interagir com o usuário e manipular arquivos. 
# Podemos solicitar informações ao usuário, mostrar resultados na tela e ler ou escrever dados em arquivos externos.

#ENTRADA DE DADOS
nome = input('Insira seu nome: ')
idade = int(input('Insira a sua idade: '))

print("Olá " + nome + "!")
print("Sua idade é " + idade + " anos.")

# Exemplo 1
idade = int(input("Digite a sua idade: "))
if idade >= 18:
    print('Você é maior de idade.')
else:
    print('Você é menor de idade.')


# SAÍDA
nome = "Paulo"
idade = 49
print(f'Olá, meu nome é {nome} e tenho {idade} anos.')
