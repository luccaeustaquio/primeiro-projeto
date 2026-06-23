print("Analisador de desconto:")

total_Valor = float(input("Digite o valor da sua compra:"))

if total_Valor >= 100.01 and total_Valor < 300.00:
    calculo_Desconto = total_Valor * 0.05
    total_Compra = total_Valor - calculo_Desconto
    print(f"Antes {total_Valor} ! Com desconto: {total_Compra}")

elif total_Valor >= 300.01 and total_Valor < 500.00:
    calculo_Desconto = total_Valor * 0.10
    total_Compra = total_Valor - calculo_Desconto
    print(f"Antes {total_Valor} ! Com desconto: {total_Compra}")

elif total_Valor >= 500.00:
     calculo_Desconto = total_Valor * 0.15
     total_Compra = total_Valor - calculo_Desconto
     print(f"Antes {total_Valor} ! Com desconto: {total_Compra}")

else:
    print(f"Compra sem desconto: {total_Valor}")