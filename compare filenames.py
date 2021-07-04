import os

foldernames1 = os.listdir('D:\RUBBISH')  # returns 'helpers_image.tif'
foldernames2 = os.listdir('D:\RUBBISH - 복사본') # return 'helpers_image.qml'
x = 0
y = 0
z = 0
a = 0

while x < len(foldernames1):
    foldernames1[x] = foldernames1[x].rsplit('.', 1)[0]
    x = x + 1

while y < len(foldernames2):
    foldernames2[y] = foldernames2[y].rsplit('.', 1)[0]
    y = y + 1

while a < len(foldernames1):
    if foldernames1[z] != foldernames2[a]:
        print(foldernames1[z])
        print(foldernames2[a])
        z = z + 1
        a = a + 1