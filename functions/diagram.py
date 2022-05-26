 """ 
 Диаграмма для сводки, отображает отношение дневной нормы ккал пользователя и уже съеденных ккал в этот день
 """
    def diagram():
        # создание диаграммы
        fig = matplotlib.figure.Figure(figsize=(4, 3), facecolor="Lavender")
        ax = fig.add_subplot(111)
        try:
            ax.pie([summ(), ckal.get() - summ()], 
                   colors=("lightcoral", "yellowgreen"),
                   wedgeprops=dict(width=0.5),
                   autopct='%1.1f%%')## данные диаграммы 
            ax.legend([f"Eaten:{summ()} kcal",
                       f"Left: {ckal.get() - summ()} kcal"]) ## легенда диаграммы
            circle = matplotlib.patches.Circle((0, 0), 0.3, color='lavender')
            ax.add_artist(circle)
            ax.axis('equal')
            canvas = FigureCanvasTkAgg(fig, master=window_main)
            canvas.get_tk_widget().pack()
            canvas.draw()
        except ValueError:
            #  вывод ошибки, если съеденных ккал больше нормы
            ax.pie([1, 0], 
                   colors=("lightcoral", "yellowgreen"),
                   wedgeprops=dict(width=0.5),
                   autopct='%1.1f%%') ## данные диаграммы (диаграмма будет заполнена)
            ax.legend([f"Eaten:{summ()} kcal",
                       f"Left: {0} kcal"]) ## легенда диаграммы
            circle = matplotlib.patches.Circle((0, 0), 0.3, color='lavender')
            ax.add_artist(circle)
            ax.axis('equal')
            canvas = FigureCanvasTkAgg(fig, master=window_main)
            canvas.get_tk_widget().pack()
            canvas.draw()

            messagebox.showwarning('WARNING', f'You overate {int(summ() - ckal.get())} calories!!!')  ## предупреждение
