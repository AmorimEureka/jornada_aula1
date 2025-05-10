
BONUS_PERCENTUAL = 0.1
nome = input("Qual o seu nome: ")
salario = float(input("Qual o seu salário: "))
bonificacao = BONUS_PERCENTUAL * salario
print(f"Senhor {nome}, seu salário é {salario}, então sua bonificação será de {bonificacao}")