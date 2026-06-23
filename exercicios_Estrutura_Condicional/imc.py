print("Calculop de IMC:")
peso = float(input("Digite o seu peso: KG"))
altura = float(input("Digite a sua altura em M"))

IMC = peso / (altura * altura)
print(f"Seu indice de massa corporal é: {IMC:.2f}")
