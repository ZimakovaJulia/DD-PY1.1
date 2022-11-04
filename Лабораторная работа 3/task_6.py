# Дан целочисленный список, состоящий из 10 элементов. Поменять местами первый максимальный и последний элементы.

list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение

max_num = list_numbers[0]
index_max = 0

for i in range(len(list_numbers)):
   if max_num < list_numbers[i]:
      max_num = list_numbers[i]
      index_max = i

list_numbers[index_max], list_numbers[-1] = list_numbers[-1], list_numbers[index_max]

print(list_numbers)
