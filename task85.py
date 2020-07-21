file = open("mbox-short.txt")
count = 0

for line in file:
    if line.startswith("From "):
        line2 = line.split()
        print(line2[1])
        count+=1

        
print("There were", count, "lines in the file with From as the first word")
