""" 
Окно архива
"""
def archive():
    """
    Находит и добавляет в таблицу продукты из базы данных архива, завписанные в день, введенный пользователем
    """
    def find_product_from_day():
        my_frame.delete(*my_frame.get_children()) ## очищает таблицу

        connect = sqlite3.connect('archive.db')  ## делаем запрос к архиву
        cursor = connect.cursor()
        # выбираем нужные нам продукты по дате и передаём в переменную
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
    # интерфейс окна архива
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
    date_entry = Entry(frame, width=10, textvariable=my_date)## окно ввода
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

    # бегунок вутри таблицы
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
