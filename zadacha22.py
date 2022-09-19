#Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

numbers = [1, 2, 1, 3, 6, 1]
list_unique_numbers = []
def sort_unique(numbers):
    unique_numbers = set(numbers)
    for number in unique_numbers:
        list_unique_numbers.append(number)
    return list_unique_numbers
print(sort_unique(numbers))
