while True:
    a = ""
    a_temp = input()
    for x in a_temp:
        try:
            if isinstance(int(x), int):
                a.append(int(x))
            elif isinstance(x, str):
                a.append(ord(x) - 96)
        except:
            ('nothing')
    print(a)