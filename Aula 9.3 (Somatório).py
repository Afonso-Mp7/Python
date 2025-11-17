from zlib import adler32

a = int(input("Insere um número."))
x = 0
while a >= 0:
    x += a
    a -= 1
print(x)