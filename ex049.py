# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

# Solicita um número ao usuário
num = int(input("Digite um número para ver sua tabuada: "))

print(f"\nTabuada de {num}:\n")

# Loop para calcular e exibir a tabuada de 1 a 10
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
