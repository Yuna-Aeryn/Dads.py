fn = open("E:\RUBBISH\mbox-short.txt")
count = 0
lines = []

for x in fn:
    if x.startswith("From") and not x.startswith("From:"):
        y = x.rstrip().split()
        print(y[1])
        count = count + 1



print("There were", count, "lines in the file with From as the first word")
