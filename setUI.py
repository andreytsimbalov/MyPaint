from tkinter import *

def setUI(self):
    self.parent.title("Paint on python")  # Устанавливаем название окна
    self.pack(fill=BOTH, expand=1)  # Размещаем активные элементы на родительском окне

    self.columnconfigure(6,
                         weight=1)  # Даем седьмому столбцу возможность растягиваться, благодаря чему кнопки не будут разъезжаться при ресайзе
    self.rowconfigure(2, weight=1)  # То же самое для третьего ряда

    self.canv = Canvas(self, bg="white")  # Создаем поле для рисования, устанавливаем белый фон
    self.canv.grid(row=2, column=0, columnspan=7,
                   padx=5, pady=5,
                   sticky=E + W + S + N)  # Прикрепляем канвас методом grid. Он будет находится в 3м ряду, первой колонке, и будет занимать 7 колонок, задаем отступы по X и Y в 5 пикселей, и заставляем растягиваться при растягивании всего окна



    self.canv.bind("<B1-Motion>", self.draw)



    color_lab = Label(self, text="Цвет: ")  # Создаем метку для кнопок изменения цвета кисти
    color_lab.grid(row=0, column=0,
                   padx=6)  # Устанавливаем созданную метку в первый ряд и первую колонку, задаем горизонтальный отступ в 6 пикселей

    red_btn = Button(self, text="Красный", width=10, command=lambda: self.set_color("red"))
    red_btn.grid(row=0, column=1)

    # Создание остальных кнопок повторяет ту же логику, что и создание
    # кнопки установки красного цвета, отличаются лишь аргументы.

    green_btn = Button(self, text="Зеле123ный", width=10, command=lambda: self.set_color("green"))
    green_btn.grid(row=0, column=2)

    blue_btn = Button(self, text="Сини33й", width=10, command=lambda: self.set_color("blue"))
    blue_btn.grid(row=0, column=3)

    black_btn = Button(self, text="Черный", width=10, command=lambda: self.set_color("black"))
    black_btn.grid(row=0, column=4)

    white_btn = Button(self, text="Белый", width=10, command=lambda: self.set_color("white"))
    white_btn.grid(row=0, column=5)

    clear_btn = Button(self, text="Clear all", width=10, command=lambda: self.canv.delete("all"))
    clear_btn.grid(row=0, column=6, sticky=W)

    size_lab = Label(self, text="Размер кисти: ")  # Создаем метку для кнопок изменения размера кисти
    size_lab.grid(row=1, column=0, padx=5)

    one_btn = Button(self, text="2", width=10, command=lambda: self.set_brush_size(2))
    one_btn.grid(row=1, column=1)

    two_btn = Button(self, text="5", width=10, command=lambda: self.set_brush_size(5))
    two_btn.grid(row=1, column=2)

    five_btn = Button(self, text="7", width=10, command=lambda: self.set_brush_size(7))
    five_btn.grid(row=1, column=3)

    seven_btn = Button(self, text="10", width=10, command=lambda: self.set_brush_size(10))
    seven_btn.grid(row=1, column=4)

    ten_btn = Button(self, text="12", width=10, command=lambda: self.set_brush_size(12))
    ten_btn.grid(row=1, column=5)

    twenty_btn = Button(self, text="15", width=10, command=lambda: self.set_brush_size(15))
    twenty_btn.grid(row=1, column=6, sticky=W)