# Ежемесячная зарплата составляет salary руб., а расходы на проживание превышают ее и составляют spend руб. в месяц.
# Рост цен ежемесячно увеличивает расходы на 3%. (Цены начинают повышаться со второго месяца).
# Определить, какую нужно иметь сумму денег, чтобы прожить 10 месяцев, используя только эти деньги и зарплату.
# Ответ округлить до целого числа.

salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение

a = salary
b = spend

for d in range(1, 11):
    a = round((a - b), 2)
    b = round((b + b * increase), 2)
#    print('Конец месяца: ', d)
#    print('Минус в конце месяца: ', a)
#    print('Расходы в следующем месяце составят: ', b)
    a = a + salary

need_money = a * (-1) + salary

print(round(need_money))
