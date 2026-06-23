quantidade_Maiores = 0
quantidade_Menores = 0

for atual in range(7):
    ano_Nascimento = int(input("Digite o seu ano de nascimento:"))

    if ano_Nascimento <= 2008:
        quantidade_Maiores += 1
    else:
        quantidade_Menores += 1


print(f"Quantidade maiores: {quantidade_Maiores}")
print(f"Quantidade menores: {quantidade_Menores}")


