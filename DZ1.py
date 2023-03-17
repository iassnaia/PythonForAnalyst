## Условие 1

Оформляйте ноутбук, используя эти советы:
Номер задачи - заголовок 2
Номер подзадачи - заголовок 3
Предоставленные наборы данных оформляйте, как код
Рекомендации для преподавателей по оценке задания:
Смотреть, чтобы студент красиво оформлял ноутбук, использовал ячейки с текстом, указывал номера заданий

## Условие 2

На складе лежат разные фрукты в разном количестве. Нужно написать функцию, которая на вход принимает любое количество 
названий фруктов и их количество, а возвращает общее количество фруктов на складе
def returns_the_total(**kwargs):
    return sum(kwargs.values())
        
print(returns_the_total(kiwi=8, mango=15, garnet=10))
def returns_the_total(**kwargs):
    return sum(kwargs.values())
        
print(returns_the_total(kiwi=8, mango=15, garnet=10))
33

##Условие 3:
Дан список с затратами на рекламу. Но в данных есть ошибки, некоторые затраты имеют отрицательную величину. 
Удалите такие значения из списка и посчитайте суммарные затраты
[100, 125, -90, 345, 655, -1, 0, 200]
Используйте list comprehensions

##Условие 3:
Дан список с затратами на рекламу. Но в данных есть ошибки, некоторые затраты имеют отрицательную величину. 
Удалите такие значения из списка и посчитайте суммарные затраты
[100, 125, -90, 345, 655, -1, 0, 200]
Используйте list comprehensions
orig_expenses = [100, 125, -90, 345, 655, -1, 0, 200]
expenses = [ i if i > 0 else 0 for i in orig_expenses]
sum(expenses)
orig_expenses = [100, 125, -90, 345, 655, -1, 0, 200]
expenses = [ i if i > 0 else 0 for i in orig_expenses]
sum(expenses)
1425

##Условие 4:
Даны два списка.
Дата покупки
['2021-09-14', '2021-12-15', '2021-09-08', '2021-12-05', '2021-10-09', '2021-09-30', '2021-12-22', '2021-11-29', '2021-12-24', '2021-11-26', '2021-10-27', '2021-12-18', '2021-11-09', '2021-11-23', '2021-09-27', '2021-10-02', '2021-12-27', '2021-09-20', '2021-12-13', '2021-11-01', '2021-11-09', '2021-12-06', '2021-12-08', '2021-10-09', '2021-10-31', '2021-09-30', '2021-11-09', '2021-12-13', '2021-10-26', '2021-12-09']
Суммы покупок по датам
[1270, 8413, 9028, 3703, 5739, 4095, 295, 4944, 5723, 3701, 4471, 651, 7037, 4274, 6275, 4988, 6930, 2971, 6592, 2004, 2822, 519, 3406, 2732, 5015, 2008, 316, 6333, 5700, 2887]

###4.1 Найдите, какая выручка у компании в ноябре
Используйте list comprehensions
date_of_purchase = ['2021-09-14', '2021-12-15', '2021-09-08', '2021-12-05', '2021-10-09', 
'2021-09-30', '2021-12-22', '2021-11-29', '2021-12-24', '2021-11-26', '2021-10-27', 
'2021-12-18', '2021-11-09', '2021-11-23','2021-09-27', '2021-10-02', '2021-12-27', '2021-09-20',
'2021-12-13', '2021-11-01', '2021-11-09','2021-12-06', '2021-12-08', '2021-10-09', 
'2021-10-31', '2021-09-30', '2021-11-09', '2021-12-13','2021-10-26', '2021-12-09']

price_of_purchase = [1270, 8413, 9028, 3703, 5739, 4095, 295, 4944, 5723, 3701, 4471, 651, 
7037, 4274, 6275, 4988, 6930, 2971, 6592, 2004, 2822, 519, 3406, 2732, 5015, 2008, 316, 
6333, 5700, 2887] 

def from_list_to_dict(a: list, b: list) ->dict:
    return {a[i] : b[i] for i in range(len(a))}
    # return dict(zip(a, b))

print(from_list_to_dict(date_of_purchase, price_of_purchase))

result = sum([p for d, p in zip(date_of_purchase, price_of_purchase) if d[5:7] == "11"])
print(f'Выручка за ноябрь: {result}')
{'2021-09-14': 1270, '2021-12-15': 8413, '2021-09-08': 9028, '2021-12-05': 3703, '2021-10-09': 2732, '2021-09-30': 2008, '2021-12-22': 295, '2021-11-29': 4944, '2021-12-24': 5723, '2021-11-26': 3701, '2021-10-27': 4471, '2021-12-18': 651, '2021-11-09': 316, '2021-11-23': 4274, '2021-09-27': 6275, '2021-10-02': 4988, '2021-12-27': 6930, '2021-09-20': 2971, '2021-12-13': 6333, '2021-11-01': 2004, '2021-12-06': 519, '2021-12-08': 3406, '2021-10-31': 5015, '2021-10-26': 5700, '2021-12-09': 2887}
Выручка за ноябрь: 25098

###4.2 Найдите выручку компании в зависимости от месяца
Для этого напишите функцию, которая на вход принимает список с датами и список с выручкой, а на выходе словарь, где ключи - это месяцы, а значения - это выручка.
Используйте аннотирование типов.



import pandas as pd

df = pd.DataFrame(price_of_purchase, index=pd.to_datetime(date_of_purchase))
print(df.resample('M').sum())
                0
2021-09-30  25647
2021-10-31  28645
2021-11-30  25098
2021-12-31  45452
