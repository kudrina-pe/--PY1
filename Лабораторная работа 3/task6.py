list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

i = 0
element_max = list_numbers[i]
element_last = list_numbers[-1]

for pos, number in enumerate(list_numbers):
    if number == max(list_numbers):
        element_max = number
        i = pos

element_last, element_max  = element_max, element_last

print(list_numbers)
