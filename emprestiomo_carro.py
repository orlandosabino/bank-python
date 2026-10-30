print("Bem vindo a gestão de empréstimos")
salario = float(input('digite seu salário: '))
moradia = float(input(" valor do aluguel:"))
despesas_fixas = float (input(" digite o valor das despesas fixas:" ))
outros_emprestimos = float(input("digite o valor de outros empréstimos: "))
valor_do_carro = float(input("digite o valor do carro a ser adquirido: "))
numero_de_parcelas = int(input("digite o número de parcelas: "))
if valor_do_carro <= 50000:
    print ("numero máximo de parcelas 24")
    numero_de_parcelas = 24
else:
    print ("numero de máximo de parcelas 60")
    numero_de_parcelas = 60
valor_da_parcela = valor_do_carro / numero_de_parcelas
limite_parcela = salario * 0.30
total_gastos_atuais = moradia + despesas_fixas + outros_emprestimos + valor_da_parcela 
print(f"\n---Resultado da Análise---")
print(f"Valor da parcela: R$ {valor_da_parcela:.2f}")
#Validação se o empréstimo cabe no orçamento
if valor_da_parcela <= limite_parcela and (total_gastos_atuais + valor_da_parcela) <= salario:
    print("Parabéns! Empréstimo APROVADO.")
else:
    print("Empréstimo NEGADO. O valor da parcela excede a margemde comprometimento de renda.")    

    

