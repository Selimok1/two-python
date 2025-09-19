student = {
    "name": "Иван",
    "age": 20,
    "course": 2,
    "grades": [4, 5, 3, 5, 4]
}
print("Имя:", student["name"])
print("Курс:", student["course"])
average_grade = sum(student["grades"]) / len(student["grades"])
print("Средний бал:", round(average_grade, 2))

student["grades"].append(5)
print("Обновлённый словарь:")
print(student)