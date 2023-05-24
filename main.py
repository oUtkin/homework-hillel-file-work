# # Завдання 1
# # Даний файл із довільним текстом, необхідно знайти всі числа у файлі та записати до списку numbers

with open('task_1.txt', 'r') as task_1_file:
    text_with_numbers = task_1_file.read().split()
    numbers = [i for i in text_with_numbers if i.isdigit()]
print(f'All numbers from task_1.txt are in a list: {numbers}')

# # Завдання 2
# # Запросити у користувача текст та записати його у файл data.txt
#
# with open('data.txt', 'w') as task_2_file:
#     task_2_text = input('Enter your text: ')
#     task_2_file.write(task_2_text)
#
# # Завдання 3
# # Запросити у користувача число N і запитати N чисел у користувача,
# # потім записати їх у файл numbers.txt через пробіл
#
# while True:
#     N = input('Enter N: ')
#     try:
#         N = int(N)
#         break
#     except ValueError:
#         print(f'{N} is not a number, try again')
#
# task_3_numbers = []
# for j in range(1, N + 1):
#     while True:
#         current_number = input(f'Enter {j} number: ')
#         try:
#             current_number = int(current_number)
#             task_3_numbers.append(current_number)
#             break
#         except ValueError:
#             print(f'{current_number} is not a number, try again')
#
# with open('numbers.txt', 'w') as task_3_file:
#     number_str = ' '.join(str(x) for x in task_3_numbers)
#     task_3_file.write(number_str)
#
# # Завдання 4
# # Згенерувати 100 рандомних чисел та записати їх у файл random_numbers.txt, де один рядок = одне число
#
# import random
#
# random_numbers = [str(random.randint(0, 100)) for x in range(100)]
#
# with open('random_numbers.txt', 'w',) as task_3_file:
#     task_3_file.write('\n'.join(random_numbers))
#
# # Завдання 5
# # Даний файл із довільним текстом, потрібно знайти кількість слів у файлі та вивести користувачеві
#
# with open('task_5.txt', 'r') as task_5_file:
#     task_5_text = task_5_file.read()
#
# count_words = len(task_5_text.split())
# if count_words == 1:
#     print(f'There is {count_words} word in task_5.txt')
# else: print(f'There are {count_words} words in task_5.txt')
#
# # Завдання 6
# # Даний файл, у якому записані числа через пробіл, необхідно вивести користувачу суму цих чисел
#
# with open('task_6.txt', 'r') as task_6_file:
#     task_6_numbers = task_6_file.read().split()
#
# number_sum = 0
# for k in task_6_numbers:
#     try:
#         number_sum += int(k)
#     except ValueError:
#         print(f'"{k}" was ignored')
#
# print(f'Sum of numbers in task_6_file.txt: {number_sum}')
#
# # Завдання 7
# # Даний файл у якому записаний текст, необхідно вивести топ 5 рядків,
# # які найчастіше повторюються, приклад:
# # 'в' - 20 разів
# # 'привіт' - 10 разів
# # 'як' - 9 разів
# # 'у' - 7
# # 'world' - 4
# # Краще за все використовувати тип даних Counter з модуля collections. Приклад:
# # Counter(words).most_common(5)
#
# from collections import Counter
#
# num_words = 5
# words_list = []
# current_word = ""
#
# with open('task_7.txt', 'r') as task_7_file:
#     words = task_7_file.read()
#
# for char in words:
#     if char.isalpha():
#         current_word += char.lower()
#     elif current_word:
#         words_list.append(current_word)
#         current_word = ""
# if current_word:
#     words_list.append(current_word)
#
# top_words = Counter(words_list).most_common(num_words)
# for word, count in top_words:
#     print(f'{word} - reapeted {count} times')
