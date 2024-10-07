#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#Ex:
#Digite um número: 1834
#Unidade: 4 dezena: 3 centena: 8 milhar: 1

# Leitura do número
numero = int(input("Digite um número de 0 a 9999: "))

# Verificar se o número está dentro da faixa permitida
if 0 <= numero <= 9999:
    # Convertendo o número para string e preenchendo com zeros à esquerda (caso seja menor que 4 dígitos)
    numero_str = f"{numero:04d}"
        
    # Separando os dígitos
    milhar = numero_str[0]
    centena = numero_str[1]
    dezena = numero_str[2]
    unidade = numero_str[3]
        
    # Exibindo os resultados
    print(f"Milhar: {milhar}")
    print(f"Centena: {centena}")
    print(f"Dezena: {dezena}")
    print(f"Unidade: {unidade}")
else:
    print("Número fora do intervalo permitido (0 a 9999).")