class Cell():
    def __init__(self, x, y, value = 0):
        self.x = x 
        self.y = y
        self.value = value 
        self.canidates = []
        self.box = self.get_box

    def get_box(self):
        """
        1 2 3
        4 5 6
        7 8 9
        """
        x = self.x-1
        y = self.y-1
        if x//3 == 0 and y//3 == 0:
            return 1
        elif x//3 == 1 and y//3 == 0:
            return 2
        elif x//3 == 2 and y//3 == 0:
            return 3
        elif x//3 == 0 and y//3 == 1:
            return 4
        elif x//3 == 1 and y//3 == 1:
            return 5
        elif x//3 == 2 and y//3 == 1:
            return 6
        elif x//3 == 0 and y//3 == 2:
            return 7
        elif x//3 == 1 and y//3 == 2:
            return 8
        elif x//3 == 2 and y//3 == 2:
            return 9


class Solver():
    def __init__(self):

        self.puzzle = {}

        for x in range(1, 10):
            for y in range(1, 10):
                self.puzzle[(x, y)] = Cell(x, y)

    def pretty_print(self):
        line = ""
        for x in range(1, 10):
            for y in range(1, 10):
                line += str(puzzle[(x, y)].value)
                if y % 3 == 0:
                    line += "|"
                else:
                    line += " "
            print(line)
            line = ""
            if x%3 == 0:
                print("-"*18)
    def update_value(self, x, y, value):
        pass

    def check_for_solo(self):
        for x in range(1, 10):
            for y in range(1, 10):
                if len(self.puzzle[(x, y)].canidates) == 1:
                    self.update_value(x, y, self.puzzle[(x, y)].canidates[0])


    def check_for_only(self):
        #rows 
        for x in range(1, 10):
            for c in range(1, 10):
                count = []
                for y in range(1, 10):
                    if c in self.puzzle[(x, y)].canidates:
                        count.append(self.puzzle[(x, y)])
                if len(count) == 1:
                    self.update_value(count[0].x , count[0].y, c)
        #columns
        for y in range(1, 10):
            for c in range(1, 10):
                count = []
                for x in range(1, 10):
                    if c in self.puzzle[(x, y)].canidates:
                        count.append(self.puzzle[(x, y)])
                if len(count) == 1:
                    self.update_value(count[0].x , count[0].y, c)
        
        #box 
        for b in range(1, 10):
            for c in range(1, 10):
                count = []
                for x in range(1, 10):
                    for y in range(1, 10):
                        cb = self.puzzle[(x, y)]
                        if cb.box == b and cb.value == c:
                            count.append[cb]
                if len(count) == 1:
                    self.update_value(count[0].x , count[0].y, c)

    def init_canidates(self):
        for x in range(1, 10):
            for y in range(1, 10):
                if self.puzzle[(x, y)] == 0:
                    for c in range(1, 10):
                        valid = True
                        for i in range(1, 10):
                            if self.puzzle[(x, i).value] == c:
                                valid = False
                        for i in range(1, 10):
                            if self.puzzle[(i, y).value] == c:
                                valid = False
                        for nx in range(1, 10):
                            for ny in range(1, 10):
                                if (self.puzzle[(nx, ny)].box == self.puzzle[(x, y)].box
                                    and self.puzzle[(nx, ny)].value == self.puzzle[(x, y)].value):

                                    valid = False
                        if valid:
                            self.puzzle[(i, y)].canidates.append(c)

                        
                            



                        



