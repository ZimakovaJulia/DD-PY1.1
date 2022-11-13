import random

def get_unique_list_numbers() -> list[int]:
    from_and_to = []
    for i in range(-10,11):
        from_and_to.append(i)
    list_num = random.sample(from_and_to,15)  # Метод sample() возвращает список уникальных элементов
    return list_num

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
