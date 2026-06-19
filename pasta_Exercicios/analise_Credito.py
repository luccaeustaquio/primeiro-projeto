salario_Bruto = float(input("Qual o seu salário bruto:"))

valor_Parcela = float(input("Qual o valor da parcela a pagar:"))

trinta_Percent = salario_Bruto * 0.3

if valor_Parcela > trinta_Percent:
    print("Credito recusado!")

else:
    print("Credito aceito!")
