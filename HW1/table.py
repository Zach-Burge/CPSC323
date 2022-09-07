from copy import copy
import csv
import copy
from tabulate import tabulate

class Table:
    """
    Represents a table of data and column names that mimics the csv file format of the data

    Class Attributes:
        column_names: The names of all the attributes in the table
        data: a list of all the instances in the table
    """
    def __init__(self, column_names=None, data=None):
        if column_names is None:
            column_names = []
        self.column_names = copy.deepcopy(column_names)
        if data is None:
            data = []
        self.data = copy.deepcopy(data)

    def load_file(self, filename):
        """Loading in the column names and data from the csv file and storing them in the class attributes"""
        with open(filename) as csvfile:
            reader = csv.reader(csvfile)
            self.column_names = next(reader)
            for row in reader:
                self.data.append(row)
        return self

    def get_column(self, col_id):
        """Returns a list of all the values from the table for a specific column (col_id)"""
        col = []
        for row in self.data:
            col.append(row[col_id])
        return col

    def make_sub_table(self, orig_table, new_table_col_names):
        """Returns a new table containing only the values from the columns specified in new_table_col_names"""
        new_table = []
        for row in orig_table.data:
            new_row = []
            for name in new_table_col_names:
                new_row.append(row[orig_table.column_names.index(name)])
            new_table.append(new_row)
        return new_table

    def pretty_print(self):
        print(tabulate(self.data, headers=self.column_names))
