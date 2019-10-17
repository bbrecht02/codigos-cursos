i = 0
inter = 7
today = 2019
contM = 0 
contm = 0

while i < 7:
    year = int(input(f"year of birth[{inter}]: "))
    i += 1
    inter -= 1
    if today - year >= 18:
        contM += 1
    else:
        contm += 1

print(contM)
print(contm)



        
    



