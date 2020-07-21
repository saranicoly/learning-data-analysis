"""
abrir um arquivo, ler e separar todas as palavras em ordem alfabetica em uma lista
"""
fname = input("Enter file name: ")
file = open(fname)
lista = []
for line in file:
	line = line.rstrip()
	words = line.split()
	for word in words:
		if word in lista:
			continue
		lista.append(word)
lista.sort()
print(lista)