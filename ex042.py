# Exercício: Refazer o DESAFIO 035 dos triângulos, acrescentando o recurso de 
# mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

# Solicita ao usuário os três lados do triângulo
lado1 = float(input("Digite o primeiro lado do triângulo: "))
lado2 = float(input("Digite o segundo lado do triângulo: "))
lado3 = float(input("Digite o terceiro lado do triângulo: "))

# Verifica se os lados informados podem formar um triângulo
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print("Os segmentos podem formar um triângulo!")

    # Determina o tipo de triângulo com base nos lados
    if lado1 == lado2 == lado3:
        tipo = "EQUILÁTERO"  # Todos os lados são iguais
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        tipo = "ISÓSCELES"  # Dois lados são iguais
    else:
        tipo = "ESCALENO"  # Todos os lados são diferentes

    # Exibe o tipo de triângulo formado
    print(f"O triângulo formado é do tipo: {tipo}")

else:
    # Caso os lados não formem um triângulo
    print("Os segmentos informados NÃO podem formar um triângulo.")
