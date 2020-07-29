"""
Write a program to read through the mbox-short.txt and figure out 
who has sent the greatest number of mail messages. The program looks for 'From ' lines 
and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address 
to a count of the number of times they appear in the file. After the dictionary is 
produced, the program reads through the dictionary using a maximum loop to find the 
most prolific committer.

"""
counts = dict()
value = 0
key = 0
email = []
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
file = open(name)
for line in file:
	if line.startswith("From "):
		words = line.split()
		email.append(words[1])
for word in email:
    counts[word] = counts.get(word, 0) + 1
for k, v in counts.items():
	if v>value:
		value=v
		key = k
print(key, value)