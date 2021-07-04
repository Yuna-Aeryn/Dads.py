largest = None
smallest = None

while True:
    fuserin = input("integer plz: ")
    if fuserin == 'done':
        break
    try:
        userin = int(fuserin)
    except:
        print("Invalid input")
    if smallest is None:
        smallest = userin
    if largest is None:
        largest = userin
    if smallest > userin:
        smallest = userin
    if largest < userin:
        largest = userin

print("Maximum is", largest)
print("Minimum is", smallest)
