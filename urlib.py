"""
since http is so common, we have a library that does all the
socket work for us and makes web pages look like a file
"""

import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.text")
for line in fhand:
	print(line.decode().strip())


"""url words"""

import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.text")

counts = dict()
for line in fhand:
	words = line.decode().split()
	for word in words:
		counts[word] = counts.get(word, 0) + 1
print(counts)