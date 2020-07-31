"""
Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below
"""

counts = dict()
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
for line in handle:
	if line.startswith("From "):
		words = line.split()
		temp = words[5]
		counts[temp[:2]] = counts.get(temp[:2], 0) + 1

lst = list()
for key, val in counts.items():
	temp = (key, val)
	lst.append(temp)

lst = sorted(lst)

for key, val in lst:
	print(key, val)