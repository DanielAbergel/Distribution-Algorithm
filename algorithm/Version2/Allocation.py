import doctest


class Allocation():
    """
    this class represent an Allocation of the object to the
    agents represent by matrix - if graph[i][j] = x its mean that agent i
    gets x%  from object j
    0 <= graph[i][j] <= 1
    """
    def __init__(self,alloction_matrix):
        self.__alloction_matrix = alloction_matrix

    def __repr__(self):
        pass

    def num_of_shering(self):
        pass

    def round(self):
        """
        this function round the alloction_matrix for 3 digit after the point
        >>> a= Allocation([[0.12345,0.9999999,0.11111],[0.2222222,0.2342,0.98765],[0.44444,0.12341345,0.003]])
        >>> a.round()
        >>> print(a.get_allocation())
        [[0.123, 0.999, 0.111], [0.222, 0.234, 0.987], [0.444, 0.123, 0.003]]
        """
        for i in range(len(self.__alloction_matrix)):
            for j in range(len(self.__alloction_matrix[i])):
                self.__alloction_matrix[i][j] = (int)(self.__alloction_matrix[i][j] * 1000)
                self.__alloction_matrix[i][j] = self.__alloction_matrix[i][j] / 1000

    def get_allocation(self):
        return self.__alloction_matrix



if __name__ == '__main__':
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))