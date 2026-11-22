'''
Curso: Santander - Python
Programa: conjuntos.py
2026
'''

# CONJUNTOS (SET)

# Um conjunto é uma estrutura de dados mutável e não ordenada que permite armazenar uma coleção de elementos únicos. 
# Os conjuntos são delimitados por chaves {} ou são criados utilizando a função set().

frutas = {"maça","banana","laranja"}
numeros = set([1,2,3,4,5])

# Os conjuntos suportam operações matemáticas de conjuntos, como a união (|), a interseção (&), a diferença (-) e a diferença simétrica (^).
conjunto1 = {1,2,3}
conjunto2 = {3,4,5}

uniao = (conjunto1 | conjunto2)
print(uniao)    # {1,2,3,4,5}

intersecao = (conjunto1 & conjunto2)
print(intersecao)   # {2,3}

diferenca = (conjunto1 - conjunto2)
print(diferenca)    # {1,2}  obs: apenas os resultados

diferenca_simetrica = (conjunto1 ^ conjunto2)
print(diferenca_simetrica)  # {1,2,4,5}


# Métodos dos Conjuntos

# Os conjuntos em Python têm vários métodos incorporados para manipular e acessar os elementos. Alguns métodos comuns são:

# add(elemento): adiciona um elemento ao conjunto.
frutas ={"maça","banana","laranja"}
frutas.add("pera")
print(frutas)   # {"laranja","banana","maçã","pera"}    obs: no print pode aparecer de forma aleatória a ordem

# remove(elemento): remove um elemento do conjunto. Se o elemento não existir, gera um erro.
frutas.remove("banana")
print(frutas) # {"laranja","maça","pera"}

# discard(elemento): remove um elemento do conjunto se estiver presente. Se o elemento não existir, não faz nada.
frutas.discard("uva")
print(frutas)   # {"laranja","maça","pera"}  obs: não houve alteração

# clear(): remove todos os elementos do conjunto.
frutas.clear()
print(frutas)   # set()

'''
As estruturas de dados em Python nos oferecem grande flexibilidade e potência para armazenar e manipular dados em nossos programas. 

As LISTAS são úteis para coleções ordenadas e mutáveis.
As TUPLAS para coleções ordenadas e imutáveis.
Os DICIONÁRIOS para armazenar pares de chave valor.
Os CONJUNTOS para coleções não ordenadas de elementos únicos.
'''
