ticketsCount = input('введите количество билетов: ')
ticketsCountInt = int(ticketsCount)

price = 0

for i in range(ticketsCountInt):
    age = int(input('введите возраст '+str(i+1)+': '))
    if age < 18:
        print('-> для этого посетителя вход бесплатный')
    elif 18 <= age < 25:
        price += 990
        print('-> для этого посетителя билет со скидкой и стоит 990руб.')
    else:
        price += 1390
        print('-> для этого посетителя билет стоит 1390руб.')

if ticketsCountInt > 3:
    price = price * 0.9
    print('-> скидка 10% от трёх человек')

print('Сумма к оплате '+str(price))
