#Faça um programa que leia o ano de nascimento de um jovem e informe,
#de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,
#se é a hora de se alistar ou se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

# Obtém o ano atual
ano_atual = date.today().year

# Solicita o ano de nascimento do usuário
ano_nascimento = int(input("Digite o ano de nascimento: "))

# Calcula a idade da pessoa
idade = ano_atual - ano_nascimento

# Verifica a situação de alistamento
if idade < 18:
    anos_faltantes = 18 - idade
    ano_alistamento = ano_atual + anos_faltantes
    print(f"Você ainda vai se alistar ao serviço militar.")
    print(f"Faltam {anos_faltantes} anos para o alistamento, que será em {ano_alistamento}.")
elif idade == 18:
    print("É hora de se alistar ao serviço militar!")
else:
    anos_passados = idade - 18
    ano_alistamento = ano_atual - anos_passados
    print("Já passou do tempo de alistamento.")
    print(f"Você deveria ter se alistado há {anos_passados} anos, em {ano_alistamento}.")
