from tkinter import *
from urllib.parse import urlparse
import socket as s
import pyperclip
import numpy as np

# 기본 tkinter 배경
root = Tk()
root.title("Password Generator")

# 계산 (변수가 개판인건 봐주세요)
def Calculate(event):
    actualcodeinput = codeinput.get()
    if len(actualcodeinput) >= 8:
        # URL에서 가져오는 userinput에서 내용을 가져오고 .com 형태로 바꾸기
        b = urlparse(Userinput.get()).netloc
        # www가 있다면 지우기
        if b[0:3] == "www":
            b = b[4:]
        # ip로 바꾸고 동시에 중간에 .을 지우기
        ip = s.gethostbyname(b).replace('.', '')
        # 유니코드로 변환
        a = ""
        for letter in actualcodeinput:
            a = a + str(ord(letter))
        # 드디어 숫자로 곱하기
        password_temp = np.multiply(float(ip), float(a))
        # 그 숫자를 float 형태로 바꾸고 뒤에 0이나 . 지우기
        password_temp = ("%.17f" % float(password_temp)).rstrip('0').rstrip('.')
        # 12자리로 자르기
        password_temp = str(password_temp)[0:12]
        # 실제 패스워드 변환과정 (이해하고 싶으면 부르셈, 좀 복잡해서 쓰기 귀찮음)
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
Userinput.grid(row=0, column=1)
Userinput.xview_moveto(0)
# the input for a
codeinput = Entry(root, width=50, borderwidth=5)
codeinput.grid(row=1, column=1)
# for user to view url in case they can't
Userview = Label(root)
Userview.grid(row=2, column=1)
# actual password output
Conclusion = Label(root)
Conclusion.grid(row=3, column=1)
# label for showing
urlhere = Label(root)
urlhere.config(text = 'URL Here:')
urlhere.grid(row=0, column=0)
passwordhere = Label(root)
passwordhere.config(text = 'Pasword Here:')
passwordhere.grid(row=1, column=0)


# 키바인딩
root.bind('<Return>', Calculate)
root.bind('<Control-c>', Copy)

root.mainloop()