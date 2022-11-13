# Дан целочисленный список, состоящий из 10 элементов. Поменять местами первый максимальный и последний элементы.

list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение

b = len(list_numbers) # Это по условию элементов 10, а в задаче 20
a = list_numbers[0]
c = 0

for i in range(b):
   if a < list_numbers[i]:
      a = list_numbers[i]
      c = i

list_numbers[c], list_numbers[-1] = list_numbers[-1], list_numbers[c]

print(list_numbers)
