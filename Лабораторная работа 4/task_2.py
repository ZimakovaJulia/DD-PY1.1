import copy
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

def get_count_char(str_):
    a = str_.lower()  # перевели строку в нижний регистр
    b = ''
    for i in a:
        if i.isalpha():
            b = ''.join([b, i])  # строка только из букв
    from collections import Counter
    c = Counter(b)  # подсчет большого количества букв, поскольку счетчик вычисляет все значения за один раз, правда я не поняла как избавиться от Counter при выводе
    # + на этом моменте я потеряла смысл в то ответе, что предоставлен для проверки. Там нет ни сортировки, ни процентного отношения
    d = len(b)  # кол-во элементов в строке из букв
    m = copy.deepcopy(c)  # мне для контроля удобней иметь библиотеку без ссылок
    n = {}
#    print(a, b, c, d, m, sep="\n")
    for x, y in m.items():
        n[x] = round(y / d, 3)  # 1 знак на 257 символов приблизительно 0.004
    return n
print(get_count_char(main_str))
