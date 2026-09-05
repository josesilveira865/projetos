# ===== ENTRADA =====
nome = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potencia do aparelho em watts (W): "))
horas_dia = float(input("Digite o tempo medio de uso diario em horas: "))

# ===== PROCESSAMENTO =====
consumo_mensal = (potencia * horas_dia * 30) / 1000
valor_kwh = 0.75
custo_estimado = consumo_mensal * valor_kwh

# ===== SAÍDA =====
print("Aparelho:", nome)
print("Potencia:", potencia, "W")
print("Uso diario:", horas_dia, "horas")
print("Consumo mensal:", format(consumo_mensal, ".2f"), "kWh")
print("Custo estimado: R$", format(custo_estimado, ".2f"))
