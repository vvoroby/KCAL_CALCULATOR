from tkinter import *

window = Tk()
#иконка приложения
# photo = PhotoImage(file='58431506a9a7d158c60a2227.png')
# window.iconphoto(False, photo)

window.title("Приложение :'Подсчёт калорий'")
window.geometry('400x620')
window['bg'] = 'lavender'

# завтрак
title=Label(window, text="Завтрак",bg="khaki",fg ="indigo", font=70, width=30)
title.grid(column=0, row=0)

btn = Button(window,text = '+', bg="pink",font=20,width=4,height = 1,
            relief=RAISED,
            bd=6)
btn.grid(column=1, row=0)

# обед
title=Label(window, text="Обед",bg="wheat",fg ="indigo",font=70,width=30 )
title.grid(column=0, row=2)
btn = Button(window,text = '+', bg="pink",font=20,width=4,height = 1,
            relief=RAISED,
            bd=6)
btn.grid(column=1, row=2)

# ужин
title=Label(window, text="Ужин",bg="cornsilk",fg ="indigo",font=70,width=30 )
title.grid(column=0, row=4)
btn = Button(window,text = '+', bg="pink",font=20,width=4,height = 1,
            relief=RAISED,
            bd=6)
btn.grid(column=1, row=4)

# перекус
title=Label(window, text="Перекус",bg="whitesmoke",fg ="indigo",font=70,width=30 )
title.grid(column=0, row=6)
btn = Button(window,text = '+', bg="pink",font=20,width=4,height = 1,
            relief=RAISED,
            bd=6)
btn.grid(column=1, row=6)

# вода
title=Label(window, text="Вода",bg="lightcyan",fg ="indigo",font=70,width=30 )
title.grid(column=0, row=8)
btn = Button(window,text = '+', bg="pink",font=20,width=4,height = 1,
            relief=RAISED,
            bd=6)
btn.grid(column=1, row=8)

# сводка (добавить виджеты)
title=Label(window, text="СВОДКА",bg="thistle",fg ="indigo",font=70,width=30,
            height=10,anchor = 'n')
title.grid(column=0, row=10)

# кнопка выхода
btn = Button(window, text="Закрыть окно", bg="red",font=20,width=12,height = 1,
            relief=RAISED,
            bd = 6,
            command=window.quit)
btn.grid()

window.mainloop()
