# João Víctor Gonçalves

# Atividade 05 - Listas
# Importações:
import statistics as st
from random import random as rd , randint as rdi 
from colorama import  Style as sty, init, Fore
init(autoreset=True)

# Funções 

def imc_calc(peso=70,altura=1.75):
    return peso / altura ** 2

# Análise da lista ( Alturas )
alturas = [ 45, 23, 67, 12, 11, 89, 23, 41, 50, 62, 78, 34, 56, 19, 72, 88, 11, 90, 39,
            65, 76, 27, 48, 59, 81, 14, 11, 93, 3, 68, 29, 52, 74, 16, 85, 20, 55, 38,
            69, 11, 83, 7, 44, 61, 18, 96, 22, 58, 31, 71, 40, 53, 87, 31 ]

print(f"""
    {sty.BRIGHT}Amostragem:{sty.RESET_ALL}

    Maior valor: {sty.BRIGHT}{max(alturas)}{sty.RESET_ALL}.
    Menor valor: {sty.BRIGHT}{min(alturas)}{sty.RESET_ALL}.
    Soma das alturas: {sty.BRIGHT}{sum(alturas)}{sty.RESET_ALL}.
    Valor absoluto de "-25": {sty.BRIGHT}{abs(-25)}{sty.RESET_ALL}.
    Arredondamento de π: {sty.BRIGHT}{round(3.14159,2)}{sty.RESET_ALL}
""")

# Usando statistics
print(f"""
    {sty.BRIGHT}Estatísticas:{sty.RESET_ALL}

    Média: {sty.BRIGHT}{st.mean(alturas):.3f}{sty.RESET_ALL}
    Mediana: {sty.BRIGHT}{st.median(alturas)}{sty.RESET_ALL}
    Moda: {sty.BRIGHT}{st.mode(alturas)}{sty.RESET_ALL}
    Variância da amostra: {sty.BRIGHT}{st.variance(alturas):.3f}{sty.RESET_ALL}
    Desvio de padrão: {sty.BRIGHT}{st.stdev(alturas):.3f}{sty.RESET_ALL}
    {print(Fore.CYAN+ "="*50)}
""")
{print(Fore.CYAN+ "="*50)}

# Matrizes

# Matriz 5x10 de floats entre 0-1

matriz_float = [[rd()for n in range(10)] for n in range(5)]
print('\nMatriz 5x10 ( Floats 0-1 ): ')
for linha in matriz_float:
    linha_formatada = [Fore.CYAN + f"{elemento:.2f}" + sty.RESET_ALL for elemento in linha]
    print(" | ".join(linha_formatada))

#  Matriz 8x4 entre 0-9

matri_int = [[rdi(0,9) for n in range(4)] for n in range(8)]
print('\nMatriz 8x4 ( Inteiros 0-9 ): ')
for linha in matri_int:
    linha_formatada = [Fore.LIGHTBLUE_EX + f"{elemento:.2f}" +sty.RESET_ALL for elemento in linha]
    print(" | ".join(linha_formatada))