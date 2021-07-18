from urllib.parse import urlparse
import socket as s
import numpy as np
from decimal import *


actualcodeinput = input("password: ")
# URL에서 가져오는 input에서 내용을 가져오고 .com 형태로 바꾸기
b = urlparse(input()).netloc
# www가 있다면 지우기
if b[0:3] == "www":
    b = b[4:]
print(b)
# ip로 바꾸고 동시에 중간에 .을 지우기
ip = s.gethostbyname(b).replace('.', '')
print(ip)
# 패스워드 유니코드로 변환
a = ""
for letter in actualcodeinput:
    a = a + str(ord(letter))
print(a)
# 드디어 숫자로 곱하기
password_temp = Decimal(np.multiply(float(ip), float(a)))
print(password_temp)
'''
password_temp = Decimal(float(password_temp))
print(password_temp)
'''
# 그 숫자를 float 형태로 바꾸고 뒤에 0이나 . 지우기 - disabled
# 12자리로 자르기
password_temp = str("%.12f" % Decimal(password_temp).sqrt())[-12:]
print(password_temp)
# 실제 패스워드 변환과정 (이해하고 싶으면 부르셈, 좀 복잡해서 쓰기 귀찮음)
global password_coded
password_coded = "".join(
    [str(chr(ord('A') + int(password_temp[0]))), str(chr(ord('a') + int(password_temp[1]))),
     str(chr(ord('a') + int(password_temp[2]))), str(chr(ord('a') + int(password_temp[3]))),
     str(password_temp[4:11]), str(chr(33 + int(password_temp[11])))])
print(password_coded)