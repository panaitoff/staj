"""
1. Подключение к API и получение данных
Напишите скрипт на Python, который подключается к API и получает данные.
Например, используйте публичное API https://jsonplaceholder.typicode.com/posts.
Сохраните полученные данные в формате JSON в файл.
"""
import requests
import json

data = requests.get('https://jsonplaceholder.typicode.com/posts').json()

with open('data.json', 'w') as f:
    json.dump(data, f)


"""
2. Обработка данных с использованием SQL
Представьте, что у вас есть таблица users в базе данных SQLite с полями id, name, и age. 
Напишите Python-скрипт, который подключается к этой базе данных, выбирает всех пользователей 
старше 30 лет и выводит их имена и возраст.
"""
import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

a = cursor.execute("SELECT * FROM users WHERE age > 30").fetchall()

for i in a:
    print(' '.join(list(map(str, i[1:]))) )

connection.commit()
connection.close()

"""
3. Объединение данных из разных источников
Напишите скрипт на Python, который объединяет данные из двух источников. 
Первый источник - это CSV-файл с информацией о продуктах (поля: product_id, product_name). 
Второй источник - это JSON-файл с данными о продажах (поля: sale_id, product_id, amount). 
Скрипт должен объединить данные по product_id и вывести итоговую таблицу с информацией о 
продажах для каждого продукта.
"""
import csv
import json


csv_file_path = 'products.csv'
json_file_path = 'sales.json'


products = {}
with open(csv_file_path, mode='r', newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        product_id = int(row['product_id'])
        product_name = row['product_name']
        products[product_id] = {
            'product_name': product_name,
            'total_sales': 0
        }


with open(json_file_path, 'r') as jsonfile:
    sales_data = json.load(jsonfile)
    for sale in sales_data:
        product_id = sale['product_id']
        amount = sale['amount']
        if product_id in products:
            products[product_id]['total_sales'] += amount


print("Product ID | Product Name | Total Sales")
print("----------------------------------------")
for product_id, product_info in products.items():
    print(f"{product_id:<10} | {product_info['product_name']:<12} | {product_info['total_sales']}")


"""
4. Оптимизация скрипта
Дан следующий скрипт на Python для обработки списка чисел. Оптимизируйте его для повышения производительности.
"""
squares = list(map(lambda x: x ** 2, range(1, 1000001)))
