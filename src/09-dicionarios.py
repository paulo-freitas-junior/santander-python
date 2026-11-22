'''
Curso: Santander - Python
Programa: dicionarios.py
2026
'''
# Um dicionário é uma estrutura de dados mutável e não ordenada que permite armazenar pares de chave-valor. 
# Cada elemento em um dicionário consiste em uma chave única e seu valor correspondente. 
# Os dicionários são delimitados por chaves {}, e os pares chave-valor são separados por vírgulas.


# DICIONÁRIOS
pessoa = {"nome":"Paulo", "idade":49,"cidade":"São Paulo"}

# Para acessar os valores de um dicionário, utilize a chave correspondente entre colchetes:
print(pessoa["nome"])       # Paulo
print(pessoa["idade"])      # 49
print(pessoa["cidade"])     # São Paulo


# Você também pode utilizar o método get() para obter o valor de uma chave. Se a chave não existir, retorna um valor padrão (por padrão, None).
# O get() é muito útil quando você não tem certeza se uma chave existe no dicionário e quer evitar um KeyError.
print(pessoa.get("nome"))
print(pessoa.get("Estado", "Não informado"))    # SE existir a chave Estado retorna valor, SE NÃO retorna "não informado"


# Exemplo 1
config = {
    "tema": "escuro"
}
tema = config.get("tema", "claro")
idioma = config.get("idioma", "pt-BR")
print(tema)         # localizou a chave e retornou
print(idioma)       # não localizou a chave e retornou 'pt-BR'


# MÉTODOS DE DICIONÁRIOS

# keys(): retorna uma visualização de todas as chaves do dicionário.
print(pessoa.keys())

# values(): retorna uma visualização de todos os valores do dicionário.
print(pessoa.values())

# items(): retorna uma visualização de todos os pares chave-valor do dicionário.
print(pessoa.items())

# update(outro_dicionario): atualiza o dicionário com os pares chave-valor de outro dicionário.
pessoa.update({"profissão":"Cientista de Dados"})
print(pessoa)
