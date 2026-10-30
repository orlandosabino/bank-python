salario = float (input("digite seu salário: "))
emprestimo = float (input("valor do empréstimo: "))
parcelas = int (input("digite o número de parcelas: "))
valor_emprestimo = emprestimo/parcelas
salario_terco = salario/3
if salario_terco > valor_emprestimo :
    print("empréstimo aprovado")
else:
    print ("emprestimo reprovado")   