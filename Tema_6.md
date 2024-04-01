# Тема 6. Базовые коллекции: словари, кортежи
Отчет по Теме №6 выполнил:
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

```python
numbers = input('Введите числа через пробел: ')
lst = numbers.split()
tpl = tuple(lst)
print(lst, tpl, sep='\n')
```
![image](https://github.com/WoodyDoodle/software_engineering/assets/123651515/d3eb5680-2fef-49ac-b006-d7621920eff4)

  
## Самостоятельная работа №2

```python
tuples = ['(1, 2, 3), 1)', 
          '(1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3)', 
          '(2, 4, 6, 6, 4, 2), 9)']

def remove_element(tpl, el):
    lst = list(tpl)
    if el in lst:
        lst.remove(el)
        return tuple(lst)
    else:
        return tpl


for tple in tuples:
    tpl = tuple(map(int, tple[:-4].strip('()').split(',')))
    element = int(tpl[-2:-1][0])
    new_tuple = remove_element(tpl, element)
    print(new_tuple)
```
![image](https://github.com/WoodyDoodle/software_engineering/assets/123651515/38b507f4-f6be-47c5-8983-749a168ac000)


## Самостоятельная работа №3

```python
nums = input('Нажмите ладонью на numpad один раз\n')


def count_numbers(string):
    num_freq = {}

    for i in string:
        i = int(i)
        num_freq[i] = num_freq.get(i, 0) + 1

    sorted_num_freq = sorted(num_freq.items(), key=lambda item: item[1])
    top_three = dict(sorted(sorted_num_freq[-3:]))
    return top_three


print(count_numbers(nums))
```
![image](https://github.com/WoodyDoodle/software_engineering/assets/123651515/986c09bd-34a4-4a17-929d-7132ea73f2ac)

 
## Самостоятельная работа №4
  
```python
tuples = ['(1, 2, 3), 8)', 
          '(1, 8, 3, 4, 8, 8, 9, 2), 8)', 
          '(1, 2, 8, 5, 1, 2, 9), 8)']

def find_element(tple, element):
    if tple.count(element) > 0:
        start_index = tple.index(element)
        end_index = tple.index(element, start_index + 1) if tple.count(element) > 1 else ()
        return tple[start_index:end_index + 1] if end_index != () else tple[start_index:]
    else:
        return ()

for tpl in tuples:
    tple = tuple(map(int, tpl[1:-4].strip('()').split(',')))
    element = int(tpl[-2])
    new_tuple = find_element(tple, element)
    print(new_tuple)
```
![image](https://github.com/WoodyDoodle/software_engineering/assets/123651515/3305f761-db0c-4001-87a3-7d0476d4a4c8)


  
## Самостоятельная работа №5
  
```python
# В продаже присутствуют йогурты разных производителей
# У кассира стоит задача посчитать общую сумму стоимости йогуртов всех производителей.

yogurts_names = [('Эрмигурт', 100), 
                 ('Чудо', 50), 
                 ('Данон', 75)]
yogurts_prices = {'Эрмигурт': 127, 
                 'Чудо': 79, 
                 'Данон': 98}

total_cost = 0

for ytype, counts in yogurts_names:
    price = yogurts_prices[ytype]
    total_cost += counts * price

print(f"Общая стоимость всех йогуртов: {total_cost} рублей.")
```
![image](https://github.com/WoodyDoodle/software_engineering/assets/123651515/0d909021-b639-4fe7-8557-e2173cbf4e0c)
