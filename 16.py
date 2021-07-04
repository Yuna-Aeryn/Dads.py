from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Bingo')

# 끝날 때 턴을 얼마나 썼느냐 알려주기 위함
count = 0

# 클릭 시 작동하는 함수
def click(b):
    global count
    if b['text'] == ' ':
        b['text'] = 'O'


    elif b['text'] == 'O':
        b['text'] = ' '

    count = count + 1

# 칸이 다 채워진 것을 확인하는 함수




# 버튼의 기능
b1 = Button(root, text=' ', height=3, width=6, command=lambda: [click(b1), click(b2), click(b6)])
b2 = Button(root, text=' ', height=3, width=6, command=lambda: [click(b2), click(b7), click(b1), click(b3)])
b3 = Button(root, text=' ', height=3, width=6, command=lambda: [click(b3), click(b4), click(b2), click(b8)])
b4 = Button(root, text=' ', height=3, width=6, command=lambda: [click(b4), click(b5), click(b3), click(b9)])
b5 = Button(root, text=' ', height=3, width=6, command=lambda: [click(b5), click(b4), click(b10)])

b6 = Button(root, text=' ', height=3, width=6, command=lambda: [click(b6), click(b7), click(b11), click(b1)])
b7 = Button(root, text=' ', height=3, width=6, command=lambda: [click(b7), click(b8), click(b6), click(b2), click(b12)])
b8 = Button(root, text=' ', height=3, width=6, command=lambda: [click(b8), click(b7), click(b9), click(b3), click(b13)])
b9 = Button(root, text=' ', height=3, width=6,
            command=lambda: [click(b9), click(b8), click(b10), click(b4), click(b14)])
b10 = Button(root, text=' ', height=3, width=6, command=lambda: [click(b10), click(b9), click(b5), click(b15)])

b11 = Button(root, text=' ', height=3, width=6, command=lambda: [click(b11), click(b12), click(b16), click(b6)])
b12 = Button(root, text=' ', height=3, width=6,
             command=lambda: [click(b12), click(b11), click(b13), click(b7), click(b17)])
b13 = Button(root, text=' ', height=3, width=6,
             command=lambda: [click(b13), click(b14), click(b12), click(b8), click(b18)])
b14 = Button(root, text=' ', height=3, width=6,
             command=lambda: [click(b14), click(b15), click(b13), click(b9), click(b19)])
b15 = Button(root, text=' ', height=3, width=6, command=lambda: [click(b15), click(b14), click(b10), click(b20)])

b16 = Button(root, text=' ', height=3, width=6, command=lambda: [click(b16), click(b17), click(b11), click(b21)])
b17 = Button(root, text=' ', height=3, width=6,
             command=lambda: [click(b17), click(b18), click(b16), click(b12), click(b22)])
b18 = Button(root, text=' ', height=3, width=6,
             command=lambda: [click(b18), click(b17), click(b19), click(b13), click(b23)])
b19 = Button(root, text=' ', height=3, width=6,
             command=lambda: [click(b19), click(b18), click(b20), click(b14), click(b24)])
b20 = Button(root, text=' ', height=3, width=6, command=lambda: [click(b20), click(b19), click(b15), click(b25)])

b21 = Button(root, text=' ', height=3, width=6, command=lambda: [click(b21), click(b22), click(b16)])
b22 = Button(root, text=' ', height=3, width=6, command=lambda: [click(b22), click(b23), click(b21), click(b17)])
b23 = Button(root, text=' ', height=3, width=6, command=lambda: [click(b23), click(b22), click(b24), click(b18)])
b24 = Button(root, text=' ', height=3, width=6, command=lambda: [click(b24), click(b25), click(b23), click(b19)])
b25 = Button(root, text=' ', height=3, width=6, command=lambda: [click(b25), click(b24), click(b20)])

quitbutton = Button(root, text='quit button', command=lambda: root.destroy)

# 버튼의 위치
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
b4.grid(row=0, column=3)
b5.grid(row=0, column=4)

b6.grid(row=1, column=0)
b7.grid(row=1, column=1)
b8.grid(row=1, column=2)
b9.grid(row=1, column=3)
b10.grid(row=1, column=4)

b11.grid(row=2, column=0)
b12.grid(row=2, column=1)
b13.grid(row=2, column=2)
b14.grid(row=2, column=3)
b15.grid(row=2, column=4)

b16.grid(row=3, column=0)
b17.grid(row=3, column=1)
b18.grid(row=3, column=2)
b19.grid(row=3, column=3)
b20.grid(row=3, column=4)

b21.grid(row=4, column=0)
b22.grid(row=4, column=1)
b23.grid(row=4, column=2)
b24.grid(row=4, column=3)
b25.grid(row=4, column=4)

while True:
    click(b1 or b2 or b3 or b4 or b5 or b6 or b7 or b8 or b9 or b10 or b11 or b12 or b13 or b14 or b15 or b16 or b17 or b18 or b19 or b20 or b21 or b22 or b23 or b24 or b25)



root.mainloop()



