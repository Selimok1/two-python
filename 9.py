import random
original_list = [random.randint(-10,10)
for _ in range(15)]
print("Исходный список:", original_list)
positive_list = [x for x in original_list if x>0]
print("Позитивные числа:", positive_list)
squares_list = [x**2 for x in original_list]
print("Кваратные числа:",squares_list)
