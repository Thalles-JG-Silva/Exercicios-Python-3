#Crie um programa que leia duas notas de um aluno e calcule sua média,
#mostre uma mensagem no final, de acordo com a média atingida:
#-Média abaixo de 5.0: REPROVADO
#-Média entre 5.0 e 6.9 RECUPERAÇÂO
#-Média 7.0 ou superior: APROVADO

# Solicita as duas notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Calcula a média das notas
media = (nota1 + nota2) / 2

# Exibe a situação do aluno de acordo com a média
if media < 5.0:
    print(f"Média: {media:.1f} - REPROVADO")
elif 5.0 <= media <= 6.9:
    print(f"Média: {media:.1f} - RECUPERAÇÃO")
else:
    print(f"Média: {media:.1f} - APROVADO")


