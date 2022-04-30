from tkinter import *

window = Tk()

#иконка приложения
# photo = PhotoImage(file='58431506a9a7d158c60a2227.png')
# window.iconphoto(False, photo)

window.title("Приложение :'Подсчёт калорий'")
window.geometry('350x620')
window['bg'] = 'lavender'

#здесь должен быть календарь и выбор даты
title = Label(window, text="Сегодня", bg = "lavender", fg ="indigo", font=70, width=30)
title.grid(column=0, row=0)

title=Label(window, bg = "lavender", font=70, width=30)
title.grid(column=0, row=1)

# кнопка выбора завтрака
btn = Button(window,text = 'Завтрак', bg="Linen", fg = "SandyBrown", font=90, width=30, height = 1, relief=RAISED, bd=6, command = breakfest)
btn.grid(column=0, row=2)

# кнопка выбоа обеда
btn = Button(window,text="Обед", bg="Honeydew", fg ="DarkSeaGreen",font=70,width=30,height = 1,relief=RAISED,bd=6)
btn.grid(column=0, row=3)

# кнопка выбора ужина
btn = Button(window,text="Ужин", bg="AliceBlue",fg ="CornflowerBlue",font=70,width=30,height = 1,relief=RAISED,bd=6)
btn.grid(column=0, row=4)

# кнопка выбора перекуса
btn = Button(window,text="Перекус",bg="MistyRose",fg ="PaleVioletRed",font=70,width=30,height = 1,relief=RAISED,bd=6)
btn.grid(column=0, row=5)

title=Label(window, bg = "lavender",font=70,width=30 )
title.grid(column=0, row=6)

# # вода
# title=Label(window, text="Вода",bg="lightcyan",fg ="indigo",font=70,width=30 )
# title.grid(column=0, row=8)
# btn = Button(window,text = '+', bg="pink",font=20,width=4,height = 1,
#             relief=RAISED,
#             bd=6)
# btn.grid(column=1, row=8)

# сводка (добавить виджеты)
title=Label(window, text="СВОДКА",bg="white",fg ="indigo",font=70,width=30,
            height=10,anchor = 'n')
title.grid(column=0, row=7)

title=Label(window, bg = "lavender",font=70,width=30 )
title.grid(column=0, row=8)

# кнопка СОХРАНЕНИЯ и выхода
btn = Button(window, text="Закрыть окно", bg="pink",
            relief=RAISED,
            bd = 6,
            command=window.quit)
btn.grid(column=0, row=9)

window.mainloop()
