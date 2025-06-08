# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# A) Os 5 primeiros.
# B) Os últimos 4 colocados.
# C) Times em ordem alfabética.
# D) Em que posição está o time da Chapecoense.

times = (
    'Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians',
    'Bragantino', 'Fluminense', 'América-MG', 'Atlético-GO', 'Santos',
    'Ceará', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá',
    'Bahia', 'Juventude', 'Grêmio', 'Sport', 'Chapecoense'
)

# A) Os 5 primeiros
print("A) Os 5 primeiros colocados:")
print(times[:5])

# B) Os últimos 4 colocados
print("\nB) Os 4 últimos colocados:")
print(times[-4:])

# C) Times em ordem alfabética
print("\nC) Times em ordem alfabética:")
print(sorted(times))

# D) Em que posição está o time da Chapecoense
print("\nD) Posição da Chapecoense:")
print(f"A Chapecoense está na {times.index('Chapecoense') + 1}ª posição.")
