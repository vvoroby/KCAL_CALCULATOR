from tkinter import *
from tkinter import ttk
import sqlite3
from datetime import date

#НА ПРИМЕРЕ ЗАВТРАКА

def find_todate():
    return date.today().strftime("%d.%m.%Y")

#калькулятор расчета кбжу по массе
global calculated_selected_product

def calculation(selected_products):
    global calculated_selected_product
    calculated_selected_product = []
    for item in enumerate(selected_products):
        if item[0] == 0:
             calculated_selected_product.append(item[1])
        else:
            calculated_selected_product.append(item[1] * my_mass.get() / 100)

    return tuple( calculated_selected_product)
        
# Записываем значение в базу данных    
def add_product_in_archive(selected_products):
    added_calculated_selected_product = []
    added_calculated_selected_product.append(find_todate())
    added_calculated_selected_product.append('breakfast')
    for item in enumerate(calculated_selected_product):
        added_calculated_selected_product.append(item[1])
        
    connect = sqlite3.connect('archive.db')
    cursor = connect.cursor()
    cursor.execute('''INSERT INTO archive (date,meal,name,g,kkal,p,f,c) VALUES (?,?,?,?,?,?,?,?)''', tuple(added_calculated_selected_product))
    connect.commit()
    connect.close()

#удаление данных из базы
def delete_product_in_archive(deleted_archive_product):
    print(deleted_archive_product[0])
    connect = sqlite3.connect('archive.db')
    cursor = connect.cursor()
    cursor.execute("DELETE FROM archive WHERE name = ?", [deleted_archive_product[0]] )
    connect.commit()
    connect.close()  
        
def add_product():
    connect = sqlite3.connect('n_base.db') ##делаем запрос к базе данных
    cursor = connect.cursor()
    cursor.execute('''SELECT * FROM n_base WHERE name = ?''', [my_product.get().title()])
    selected_products = cursor.fetchone()
    connect.close()

    #записываем значение в таблицу
    my_frame.insert(parent='', index='end', values=calculation(selected_products))
    my_frame.pack()

    new_product_entry.delete(0, END)  ##очищает окно ввода
    new_mass_entry.delete(0, END)

    #добавить запись в базу данных
    add_product_in_archive(selected_products)
    
def delete_product():
    # захватить запись в переменную
    selected = my_frame.focus()
    deleted_selected_product = my_frame.item(selected, 'values')

    # удалить запись из таблицы
    selected_item = my_frame.selection()[0]
    my_frame.delete(selected_item)

    ## удалить запись из базы данных
    delete_product_in_archive(deleted_selected_product)    
    
window = Tk()
window.title("Завтрак")
window.geometry('620x620')
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

my_frame['columns'] = ('#1', '#2', '#3', '#4', '#5', '#6','#7','#8')

# формат колонок
my_frame.column("#0", width=0, stretch=NO)
my_frame.column("#1", anchor=CENTER, width=150)
my_frame.column("#2", anchor=CENTER, width=80)
my_frame.column("#3", anchor=CENTER, width=80)
my_frame.column("#4", anchor=CENTER, width=80)
my_frame.column("#5", anchor=CENTER, width=80)
my_frame.column("#6", anchor=CENTER, width=80)

# заголовки колонок
my_frame.heading("#0", text="", anchor=CENTER)
my_frame.heading("#1", text="name product", anchor=CENTER)
my_frame.heading("#2", text="mass", anchor=CENTER)
my_frame.heading("#3", text="kcal", anchor=CENTER)
my_frame.heading("#4", text="p", anchor=CENTER)
my_frame.heading("#5", text="f", anchor=CENTER)
my_frame.heading("#6", text="c", anchor=CENTER)

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

b2 = Button(text="Добавить ", command=add_product)
b2.pack(pady=5)

b3 = Button(text="Удалить ", command=delete_product)
b3.pack(pady=5)

btn = Button(window, text="Закрыть", bg="pink", relief=RAISED, bd = 1, command=window.destroy)
btn.pack(side=TOP, pady=40)

window.mainloop()
