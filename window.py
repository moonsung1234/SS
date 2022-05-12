
from tkinter import *

class Window :
    def __init__(self, width, height, setter) :
        self.width = width
        self.height = height
        self.button_list = []
        self.button_index = 0
        self.setter = setter

        self.root = Tk()
        self.root.title("Seat Setter")
        self.root.geometry("{}x{}".format(self.width, self.height))

        self.restart_button = Button(self.root, width=15, height=7, text="restart", bg="skyblue", command=self.__onClickForRestartButton)
        self.restart_button.grid()

    def __onClickForRestartButton(self) :
        self.setter.fix(self.getFixNumber())
        self.setter.set()
        self.set(self.setter.list)

    def __onClick(self, text) :
        for button in self.button_list :
            if button["text"] == text :
                button["bg"] = "red" if button["bg"] == "white" else "white"

                break 

    def set(self, seat_list) :
        if len(self.button_list) != 0 :
            for i in range(len(seat_list)) :
                for j in range(len(seat_list[i])) : 
                    self.button_list[i * len(seat_list[i]) + j]["text"] = seat_list[i][j]
                    self.button_list[i * len(seat_list[i]) + j]["command"] = lambda t=seat_list[i][j] : self.__onClick(t)
        else :
            for i in range(len(seat_list)) :
                for j in range(len(seat_list[i])) :
                    button = Button(self.root, width=12, height=5, text=seat_list[i][j], bg="white", command=lambda t=seat_list[i][j] : self.__onClick(t))
                    button.grid(row=i + 1, column=j + 1)

                    self.button_list.append(button)

    def getFixNumber(self) :
        return_arr = []

        for i in range(len(self.button_list)) :
            if self.button_list[i]["bg"] == "red" :
                return_arr.append([int(self.button_list[i]["text"]), i])

        return return_arr

    def show(self) :
        self.root.mainloop()