import copy
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

def get_count_char(str_):
    b = ''
    for i in str_.lower():
        if i.isalpha():
            b = ''.join([b, i])  # строка только из букв
    from collections import Counter
    m = Counter(b)
    return m

result_dict = get_count_char(main_str)
print(result_dict)

def percentage_dictionary(dict_):
    number_letters = 0
    for i in dict_.values():
        number_letters = number_letters + i
    n = {}
    for x, y in dict_.items():
        n[x] = round(y * 100 / number_letters, 1)  # 1 знак на 257 символов приблизительно 0.4
    return n

print(percentage_dictionary(result_dict))
