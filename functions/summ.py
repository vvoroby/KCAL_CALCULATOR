"""
Функция для подсчета калорий съеденных сегодня
"""
def summ():
    connect = sqlite3.connect('archive.db') ## делаем запрос к базе данных
    cursor = connect.cursor()
    # выбираем нужные нам продукты по дате и передаём в переменную
    cursor.execute('''SELECT kkal FROM archive WHERE date = ?''', [find_today()])
    items=cursor.fetchall()
    #суммируем калории
    summa=0
    for item in items:
        summa += item[0]
    connect.close()
    return summa
