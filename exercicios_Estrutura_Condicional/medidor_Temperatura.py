temperatura_City = int(input("Qual a temperatura em graus Celsius: C"))

if temperatura_City < 15:
    print("Clima frio")

elif temperatura_City > 15 and temperatura_City <= 25:
    print("Clima agradável")
else:
    print("Clima quente!")