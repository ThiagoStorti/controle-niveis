'''Instalar a biblioteca colorama
 no terminal: pip install colorama'''

from colorama import Fore, Style, init

# Inicializa o Colorama
init(autoreset=True)

# Lista com os níveis do reservatório
niveis = [ "Muito baixo (CRÍTICO)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (ALERTA)"]

# Define a cor de acordo com o nível
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

# Simula o nível atual do reservatório
nivel_atual = 4

print("=== MONITORAMENTO DO RESERVATÓRIO ===\n")

# Exibe os níveis com suas respectivas cores
for indice, situacao in enumerate(niveis, start=1):
    cor = definir_cor(indice)

    if indice == nivel_atual:
        print(cor + f">> NÍVEL ATUAL: {indice} - {situacao}")
    else:
        print(cor + f"Nível {indice} - {situacao}")

# Restaura o estilo padrão do terminal
print(Style.RESET_ALL + "\nMonitoramento finalizado.")