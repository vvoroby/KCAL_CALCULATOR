import matplotlib.figure
import matplotlib.patches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Окно при нажатии на кнопку завтрак
def breafest():
    window = Tk()
    window.title("Завтрак")
    window.geometry('350x620')
    window['bg'] = 'Linen'

    title = Label(window, text="Завтрак", bg="Linen", fg="SandyBrown", font=70, width=30)
    title.pack()

    main_frame = Frame(window)
    main_frame.pack()

    # бегунок
    frame_scroll = Scrollbar(main_frame)
    frame_scroll.pack(side=RIGHT, fill=Y)

    frame_scroll = Scrollbar(main_frame, orient='horizontal')
    frame_scroll.pack(side=BOTTOM, fill=X)

    my_frame = ttk.Treeview(main_frame, yscrollcommand=frame_scroll.set, xscrollcommand=frame_scroll.set)
    my_frame.pack()

    frame_scroll.config(command=my_frame.yview)
    frame_scroll.config(command=my_frame.xview)

    # определение колонок
    my_frame['columns'] = (
    'player_№', 'player_product', 'player_mass', 'player_kkal', 'player_b', 'player_j', 'player_y')

    # формат колонок
    my_frame.column("#0", width=0, stretch=NO)
    my_frame.column("player_№", anchor=CENTER, width=30)
    my_frame.column("player_product", anchor=CENTER, width=150)
    my_frame.column("player_mass", anchor=CENTER, width=80)
    my_frame.column("player_kkal", anchor=CENTER, width=80)
    my_frame.column("player_b", anchor=CENTER, width=80)
    my_frame.column("player_j", anchor=CENTER, width=80)
    my_frame.column("player_y", anchor=CENTER, width=80)

    # заголовки колонок
    my_frame.heading("#0", text="", anchor=CENTER)
    my_frame.heading("player_№", text="№", anchor=CENTER)
    my_frame.heading("player_product", text="Продукт", anchor=CENTER)
    my_frame.heading("player_mass", text="Масса", anchor=CENTER)
    my_frame.heading("player_kkal", text="Ккал", anchor=CENTER)
    my_frame.heading("player_b", text="Белки", anchor=CENTER)
    my_frame.heading("player_j", text="Жиры", anchor=CENTER)
    my_frame.heading("player_y", text="Углеводы", anchor=CENTER)

    # добавление данных (визуальный пример)
    my_frame.insert(parent='', index='end', text='',
                   values=('1', 'Молоко', '100', '43', '2,8', '1', '4,6'))
    my_frame.insert(parent='', index='end', text='',
                   values=('2', 'Хлеб', '100', '156', '3,5', '6,7', '6,2'))
    my_frame.pack()

    # таблица для добавления данных
    frame = Frame(window)
    frame.pack(pady=50)

    # заголовки
    new_product = Label(frame, text="Продукт")
    new_product.grid(row=0, column=0)

    new_mass = Label(frame, text="Масса")
    new_mass.grid(row=0, column=1)

    # окна для ввода данных
    new_product_entry = Entry(frame)
    new_product_entry.grid(row=1, column=0)

    new_mass_entry = Entry(frame)
    new_mass_entry.grid(row=1, column=1)

    # Блок функций

    # выбрать запись
    def select_record():
        # очистить поля ввода
        new_product_entry.delete(0, END)
        new_mass_entry.delete(0, END)

        # захватить запись
        selected = my_frame.focus()
        # захват значений записи
        values = my_frame.item(selected, 'values')
        # temp_label.config(text=selected)

        # вывод в поля ввода
        new_product_entry.insert(0, values[0])
        new_mass_entry.insert(0, values[1])

    # сохранить запись
    def update_record():
        selected = my_frame.focus()
        # сохранить новые данные
        my_frame.item(selected, text="", values=(new_product_entry.get(), new_mass_entry.get()))

        # очистить поле ввода
        new_product_entry.delete(0, END)
        new_mass_entry.delete(0, END)

    # def delete_record():

    # def add_record():

    # Кнопки
    select_button = Button(window, text="Выбрать"  ##command=select_record)
                           )
    select_button.pack(pady=5)

    refresh_button = Button(window, text="Заменить"  ##command=update_record)
                            )
    refresh_button.pack(pady=5)

    delete_button = Button(window, text="Удалить"  ##command=delete_record)
                           )
    delete_button.pack(pady=5)

    add_button = Button(window, text="Добавить"  ##command=add_record)
                        )
    add_button.pack(pady=5)

    window.mainloop()
            
            

