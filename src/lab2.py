import csv

def record_expenses(expenses):
    date = input('Введите дату: ')
    category = input('Введите категорию: ')
    amount = float(input('Введите сумму: '))
    expenses.append({'date': date, 'category': category, 'amount': amount})
    with open('src/expenses.csv', 'a', newline='') as file:
        fieldnames = ['date', 'category', 'amount']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(expenses[-1])

def view_expenses():
    with open('src/expenses.csv', 'r', newline='') as file:
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