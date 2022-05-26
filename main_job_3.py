import matplotlib.figure
import matplotlib.patches
import sqlite3
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Radiobutton
from tkinter.ttk import Combobox
from datetime import date
from functools import partial
from tkinter import messagebox

"""
Закрывает текущее окно, открывает главное окно
"""

def open_main(window_now):
    window_now.destroy()
    main()

"""
Закрывает главное окно, открывает окно с приемом пищи
"""

def open_meal(window_main, meal, bg_color, fg_color):
    window_main.destroy()
    windows(meal, bg_color, fg_color)

"""
Закрывает главное окно, открывает окно архива
"""
def open_archive(window_main):
    window_main.destroy()
    archive()

"""
Закрывает главное окно, открывает окно калькулятора
"""
def open_cakculator(window_main):
    window_main.destroy()
    ckal_calculator()

"""
Закрывает главное окно, открывает окно для добавления в БД
"""
def open_insert_new_product(window_meal, meal, bg_color, fg_color):
    window_meal.destroy()
    insert_new_product(meal, bg_color, fg_color)

"""
Окно для добавления нового продукта в БД
"""
def insert_new_product(meal, bg_color, fg_color):
    """ 
    Добавляет продукт в БД
    """
    def insert_product_in_db():
        connect = sqlite3.connect('n_base.db') ## создаём соединение с БД
        cursor = connect.cursor()
        try:
            # добавляем в базу
            cursor.execute('''INSERT INTO n_base VALUES (?,?,?,?,?,?)''',
                           (str(Entry1.get()).title(), int(Entry2.get()), int(Entry3.get()), int(Entry4.get()), int(Entry5.get()), int(Entry6.get())))
            # очищают окна ввода
            Entry1.delete(0, END)  
            Entry2.delete(0, END)
            Entry3.delete(0, END)  
            Entry4.delete(0, END)
            Entry5.delete(0, END) 
            Entry6.delete(0, END)
            connect.commit()
            connect.close()
        # вывод ошибки    
        except:
            messagebox.showerror('ERROR', 'Data entered incorrectly!')
    # окно для добавления продукта
    window_insert = Tk()
    window_insert.title('Entering a new product to the database.') 
    window_insert.geometry('750x280')
    window_insert['bg'] = 'lavender'
    photo = PhotoImage(file='58431506a9a7d158c60a2227.png')
    window_insert.iconphoto(False, photo)
    # пояснение для пользователя
    title = Label(window_insert,
                  text="Enter your product and its kpfc(for 100 g of product).",
                  bg="lavender", fg="purple4")
    title.pack(pady=20)

    # переменные для ввода данных
    insert_product = StringVar()
    insert_mass = IntVar()
    insert_kkal = IntVar()
    insert_p = IntVar()
    insert_f = IntVar()
    insert_c = IntVar()

    # таблица для добавления данных
    low_frame = Frame(window_insert)
    low_frame.pack(pady=20)

    # заголовки
    Label1 = Label(low_frame, text="Product name").grid(row=0, column=0)
    Label2 = Label(low_frame, text="Mass").grid(row=0, column=1)  ## необходимо вводить 100 грамм
    Label3 = Label(low_frame, text="Kcal").grid(row=0, column=2)
    Label4 = Label(low_frame, text="Proteins").grid(row=0, column=3)
    Label5 = Label(low_frame, text="Fats").grid(row=0, column=4)
    Label6 = Label(low_frame, text="Carbohydrates").grid(row=0, column=5)
    # поля ввода данных о новом продукте
    Entry1 = Entry(low_frame, textvariable=insert_product)
    Entry1.grid(row=1, column=0)
    Entry2 = Entry(low_frame, textvariable=insert_mass)
    Entry2.grid(row=1, column=1)
    Entry3 = Entry(low_frame, textvariable=insert_kkal)
    Entry3.grid(row=1, column=2)
    Entry4 = Entry(low_frame, textvariable=insert_p)
    Entry4.grid(row=1, column=3)
    Entry5 = Entry(low_frame, textvariable=insert_f)
    Entry5.grid(row=1, column=4)
    Entry6 = Entry(low_frame, textvariable=insert_c)
    Entry6.grid(row=1, column=5)

    # кнопки
    select_button = Button(window_insert, text="Add", command=insert_product_in_db)
    select_button.pack(pady=5)

    btn = Button(window_insert, text="Close", bg="pink", fg="HotPink4", relief=RAISED, bd=1, command=partial(open_meal, window_insert, meal, bg_color, fg_color))
    btn.pack(side=TOP, pady=40)

    window_insert.mainloop()

