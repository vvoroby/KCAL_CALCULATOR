import matplotlib.figure
import matplotlib.patches
import sqlite3
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Radiobutton
from tkinter.ttk import Combobox
from datetime import date

global ckal
# Окно при запуске приложения и вычислении его нормы ккал
def ckal_calculator():
    global ckal
    # функция для подсчета нормы ккал, исходя из физических нагрузок
    def calculeter():
        if my_activiti.get() == "Физическая нагрузка отсутствует или минимальная":
            ckal.set(int((my_height.get() * 6.25 + my_weight.get() * 10 - my_age.get() * 5 + my_gender.get()) * 1.2))
        elif my_activiti.get() == "Тренировки средней тяжести 2-3 раза в неделю":
            ckal.set(int((my_height.get() * 6.25 + my_weight.get() * 10 - my_age.get() * 5 + my_gender.get()) * 1.38))
        elif my_activiti.get() == "Тренировки средней тяжести 4-5 раз в неделю":
            ckal.set(int((my_height.get() * 6.25 + my_weight.get() * 10 - my_age.get() * 5 + my_gender.get()) * 1.46))
        elif my_activiti.get() == "Тренировки каждый день":
            ckal.set(int((my_height.get() * 6.25 + my_weight.get() * 10 - my_age.get() * 5 + my_gender.get()) * 1.64))
        elif my_activiti.get() == "Ежедневная физическая нагрузка + физическая работа":
            ckal.set(int((my_height.get() * 6.25 + my_weight.get() * 10 - my_age.get() * 5 + my_gender.get()) * 1.9))

            # окошко расчёта калорий

    window = Tk()
    window.title('Расчет нормы калорий')
    window.geometry("300x350")
    window['bg'] = 'lavender'

    label = Label(text="Введите свои личные данные", bg="lavender")
    label.pack(pady=5)

    # создаем переменные
    my_height = IntVar()
    my_weight = IntVar()
    my_age = IntVar()
    my_gender = IntVar()
    my_activiti = StringVar()
    ckal = IntVar()

    # блок невидимых рамок для красивого интерфейса
    f_1 = Frame(window)
    f_2 = Frame(window)
    f_3 = Frame(window)
    f_4 = Frame(window)
    f_5 = Frame(window)
    f_6 = Frame(window)

    # ввод данных
    height_label = Label(f_1, text="Рост ", bg="lavender")
    height_entry = Entry(f_1, width=8, textvariable=my_height)
    height2_label = Label(f_1, text="см ", bg="lavender")

    weight_label = Label(f_2, text="Вес ", bg="lavender")
    weight_entry = Entry(f_2, width=8, textvariable=my_weight)
    weight2_label = Label(f_2, text="кг ", bg="lavender")

    age_label = Label(f_3, text="Возраст ", bg="lavender")
    age_entry = Entry(f_3, width=8, textvariable=my_age)

    gender_label = Label(f_4, text="Пол ", bg="lavender")
    rad1 = Radiobutton(f_4, text='М', value=4, variable=my_gender)
    rad2 = Radiobutton(f_4, text='Ж', value=-161, variable=my_gender)

    activiti_label = Label(f_5, text="Активность ", bg="lavender")
    activiti = Combobox(f_5, textvariable=my_activiti, width=48,
                        values=["Физическая нагрузка отсутствует или минимальная",
                                "Тренировки средней тяжести 2-3 раза в неделю",
                                "Тренировки средней тяжести 4-5 раз в неделю",
                                "Тренировки каждый день",
                                "Ежедневная физическая нагрузка + физическая работа"])

    # вывод данных
    ckal_label1 = Label(f_6, text="Ваша норма: ", bg="lavender")
    ckal_label2 = Label(f_6, textvariable=ckal, bg="lavender")
    ckal_label3 = Label(f_6, text="ккал ", bg="lavender")

    message_button = Button(text="Узнать", bg="pink", command=calculeter)

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

    btn = Button(window, text="Сохранить", bg="pink", command=window.destroy)
    btn.pack(pady=30, side=TOP)

    window.mainloop()

    return ckal

# Функция для поиска нынешней даты
def find_today():
    return date.today().strftime("%d.%m.%Y")

# Таблица при нажатии на кнопку архив
def archive():
    window = Tk()
    window.title("Завтрак")
    window.geometry('350x620')
    window['bg'] = 'Lavender'

    title = Label(window, text="Архив", bg="Lavender", fg="purple4", font=70, width=30)
    title.pack(pady=5)

    my_date = StringVar()

    frame = Frame(window)
    date_label = Label(frame, text="Дата ", bg="lavender")
    date_entry = Entry(frame, width=8, textvariable=my_date)
    date_label.pack(side=LEFT)
    date_entry.pack(side=RIGHT)
    frame.pack(pady=5)

    message_button = Button(window, text="Узнать", bg="pink"  ##, command=calculeter)
                            )
    message_button.pack(pady=15)

    # Таьлица
    main_frame = Frame(window)
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
    my_frame.heading("player_eating", text="Прием пищи", anchor=CENTER)
    my_frame.heading("player_product", text="Продукт", anchor=CENTER)
    my_frame.heading("player_mass", text="Масса", anchor=CENTER)
    my_frame.heading("player_kkal", text="Ккал", anchor=CENTER)
    my_frame.heading("player_p", text="Белки", anchor=CENTER)
    my_frame.heading("player_f", text="Жиры", anchor=CENTER)
    my_frame.heading("player_c", text="Углеводы", anchor=CENTER)

    # кнопка СОХРАНЕНИЯ и выхода
    btn = Button(window, text="Закрыть", bg="pink", relief=RAISED, bd=1, command=window.destroy)
    btn.pack(side=TOP, pady=60)

    window.mainloop()

