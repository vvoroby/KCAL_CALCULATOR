from tkinter import *
from tkinter import ttk
import sqlite3
from datetime import date

#ЧЕРНОВИК!!!!!!!!!!

def add_data():
    def calculation(items):
            new = []
            for item in enumerate(items):
                if item[0] == 0:
                    new.append(item[1])
                else:
                    new.append(item[1] * my_mass.get() / 100)

            return tuple(new)
        
    connect = sqlite3.connect('n_base.db') ##делаем запрос к базе данных
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM n_base WHERE name = ?", [my_product.get()])
    items = cursor.fetchone()
    connect.close()

    tree.insert(parent='', index='end', values=calculation(items)) ##записываем значение в визуальную таблицу
    tree.pack()

    new_product_entry.delete(0, END)  ##очищает окно ввода
    new_mass_entry.delete(0, END)
    
#соединение с базой данных    
    conn =sqlite3.connect('archive.db')
    cur =conn.cursor()
#ввод данных в базу     
    sql = f'INSERT INTO archive VALUES({calculation(items).get()})'
    
    with conn:
        conn.executemany(sql, calculation(items).get())
#добавление данных в таблицу        
        for row in calculation(items).get():
            tree.insert("",0, values=row)
    
#удаление данных из базы
def delete_data():
    conn =sqlite3.connect('archive.db')
    cur =conn.cursor()
    delete='DELETE FROM archive WHERE meal= "Breakfast" '
# захватить запись в переменную
    selected = tree.focus()
    values = tree.item(selected, 'values')
# удалить запись из таблицы
    selected_item = tree.selection()
    tree.delete(selected_item)
    with conn:
        conn.executemany(delete, selected_item)  

window = Tk()

window.title("Приложение :'Подсчёт калорий'")
window.geometry('620x620')

tree =ttk.Treeview(window,show='headings')
tree.pack()

tree['columns'] = ('#1', '#2', '#3', '#4', '#5', '#6','#7','#8')

# формат колонок
tree.column("#0", width=0, stretch=NO)
tree.column("#1", anchor=CENTER, width=150)
tree.column("#2", anchor=CENTER, width=150)
tree.column("#3", anchor=CENTER, width=150)
tree.column("#4", anchor=CENTER, width=80)
tree.column("#5", anchor=CENTER, width=80)
tree.column("#6", anchor=CENTER, width=80)
tree.column("#7", anchor=CENTER, width=80)
tree.column("#8", anchor=CENTER, width=80)

# заголовки колонок
tree.heading("#0", text="", anchor=CENTER)
tree.heading("#1", text="meal", anchor=CENTER)
tree.heading("#2", text="date", anchor=CENTER)
tree.heading("#3", text="name product", anchor=CENTER)
tree.heading("#4", text="mass", anchor=CENTER)
tree.heading("#5", text="kcal", anchor=CENTER)
tree.heading("#6", text="p", anchor=CENTER)
tree.heading("#7", text="f", anchor=CENTER)
tree.heading("#8", text="c", anchor=CENTER)

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

b2 = Button(text="Добавить данные", command=add_data)
b2.pack(pady=5)

b3 = Button(text="Удалить данные", command=delete_data)
b3.pack(pady=5)

window.mainloop()

