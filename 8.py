text = input("Введите текст:")
result = ""

for char in text:
        if char.isalpha():
            if char.isupper():
                shifted = chr((ord(char) - ord('A') + 3) % 26 + ord('A'))
            else:
                shifted = chr((ord(char) - ord('a') + 3) % 26 + ord('a'))
            result += shifted
        else:
            result += char
print("Результат:", result)

