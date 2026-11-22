'''
Curso: Santander - Python
Programa: estruturas_condicionais.py
2026
'''

# ESTRUTURAS DE CONTROLE

# IF
#===

idade = 49
if idade > 18:
    print ("Maior de idade")


# IF - ELSE
#===========

idade = 15
if idade >= 18:
    print ("Maior de idade")
else:
    print ("Menor de idade")


# IF - ELIF - ELSE
#==================

'''
if condicao1:

   # Bloco de código a executar se a condicao1 for verdadeira
   instruções

elif condicao2:

   # Bloco de código a executar se a condicao2 for verdadeira
   instruções

else:

   # Bloco de código a executar se nenhuma condição anterior for verdadeira
   instruções
'''

# Exemplo 1
#============

nota = 85

if nota >= 90:
    print ("Excelente!")

elif nota >= 80:
    print ("Muito bom")

elif nota >= 70:
    print ("Bom")

else:
    print ("Precisa melhorar")


# Exemplo 2 
#============

idade = 65

if idade < 18:
    print ("Menor de idade")

elif idade >= 18 and idade < 60:
    print ("Pessoa adulta")

elif idade > 15:
    print ("Maior de 15 anos")  # resposta. Mesmo sendo idoso essa condição é a primeira

elif idade == 60:
    print ("Pessoa com 60 anos")

else:
    print("Você é uma pessoa idosa acima de 60 anos")