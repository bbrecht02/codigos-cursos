from random import randint
import time
import sys
print("JOGO DA ADVINHAÇÃO")
print("Vou pensar num numero entre 0 e 5 ")
pc= randint(0, 5)
print("Pensando no numero....")
time.sleep(2)
usr= int(input("Digite um numero (0 a 5): "))
while usr>=6:
    print("Erro! digite um numero entre 0 e 5")
    sys.exit()
    
print("Processando...")
time.sleep(3)

if usr==pc:
    print("Você venceu!")
else:
    print("Você perdeu :/ o numero que eu pensei foi: {} e não {} ".format(pc,usr))
