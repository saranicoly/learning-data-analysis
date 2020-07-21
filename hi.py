# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
count = 0
total = 0
list_num = []
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count+=1
    var = line[21:]
    var = float(var)
    list_num.append(var)
    #print(count, line)
for item in list_num:
	total = total+item
total = total/count
print("Average spam confidence: ", total)