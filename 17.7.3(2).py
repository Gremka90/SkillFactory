money = int(input('Введите планируему сумму: '))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

deposit = per_cent.copy()
for key, value in deposit.items():
    deposit[key] = int(value * money)

print(deposit)
print("Максимальная сумма вклада за год:", max(deposit.values()))