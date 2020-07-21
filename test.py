"""dict_name_age = {"sara":19, "caio": 20, "mayara":21}
for k,v in dict_name_age.items():
    print(k,"tem", v, "anos")
"""

# a palavra que mais aparece

name = input("Enter file:")
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) +1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
