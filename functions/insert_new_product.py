# добавляет новый продукт в бд
def insert_new_product():
    # добавляет прокудк в бд
    def insert_product_in_db():
        connect = sqlite3.connect('n_base.db')
        cursor = connect.cursor()
        cursor.execute('''INSERT INTO n_base VALUES (?,?,?,?,?,?)''', (insert_product.get(), insert_mass.get(), insert_kkal.get(), insert_p.get(), insert_f.get(), insert_c.get()))
        connect.commit()
        connect.close()

    window_insert = Tk()
    window_insert.title('New product') 
    window_insert.geometry('750x280')
    window_insert['bg'] = 'lavender'

    title = Label(window_insert, text="Enter your product and its kpfc (for 100 g of product.)", bg="lavender", fg="purple4")
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
    Label2 = Label(low_frame, text="Mass").grid(row=0, column=1) ## рекоммендуется вводить 100 грамм
    Label3 = Label(low_frame, text="Kcal").grid(row=0, column=2)
    Label4 = Label(low_frame, text="Proteins").grid(row=0, column=3)
    Label5 = Label(low_frame, text="Fats").grid(row=0, column=4)
    Label6 = Label(low_frame, text="Carbohydrates").grid(row=0, column=5)

    Entry1 = Entry(low_frame, textvariable=insert_product).grid(row=1, column=0)
    Entry2 = Entry(low_frame, textvariable=insert_mass).grid(row=1, column=1)
    Entry3 = Entry(low_frame, textvariable=insert_kkal).grid(row=1, column=2)
    Entry4 = Entry(low_frame, textvariable=insert_p).grid(row=1, column=3)
    Entry5 = Entry(low_frame, textvariable=insert_f).grid(row=1, column=4)
    Entry6 = Entry(low_frame, textvariable=insert_c).grid(row=1, column=5)

    # Кнопки
    select_button = Button(window_insert, text="Add", command=insert_product_in_db)
    select_button.pack(pady=5)

    btn = Button(window_insert, text="Close", bg="pink", fg="HotPink4", relief=RAISED, bd=1, command=window_insert.destroy)
    btn.pack(side=TOP, pady=40)

    window_insert.mainloop()

insert_new_product()
