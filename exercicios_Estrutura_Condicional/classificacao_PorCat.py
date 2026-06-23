#Até 9 anos: Mirim• Até 14 anos:
# Infantil• Até 19 anos: Junior• Até 25 anos: Sênior• Acima de 25 anos: Master


idade_Atleta = int(input("Atleta: \n Digite a sua idade:"))

if idade_Atleta <=  14:
    print("Atleta Mirim")
elif idade_Atleta <= 19:
    print("Atleta da categoria infantil!")
elif idade_Atleta <= 25:
    print("Atleta Sênior")
else:
    print("Atleta Master")