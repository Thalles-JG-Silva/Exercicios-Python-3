# Exercício: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
# de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

# Importando a biblioteca para obter o ano atual
from datetime import date

# Solicitando o ano de nascimento do usuário
ano_nascimento = int(input("Digite o ano de nascimento do atleta: "))

# Obtendo o ano atual
ano_atual = date.today().year

# Calculando a idade do atleta
idade = ano_atual - ano_nascimento

# Determinando a categoria do atleta com base na idade
if idade <= 9:
    categoria = "MIRIM"
elif idade <= 14:
    categoria = "INFANTIL"
elif idade <= 19:
    categoria = "JUNIOR"
elif idade <= 25:
    categoria = "SÊNIOR"
else:
    categoria = "MASTER"

# Exibindo o resultado para o usuário
print(f"O atleta tem {idade} anos e pertence à categoria: {categoria}")
