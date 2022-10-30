def get_count_char(str_):
    list_letters = "".join(str_.lower().split())
    dict_ = {}
    for symbol in list_letters:
        if symbol.isalpha():  # если символ является буквой
            if symbol not in dict_:  # если символа нет в словаре
                dict_[symbol] = 1  # частота символа равна 1
            else:
                dict_[symbol] += 1  # увеличить значение частоты символа на 1
    return dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))


def get_percent_char(str_):
    dict_ = get_count_char(str_)  # принять словарь
    sum_ = sum(dict.values(dict_))  # найти сумму всех значений в словаре
    dict_percent = {}  # создать новый словарь
    for symbol in dict_:
        dict_percent[symbol] = round(dict_[symbol] / sum_ * 100, 2)
    return dict_percent


print(get_percent_char(main_str))
