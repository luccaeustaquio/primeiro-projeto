print("Tabuada automatizada.")

num = int(input("Digite um número para realizar uma tabuada:"))
opcao = 1
quant = 0

while(opcao == 1):

    for atual in range(11):
        tabuada = num * atual

        print("-----------------------------")
        print(f"{num} * {atual} : {tabuada}")
        print("============================")

    quant += 1
    opcao = int(input("Deseja iniciar novamente: Digite 1 pra sim 2- Nao"))
    if opcao == 1:
        num = int(input("Digite um número para realizar uma tabuada:"))
    else:
        print("Programa finalizado com sucesso!")
        print(f"Voce realizou {quant} tabuada(s)")
