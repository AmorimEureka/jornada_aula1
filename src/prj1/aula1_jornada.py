
# BONUS_PERCENTUAL = 0.1
# nome = input("Qual o seu nome: ")
# salario = float(input("Qual o seu salário: "))
# bonificacao = BONUS_PERCENTUAL * salario
# print(f"Senhor {nome}, seu salário é {salario}, então sua bonificação será de {bonificacao}")

# Criando lista c/ N dias
mes_dezembro = [None] * 5

# Obtendo temperaturas dos dias
for dia in range(len(mes_dezembro)):
    mes_dezembro[dia] = int(input(f"Qual a temperatura do dia {dia + 1}: "))

temp_acumulada = 0

# calculando a média do mês
for t in range(len(mes_dezembro)):
    temp_acumulada += mes_dezembro[t]

media_mensal = temp_acumulada / len(mes_dezembro)

# Exibindo dados das temperaturas do mês e a média do mês
for dia in range(len(mes_dezembro)):
    print(f"A temperatura do dia {dia +1} foi {mes_dezembro[dia]} graus")

print(f"A média mensal de temperaturas é: {media_mensal} graus")

