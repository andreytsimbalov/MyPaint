'''
Paint, написанный на python
'''


from tkinter import *
import setUI as s

class Paint(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        s.setUI(self)
        self.brush_size = 10
        self.brush_color = "black"

    def draw(self, event):
        self.canv.create_oval(event.x - self.brush_size,
                              event.y - self.brush_size,
                              event.x + self.brush_size,
                              event.y + self.brush_size,
                              fill=self.brush_color, outline=self.brush_color)

    def set_color(self, new_color): # изменение цвета кисти
        self.brush_color = new_color

    def set_brush_size(self, new_size): # изменение размера кисти
        self.brush_size = new_size



def main():
    print('start proj')
    root = Tk()
    root.geometry("640x480+100+100")
    app = Paint(root)
    print(2+2)
    app.mainloop()


if __name__ == "__main__":
    main()