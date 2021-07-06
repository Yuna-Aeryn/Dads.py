from tkinter import *
from urllib.parse import urlparse
import socket as s
import pyperclip

root = Tk()
root.title("Password Generator")

# calculate
def Calculate():
    # input > .com형태 > www 지우고 > ip로 바꾸고 > .지우고 > 곱하기 > 12자리까지 자르고 > 암호화
    b = urlparse(Userinput.get()).netloc
    if b[0:3] == "www":
        b = b[4:]
    ip = s.gethostbyname(b).replace('.', '')
    # a는 나중에 정의함
    password_temp = str(ip * a)[0:12]
    global password_coded
    password_coded = str(chr(ord('A')+int(password_temp[0]))) + str(chr(ord('a')+int(password_temp[1]))) + str(chr(ord('a')+int(password_temp[2]))) + str(chr(ord('a')+int(password_temp[3]))) + str(password_temp[4:11]) + str(chr(33+int(password_temp[11])))
    print(password_coded)
    Conclusion.config(text=password_coded)
    Userview.config(text=b)

# copy
def copy():
    pyperclip.copy(password_coded)

# the input for a
codeinput = Entry(root, width=50, borderwidth=5)
codeinput.pack()
# URL input
Userinput = Entry(root, width=50, borderwidth=5)
Userinput.pack()
Userinput.xview_moveto(0)
# for user to view url in case they can't
Userview = Label(root)
Userview.pack()
# actual password output
Conclusion = Label(root)
Conclusion.pack()
# Button placements
Button1 = Button(root, text='Calculate', padx=50, pady=20, command=Calculate)
Button1.pack()
Button2 = Button(root, text='Copy', padx = 10, pady = 10, command = copy)
Button2.pack()

a = ""
a_temp = codeinput.get()
for x in a_temp:
    try:
        if isinstance(float(x), int):
            a.append(float(x))
        elif isinstance(str(x), str):
            a.append(ord(x) - 96)
    except:
        print('nothing')

root.mainloop()










