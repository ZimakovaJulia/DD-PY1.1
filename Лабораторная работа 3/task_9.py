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

balance = salary
expenses = spend

for d in range(1, 11):
    balance = round((balance - expenses), 2)
    expenses = round((expenses + expenses * increase), 2)
    balance = balance + salary

need_money = salary - balance

print(round(need_money))
