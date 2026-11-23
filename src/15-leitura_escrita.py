'''
Curso: Santander - Python
Programa:leitura_arquivos.py
2026
'''

# LEITURA DE ARQUIVOS
# Python nos permite ler e escrever dados em arquivos externos. 
# Podemos abrir arquivos em diferentes modos, como leitura ("r"), escrita ("w") ou anexar ("a"), e realizar operações de leitura e escrita.

# Para ler o conteúdo de um arquivo, primeiro devemos abri-lo utilizando a função open() em modo de leitura ("r"). 
# Depois, podemos ler o conteúdo do arquivo utilizando métodos como read() ou readlines().
arquivo = open("D:/GitHub Respositorios/santander-python/data/dados.txt","r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()


# ESCRITA DE ARQUIVOS
# Para escrever dados em um arquivo, abrimos em modo de escrita ("w") utilizando a função open(). 
# Se o arquivo não existir, será criado automaticamente. Se o arquivo já existir, seu conteúdo será sobrescrito.
arquivo = open("D:/GitHub Respositorios/santander-python/data/dados.txt","w")
arquivo.write("Ola Mundo!")
arquivo.close()

# Usando with
with open("D:/GitHub Respositorios/santander-python/data/dados.txt","r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
    