while True:
    actualUserinput_temp = Userinput.get()
    if len(actualUserinput_temp) >= 8:
        actualUserinput = actualUserinput_temp
        break
    elif len(actualUserinput_temp) < 8:
        continue

print(actualUserinput)