
from tkinter import *
from tkinter import simpledialog
from tkinter import filedialog
import tkinter.font as font

class Window :
    def __init__(self, width, height, setter) :
        self.width = width
        self.height = height
        self.button_list = {}
        self.button_index = 0
        self.setter = setter

        self.root = Tk()
        self.root.title("Seat Setter")
        self.root.geometry("{}x{}".format(self.width, self.height))
        self.root.resizable(width=FALSE, height=FALSE)

        self.menubar = Menu(self.root)

        self.file_menu = Menu(self.menubar)
        self.file_menu.add_command(label="save", command=self.__onClickForSaveMenu)
        self.file_menu.add_command(label="load", command=self.__onClickForLoadMenu)
        
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        self.root.config(menu=self.menubar)

        self.restart_button = Button(self.root, width=15, height=7, text="restart", bg="skyblue", command=self.__onClickForRestartButton)
        self.restart_button.grid()

    def __onClickForSaveMenu(self) :
        path = filedialog.askdirectory(title="save")

        if len(path) == 0 :
            return

        file = open(path + "/{}".format("save.ss"), "w")

        print(self.setter.list)

        file.write(str(self.setter.list))

    def __onClickForLoadMenu(self) :
        path = filedialog.askopenfilename(initialdir="/", title="load")
        file = open(path, "r")
        number_list = ""

        while True :
            line = file.readline()

            if not line :
                break

            number_list += line

        print(number_list)

    def __onClickForRestartButton(self) :
        self.setter.fix(self.getFixNumber())
        self.setter.set()
        self.set(self.setter.list)

    def __onClickForNumberButton(self, key) :
        self.button_list[key]["bg"] = "red" if self.button_list[key]["bg"] == "white" else "white"
        
    def __onClickForInitButton(self, key) :
        index = 0

        for _key in self.button_list :
            if self.button_list[_key]["text"] == "클릭하여 번호 변경" :
                self.button_list[key]["text"] = simpledialog.askstring(title="Input", prompt="번호를 입력해주세요.")

                break

            elif index == len(self.button_list) - 1 :
                self.__onClickForNumberButton(key)

                break

            index += 1

    def init(self) :
        for i in range(self.setter.row) :
            for j in range(self.setter.column) : 
                button = Button(
                    self.root, 
                    width=int(self.width / 10 / self.setter.column), 
                    height=int(self.height / 15 / self.setter.row), 
                    text="클릭하여 번호 변경",
                    bg="white",
                    command=lambda key="{}{}".format(i, j) : self.__onClickForInitButton(key)
                )
                button.grid(row=i, column=j + 1)

                self.button_list["{}{}".format(i, j)] = button

    def set(self, seat_list) :
        if len(self.button_list) != 0 :
            for i in range(len(seat_list)) :
                for j in range(len(seat_list[i])) :
                    self.button_list["{}{}".format(i, j)]["text"] = seat_list[i][j]                 
                    self.button_list["{}{}".format(i, j)]["command"] = lambda key="{}{}".format(i, j) : self.__onClickForNumberButton(key)
        # else :
        #     for i in range(len(seat_list)) :
        #         for j in range(len(seat_list[i])) :
        #             button = Button(self.root, width=12, height=5, text=seat_list[i][j], bg="white", command=lambda t=seat_list[i][j] : self.__onClick(t))
        #             button.grid(row=i + 1, column=j + 1)

        #             self.button_list.append(button)

    def getFixNumber(self) :
        return_arr = []
        index = 0

        for key in self.button_list :
            if self.button_list[key]["bg"] == "red" :
                return_arr.append([int(self.button_list[key]["text"]), index])
                
            index += 1

        return return_arr

    def show(self) :
        self.root.mainloop()