odd_numbers = []
number = int(input('Введите число: '))


for i in range(1, number):
    if 0 != (i % 2):
        odd_numbers.append(i)

print(odd_numbers)
