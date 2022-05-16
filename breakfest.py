import matplotlib.figure
import matplotlib.patches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from tkinter.ttk import Radiobutton
from tkinter.ttk import Combobox
import sqlite3

#кнопка вывода данных
def add_product():
    connect = sqlite3.connect('n_base.db')
    cursor = connect.cursor() ## Создаем курсор - это специальный объект который делает запросы и получает их результаты
    cursor.execute("SELECT * FROM n_base WHERE name = ?", [my_product.get()]) ##Делаем SELECT запрос к базе данных, используя обычный SQL-синтаксис
    my_frame.insert(parent='', index='end', values=cursor.fetchone())
    my_frame.pack()
    connect.close() ##закрываем соединение с базой данных

# def delete_product():


# Таблица при нажатии на кнопку завтрак
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
my_frame['columns'] = ('player_product', 'player_mass', 'player_kkal', 'player_p', 'player_f', 'player_c')

# формат колонок
my_frame.column("#0", width=0, stretch=NO)
my_frame.column("player_product", anchor=CENTER, width=150)
my_frame.column("player_mass", anchor=CENTER, width=80)
my_frame.column("player_kkal", anchor=CENTER, width=80)
my_frame.column("player_p", anchor=CENTER, width=80)
my_frame.column("player_f", anchor=CENTER, width=80)
my_frame.column("player_c", anchor=CENTER, width=80)

# заголовки колонок
my_frame.heading("#0", text="", anchor=CENTER)
my_frame.heading("player_product", text="Продукт", anchor=CENTER)
my_frame.heading("player_mass", text="Масса", anchor=CENTER)
my_frame.heading("player_kkal", text="Ккал", anchor=CENTER)
my_frame.heading("player_p", text="Белки", anchor=CENTER)
my_frame.heading("player_f", text="Жиры", anchor=CENTER)
my_frame.heading("player_c", text="Углеводы", anchor=CENTER)

# # добавление данных (визуальный пример)
# my_frame.insert(parent='', index='end', text='',
#                    values=('Молоко', '100', '43', '2,8', '1', '4,6'))
# my_frame.insert(parent='', index='end', text='',
#                    values=('Хлеб', '100', '156', '3,5', '6,7', '6,2'))
# my_frame.pack()

# таблица для добавления данных
low_frame = Frame(window)
low_frame.pack(pady=50)

# заголовки
new_product = Label(low_frame, text="Продукт")
new_product.grid(row=0, column=0)

new_mass = Label(low_frame, text="Масса")
new_mass.grid(row=0, column=1)

# окна для ввода данных
my_product = StringVar()
my_mass = IntVar()

new_product_entry = Entry(low_frame, textvariable=my_product)
new_product_entry.grid(row=1, column=0)

new_mass_entry = Entry(low_frame, textvariable=my_mass)
new_mass_entry.grid(row=1, column=1)


# Кнопки
select_button = Button(window, text="Добавить", command=add_product)
select_button.pack(pady=5)

delete_button = Button(window, text="Удалить"##, command=delete_product)
                       )
delete_button.pack(pady=5)


window.mainloop()
