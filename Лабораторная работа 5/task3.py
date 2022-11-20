from random import randint


def get_unique_list_numbers() -> list[int]:
    list_unique_numbers = []
    while len(list_unique_numbers) < 15:
        i = randint(-10, 10)
        if i not in list_unique_numbers:
            list_unique_numbers.append(i)
    return list_unique_numbers

list_unique_numbers = get_unique_list_numbers()

print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
