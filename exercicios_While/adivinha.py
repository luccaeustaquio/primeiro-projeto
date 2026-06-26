import random

num_Dig = int(input("Digite um número:"))
num_Aleatorio = random.randint(1, 20)

while num_Dig != num_Aleatorio:
    num_Dig = int(input("Digite um número:"))

    if num_Dig == num_Aleatorio:
        print(f"Acertou ! O número era {num_Dig}")