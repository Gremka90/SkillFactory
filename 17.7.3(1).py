deposit = []
money = int(input('Введите планируему сумму: '))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

data_item = per_cent.items()
for key, value in data_item:
    deposit.append(value * money)

print(deposit)
print("Максимальная сумма вклада за год:", max(deposit))