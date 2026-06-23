#Calcule e exiba o prejuízo total (soma de todos os cancelamentos). = sum
#Descubra a quantidade total de clientes que cancelaram. =len
#Descubra qual foi o maior valor de assinatura cancelada. = max
#Use um laço for e métodos/contadores para descobrir quantos clientes do plano básico (que custa 39.90) cancelaram.
assinaturas_canceladas = [39.90, 99.90, 149.90, 39.90, 59.90, 149.90, 99.90, 39.90]

prejuizo_total = sum(assinaturas_canceladas)
quant_Cancel = len(assinaturas_canceladas)
maior_Cancel = max(assinaturas_canceladas)
cancel_Plano_Basico = []
plano_Basic_Cancel = []

for atual in assinaturas_canceladas:

        if atual <= 39.90 :
         cancel_Plano_Basico.append(atual)

print(f"Quantidade de pessoas que cancelaram: {quant_Cancel}") 
print(f"Valor total do prejuizo: {prejuizo_total:.2f}")
print(f"Maior plano cancelado: {maior_Cancel:.2f}")
print(f"Planos básicos cancelados: {cancel_Plano_Basico}")
        

