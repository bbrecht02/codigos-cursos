#variavel
nome= "bennyson brecht gomes correia"
teste= "    aprenda python    "
#fatiamento
print(nome[5])
print (nome.count("B"))           #contagem de um caracter especifico
print (len(nome))                 #quantidade de caracteres da string
print (nome.find("Gomes"))        #encontrar um conjunto de caracter especifico
print ("Bennyson" in nome) 

#transformação
print(nome.replace("bennyson","beatiz")) #troca o conjunto de string selecionado por outro dito
print(nome.upper())                #coloca toda a string em letra maiusculas
print(nome.lower())                #coloca toda a string em letra minusculas
print (nome.capitalize())           #coloca a primeira letra da primeira palavra em maiuscula
print (nome.title())                #faz uma quebra da string e coloca letra maiuscula em cada primeira das palavras 
print(teste.strip())                 #remove todos espaços inuteis
print(teste.rstrip())                 #remove só os ultimos espaços inuteis
print(teste.lstrip())                 #remove só os primeiros espaços inuteis

#divisão
print (nome.split())                 #gera uma lista com todas as palavras da cadeia de caracteres removendo os espaços entre elas 
print ("-".join(nome))
