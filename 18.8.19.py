a = int(input('Введите кол-во билетов: '))
Summ = 0

for i in range(a):
    tiket = int(input('Введите восраст посетителя:'))
    if tiket < 18:
        pass
    elif 18 <= tiket < 25:
        Summ = Summ + 990
    elif tiket > 25:
        Summ = Summ + 1390

if a > 3:
    discount = Summ * 0.1
    Summ = Summ - discount

print(f'Общая стоимость составляет {Summ} ')