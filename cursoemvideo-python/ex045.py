import time 
from random import *
print("Suas Opções:\n[0] PEDRA\n[1]PAPEL\n[2]TESOURA")
User= int(input("Qual sua opção: "))
opcoes= ["pedra", "papel", "tesoura"] 
option = randint(0, 2)
pc= opcoes[option]
print("JO")
time.sleep(1.5)
print("KEN")
time.sleep(1.5)
print("PO!!!")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print ("JOGADOR JOGOU {}".format(opcoes[User].upper()))
print ("COMPUTADOR JOGOU {}".format(opcoes[option].upper()))
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
if pc== "pedra" and User== 0:
    print("EMPATE")
elif pc== "pedra" and User== 1:
    print("JOGADOR VENCE")
elif pc== "pedra" and User==2:
    print("COMPUTADOR VENCE")
elif pc== "papel" and User==0:
    print("COMPUTADOR VENCE")
elif pc== "papel" and User==1: 
    print("EMPATE")
elif pc== "papel" and User==2:
    print("JOGADOR VENCE")
elif pc== "tesoura" and User==0:
    print("JOGADOR VENCE")
elif pc== "tesoura" and User==1:
    print("COMPUTADOR VENCE")
elif pc== "tesoura" and User==2:
    print("EMPATE")
