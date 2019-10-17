list = []
c = 1
i = 1
while i < 6:
    weight = float(input(f"weight[{c}]: "))
    list.append(weight)
    i += 1
    c += 1

print(f"\nBigger: {max(list)}", end = "kg\n")
print(f"Smaller: {min(list)}", end = "kg\n")

