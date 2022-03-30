per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []

money_str = input('введите сумму: ')
money = int(money_str)

for key in per_cent:
    deposit.append(money * per_cent[key] / 100)

print('Все возможные варианты:', deposit)
print('Максимальная сумма, которую вы можете заработать — ', max(deposit))
