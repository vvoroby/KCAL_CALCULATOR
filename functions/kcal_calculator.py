from tkinter import *
from tkinter.ttk import Radiobutton
from tkinter.ttk import Combobox

"""
Окно для рассчета дневной нормы ккал пользователя (запускается первым при старте программы)
"""
def ckal_calculator():
    global ckal
    """
    Функция для рассчета дневной нормы ккал, исходя из данных, введеннных пользователем
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

    # интерфейс окна для рассчета дневной нормы ккал
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

    #кнопка "сохранить"
    btn = Button(window_calculetor, text="Save", bg="pink", command=partial(open_main, window_calculetor))
    btn.pack(pady=30, side=TOP)

    window_calculetor.mainloop()

    return ckal
