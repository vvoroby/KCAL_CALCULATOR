"""
Окно с приемом пищи. 
Функция принимает переменные: название приема пищи, задний фон и цвет текста, в итоге получаются окна с одинаковым интерфейсом и разным дизаином
"""
def windows(meal, bg_color, fg_color): 
    """
    Калькулятор расчета кбжу по массе, введеной пользователем
    """
    def calculation(selected_products):
        calculated_selected_product = []
        # цикл просчитывает массу, ккал, белки, жиры, углеводы для введенной массы
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
        connect = sqlite3.connect('n_base.db') ## делаем запрос к базе данных
        cursor = connect.cursor()
        cursor.execute('''SELECT * FROM n_base WHERE name = ?''', [new_product_entry.get().title()]) ## получаем нужный продукт из БД
        try:
            calculated_selected_product = calculation(cursor.fetchone())
            connect.close()

            # записываем значение в таблицу
            my_frame.insert(parent='', index='end', values=calculated_selected_product)
            my_frame.pack()

            # очищает окно ввода
            new_product_entry.delete(0, END)  
            new_mass_entry.delete(0, END)

            add_product_to_base(calculated_selected_product)

        except:
            res = messagebox.askquestion('ERROR!', 'Data entered incorrectly. Do you want to add your product to the database?') ## ввывод ошибки и вопроса, если продукта нет в базе данных
            if res == 'yes':
                open_insert_new_product(window_meal,meal,bg_color,fg_color)

    """
    Функция добавляет продукт в БД архива
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
                       tuple(added_calculated_selected_product)) ## добавление продукта в архив
        connect.commit()
        connect.close()
 
    """
    Функция удаляет продукт из таблицы, при помощи курсора
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
    Функция удаляет продукт из БД архива
    """
    def delete_product_from_base(deleted_selected_product):
        connect = sqlite3.connect('archive.db') ## создаём соединения с архивом
        cursor = connect.cursor()
        cursor.execute("DELETE FROM archive WHERE name = ? AND g = ?",
                       [deleted_selected_product[0], deleted_selected_product[1]]) ## удаляем продукт из архива
        connect.commit()
        connect.close()

    # интерфейс окна с приемом пищи
    window_meal = Tk()
    window_meal.title(meal)
    window_meal.geometry('350x620')
    window_meal['bg'] = bg_color
    photo = PhotoImage(file='58431506a9a7d158c60a2227.png')
    window_meal.iconphoto(False, photo)

    # заголовок таблицы
    title = Label(window_meal, text=meal, bg=bg_color, fg=fg_color, font=70, width=30)
    title.pack()

    main_frame = Frame(window_meal)
    main_frame.pack()

    # бегунок внутри таблицы
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

    # добавляем продукты в таблицу, добавленные ранее в этот день
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
