num = int(input("Digite um número:"))
num2 = int(input("Digite outro número:"))

opcao = int(input("Digite a operacao que deseja realizar:\n"
                    "1- Somar\n"
                    "2- Subtrair\n"
                    "3- Multiplicar\n"
                    "4- Dividir\n"
                    "5- Sair"))




match opcao:
        case 1 :
            print("Soma")
            soma = num + num2
            print(f"Soma: {num} + {num2} = {soma}")
        case 2:
            print("Subtracao")
            sub = num - num2
            print(f"Soma: {num} + {num2} = {sub}")
        case 3:
            print("Multiplicacao")
            mult = num * num2
            print(f"Soma: {num} + {num2} = {mult}")
        case 4:
            print("Dividir")
            div = num / num2
            print(f"Soma: {num} + {num2} = {div}")
        case 5:
            print("PROGRAMA FINALIZADO!")

        case _ :
            print("Número inválidoS")

print("Programa finalizado")


