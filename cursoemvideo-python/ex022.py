import time
nome= (str(input("digite seu nome completo:"))).strip()
print ("Analisando seu nome...")
time.sleep(1)
print ("seu nome em letras maiúsculas é:", nome.upper())
print ("seu nome em letras minúsculas é:", nome.lower())
print ("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(" ")))
s= nome.split()
print (s)
print ("seu primeiro nome é: {} e ele tem {} letras".format(s[0],nome.find(' ')))



