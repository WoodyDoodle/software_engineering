num = int(input('Введите число от 0 до 10: '))
if 0 <= num <= 3:
    print('Число в дипазоне между 0 и 3 включительно.')
elif 3 < num < 6:
    print('Число в дипазоне между 3 и 6.')
elif 6 <= num <= 10:
    print('Число в дипазоне между 6 и 10 включительно.')
else:
    print('Ошибка. Число не принадлежит диапазону от 0 до 10.')