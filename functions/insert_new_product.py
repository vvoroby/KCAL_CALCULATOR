"""
Окно для добавления нового продукта в БД
"""
def insert_new_product(meal, bg_color, fg_color):
    """ 
    Добавляет продукт пользователя в БД
    """
    def insert_product_in_db():
        connect = sqlite3.connect('n_base.db') ## создаём соединение с БД, где хранися список всех продуктов
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
    # интерфейс окна для добавления продукта
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
insert_new_product()
