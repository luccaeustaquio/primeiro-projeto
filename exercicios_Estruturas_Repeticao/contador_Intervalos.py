print("Bem vindo ao COntador de Intervalos!")
print("Precisamos de um valor inicial, um valor final e um valor de passo (de quanto em quanto a contagem deve andar) ")

valor_Inicial = int(input("Digite o valor inicial: "))
valor_Final = int(input("Digite um valor final: "))
valor_Passo = int(input("Digite um valor de passo: "))

print(f"Contagem em {valor_Passo} passos")

for atual in range(valor_Inicial,valor_Final,valor_Passo):

    print(f"{atual}")