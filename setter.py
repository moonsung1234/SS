
import random

class Setter :
    def __init__(self, row, column, number) :
        self.row = row
        self.column = column
        self.number = number
        self.list = []
        self.fix_number_list = []

    def fix(self, number_list) :
        self.fix_number_list = number_list

    def set(self) :
        self.list = [i for i in range(1, self.number + 1)]
        return_array = []

        random.shuffle(self.list)
        
        if len(self.fix_number_list) != 0 :
            for info in self.fix_number_list :
                index = self.list.index(info[0])
                temp = self.list[info[1]]
                self.list[info[1]] = info[0]
                self.list[index] = temp

        for i in range(self.row) :
            temp_list = []

            for j in range(self.column) :
                temp_list.append(self.list[i * self.column + j])

            return_array.append(temp_list)

        self.list = return_array

        return self.list



