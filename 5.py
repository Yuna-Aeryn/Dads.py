favorite_num = {
    'Jack': 2,
    'Mina': 3,
    'Life': 4,
}

friends = ['Jack', 'Mina', 'Life', 'Fray']


'''
for name, number in favorite_num.items():
    print(name + " likes the number " + str(number))

for name in favorite_num.keys():
    print("\n" + name)

for number in favorite_num.values():
    print("\n" + str(number))

'''

for name in friends:
    if name in favorite_num.keys():
        print(name + " has taken the poll")
    elif name not in favorite_num.keys():
        print(name + " has not taken the poll")