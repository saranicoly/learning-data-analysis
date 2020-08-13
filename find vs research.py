""" using re.search() like find() """

hand = open("arquivo.txt")
for line in hand:
	line = line.rstrip()
	if line.find("From: ")>=0:
		print(line)



import re
hand = open("arquivo.txt")
for line in hand:
	line = line.rstrip()
	if re.search("From: ", line):
		print(line)


""" using re.search() like startswith() """

hand = open("arquivo.txt")
for line in hand:
	line = line.rstrip()
	if line.startswith("From: "):
		print(line)


import re
hand = open("arquivo.txt")
for line in hand:
	line = line.rstrip()
	if re.search("^From: ", line):
		print(line)
#we fine-tune what is matched by adding special characters to the string


import re
x = "My favorite numbers are 19 and 42"
y = re.findall("[0-9]+", x)
print(y)

import re
x = "From: Using the : character"
y = re.findall("^F.+:", x)
print(y)
#^F    first character in the match is an F
#.+    one or more characters
#:    last character in the match is a :

#From emailaddress@mail.com anything 27 other
y = re.findall("\S+@\S+", x)
print(y)