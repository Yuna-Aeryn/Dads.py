fn = open('E:\RUBBISH//mbox-short.txt')

words = []
for y in fn:
    if y.startswith("From") and not y.startswith("From:"):
        ylst = y.split()
        words.append(ylst[1])
    else:
        continue



k = dict()
for word in words:
    if word not in k:
        k[word] = 1
    else:
        k[word] = k[word] + 1



bignumber = None
bigname = None
for name, number in k.items():
    if bignumber is None:
        bignumber = number
        bigname = name
    if bignumber <= number:
        bignumber = number
        bigname = name

print(bigname, bignumber)