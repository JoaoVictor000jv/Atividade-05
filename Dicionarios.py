# João Víctor 
# Atividade 05 - Dicionarios
# Importações:
from Listas import imc_calc 

# Exemplos de pessoas
pessoas = {
    "Marília": {"peso": 60, "altura": 1.65},
    "Gabriel": {"peso": 80, "altura": 1.80},
    "Beatriz": {"peso": 55, "altura": 1.60},
    "Andrade": {"peso": 90, "altura": 1.82},
    "Zé Augusto": {"peso": 70, "altura": 1.70}
}

#  Calculando e adicionando o IMC para cada pessoa

for nome, dados in pessoas.items():
    imc = imc_calc(peso=dados["peso"], altura=dados["altura"])
    dados["imc"] = round(imc, 2)

# Exibindo os resyultados

print(f'\nPessoas: \n')
for nome, dados in pessoas.items():
    print(f"{nome} - Peso: {dados["peso"]}kg, Altura: {dados["altura"]}m, IMC: {dados["imc"]}") 
