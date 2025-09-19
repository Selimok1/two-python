start = int(input("Начало диапозона:"))
end = int(input("Конец диапозона:"))
found = False
for i in range(start, end + 1):
    if i % 2 == 0:
        print(i, end=" ")
        found = True
if not found:
    print("В этом диапазоне нет чётных чисел")