print("Sistema de senha!")
usuario_User = input("Digite o usuário:")
usuario_Senha = int(input("Digite a senha:"))
usuario = "admin"
senha = int(9988)


if usuario_User == usuario and usuario_Senha == senha:
    print("Acesso liberado! Bem vindo admin")

else:
    print("Acesso negado")
