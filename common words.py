# the top 10 most common words

fhand = open('romeo.txt')
counts = dict()
for line in fhand:
	words = line.split()
	for word in words:
		counts[word] = counts.get(word, 0) + 1


lst = list()
for key, val in counts.items():
	newtup == (value, key)
	lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[:10]:
	print(key, val)


"""
the two last parties can be replaced by:

>>> print( sorted( [(v,k) for k,v in d.items()]))
"""