"""
Функция для поиска нынешней даты
"""
def find_today():
    return date.today().strftime("%d.%m.%Y")

"""
Функция для подсчета общего числа калорий
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

"""
Окно при запуске приложения, вычисляет дневную норму ккал
"""
def ckal_calculator():
    global ckal
    """
    Функция для подсчета нормы ккал, исходя из физических нагрузок
    """
    def calculeter():
        try:
            # просчёт нормы калорий в зависимости от нагрузки человека по формуле Миффлина-Сан Жеора
            if my_activiti.get() == "Physical activity is absent or minimal":
                ckal.set(int((my_height.get() * 6.25 + my_weight.get() * 10 - my_age.get() * 5 + my_gender.get()) * 1.2))
            elif my_activiti.get() == "Midle workouts 2-3 times a week":
                ckal.set(int((my_height.get() * 6.25 + my_weight.get() * 10 - my_age.get() * 5 + my_gender.get()) * 1.38))
            elif my_activiti.get() == "Midle workouts 4-5 times a week":
                ckal.set(int((my_height.get() * 6.25 + my_weight.get() * 10 - my_age.get() * 5 + my_gender.get()) * 1.46))
            elif my_activiti.get() == "Workout every day":
                ckal.set(int((my_height.get() * 6.25 + my_weight.get() * 10 - my_age.get() * 5 + my_gender.get()) * 1.64))
            elif my_activiti.get() == "Workout every day + physical work":
                ckal.set(int((my_height.get() * 6.25 + my_weight.get() * 10 - my_age.get() * 5 + my_gender.get()) * 1.9))
        # вывод ошибок
            if ckal.get() <= 0:
                messagebox.showerror('ERROR', 'Data entered incorrectly!')
        except:
            messagebox.showerror('ERROR', 'Data entered incorrectly.!')

    # окно расчёта калорий
    window_calculetor = Tk()
    window_calculetor.title('Calorie Calculation')
    window_calculetor.geometry("300x350")
    window_calculetor['bg'] = 'lavender'
    photo = PhotoImage(file='58431506a9a7d158c60a2227.png')
    window_calculetor.iconphoto(False, photo)

    label = Label(text="Enter your personal data", bg="lavender")
    label.pack(pady=5)

    # переменные для ввода данных
    my_height = IntVar()
    my_weight = IntVar()
    my_age = IntVar()
    my_gender = IntVar()
    my_activiti = StringVar()
    ckal = IntVar()

    # блок невидимых рамок для красивого интерфейса
    f_1 = Frame(window_calculetor)
    f_2 = Frame(window_calculetor)
    f_3 = Frame(window_calculetor)
    f_4 = Frame(window_calculetor)
    f_5 = Frame(window_calculetor)
    f_6 = Frame(window_calculetor)

    # ввод данных
    height_label = Label(f_1, text="Height ", bg="lavender")
    height_entry = Entry(f_1, width=8, textvariable=my_height)
    height2_label = Label(f_1, text="cm ", bg="lavender")

    weight_label = Label(f_2, text="Weight ", bg="lavender")
    weight_entry = Entry(f_2, width=8, textvariable=my_weight)
    weight2_label = Label(f_2, text="kg ", bg="lavender")

    age_label = Label(f_3, text="Age ", bg="lavender")
    age_entry = Entry(f_3, width=8, textvariable=my_age)

    gender_label = Label(f_4, text="Gender ", bg="lavender")
    rad1 = Radiobutton(f_4, text='М', value=4, variable=my_gender)
    rad2 = Radiobutton(f_4, text='W', value=-161, variable=my_gender)

    activiti_label = Label(f_5, text="Activity ", bg="lavender")
    activiti = Combobox(f_5, textvariable=my_activiti, width=48,
                        values=["Physical activity is absent or minimal",
                                "Midle workouts 2-3 times a week",
                                "Midle workouts 4-5 times a week",
                                "Workout every day",
                                "Workout every day + physical work"])

    # вывод данных
    ckal_label1 = Label(f_6, text="Your calories norm: ", bg="lavender")
    ckal_label2 = Label(f_6, textvariable=ckal, bg="lavender")
    ckal_label3 = Label(f_6, text="kcal ", bg="lavender")
    # кнопка "узнать"
    message_button = Button(text="Get to know", bg="pink", command=calculeter)

    # упорядочивание элементов окна
    f_1.pack(pady=5)
    f_2.pack(pady=5)
    f_3.pack(pady=5)
    f_4.pack(pady=5)
    f_5.pack(pady=5)
    message_button.pack(pady=5)
    f_6.pack(pady=5)

    height_label.pack(side=LEFT)
    weight_label.pack(side=LEFT)
    age_label.pack(side=LEFT)
    gender_label.pack(side=LEFT)
    activiti_label.pack(side=LEFT)
    ckal_label1.pack(side=LEFT)

    height_entry.pack(side=LEFT)
    height2_label.pack(side=LEFT)
    weight_entry.pack(side=LEFT)
    weight2_label.pack(side=LEFT)
    age_entry.pack(side=LEFT)
    rad1.pack(side=LEFT)
    rad2.pack(side=LEFT)
    activiti.pack(side=LEFT)
    ckal_label2.pack(side=LEFT)
    ckal_label3.pack(side=LEFT)

    btn = Button(window_calculetor, text="Save", bg="pink", command=partial(open_main, window_calculetor))
    btn.pack(pady=30, side=TOP)

    window_calculetor.mainloop()

    return ckal

""" 
Таблица при нажатии на кнопку архив
"""
def archive():
    """
    Находит приемы пищи в нужный день
    """
    def find_product_from_day():
        my_frame.delete(*my_frame.get_children()) ## очищает таблицу

        connect = sqlite3.connect('archive.db')  ## делаем запрос к архиву
        cursor = connect.cursor()
        ## выбираем нужные нам продукты по дате и передаём в переменную
        cursor.execute('''SELECT meal,name,g,kkal,p,f,c  FROM archive WHERE date = ?''', [date_entry.get()])
        all_products = cursor.fetchall()
        connect.close()
        # проверяем на наличие ошибок
        if all_products!=[]:
            for item in all_products:
                my_frame.insert(parent='', index='end', values=item)
                my_frame.pack()
        else:
            messagebox.showerror('ERROR','''The value is not in the archive.
(Check if the date is entered correctly:__.__.____ )''')## вывод ошибки
    # окно архива
    window_archive = Tk()
    window_archive.title("Archive")
    window_archive.geometry('350x620')
    window_archive['bg'] = 'Lavender'
    photo = PhotoImage(file='58431506a9a7d158c60a2227.png')
    window_archive.iconphoto(False, photo)
    
    title = Label(window_archive, text="Archive", bg="Lavender", fg="purple4", font=70, width=30)## создаем заголовок
    title.pack(pady=5)
    # переменная для ввода данных
    my_date = StringVar()

    # окно ввода даты
    frame = Frame(window_archive)
    date_label = Label(frame, text="Date ", bg="lavender")## заголовок окна
    date_entry = Entry(frame, width=10, textvariable=my_date)##  окно ввода
    # упорядочивание окна и заголовка
    date_label.pack(side=LEFT)
    date_entry.pack(side=RIGHT)
    frame.pack(pady=5)

    # кнопка "найти"
    message_button = Button(window_archive, text="Find", bg="pink", command=find_product_from_day)
    message_button.pack(pady=15)

    # таблица
    main_frame = Frame(window_archive)
    main_frame.pack(pady=40)

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
    'player_eating', 'player_product', 'player_mass', 'player_kkal', 'player_p', 'player_f', 'player_c')

    # формат колонок
    my_frame.column("#0", width=0, stretch=NO)
    my_frame.column("player_eating", anchor=CENTER, width=80)
    my_frame.column("player_product", anchor=CENTER, width=150)
    my_frame.column("player_mass", anchor=CENTER, width=80)
    my_frame.column("player_kkal", anchor=CENTER, width=80)
    my_frame.column("player_p", anchor=CENTER, width=80)
    my_frame.column("player_f", anchor=CENTER, width=80)
    my_frame.column("player_c", anchor=CENTER, width=80)

    # заголовки колонок
    my_frame.heading("#0", text="", anchor=CENTER)
    my_frame.heading("player_eating", text="Meal", anchor=CENTER)
    my_frame.heading("player_product", text="Product name", anchor=CENTER)
    my_frame.heading("player_mass", text="Mass", anchor=CENTER)
    my_frame.heading("player_kkal", text="Kcal", anchor=CENTER)
    my_frame.heading("player_p", text="Proteins", anchor=CENTER)
    my_frame.heading("player_f", text="Fats", anchor=CENTER)
    my_frame.heading("player_c", text="Carbohydrates", anchor=CENTER)

    # кнопка сохранения и выхода
    btn = Button(window_archive, text="Close", bg="pink", relief=RAISED, bd=1, command=partial(open_main, window_archive))
    btn.pack(side=TOP, pady=60)

    window_archive.mainloop()

"""
Окна c приемами пищи
"""
def windows(meal, bg_color, fg_color):
    """
    Калькулятор расчета кбжу по массе
    """
    def calculation(selected_products):
        calculated_selected_product = []
        # цикл просчитывает кбжу для введенной массы
        for item in selected_products:
            if type(item) == str:
                calculated_selected_product.append(item)
            else:
                calculated_selected_product.append(item * int(new_mass_entry.get()) / 100)
        return tuple(calculated_selected_product)

    """
    Функция добавляет продукт в таблицу
    """
    def add_product():
        connect = sqlite3.connect('n_base.db')  ## делаем запрос к базе данных
        cursor = connect.cursor()
        cursor.execute('''SELECT * FROM n_base WHERE name = ?''', [new_product_entry.get().title()])## получаем нужный продукт из БД
        try:
            calculated_selected_product = calculation(cursor.fetchone())
            connect.close()

            # записываем значение в таблицу
            my_frame.insert(parent='', index='end', values=calculated_selected_product)
            my_frame.pack()

            #очищает окно ввода
            new_product_entry.delete(0, END)  
            new_mass_entry.delete(0, END)

            add_product_to_base(calculated_selected_product)

        except:
            res = messagebox.askquestion('ERROR!', 'Data entered incorrectly. Do you want to add your product to the database?') ## ввывод ошибки и вопроса
            if res == 'yes':
                open_insert_new_product(window_meal,meal,bg_color,fg_color)

    """
    Функция добавляет продукт в БД
    """
    def add_product_to_base(calculated_selected_product):
        # добавить запись в базу данных
        added_calculated_selected_product = []
        added_calculated_selected_product.append(find_today())
        added_calculated_selected_product.append(meal.lower())
        for item in calculated_selected_product:
            added_calculated_selected_product.append(item)

        connect = sqlite3.connect('archive.db') ## создаём соединение с архивом
        cursor = connect.cursor()
        cursor.execute('''INSERT INTO archive (date,meal,name,g,kkal,p,f,c) VALUES (?,?,?,?,?,?,?,?)''',
                       tuple(added_calculated_selected_product))## добавление продукта в архив
        connect.commit()
        connect.close()

   """
   Функция удаляет продукт из таблицы
   """
    def delete_product():
        # захватить запись в переменную
        selected = my_frame.focus()
        deleted_selected_product = my_frame.item(selected, 'values')

        # удалить запись из таблицы
        selected_item = my_frame.selection()[0]
        my_frame.delete(selected_item)

        delete_product_from_base(deleted_selected_product)

   """
   Функция удаляет продукт из БД
   """
    def delete_product_from_base(deleted_selected_product):
        connect = sqlite3.connect('archive.db')## создаём соединения с архивом
        cursor = connect.cursor()
        cursor.execute("DELETE FROM archive WHERE name = ? AND g = ?",
                       [deleted_selected_product[0], deleted_selected_product[1]])## удаляем продукт из архива
        connect.commit()
        connect.close()

    # таблица при нажатии на кнопку с приёмом пищи
    window_meal = Tk()
    window_meal.title(meal)
    window_meal.geometry('350x620')
    window_meal['bg'] = bg_color
    photo = PhotoImage(file='58431506a9a7d158c60a2227.png')
    window_meal.iconphoto(False, photo)

    #заголовок таблицы
    title = Label(window_meal, text=meal, bg=bg_color, fg=fg_color, font=70, width=30)
    title.pack()

    main_frame = Frame(window_meal)
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
    my_frame.heading("player_product", text="Product name", anchor=CENTER)
    my_frame.heading("player_mass", text="Mass", anchor=CENTER)
    my_frame.heading("player_kkal", text="Kcal", anchor=CENTER)
    my_frame.heading("player_p", text="Proteins", anchor=CENTER)
    my_frame.heading("player_f", text="Fats", anchor=CENTER)
    my_frame.heading("player_c", text="Carbohydrates", anchor=CENTER)

    # добавляем продукты в таблицу, добавленные ранее
    connect = sqlite3.connect('archive.db')  ## делаем запрос к базе данных
    cursor = connect.cursor()
    # получаем нужные записи из архива, передаём в переменную
    cursor.execute('''SELECT name,g,kkal,p,f,c  FROM archive WHERE date = ? AND meal = ?''', [find_today(), meal.lower()])
    all_products = cursor.fetchall()
    connect.close()
    # добавляем записи в таблицу
    for item in all_products:
        my_frame.insert(parent='', index='end', values=item)
        my_frame.pack()

    # таблица для добавления данных
    low_frame = Frame(window_meal)
    low_frame.pack(pady=50)

    # заголовки
    new_product = Label(low_frame, text="Product")
    new_product.grid(row=0, column=0)

    new_mass = Label(low_frame, text="Mass")
    new_mass.grid(row=0, column=1)

    # окна для ввода данных
    my_product = StringVar()
    my_mass = IntVar()

    new_product_entry = Entry(low_frame, textvariable=my_product)
    new_product_entry.grid(row=1, column=0)

    new_mass_entry = Entry(low_frame, textvariable=my_mass)
    new_mass_entry.grid(row=1, column=1)

    # кнопки
    select_button = Button(window_meal, text="Add", command=add_product)
    select_button.pack(pady=5)

    delete_button = Button(window_meal, text="Delete", command=delete_product)
    delete_button.pack(pady=5)

    btn = Button(window_meal, text="Close", bg="pink", fg="HotPink4", relief=RAISED, bd=1, command=partial(open_main, window_meal))
    btn.pack(side=TOP, pady=40)

    window_meal.mainloop()

"""
Главное окно с кнопками
"""
def main():
    """ 
    Диаграмма для сводки
    """
    def diagram():
        # создание диаграммы
        fig = matplotlib.figure.Figure(figsize=(4, 3), facecolor="Lavender")
        ax = fig.add_subplot(111)
        try:
            ax.pie([summ(), ckal.get() - summ()], 
                   colors=("lightcoral", "yellowgreen"),
                   wedgeprops=dict(width=0.5),
                   autopct='%1.1f%%')## данные диаграммы 
            ax.legend([f"Eaten:{summ()} kcal",
                       f"Left: {ckal.get() - summ()} kcal"]) ## легенда диаграммы
            circle = matplotlib.patches.Circle((0, 0), 0.3, color='lavender')
            ax.add_artist(circle)
            ax.axis('equal')
            canvas = FigureCanvasTkAgg(fig, master=window_main)
            canvas.get_tk_widget().pack()
            canvas.draw()
        except ValueError:
            #  вывод ошибки при переедании 
            ax.pie([1, 0], 
                   colors=("lightcoral", "yellowgreen"),
                   wedgeprops=dict(width=0.5),
                   autopct='%1.1f%%')##  данные диаграммы( диаграмма будет заполнена )
            ax.legend([f"Eaten:{summ()} kcal",
                       f"Left: {0} kcal"])## легенда диаграммы
            circle = matplotlib.patches.Circle((0, 0), 0.3, color='lavender')
            ax.add_artist(circle)
            ax.axis('equal')
            canvas = FigureCanvasTkAgg(fig, master=window_main)
            canvas.get_tk_widget().pack()
            canvas.draw()

            messagebox.showwarning('WARNING', f'You overate {int(summ() - ckal.get())} calories!!!')  ## предупреждение

    window_main = Tk()

    #иконка приложения
    photo = PhotoImage(file='58431506a9a7d158c60a2227.png')
    window_main.iconphoto(False, photo)

    # главное окно
    window_main.title("App:'Calories Calculator'")
    window_main.geometry('350x620')
    window_main['bg'] = 'Lavender'

    hat = Frame(window_main)
    hat['bg'] = 'lavender'

    # показывает нынешнюю дату
    title = Label(hat, text=find_today(), bg = 'lavender', fg="purple4", font=20, width=12)
    title.pack(pady=3, side=LEFT)

    # кнопки калькулятора и архива
    btn = Button(hat, text='Сalculator', bg="pink", fg="HotPink4", relief=RAISED, bd=6, width=12, command=partial(open_cakculator, window_main))
    btn.pack(pady=3, side=RIGHT)

    btn = Button(hat, text ='Archive', bg="pink", fg ="HotPink4", relief=RAISED, bd = 6, width=12, command=partial(open_archive, window_main))
    btn.pack(pady=3, side=RIGHT)

    hat.pack()

    # кнопка выбора завтрака
    btn = Button(window_main, text ='Breakfast', bg="Linen", fg ='SandyBrown', font=90, width=30, height=1, relief=RAISED, bd=6, command=partial(open_meal, window_main, "Breakfast", "Linen", "SandyBrown"))
    btn.pack(pady=3, side=TOP)

    # кнопка выбора обеда
    btn = Button(window_main, text="Lunch", bg="Honeydew", fg ="DarkSeaGreen", font=70, width=30, height=1, relief=RAISED, bd=6, command=partial(open_meal, window_main, "Lunch", "Honeydew", "DarkSeaGreen"))
    btn.pack(pady=2, side=TOP)

    # кнопка выбора ужина
    btn = Button(window_main, text="Dinner", bg="AliceBlue", fg ="CornflowerBlue", font=70, width=30, height=1, relief=RAISED, bd=6, command=partial(open_meal, window_main, "Dinner", "AliceBlue", "CornflowerBlue"))
    btn.pack(pady=2, side=TOP)

    # кнопка выбора перекуса
    btn = Button(window_main, text="Snack", bg="MistyRose", fg ="PaleVioletRed", font=70, width=30, height=1, relief=RAISED, bd=6, command=partial(open_meal, window_main, "Snack", "MistyRose", "PaleVioletRed"))
    btn.pack(pady=2, side=TOP)

    diagram() ##вызов диаграммы

    # кнопка сохранения и выхода
    btn = Button(window_main, text="Close", bg="Pink", fg="HotPink4", relief=RAISED, bd=1, command=window_main.destroy)
    btn.pack(side=TOP)

    window_main.mainloop()

# вызов окна с рачсетом нормы ккал и сохранение нормы
ckal_calculator()
