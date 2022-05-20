import tkinter as tk
import tkinter.ttk as ttk
import sqlite3

#соединение с базой данных

def connect():
    conn =sqlite3.connect('n_base.db')
    cur =conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS n_base (name TEXT,g INT,kkal INT,p INT,f INT ,c INT)''')
    conn.commit()
    conn.close()

#вывод данных

def View():
    conn =sqlite3.connect('n_base.db')
    cur =conn.cursor()
    #sql = 'INSERT INTO n_base (name,g ,kkal ,p ,f  ,c ) values(?, ?, ?, ? ,?, ?)'
#проверка работы ,вывод данных с условием
    #with conn:
        #data = conn.execute("SELECT * FROM n_base WHERE kkal >=350")
        #for row in data:
           #print(row)
           
#вывод с сортировкой    
    #cur.execute("SELECT * FROM n_base ORDER BY name")
    #remaining_rows = cur.fetchall()
    #print(remaining_rows)
    #conn.close()
    cur.execute("SELECT * FROM n_base")
    rows = cur.fetchall()
    for row in rows:
        print(row) # it print all records in the database
        tree.insert("", tk.END, values=row)
    conn.close()


window = tk.Tk()

window.title("Приложение :'Подсчёт калорий'")
window.geometry('620x620')

#добавление данных в базу данных
#cur.execute('''INSERT INTO n_base VALUES('Shake',67,78,7,7,9)''')

#создание окна 

tree =ttk.Treeview(window, columns=("#1", "#2", "#3","#4", "#5", "#6","#7", "#8"),
                   show='headings')

tree.heading("#1", text="name")
tree.heading("#2", text="g")
tree.heading("#3", text="kkal")
tree.heading("#4", text="p")
tree.heading("#5", text="f")
tree.heading("#6", text="c")
tree.pack()

b2 = tk.Button(text="view data", command=View)
b2.pack()
