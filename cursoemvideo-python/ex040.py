primeira_nota= float(input("primeira nota: ")) 
segunda_nota= float(input("Segunda nota: "))
media= (primeira_nota+segunda_nota)/2
if media>=7.0:
    print("com {} de media você esta APROVADO".format(media))
elif media>5.0 and  media<6.9:
    print("com {} de media você esta em RECUPERAÇÃO".format(media))
elif media<5.0:
    print("com {} de media você esta REPROVADO".format(media))
    print("se ferrou menino")

    
    