
class Solver():
    def __init__(self):

        self.puzzle = {}
        self.canidates = {}

        for x in range(1, 10):
            for y in range(1, 10):
                self.puzzle[(x, y)] = 0
                self.canidates[(x, y)] = []

    def pretty_print(self):
        line = ""
        for x in range(1, 10):
            for y in range(1, 10):
                line += str(puzzle[(x, y)])
                if y % 3 == 0:
                    line += "|"
                else:
                    line += " "
            print(line)
            line = ""
            if x%3 == 0:
                print("-"*18)


    def get_box(self, x, y):
        """
        1 2 3
        4 5 6
        7 8 9
        """
        x -= 1
        y -= 1
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


    def init_canidates(self):
        for x in range(1, 10):
            for y in range(1, 10):
                if self.puzzle[(x, y)] == 0:
                    for c in range(1, 10):
                        valid = True
                        for i in range(1, 10):
                            if self.puzzle[(x, i)] == c:
                                valid = False
                        for i in range(1, 10):
                            if self.puzzle[(i, y)] == c:
                                valid = False
                        
                            



                        



