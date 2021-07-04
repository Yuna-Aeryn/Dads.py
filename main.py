guests = ['albert', 'me' , 'Fray']
for human in guests:
    print(" i invite " + human + " to dinner!")

'''
print(guests[-1] + "cannot make it!")

guests[-1] = 'new person'

for x in guests:
    print("i invite" + x + "to the party!")\
'''

new_sentence = "edit, just found a new table"
print(new_sentence.upper())

guests.insert(0, 'the fray')
guests.insert(2, 'how to save a life')
guests.append('now')

for people in guests:
    print(people + ' invited!')

print("\ni can only invite two people to dinner, the stage is too small")

z = guests.pop()
print('srry '+ z + " can't make it x happen!" )
for x in guests:
    print(x + " you are still invited!")

print(guests)
del guests[0]
del guests[1]
del guests[2]
print(guests)
