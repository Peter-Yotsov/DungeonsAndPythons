class Coordinates:
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def __repr__(self):
        return '[{}, {}]'.format(self.row, self.column)
