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
    n = {}
    for x, y in m.items():
        n[x] = round(y * 100 / len(b), 1)  # 1 знак на 257 символов приблизительно 0.4
    return print(m, n, sep="\n")
print(get_count_char(main_str))
