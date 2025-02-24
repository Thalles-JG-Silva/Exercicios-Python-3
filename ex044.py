# Exercício: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

# Exibe o nome da loja formatado no centro da tela
print('{:=^40}'.format(' LOJAS GUANABARA '))

# Solicita ao usuário o preço do produto
preco = float(input("Preço das compras: R$ "))

# Exibe as opções de pagamento disponíveis
print('''FORMAS DE PAGAMENTO
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

# Solicita a opção de pagamento escolhida pelo usuário
opcao = int(input("Qual é a opção de pagamento? "))

# Verifica a opção escolhida e aplica os descontos ou juros conforme necessário
if opcao == 1:
    total = preco * 0.90  # Aplica 10% de desconto
    print("Pagamento à vista no dinheiro/cheque. Você tem 10% de desconto.")
elif opcao == 2:
    total = preco * 0.95  # Aplica 5% de desconto
    print("Pagamento à vista no cartão. Você tem 5% de desconto.")
elif opcao == 3:
    total = preco  # Sem desconto, valor normal
    print(f"Pagamento parcelado em 2x no cartão. O valor final é R$ {total:.2f}")
elif opcao == 4:
    parcelas = int(input("Quantas parcelas? "))  # Solicita a quantidade de parcelas
    total = preco * 1.20  # Aplica 20% de juros
    valor_parcela = total / parcelas  # Calcula o valor de cada parcela
    print(f"Pagamento parcelado em {parcelas}x de R$ {valor_parcela:.2f} COM JUROS.")
else:
    total = 0  # Caso a opção seja inválida
    print("Opção INVÁLIDA de pagamento. Tente novamente.")

# Exibe o valor total final a ser pago
if total > 0:
    print(f"O total da sua compra será R$ {total:.2f}")
