counts = dict()
line = str(input("Enter a line of text"))
#split the line into a list of words
words = line.split()
print("Words:", words)

print("Counting...")
for word in words:
    counts[word] = counts.get(word, 0) + 1
print("Counts: ", counts)
