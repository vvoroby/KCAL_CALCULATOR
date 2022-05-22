from datetime import date
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Radiobutton
from tkinter.ttk import Combobox

def archive():
    def find_product_from_day():
        my_frame.delete(*my_frame.get_children()) ##очищает таблицу

        connect = sqlite3.connect('archive.db')  ##делаем запрос к базе данных
        cursor = connect.cursor()
        cursor.execute('''SELECT meal,name,g,kkal,p,f,c  FROM archive WHERE date = ?''', [my_date.get()])
        all_products = cursor.fetchall()
        connect.close()
        print(all_products)
        for item in all_products:
            my_frame.insert(parent='', index='end', values=item)
            my_frame.pack()

    window = Tk()
    window.title("Archive")
    window.geometry('350x620')
    window['bg'] = 'Lavender'

    title = Label(window, text="Archive", bg="Lavender", fg="purple4", font=70, width=30)
    title.pack(pady=5)

    my_date = StringVar()

    frame = Frame(window)
    date_label = Label(frame, text="Дата ", bg="lavender")
    date_entry = Entry(frame, width=10, textvariable=my_date)
    date_label.pack(side=LEFT)
    date_entry.pack(side=RIGHT)
    frame.pack(pady=5)

    message_button = Button(window, text="Узнать", bg="pink", command=find_product_from_day)
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
