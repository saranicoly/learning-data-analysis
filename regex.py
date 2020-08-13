""" Read a file, get all the numbers througout the text and give the sum of them"""

import re
name = input("Enter file: ")
handle = open(name)
lista = []
for line in handle:
	y = re.findall("[0-9]+", line)
	print("Inicialmente: ", y)
	count=0
	if len(y)>0:
		while len(y)!=count:
			y[count] = int(y[count])
			lista.append(y[count])
			print(y[count], "convertido para int e adicionado a lista")
			count+=1
			

print(sum(lista))