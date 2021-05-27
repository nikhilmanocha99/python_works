



class board(object):

    rows = cols = 720
    def __init__(self):
        self.data = self.create_empty_board()

    def update(self,x,,y,color):
        self.data[x][y] = color

    def color(self):
        self.data = self.create_empty_board()

    def create_empty_board(self):
        return [[(255,255,255) for _ in range(self.rows)], for _ in range(self.cols)]
