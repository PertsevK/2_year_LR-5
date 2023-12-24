import tkinter
from tkinter import messagebox


class Task1Window(tkinter.Frame):  # MainWindow наслідуючий клас Frame
    """Graphical user interface and the logic of solving the task Begin1"""

    def __init__(self, parent):
        """Initial settings of the user interface"""
        super().__init__(parent)  # виклик конструктора базового класу
        # Розтягнути фрейм за розмірами вікна
        self.pack(fill=tkinter.BOTH, expand=1)
        # Розтягнути сітку 2х3 за розмірами фрейма
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        # Створити об'єкти віджетів (змінні екземпляра)
        self.lb1 = tkinter.Label(self, text="Enter the sequence number of the Fibonacci number:")  # статич. текст
        self.lb3 = tkinter.Label(self, text="")  # статичний текст
        self.lb4 = tkinter.Label(self, text="")  # статичний текст
        self.a_entr = tkinter.Entry(self)  # поле введення для a
        # Командна кнопка (запуск обчислень)
        self.btn1 = tkinter.Button(self, text="Get the number", command=self.Fib)
        self.p_str = tkinter.StringVar()  # змінна tkinter: P в текстовому вигляді
        self.lb2 = tkinter.Label(self, textvariable=self.p_str)  # Текстове поле(P)
        # Розмістити віджети в сітці 2х3
        self.lb1.grid(row=0, column=0, sticky=tkinter.NSEW)
        self.a_entr.grid(row=0, column=1, sticky=tkinter.NSEW)
        self.btn1.grid(row=1, column=0, sticky=tkinter.NSEW)
        self.lb2.grid(row=1, column=1, sticky=tkinter.NSEW)
        self.lb3.grid(row=0, column=2, sticky=tkinter.NSEW)
        self.lb4.grid(row=1, column=2, sticky=tkinter.NSEW)

    def Fib(N):
        """Input-calculation-output according to the task Begin1"""
        # Зчитування з поля введення
        try:
            a = int(N.a_entr.get())  # вважати і перетворити в дійсне
        except ValueError:
            # Вивести вікно з помилкою
            messagebox.showerror("Data ERROR", "The entered data must be a number!")
            N.a_entr.delete(0, tkinter.END)  # очистити поле введення
        else:
            # Перевірити вхідні дані
            if a < 0:  # якщо негативне
                # Змінити на позитивне значення
                a = abs(a)
                N.a_entr.delete(0, tkinter.END)
                N.a_entr.insert(tkinter.END, str(a))
                # Вивести вікно з попередженням
                messagebox.showinfo("Data Warning", "Number has changed to positive")
            # обчислення
            if a == 0: t3 = 0
            elif a == 1 or a == 2: t3 = 1
            else:
                t1 = 1
                t2 = 1
                for i in range(a - 2):
                    t3 = t2 + t1
                    t1 = t2
                    t2 = t3
            # Виведення результату в текстову мітку (за допомогою змінної tkinter)
            N.p_str.set(str(t3))
