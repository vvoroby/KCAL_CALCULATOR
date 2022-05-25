from tkinter import *
from tkinter.ttk import Radiobutton
from tkinter.ttk import Combobox

# Функция для подсчета нормы ккал, исходя из физических нагрузок

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

window=Tk()
window.title('Расчет нормы калорий')
window.geometry("300x350")
window['bg'] = 'lavender'

label = Label(text="Введите свои личные данные", bg="lavender")
label.pack(pady=5)

# Создаем переменные
my_height = IntVar()
my_weight = IntVar()
my_age = IntVar()
my_gender = IntVar()
my_activiti = StringVar()
ckal = IntVar()

# Блок невидимых рамок для красивого интерфейса
f_1 = Frame(window)
f_2 = Frame(window)
f_3 = Frame(window)
f_4 = Frame(window)
f_5 = Frame(window)
f_6 = Frame(window)

# Ввод данных
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
activiti = Combobox(f_5, textvariable=my_activiti, width=48, values=["Физическая нагрузка отсутствует или минимальная",
                      "Тренировки средней тяжести 2-3 раза в неделю",
                      "Тренировки средней тяжести 4-5 раз в неделю",
                      "Тренировки каждый день",
                      "Ежедневная физическая нагрузка + физическая работа"])

ckal_label1 = Label(f_6, text="Ваша норма: ", bg="lavender")
ckal_label2 = Label(f_6, textvariable=ckal, bg="lavender")

message_button = Button(text="Узнать", bg="pink", command=calculeter)

# Упорядочивание элементов окна
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

window.mainloop()