# Окно при нажатии на кнопку обед
def lunch():
    window = Tk()
    window.title("Обед")
    window.geometry('350x620')
    window['bg'] = "Honeydew"

    title = Label(window, text="Обед", bg="Honeydew", fg="DarkSeaGreen", font=70, width=30)
    title.pack()

    main_frame = Frame(window)
    main_frame.pack()

    # бегунок
    frame_scroll = Scrollbar(main_frame)
    frame_scroll.pack(side=RIGHT, fill=Y)

    frame_scroll = Scrollbar(main_frame, orient='horizontal')
    frame_scroll.pack(side=BOTTOM, fill=X)

    my_frame = ttk.Treeview(main_frame, yscrollcommand=frame_scroll.set, xscrollcommand=frame_scroll.set)
    my_frame.pack()

    frame_scroll.config(command=my_frame.yview)
    frame_scroll.config(command=my_frame.xview)

    # определение колонок
    my_frame['columns'] = (
    'player_№', 'player_product', 'player_mass', 'player_kkal', 'player_b', 'player_j', 'player_y')

    # формат колонок
    my_frame.column("#0", width=0, stretch=NO)
    my_frame.column("player_№", anchor=CENTER, width=30)
    my_frame.column("player_product", anchor=CENTER, width=150)
    my_frame.column("player_mass", anchor=CENTER, width=80)
    my_frame.column("player_kkal", anchor=CENTER, width=80)
    my_frame.column("player_b", anchor=CENTER, width=80)
    my_frame.column("player_j", anchor=CENTER, width=80)
    my_frame.column("player_y", anchor=CENTER, width=80)

    # заголовки колонок
    my_frame.heading("#0", text="", anchor=CENTER)
    my_frame.heading("player_№", text="№", anchor=CENTER)
    my_frame.heading("player_product", text="Продукт", anchor=CENTER)
    my_frame.heading("player_mass", text="Масса", anchor=CENTER)
    my_frame.heading("player_kkal", text="Ккал", anchor=CENTER)
    my_frame.heading("player_b", text="Белки", anchor=CENTER)
    my_frame.heading("player_j", text="Жиры", anchor=CENTER)
    my_frame.heading("player_y", text="Углеводы", anchor=CENTER)

    # добавление данных (визуальный пример)
    my_frame.insert(parent='', index='end', text='',
                   values=('1', 'Молоко', '100', '43', '2,8', '1', '4,6'))
    my_frame.insert(parent='', index='end', text='',
                   values=('2', 'Хлеб', '100', '156', '3,5', '6,7', '6,2'))
    my_frame.pack()

    # таблица для добавления данных
    frame = Frame(window)
    frame.pack(pady=50)

    # заголовки
    new_product = Label(frame, text="Продукт")
    new_product.grid(row=0, column=0)

    new_mass = Label(frame, text="Масса")
    new_mass.grid(row=0, column=1)

    # окна для ввода данных
    new_product_entry = Entry(frame)
    new_product_entry.grid(row=1, column=0)

    new_mass_entry = Entry(frame)
    new_mass_entry.grid(row=1, column=1)

    # Блок функций

    # выбрать запись
    def select_record():
        # очистить поля ввода
        new_product_entry.delete(0, END)
        new_mass_entry.delete(0, END)

        # захватить запись
        selected = my_frame.focus()
        # захват значений записи
        values = my_frame.item(selected, 'values')
        # temp_label.config(text=selected)

        # вывод в поля ввода
        new_product_entry.insert(0, values[0])
        new_mass_entry.insert(0, values[1])

    # сохранить запись
    def update_record():
        selected = my_frame.focus()
        # сохранить новые данные
        my_frame.item(selected, text="", values=(new_product_entry.get(), new_mass_entry.get()))

        # очистить поле ввода
        new_product_entry.delete(0, END)
        new_mass_entry.delete(0, END)

    # def delete_record():

    # def add_record():

    # Кнопки
    select_button = Button(window, text="Выбрать"  ##command=select_record)
                           )
    select_button.pack(pady=5)

    refresh_button = Button(window, text="Заменить"  ##command=update_record)
                            )
    refresh_button.pack(pady=5)

    delete_button = Button(window, text="Удалить"  ##command=delete_record)
                           )
    delete_button.pack(pady=5)

    add_button = Button(window, text="Добавить"  ##command=add_record)
                        )
    add_button.pack(pady=5)

    window.mainloop()            
            
            
            
