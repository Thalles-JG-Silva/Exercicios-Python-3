#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.

# Solicita as informações do usuário
valor_casa = float(input("Digite o valor da casa: R$ "))
salario_comprador = float(input("Digite o salário do comprador: R$ "))
anos_pagamento = int(input("Em quantos anos o comprador deseja pagar? "))

# Calcula o valor da prestação mensal
prestacao_mensal = valor_casa / (anos_pagamento * 12)

# Calcula o valor máximo permitido para a prestação (30% do salário)
limite_prestacao = salario_comprador * 0.3

# Verifica se a prestação mensal está dentro do limite
if prestacao_mensal <= limite_prestacao:
    print(f"Empréstimo aprovado! A prestação mensal será de R$ {prestacao_mensal:.2f}.")
else:
    print(f"Empréstimo negado. A prestação mensal de R$ {prestacao_mensal:.2f} excede 30% do salário.")
