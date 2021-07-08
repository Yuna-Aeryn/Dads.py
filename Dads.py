from tkinter import *
from urllib.parse import urlparse
import socket as s
import pyperclip
import numpy as np

root = Tk()
root.title("Password Generator")

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
capitalalphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def Calculate(event):
    actualcodeinput = codeinput.get()
    if len(actualcodeinput) >= 8:
        b = urlparse(Userinput.get()).netloc
        if b[0:3] == "www":
            b = b[4:]
        ip = s.gethostbyname(b).replace('.', '')
        a = ""
        try:
            for x in actualcodeinput:
                if x in alphabet:
                    a = a + str(alphabet.index(x) + 1)
                elif x in capitalalphabet:
                    a = a + str(capitalalphabet.index(x) + 1)
                else:
                    a = a + x
            password_temp = np.multiply(float(ip), float(a))
        except:
            Conclusion.config(text='only characters or numbers')
        password_temp = ("%.17f" % float(password_temp)).rstrip('0').rstrip('.')
        password_temp = str(password_temp)[0:12]
        global password_coded
        password_coded = "".join(
            [str(chr(ord('A') + int(password_temp[0]))), str(chr(ord('a') + int(password_temp[1]))),
             str(chr(ord('a') + int(password_temp[2]))), str(chr(ord('a') + int(password_temp[3]))),
             str(password_temp[4:11]), str(chr(33 + int(password_temp[11])))])
        Userview.config(text=b)
        Conclusion.config(text=password_coded)
    else:
        Userview.config(text="")
        Conclusion.config(text='8 or more characters')

# copy
def Copy(event):
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


#엔터키
root.bind('<Return>',Calculate)
root.bind('<Control-c>', Copy)

root.mainloop()