# Окно при нажатии на кнопку ужин
def dinner():
    window = Tk()
    window.title("Ужин")
    window.geometry('350x620')
    window['bg'] = "AliceBlue"

    title = Label(window, text="Ужин", bg="AliceBlue", fg="CornflowerBlue", font=70, width=30)
    title.pack()

    main_frame = Frame(window)
    main_frame.pack()

    # бегунок
    frame_scroll = Scrollbar(main_frame)
    frame_scroll.pack(side=RIGHT, fill=Y)

    frame_scroll = Scrollbar(main_frame, orient='horizontal')
    frame_scroll.pack(side=BOTTOM, fill=X)

    my_frame = ttk.Treeview(main_frame, yscrollcommand=frame_scroll.set, xscrollcommand=frame_scroll.set)
    my_frame.pack()

    frame_scroll.config(command=my_frame.yview)
    frame_scroll.config(command=my_frame.xview)

    # определение колонок
    my_frame['columns'] = (
    'player_№', 'player_product', 'player_mass', 'player_kkal', 'player_b', 'player_j', 'player_y')

    # формат колонок
    my_frame.column("#0", width=0, stretch=NO)
    my_frame.column("player_№", anchor=CENTER, width=30)
    my_frame.column("player_product", anchor=CENTER, width=150)
    my_frame.column("player_mass", anchor=CENTER, width=80)
    my_frame.column("player_kkal", anchor=CENTER, width=80)
    my_frame.column("player_b", anchor=CENTER, width=80)
    my_frame.column("player_j", anchor=CENTER, width=80)
    my_frame.column("player_y", anchor=CENTER, width=80)

    # заголовки колонок
    my_frame.heading("#0", text="", anchor=CENTER)
    my_frame.heading("player_№", text="№", anchor=CENTER)
    my_frame.heading("player_product", text="Продукт", anchor=CENTER)
    my_frame.heading("player_mass", text="Масса", anchor=CENTER)
    my_frame.heading("player_kkal", text="Ккал", anchor=CENTER)
    my_frame.heading("player_b", text="Белки", anchor=CENTER)
    my_frame.heading("player_j", text="Жиры", anchor=CENTER)
    my_frame.heading("player_y", text="Углеводы", anchor=CENTER)

    # добавление данных (визуальный пример)
    my_frame.insert(parent='', index='end', text='',
                   values=('1', 'Молоко', '100', '43', '2,8', '1', '4,6'))
    my_frame.insert(parent='', index='end', text='',
                   values=('2', 'Хлеб', '100', '156', '3,5', '6,7', '6,2'))
    my_frame.pack()

    # таблица для добавления данных
    frame = Frame(window)
    frame.pack(pady=50)

    # заголовки
    new_product = Label(frame, text="Продукт")
    new_product.grid(row=0, column=0)

    new_mass = Label(frame, text="Масса")
    new_mass.grid(row=0, column=1)

    # окна для ввода данных
    new_product_entry = Entry(frame)
    new_product_entry.grid(row=1, column=0)

    new_mass_entry = Entry(frame)
    new_mass_entry.grid(row=1, column=1)

    # Блок функций

    # выбрать запись
    def select_record():
        # очистить поля ввода
        new_product_entry.delete(0, END)
        new_mass_entry.delete(0, END)

        # захватить запись
        selected = my_frame.focus()
        # захват значений записи
        values = my_frame.item(selected, 'values')
        # temp_label.config(text=selected)

        # вывод в поля ввода
        new_product_entry.insert(0, values[0])
        new_mass_entry.insert(0, values[1])

    # сохранить запись
    def update_record():
        selected = my_frame.focus()
        # сохранить новые данные
        my_frame.item(selected, text="", values=(new_product_entry.get(), new_mass_entry.get()))

        # очистить поле ввода
        new_product_entry.delete(0, END)
        new_mass_entry.delete(0, END)

    # def delete_record():

    # def add_record():

    # Кнопки
    select_button = Button(window, text="Выбрать"  ##command=select_record)
                           )
    select_button.pack(pady=5)

    refresh_button = Button(window, text="Заменить"  ##command=update_record)
                            )
    refresh_button.pack(pady=5)

    delete_button = Button(window, text="Удалить"  ##command=delete_record)
                           )
    delete_button.pack(pady=5)

    add_button = Button(window, text="Добавить"  ##command=add_record)
                        )
    add_button.pack(pady=5)

    window.mainloop()
            
            
            
