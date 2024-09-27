import json

with open('faturamento.json', 'r') as file:
    faturamento_diario = json.load(file)

faturamento_valido = [valor for valor in faturamento_diario if valor > 0]

menor_faturamento = min(faturamento_valido)

maior_faturamento = max(faturamento_valido)

media_mensal = sum(faturamento_valido) / len(faturamento_valido)

dias_acima_media = sum(1 for valor in faturamento_valido if valor > media_mensal)

print(f"Menor faturamento diário: R$ {menor_faturamento:.2f}")
print(f"Maior faturamento diário: R$ {maior_faturamento:.2f}")
print(f"Número de dias acima da média mensal: {dias_acima_media}")
