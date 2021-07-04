fname = input("Enter file name: ")
fh = open(fname)
total = 0
count = 0

for line in fh:
    if line.startswith('X-DSPAM-Confidence:'):
        total = total + float(line[21:])
        count = count + 1

asc = total/count
print('Average spam confidence: ' + str(asc))
