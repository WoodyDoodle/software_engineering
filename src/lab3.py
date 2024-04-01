import re

file = open('src/input.txt', 'r', encoding='utf-8')

number_of_words = 0
number_of_lines = 0
number_of_characters = 0

for string in file:
    number_of_words += len(string.split())
    number_of_lines += 1
    for letter in string:
        number_of_characters += 1 if re.match(r'[a-zA-Z]+', letter) else 0

print('Файл содержит:', 
      f'{number_of_characters} букв', 
      f'{number_of_words} слов', 
      f'{number_of_lines} строк',
      sep='\n')

file.close()