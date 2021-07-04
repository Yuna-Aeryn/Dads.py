fname = input("Enter file name: ")
fh = open(fname)
for x in fh:
    x = x.upper()
    x = x.rstrip()
    print(x)