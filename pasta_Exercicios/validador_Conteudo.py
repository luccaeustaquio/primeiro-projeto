nascimento = int(input("Digite o seu ano de nascimento:"))
ano_Atual = 2026

validador = ano_Atual - nascimento

if validador >= 16:
    print("Acesso liberado")

else:
    print("Acesso bloqueado")