# Окно при нажатии на кнопку перекус
def snack():
    window = Tk()
    window.title("Перекус")
    window.geometry('350x620')
    window['bg'] = "MistyRose"

    title = Label(window, text="Перекус", bg="MistyRose", fg="PaleVioletRed", font=70, width=30)
    title.pack()

    main_frame = Frame(window)
    main_frame.pack()

    # бегунок
    frame_scroll = Scrollbar(main_frame)
    frame_scroll.pack(side=RIGHT, fill=Y)

    frame_scroll = Scrollbar(main_frame, orient='horizontal')
    frame_scroll.pack(side=BOTTOM, fill=X)

    my_frame = ttk.Treeview(main_frame, yscrollcommand=frame_scroll.set, xscrollcommand=frame_scroll.set)
    my_frame.pack()

    frame_scroll.config(command=my_frame.yview)
    frame_scroll.config(command=my_frame.xview)

    # определение колонок
    my_frame['columns'] = (
    'player_№', 'player_product', 'player_mass', 'player_kkal', 'player_b', 'player_j', 'player_y')

    # формат колонок
    my_frame.column("#0", width=0, stretch=NO)
    my_frame.column("player_№", anchor=CENTER, width=30)
    my_frame.column("player_product", anchor=CENTER, width=150)
    my_frame.column("player_mass", anchor=CENTER, width=80)
    my_frame.column("player_kkal", anchor=CENTER, width=80)
    my_frame.column("player_b", anchor=CENTER, width=80)
    my_frame.column("player_j", anchor=CENTER, width=80)
    my_frame.column("player_y", anchor=CENTER, width=80)

    # заголовки колонок
    my_frame.heading("#0", text="", anchor=CENTER)
    my_frame.heading("player_№", text="№", anchor=CENTER)
    my_frame.heading("player_product", text="Продукт", anchor=CENTER)
    my_frame.heading("player_mass", text="Масса", anchor=CENTER)
    my_frame.heading("player_kkal", text="Ккал", anchor=CENTER)
    my_frame.heading("player_b", text="Белки", anchor=CENTER)
    my_frame.heading("player_j", text="Жиры", anchor=CENTER)
    my_frame.heading("player_y", text="Углеводы", anchor=CENTER)

    # добавление данных (визуальный пример)
    my_frame.insert(parent='', index='end', text='',
                   values=('1', 'Молоко', '100', '43', '2,8', '1', '4,6'))
    my_frame.insert(parent='', index='end', text='',
                   values=('2', 'Хлеб', '100', '156', '3,5', '6,7', '6,2'))
    my_frame.pack()

    # таблица для добавления данных
    frame = Frame(window)
    frame.pack(pady=50)

    # заголовки
    new_product = Label(frame, text="Продукт")
    new_product.grid(row=0, column=0)

    new_mass = Label(frame, text="Масса")
    new_mass.grid(row=0, column=1)

    # окна для ввода данных
    new_product_entry = Entry(frame)
    new_product_entry.grid(row=1, column=0)

    new_mass_entry = Entry(frame)
    new_mass_entry.grid(row=1, column=1)

    # Блок функций

    # выбрать запись
    def select_record():
        # очистить поля ввода
        new_product_entry.delete(0, END)
        new_mass_entry.delete(0, END)

        # захватить запись
        selected = my_frame.focus()
        # захват значений записи
        values = my_frame.item(selected, 'values')
        # temp_label.config(text=selected)

        # вывод в поля ввода
        new_product_entry.insert(0, values[0])
        new_mass_entry.insert(0, values[1])

    # сохранить запись
    def update_record():
        selected = my_frame.focus()
        # сохранить новые данные
        my_frame.item(selected, text="", values=(new_product_entry.get(), new_mass_entry.get()))

        # очистить поле ввода
        new_product_entry.delete(0, END)
        new_mass_entry.delete(0, END)

    # def delete_record():

    # def add_record():

    # Кнопки
    select_button = Button(window, text="Выбрать"  ##command=select_record
                           )
    select_button.pack(pady=5)

    refresh_button = Button(window, text="Заменить"  ##command=update_record
                            )
    refresh_button.pack(pady=5)

    delete_button = Button(window, text="Удалить"  ##command=delete_record
                           )
    delete_button.pack(pady=5)

    add_button = Button(window, text="Добавить"  ##command=add_record
                        )
    add_button.pack(pady=5)

    window.mainloop()
            
            
