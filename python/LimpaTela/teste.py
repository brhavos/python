import os # Biblioteca para executar comandas do sistema operacional.

# Limpa a tela:
if os.name in ('nt', 'dos'):            # Verifica se o sistema operacional é o Windows (de 95 em diante) ou DOS.
    os.system("cls")
else:                                   # Demais sistemas operacionais - no caso Linux, Unix, etc.
    os.system("clear")

# ------------------------------------------------------

print("Olá Mundo! Estou programando em Python utilizando o VS-Code.")

a=2

b=3

c=a+b

print(c)

# FIM #