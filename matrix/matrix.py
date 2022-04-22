class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        print("this is the matrix " + matrix_string)
        self.list_rows = self.matrix_string.split("\n")
        #extract elements from list make them into integers and make them into a matrix
        #as stuck together lists

    def row(self, index):

        return self[index:(index+3)]

    def column(self, index):
        pass
