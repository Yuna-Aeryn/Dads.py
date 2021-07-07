from tkinter import *
from urllib.parse import urlparse
import socket as s
import pyperclip

root = Tk()
root.title("Password Generator")

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
capitalalphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# calculate
def Calculate():
    # input > .com형태 > www 지우고 > ip로 바꾸고 > .지우고 > a 값 받고 > 곱하기 > 12자리까지 자르고 > 암호화
    b = urlparse(Userinput.get()).netloc
    if b[0:3] == "www":
        b = b[4:]
    ip = s.gethostbyname(b).replace('.', '')
    password_temp = str(ip * 381591015)[0:12]
    global password_coded
    password_coded = "".join([str(chr(ord('A')+int(password_temp[0]))),str(chr(ord('a')+int(password_temp[1]))),str(chr(ord('a')+int(password_temp[2]))),str(chr(ord('a')+int(password_temp[3]))),str(password_temp[4:11]),str(chr(33+int(password_temp[11])))])
    Conclusion.config(text=password_coded)
    Userview.config(text=b)

# copy
def copy():
    pyperclip.copy(password_coded)

# URL input
Userinput = Entry(root, width=50, borderwidth=5)
Userinput.pack()
Userinput.xview_moveto(0)
# the input for a
codeinput = Entry(root, width=50, borderwidth=5)
codeinput.pack()
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

root.mainloop()