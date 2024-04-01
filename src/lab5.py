# В продаже присутствуют йогурты разных производителей
# У кассира стоит задача посчитать общую сумму стоимости йогуртов всех производителей.

yogurts_names = [('Эрмигурт', 100), 
                 ('Чудо', 50), 
                 ('Данон', 75)]
yogurts_prices = {'Эрмигурт': 127, 
                 'Чудо': 79, 
                 'Данон': 98}

total_cost = 0

for ytype, counts in yogurts_names:
    price = yogurts_prices[ytype]
    total_cost += counts * price

print(f"Общая стоимость всех йогуртов: {total_cost} рублей.")