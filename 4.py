user_0 = {
    'name': 'Emma',
    'last': 'ferico',
    'first': 'falla',
}

friends = ['name', 'last']

for name in user_0.keys():
    if name not in friends:
        print("my name is:" + name)
    if name in friends:
        print("i see your favorite name is: " + name)