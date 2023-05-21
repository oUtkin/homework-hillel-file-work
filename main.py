## Завдання 1
## Даний файл із довільним текстом, необхідно знайти всі числа у файлі та записати до списку numbers

# with open('task_1.txt', 'r') as task_1_file:
#     text_with_numbers = task_1_file.read()
#     count_digit = 0
# for i in text_with_numbers:
#     if i.isdigit():
#         count_digit += 1
# print(f'Number of digits in task_1.txt: {count_digit}')
# task_1_file.close()

## Завдання 2
## Запросити у користувача текст та записати його у файл data.txt

# with open('data.txt', 'w') as task_2_file:
#     task_2_file.write(input('Enter your text: '))
# task_2_file.close()

## Завдання 3
## Запросити у користувача число N і запитати N чисел у користувача,
## потім записати їх у файл numbers.txt через пробіл

# N = int(input('Enter N: '))
# numbers = []
# for j in range(1, N + 1):
#     current_number = input(f'Enter {j} number: ')
#     numbers.append(current_number)
#
# with open('numbers.txt', 'w') as task_3_file:
#     task_3_file.write(' '.join(numbers))
# task_3_file.close()

## Завдання 4
## Згенерувати 100 рандомних чисел та записати їх у файл random_numbers.txt, де один рядок = одне число

# import random
#
# random_numbers = [str(random.randint(0, 100)) for x in range(100)]
# print(random_numbers)
#
# with open('random_numbers.txt', 'w') as task_3_file:
#     task_3_file.write('\n'.join(random_numbers))

## Завдання 5
## Даний файл із довільним текстом, потрібно знайти кількість слів у файлі та вивести користувачеві

# with open('task_5.txt', 'r') as task_5_file:
#     task_5_text = task_5_file.read()
#
# count_words = len(task_5_text.split())
# if count_words == 1:
#     print(f'There is {count_words} word in task_5.txt')
# else: print(f'There are {count_words} words in task_5.txt')

## Завдання 6
## Даний файл, у якому записані числа через пробіл, необхідно вивести користувачу суму цих чисел

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