# Тема 7. Работа с файлами (ввод, вывод)
Отчет по Теме №7 выполнил:
- Крутиков Дмитрий Геннадьевич
- ИНО ЗБ ПОАС-22-2

| Задание | Сам_раб |
| ------ | ------ |
| Задание 1 | + |
| Задание 2 | + |
| Задание 3 | + |
| Задание 4 | + |
| Задание 5 | + |

## Самостоятельная работа №1
### Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.

Файл ['statya.txt'](https://github.com/WoodyDoodle/software_engineering/blob/Tema_7/src/statya.txt)

```python
import re

file = open('src/statya.txt', 'r', encoding='utf-8')
words = file.read().split()
stopwords = ['в', 'на', 'и', 'с', 'к', 'а']
print(f'Длина статьи: {len(words)} слов.')


def clean_text(words, stopwords):
    words = [re.sub(r'[,()."—:«»]', '', i) for i in words if i not in stopwords and len(i) > 1]
    return words


def find_most_frequent(words):
    words = clean_text(words, stopwords)
    num_freq = {}
    for word in words:
        num_freq[word] = num_freq.get(word, 0) + 1
    sorted_num_freq = sorted(num_freq.items(), key=lambda item: item[1])
    top = sorted_num_freq[-1]
    return top


res = find_most_frequent(words)
print(f'Самое встречающееся слово: "{res[0]}". Встречается {res[1]} раз.')

file.close()
```

### Содержимое текстового файла:
![image](https://github.com/WoodyDoodle/software_engineering/assets/123651515/64266a50-ea1a-4193-8ca4-989869056119)

### Результат выполнения программы:
![image](https://github.com/WoodyDoodle/software_engineering/assets/123651515/313c6dbf-5d46-42b7-9e2a-f059052a1fb6)

  
## Самостоятельная работа №2
### У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.
Файл [expenses.csv](https://github.com/WoodyDoodle/software_engineering/blob/Tema_7/src/expenses.csv)
```python
import csv

def record_expenses(expenses):
    date = input('Введите дату: ')
    category = input('Введите категорию: ')
    amount = float(input('Введите сумму: '))
    expenses.append({'date': date, 'category': category, 'amount': amount})
    with open('expenses.csv', 'a', newline='') as file:
        fieldnames = ['date', 'category', 'amount']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(expenses[-1])

def view_expenses():
    with open('expenses.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"{row['date']}, {row['category']}, {row['amount']}")

expenses = []

while True:
    print('1. Добавить запись')
    print('2. Просмотреть записи')
    choice = int(input('Введите номер действия: '))

    if choice == 1:
        record_expenses(expenses)
    elif choice == 2:
        view_expenses()
        break
```
![image](https://github.com/WoodyDoodle/software_engineering/assets/123651515/980d814e-01d9-47be-99ff-a8bca9236d0e)
![image](https://github.com/WoodyDoodle/software_engineering/assets/123651515/e5738d0b-775e-4a5c-bec9-c7ae64a4f623)


## Самостоятельная работа №3
### Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк.

Файл ['input.txt'](https://github.com/WoodyDoodle/software_engineering/blob/Tema_7/src/input.txt)

```python
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
```
![image](https://github.com/WoodyDoodle/software_engineering/assets/123651515/3ef0189a-4534-40a7-8c22-b0a2d47f5245)

  
## Самостоятельная работа №4
### Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****.

Файл ['input2.txt'](https://github.com/WoodyDoodle/software_engineering/blob/Tema_7/src/input2.txt)

```python
import re

file = open('src/input2.txt', 'r', encoding='utf-8')
stopwords = file.read().split()
string = '''Hello, world! Python IS the programming language of thE future. My EMAIL is....
PYTHON is awesome!!!!'''


def censor_text(string, stopwords):
    for stopword in stopwords:
        string = re.sub(stopword, lambda x: '*' * len(x.group()), string, flags=re.IGNORECASE)
    return string


res = censor_text(string, stopwords)
print(res)

file.close()
```

![image](https://github.com/WoodyDoodle/software_engineering/assets/123651515/68ead621-7fa5-44a5-a716-701306f06788)

  
## Самостоятельная работа №5
### Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.
#### Создать текстовый файл “abc.txt” и записать в него все буквы русского алфавита, каждое на новой строке. Затем прочитать этот файл и вывести на экран кол-во букв.
  
```python
let = ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о",
       "п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]

with open("src/abc.txt", "w") as f:
    print("Создан файл data.txt")
    for i in let:
        f.write(i + "\n")

with open("src/abc.txt", "r") as f:
    total = len(f.readlines())

print("Сумма чисел в файле:", total)
```
![image](https://github.com/WoodyDoodle/software_engineering/assets/123651515/b80551c6-7f5e-4ac0-a06b-756444d625dd)
