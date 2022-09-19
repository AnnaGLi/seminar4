#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input('enter a number: '))
list_1 = []
numm = 2
while number > numm * numm:
    if number % numm == 0:
        list_1.append(numm)
        number //= numm
    else:
        numm += 1
if number > 1:
    list_1.append(number)
print(list_1)
