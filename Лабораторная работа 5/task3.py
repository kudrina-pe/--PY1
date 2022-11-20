from random import randint


def get_unique_list_numbers(start, stop, count) -> list[int]:
    list_unique_numbers = []
    while len(list_unique_numbers) < count:
        i = randint(start, stop)
        if i not in list_unique_numbers:
            list_unique_numbers.append(i)
    return list_unique_numbers

list_unique_numbers = get_unique_list_numbers(-10, 10, 15)

print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
