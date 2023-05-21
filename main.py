# Завдання 1
# Даний файл із довільним текстом, необхідно знайти всі числа у файлі та записати до списку numbers

task_1_file = open('task_1.txt', 'r')
task_1_file.read()
print(task_1_file)
count_digit = 0
for char in task_1_file:
    if char.isdigit():
        count_digit += 1
print(count_digit)
task_1_file.close()

# Завдання 2
# Запросити у користувача текст та записати його у файл data.txt
#
# Завдання 3
# Запросити у користувача число N і запитати N чисел у користувача,
# потім записати їх у файл numbers.txt через пробіл
#
# Завдання 4
# Згенерувати 100 рандомних чисел та записати їх у файл random_numbers.txt, де один рядок = одне число
#
# Завдання 5
# Даний файл із довільним текстом, потрібно знайти кількість слів у файлі та вивести користувачеві
#
# Завдання 6
# Даний файл, у якому записані числа через пробіл, необхідно вивести користувачу суму цих чисел
#
# Завдання 7
# Даний файл у якому записаний текст, необхідно вивести топ 5 рядків,
# які найчастіше повторюються, приклад:
# 'в' - 20 разів
# 'привіт' - 10 разів
# 'як' - 9 разів
# 'у' - 7
# 'world' - 4
# Краще за все використовувати тип даних Counter з модуля collections. Приклад:
# Counter(words).most_common(5)