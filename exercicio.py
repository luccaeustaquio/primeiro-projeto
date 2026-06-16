faturamento_sujo = [1200, -50, 3400, 2100, -120, 1500, 5000, -10]
vendas_limpas = []

for atual in faturamento_sujo :
 
    if atual > 0:
       vendas_limpas.append(atual)


print("Vendas Limpas: ", vendas_limpas)        