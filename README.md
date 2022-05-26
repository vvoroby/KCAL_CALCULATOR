# Kcal Calculator
## Вступление ##

Мы разработали программу, при помощи которой вы сможете:
* узнать вашу дневную норму Ккал
* конролировать свое питание в течение дня, занося съеденные продукты в ваш личный пищевой дневник
* контролировать количество употребленных Ккал по отношению к вашей дневной норме
* узнавать сколько Ккал, белков, жиров, углеводов содержиться в продуктах (которые хранятся в нашей базе данных)
* добавлять свои продукты или блюда в базу данных, чтобы в дальнейшем вносить их в ваш пищевой дневник
* просматривать записи в вашем пищевом дневнике за предыдущие дни

Для того чтобы начать работу с программой скайчайте все файлы из папки MAIN и запустите код.
***
## Использованные модули ##
* matplotlib
* sqlite3
* tkinter
* datetime
* functools

***
## База данных ##
В нашей базе данных находится 100 различных записей с наименованием продуктов, их калорийностью, содержанием белков, жиров, углеводов на 100 грамм.

ВАЖНО! Для того чтобы просмотреть базу данных (список продуктов и их КБЖУ, архив) необходимо установить программу, которая работает с расширенрием .db 
>[база данных](https://github.com/vvoroby/project-2-semester/blob/main/database/n_base.db?raw=true)

Вы можете самостоятельно добавить продукт в базу данных с помощью функции: 
>[функция добавления нового прдукта в БД](https://github.com/vvoroby/project-2-semester/blob/main/functions/insert_new_product.py)

***
## Калькулятор ##
Функция калькулятор рассчивает дневную норму калорий для человека по его росту, весу, возрасту, полу и уровню физической активности.
Для рассчета используется формула: (ВЕС*10+РОСТ*6,25+ВОЗРАСТ*5-161(+5))*КОЭФ.АКТИВНОСТИ

>[калькулятор](https://github.com/vvoroby/project-2-semester/blob/main/functions/kcal_calculator.py)

![image](https://user-images.githubusercontent.com/99788525/170520179-7ab74055-8bc4-47bc-94da-ced4a266a930.png)![image](https://user-images.githubusercontent.com/99788525/170520805-d49bb12f-8d81-4b5c-93eb-c06d5165f3c4.png)

***
## Интерфейс ##
У нас есть главное окошко с кнопками, которые открывают новые окна с таблицами для завтрака, обеда, ужина, перекуса. Кроме того, сверху главного окна отображается актуальная дата и имеются кнопки, открывающие архив и окно "калькулятор".
В нижней части окна находится диаграмма, которая отображает процент употребленных калорий от общей нормы человека.

![image](https://user-images.githubusercontent.com/99788525/170520918-6804f425-9d24-45d7-ae93-8d03a0f1e39d.png)

***
## Окна приёмов пищи ##
В каждом окне находится таблица, в которую пользователь может ввести название продукта и его массу. Если такой продукт имеется в базе данных, то для его массы подсчитывается КБЖУ (количество Ккал, белков, жиров, углеводов) и заносится в таблицу, а также в архив(при занесении в архив фиксируется название приема пищи и дата). Если же такого продукта в базе данных нет, то появляется окошко, которое предлагает пользователю ввести новый(собственный) продукт или блюдо в базу данных.

Функция для окошек приёмов пищи:
>[окна](https://github.com/vvoroby/project-2-semester/blob/main/functions/windows.py)

Функция для добавления нового продукта в базу данных:
>[ввод нового продукта](https://github.com/vvoroby/project-2-semester/blob/main/functions/insert_new_product.py)

Кроме того, запись о продукте можно удалить из таблицы, она автоматически удалится из архива.

## Архив ##
В окно архива можно ввести дату, в таблице отобразятся все приёмы пищи за тот день, продукты и их КБЖУ.

>[функция архива](https://github.com/vvoroby/project-2-semester/blob/main/functions/archive.py)

ВАЖНО! Для того чтобы просмотреть базу данных (список продуктов и их КБЖУ, архив) необходимо установить программу, которая работает с расширенрием .db 
>[архив](https://github.com/vvoroby/project-2-semester/blob/main/database/archive.db?raw=true)

***
## Диаграмма ##
Диаграмма отображает сколько калорий от своей дневной нормы пользователь уже употребил и сколько осталось. Программа выводит предупреждение, если количество съеденных калорий превысило норму.

>[диаграмма](https://github.com/vvoroby/project-2-semester/blob/main/functions/diagram.py)

***
## Ошибки ##
При неправильном вводе пользователь будет получать предупреждение об ошибке.

![image](https://user-images.githubusercontent.com/99788525/170520596-e2f197b9-00ff-49c0-844a-03a955bbb0ff.png) ![image](https://user-images.githubusercontent.com/99788525/170520674-9cc1475f-d53f-4f02-92db-dc805fe2e0fd.png)![image](https://user-images.githubusercontent.com/99788525/170520978-aa4b63df-cfa1-40c5-a17f-7f3e75e5f785.png)


***
## Завершение ##
>Мы будем рады вашим замечаниям и пожеланиям!
