# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
""" Esse programa abre um site, pega todos os números nele e apresenta a soma"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
lista = []

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
	conteudo = int(tag.contents[0])
	lista.append(conteudo)

print("it's working: ", sum(lista))