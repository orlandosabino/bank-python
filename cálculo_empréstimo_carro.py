#Entrada de dados
valor_carro = float(input("Digite o valor docarro: "))
entrada = float(input("Digite o valor da entrada "))
taxa_de_juros = float(input("Digite a taxa de juros "))
meses = int(input("Digite em quantos meses deseja pagar: "))
#Valor financiado
valor_financiado = valor_carro - entrada
#Cálculo da parcela (juros simples)
parcela = (valor_financiado * (1+ (taxa_de_juros/100) * meses)) / meses
#Saída
print(f"Valor financiado: R$ {valor_financiado:.2f}")
print(f"Parcela mensal: R$ {parcela:.2f}")