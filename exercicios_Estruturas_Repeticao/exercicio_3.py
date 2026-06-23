carrinhos_vendas = [150.00, 450.50, 89.90, 1200.00, 320.00, 45.00, 750.00]

faturamento_total = sum(carrinhos_vendas)
quant_Carrinho = len(carrinhos_vendas)

ticket_Medio = faturamento_total / quant_Carrinho

mais_caro = max(carrinhos_vendas)
mais_barato  = min(carrinhos_vendas)


print(f"Faturamento total {faturamento_total}")
print(f"'Ticket Medio do Carrinho: {ticket_Medio : .2f}")
print(f"Produto mais caro: {mais_caro}")
print(f"Produto mais barato: {mais_barato}")






