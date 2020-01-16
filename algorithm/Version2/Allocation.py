





class Allocation():
    """
    this class represent an Allocation of the object to the
    agents represent by matrix - if graph[i][j] = x its mean that agent i
    gets x%  from object j
    0 <= graph[i][j] <= 1
    """
    def __init__(self,alloction_matrix):
        self.alloction_matrix = alloction_matrix

    def __repr__(self):
        pass

    def round(self):
        pass