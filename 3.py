a = int(input("Первое число: "))
b = int(input("Второе число: "))
c = int(input("Третье число: "))
min_num = a
if b < min_num:
    min_num = b
if c < min_num:
    min_num = c
print("Самое маленькое число:", min_num)