# таблица при нажатии на кнопку завтрак
def breakfast():
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

    # добавление данных (визуальный пример)
    my_frame.insert(parent='', index='end', text='',
                    values=('1', 'Молоко', '100', '43', '2,8', '1', '4,6'))
    my_frame.insert(parent='', index='end', text='',
                    values=('2', 'Хлеб', '100', '156', '3,5', '6,7', '6,2'))
    my_frame.pack()

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

    # блок функций

    # Кнопки
    select_button = Button(window, text="Добавить")
                           ##command=partial(add_product, my_product.get(), my_mass.get(), my_frame, new_product_entry, new_mass_entry, 'breakfast'))
    select_button.pack(pady=5)

    delete_button = Button(window, text="Удалить")
                            ##command=partial(delete_product, my_frame))
    delete_button.pack(pady=5)

    btn = Button(window, text="Закрыть", bg="pink", relief=RAISED, bd=1, command=window.destroy)
    btn.pack(side=TOP, pady=40)

    window.mainloop()


# таблица при нажатии на кнопку обед
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

    # блок функций

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

    # кнопки
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


# таблица при нажатии на кнопку ужин
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

    # блок функций

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

    # кнопки
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


# таблица при нажатии на кнопку перекус
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

    # блок функций

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

    # кнопки
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


# вызов окна с рачсетом нормы ккал и сохранение нормы
ckal = ckal_calculator()

window = Tk()

# иконка приложения
# photo = PhotoImage(file='58431506a9a7d158c60a2227.png')
# window.iconphoto(False, photo)

window.title("Приложение :'Подсчёт калорий'")
window.geometry('350x620')
window['bg'] = 'Lavender'

hat = Frame(window)
hat['bg'] = 'lavender'

title = Label(hat, text=find_today(), bg = 'lavender', fg="purple4", font=70, width=20)
title.pack(pady=3, side=LEFT)

btn = Button(hat, text ='Архив', bg="pink", fg ="HotPink4", relief=RAISED, bd = 6, width=12, command=archive)
btn.pack(pady=3, side=RIGHT)

hat.pack()

# кнопка выбора завтрака
btn = Button(window, text ='Завтрак', bg="Linen", fg ='SandyBrown', font=90, width=30, height=1, relief=RAISED, bd=6, command = breakfast)
btn.pack(pady=3, side=TOP)

# кнопка выбора обеда
btn = Button(window, text="Обед", bg="Honeydew", fg ="DarkSeaGreen", font=70, width=30, height=1, relief=RAISED, bd=6, command = lunch)
btn.pack(pady=2, side=TOP)

# кнопка выбора ужина
btn = Button(window, text="Ужин", bg="AliceBlue", fg ="CornflowerBlue", font=70, width=30, height=1, relief=RAISED, bd=6, command = dinner)
btn.pack(pady=2, side=TOP)

# кнопка выбора перекуса
btn = Button(window, text="Перекус", bg="MistyRose", fg ="PaleVioletRed", font=70, width=30, height=1, relief=RAISED, bd=6, command = snack)
btn.pack(pady=2, side=TOP)

#диаграмма для сводки
fig = matplotlib.figure.Figure(figsize=(4,3), facecolor="Lavender")
ax = fig.add_subplot(111)
#labels = ['Съедено','Осталось']
#данные для примера
ax.pie([20,80], colors = ("lightcoral", "yellowgreen"),
       #labels=labels,
       wedgeprops=dict(width=0.5),
       autopct='%1.1f%%')
ax.legend(['Съедено: kcal',
          f"Осталось: {ckal.get()} kcal"])
circle=matplotlib.patches.Circle((0,0), 0.3, color='lavender')
ax.add_artist(circle)
ax.axis('equal')
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().pack()
canvas.draw()

#текст внутри диаграммы (grid)
# title=Label(window,text='''съедено:500ккал
# осталось:1200ккал''',font=("Courier", 10, "roman"), bg="white" )
# title.pack()

# кнопка СОХРАНЕНИЯ и выхода
btn = Button(window, text="Закрыть", bg="Pink", fg="HotPink4", relief=RAISED, bd = 1, command=window.destroy)
btn.pack(side=TOP)

window.mainloop()
