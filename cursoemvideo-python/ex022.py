import time
nome= (str(input("digite seu nome completo:"))).strip()
print ("Analisando seu nome...")
time.sleep(1)
print ("seu nome em letras maiúsculas é:", nome.upper())
print ("seu nome em letras maiúsculas é:", nome.lower())
print ("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(" ")))
print ("seu primeiro nome é {} e possui {} letras".format(nome[0:8],len(nome[0:8])))
