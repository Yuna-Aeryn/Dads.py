from urllib.parse import urlparse
import socket as s

while True:
    a = input()
    b = urlparse(a).netloc
    if b[0:3] == "www":
        b = b[4:]
    ip = s.gethostbyname(b).replace('.', '')
    password_temp = str(ip * 381591015)[0:12]
    print(password_temp)