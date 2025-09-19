numbers = [12, -5,23,0,4,17,-8,0,11]
print("Количество элементов:", len(numbers))
print("Последний элемент:",numbers[-1])
reverse_list = numbers[::-1]
print("Обратный порядок:",reverse_list )

if 5 in numbers and 17 in numbers:
    print("yes")
else:
    print("no")