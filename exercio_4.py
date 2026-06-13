gastos_clientes = [50.00, 120.50, 450.00, 89.90, 210.00, 350.00, 25.00, 180.00]

class_Bronze = 0
class_Ouro = 0
class_Prata = 0

gastos_clientes_Ouro = []
gastos_clientes_Prata = []
gastos_clientes_Bronze = []

for atual in gastos_clientes:

    if atual <= 100.00 :
           class_Bronze += 1
           gastos_clientes_Bronze = sum(atual)

    elif atual <= 300.00 :
         class_Prata += 1

    else :
        class_Ouro += 1



print(f"Classe Ouro: {class_Ouro}")
print(f"Classe Prata: {class_Prata}")
print(f"Classe Bronze: {class_Bronze}")

