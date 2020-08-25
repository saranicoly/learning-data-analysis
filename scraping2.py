# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

""" esse programa a partir de um link inicial vai pegando diversos links até um número definido
na variável con"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#variables
lista = []
pos = int(input("Digite a posição: "))
pos = pos-1
con = int(input("Digite a contagem: "))
contador = 1

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    lista.append(tag.get('href', None))
print(lista[pos])

while contador<con:
	url2 = lista[pos]
	html2 = urllib.request.urlopen(url2, context=ctx).read()
	soup2 = BeautifulSoup(html2, 'html.parser')
	lista = []
	tags = soup2('a')
	for tag in tags:
	    lista.append(tag.get('href', None))
	print(lista[pos])
	contador+=1