# Главное окно
window = Tk()

#иконка приложения (ЗАГРУЗИТЬ ИЗОБРАЖЕНИЕ)
# photo = PhotoImage(file='58431506a9a7d158c60a2227.png')
# window.iconphoto(False, photo)

window.title("Приложение :'Подсчёт калорий'")
window.geometry('350x620')
window['bg'] = 'lavender'

# ЗДЕСЬ ДОЛЖЕН БЫТЬ КАЛЕНДАРЬ И ВЫБОР ДАТЫ
title = Label(window, text="Сегодня", bg = "lavender", fg ="indigo", font=70, width=30)
title.grid(column=0, row=0)

title=Label(window, bg = "lavender", font=70, width=30)
title.grid(column=0, row=1)

# кнопка выбора завтрака
btn = Button(window, text ='Завтрак', bg="Linen", fg ='SandyBrown', font=90, width=30, height=1, relief=RAISED, bd=6, command = breafest)
btn.grid(column=0, row=2)

# кнопка выбоа обеда
btn = Button(window, text="Обед", bg="Honeydew", fg ="DarkSeaGreen", font=70, width=30, height=1, relief=RAISED, bd=6, command = lunch)
btn.grid(column=0, row=3)

# кнопка выбора ужина
btn = Button(window, text="Ужин", bg="AliceBlue", fg ="CornflowerBlue", font=70, width=30, height=1, relief=RAISED, bd=6, command = dinner)
btn.grid(column=0, row=4)

# кнопка выбора перекуса
btn = Button(window, text="Перекус", bg="MistyRose", fg ="PaleVioletRed", font=70, width=30, height=1, relief=RAISED, bd=6, command = snack)
btn.grid(column=0, row=5)

title=Label(window, bg = "lavender", font=70, width=30 )
title.grid(column=0, row=6)

# # вода
# title=Label(window, text="Вода",bg="lightcyan",fg ="indigo",font=70,width=30 )
# title.grid(column=0, row=8)
# btn = Button(window,text = '+', bg="pink",font=20,width=4,height = 1,
#             relief=RAISED,
#             bd=6)
# btn.grid(column=1, row=8)

# сводка (ДОБАВИТЬ ВИДЖЕТЫ)
#title=Label(window, text="СВОДКА", bg="white", fg ="indigo", font=70, width=30, height=10, anchor = 'n')
#title.grid(column=0, row=7)

#title=Label(window, bg = "lavender", font=70, width=30 )
#title.grid(column=0, row=8)

#диаграмма для сводки
fig = matplotlib.figure.Figure(figsize=(5,5))
ax = fig.add_subplot(111)
ax.set_title('CВОДКА')
colors = ("lightcoral", "yellowgreen")
#labels = ['Съедено','Осталось']
#данные для примера
ax.pie([20,80],colors = colors,
       #labels=labels,
       wedgeprops=dict(width=0.5),
       autopct='%1.1f%%') 
ax.legend(['Съедено',
          'Осталось'])
circle=matplotlib.patches.Circle( (0,0), 0.3, color='white')
ax.add_artist(circle)
ax.axis('equal')
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().grid(column=0, row=7)
canvas.draw()

#текст внутри диаграммы
title=Label(window,text='''съедено:500ккал
осталось:1200ккал''',font=("Courier", 10, "roman"), bg="white" )
title.grid(column=0, row=7)

# кнопка СОХРАНЕНИЯ и выхода
btn = Button(window, text="Закрыть окно", bg="pink", relief=RAISED, bd = 6, command=window.quit)
btn.grid(column=0, row=9)

window.mainloop()
