from copy import copy
import csv
import copy

class Table:
    def __init__(self, column_names=None, data=None):
        if column_names is None:
            column_names = []
        self.column_names = copy.deepcopy(column_names)
        if data is None:
            data = []
        self.data = copy.deepcopy(data)

    def load_file(self, filename):
        with open(filename) as csvfile:
            reader = csv.reader(csvfile)
            self.column_names = next(reader)
            for row in reader:
                self.data.append(row)
        return self

    def get_column(self, col_id):
        col = []
        for row in self.data:
            col.append(row[col_id])
