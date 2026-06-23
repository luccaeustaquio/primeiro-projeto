nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))

lista_Notas = []

lista_Notas.append(nota1)
lista_Notas.append(nota2)
lista_Notas.append(nota3)


media = sum(lista_Notas) / len(lista_Notas)

if media >= 7:
    print(f"Aluno(a) Aprovado(a) com média {media:.2f}")
elif media >= 3 and media < 7:
    print(f"Aluno(a) em Recuperaçao com média {media:.2f}")
    fez_recuperacao = input("Aluno já fez a recuperaçao? ")
    if fez_recuperacao == "s":
        nota_recuperacao = float(input("Digite a nota da recuperaçao: "))
        if nota_recuperacao >= 5:
            print("Aluno(a) aprovado pela recuperaçao")
        else:
            print("Aluno(a) nao obteve nota suficiente para ser aprovado após a recuperacao.")
else:
    print(f"Aluno(a) em Recuprovado com média {media:.2f}")