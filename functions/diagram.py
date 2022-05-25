def diagram():
        # диаграмма для сводки
        fig = matplotlib.figure.Figure(figsize=(4, 3), facecolor="Lavender")
        ax = fig.add_subplot(111)
        try:
            ax.pie([summ(), ckal.get() - summ()], colors=("lightcoral", "yellowgreen"),
                   wedgeprops=dict(width=0.5),
                   autopct='%1.1f%%')
            ax.legend([f"Eaten:{summ()} kcal",
                       f"Left: {ckal.get() - summ()} kcal"])
            circle = matplotlib.patches.Circle((0, 0), 0.3, color='lavender')
            ax.add_artist(circle)
            ax.axis('equal')
            canvas = FigureCanvasTkAgg(fig, master=window_main)
            canvas.get_tk_widget().pack()
            canvas.draw()
        except ValueError:
            ax.pie([1, 0], colors=("lightcoral", "yellowgreen"),
                   wedgeprops=dict(width=0.5),
                   autopct='%1.1f%%')
            ax.legend([f"Eaten:{summ()} kcal",
                       f"Left: {0} kcal"])
            circle = matplotlib.patches.Circle((0, 0), 0.3, color='lavender')
            ax.add_artist(circle)
            ax.axis('equal')
            canvas = FigureCanvasTkAgg(fig, master=window_main)
            canvas.get_tk_widget().pack()
            canvas.draw()

            messagebox.showwarning('WARNING', f'You overate {int(summ() - ckal.get())} calories!!!')  # предупреждение
