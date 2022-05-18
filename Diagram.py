#диаграмма для сводки
def diagram():
  fig = matplotlib.figure.Figure(figsize=(4,3), facecolor="Lavender")
  ax = fig.add_subplot(111)
  #labels = ['Съедено','Осталось']
#данные для примера
  ax.pie([20,80], colors = ("lightcoral", "yellowgreen"),
         #labels=labels,],
         wedgeprops=dict(width=0.5),
         autopct='%1.1f%%')
  ax.legend(['Съедено: 500 kcal',
             'Осталось: 1200 kcal'])
  circle=matplotlib.patches.Circle((0,0), 0.3, color='lavender')
  ax.add_artist(circle)
  ax.axis('equal')
  canvas = FigureCanvasTkAgg(fig, master=window)
  canvas.get_tk_widget().pack()
  canvas.draw()

#текст внутри диаграммы (grid)
  # title=Label(window,text='''съедено:500ккал
  # осталось:1200ккал''',font=("Courier", 10, "roman"), bg="white" )
  # title.pack()
