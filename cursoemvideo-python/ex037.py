num= int(input("digite um numero inteiro: "))
print("[1] BINARIO")
print("[2] OCTAL")
print("[3] HEXADECIMAL")
base= int(input("Escolha uma das bases para converção: "))
if base==1:
    print("{} equivale a {} em binario".format(num,bin(num)))
if base==2:
    print("{} equivale a {} em octal".format(num,oct(num)))
if base==3:
    print("{} equivale a {} em hexadecimal".format(num,hex(num)))
