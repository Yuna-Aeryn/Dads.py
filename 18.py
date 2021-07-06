alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
capitalalphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

a = ""
for x in input():
    if x in alphabet:
        a = a + str(alphabet.index(x) + 1)
    elif x in capitalalphabet:
        a = a + str(capitalalphabet.index(x) + 1)
    else:
        a = a + x


print(float(a))
