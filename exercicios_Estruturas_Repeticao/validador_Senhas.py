senha_Correta = 1234

for atual in range(0,3):

    senha_Digitada = int(input("Digite a senha: "))
    if senha_Digitada == senha_Correta:
        print("Acesso permitido")
        print("Playboyzinho")
        break
    else:
        print("Receba block")