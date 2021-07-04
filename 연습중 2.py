
fh = open("E:\RUBBISH//a.txt")
lst = list()
for line in fh:
    words = line.rstrip().split()
    for x in words:
        if x not in lst:
            lst.append(x)
        else:
            continue

print(sorted(lst))
