class Cell():
    def __init__(self, x, y, value = 0):
        self.x = x 
        self.y = y
        self.value = value 
        self.canidates = []
        self.box = self.get_box()

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
                line += str(self.puzzle[(x, y)].value)
                if y % 3 == 0:
                    line += "|"
                else:
                    line += " "
            print(line)
            line = ""
            if x%3 == 0:
                print("-"*18)

    def update_value(self, x, y, value):
        self.puzzle[(x, y)].value = value
        self.puzzle[(x, y)].canidates = []
        for nx in range(1, 10):
            if value in self.puzzle[(nx, y)].canidates:
                self.puzzle[(nx, y)].canidates.remove(value)
        
        for ny in range(1, 10):
            if value in self.puzzle[(x, ny)].canidates:
                self.puzzle[(x, ny)].canidates.remove(value)

        for nx in range(1, 10):
            for ny in range(1, 10):
                if value in self.puzzle[(nx, ny)].canidates and self.puzzle[(nx, ny)].box == self.puzzle[(x, y)].box:
                    self.puzzle[(nx, ny)].canidates.remove(value)


    def check_for_solo(self):
        change = False
        for x in range(1, 10):
            for y in range(1, 10):
                if len(self.puzzle[(x, y)].canidates) == 1:
                    print(f"Cell updated at {x} , {y} to {self.puzzle[(x, y)].canidates[0]}")
                    print("reason: only one canidate")
                    self.update_value(x, y, self.puzzle[(x, y)].canidates[0])
                    change = True
        return change



    def check_for_only(self):
        change = False
        #rows 
        for x in range(1, 10):
            for c in range(1, 10):
                count = []
                for y in range(1, 10):
                    if c in self.puzzle[(x, y)].canidates:
                        count.append(self.puzzle[(x, y)])
                if len(count) == 1:
                    print(f"Cell updated at {x} , {y} to {c}")
                    print("reason: only one in row")
                    self.update_value(count[0].x , count[0].y, c)
                    change = True
        #columns
        for y in range(1, 10):
            for c in range(1, 10):
                count = []
                for x in range(1, 10):
                    if c in self.puzzle[(x, y)].canidates:
                        count.append(self.puzzle[(x, y)])
                if len(count) == 1:
                    print(f"Cell updated at {x} , {y} to {c}")
                    print("reason: only one in column")
                    self.update_value(count[0].x , count[0].y, c)
                    change = True
        
        #box 
        for b in range(1, 10):
            for c in range(1, 10):
                count = []
                for x in range(1, 10):
                    for y in range(1, 10):
                        cb = self.puzzle[(x, y)]
                        if cb.box == b and cb.value == c:
                            count.append(cb)
                if len(count) == 1:
                    print(f"Cell updated at {x} , {y} to {c}")
                    print(f"reason: only one in box {b}")
                    self.update_value(count[0].x , count[0].y, c)
                    change = True
        return change

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
    def count_done(self):
        count = 0
        for x in range(1, 10):
            for y in range(1, 10):
                if self.puzzle[(x, y)].value != 0:
                    count += 1
        return count
    def full_solve(self):
        self.init_canidates()
        while True:
            if self.count_done() == 81:
                print("donzo")
                self.pretty_print()
                break
            if self.check_for_only() or self.check_for_solo():
                pass
            else:
                print("No new moves found")
                self.pretty_print()
                break
            

                        
                            



                        



