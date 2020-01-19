import doctest
import math


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
        """

        :param graph:
        :return:
        >>> g = [[0.    ,0.    ,0.    ,1.   ],[0.    ,0.329 ,1.    ,0.   ],[1.    ,0.67  ,0.    ,0.   ]]
        >>> a = Allocation(g)
        >>> a.num_of_shering()
        1
        >>> g = [[0.   , 0.    ,0.    ,0.977],[0.    ,0.305 ,1.    ,0.022],[1.    ,0.694 ,0.    ,0.   ]]
        >>> a = Allocation(g)
        >>> a.num_of_shering()
        2
        """
        num_of_edge = 0
        for i in range(len(self.__alloction_matrix)):
            for j in range(len(self.__alloction_matrix[0])):
                num_of_edge += math.ceil(self.__alloction_matrix[i][j])
        num_of_obj = len(self.__alloction_matrix[0])
        return num_of_edge - num_of_obj

    def round(self):
        """
        this function round the alloction_matrix for 3 digit after the point
        >>> a= Allocation([[0.12345,0.9999999,0.11111],[0.2222222,0.2342,0.98765],[0.44444,0.12341345,0.003]])
        >>> a.round()
        >>> print(a.get_allocation())
        [[0.123, 0.999, 0.111], [0.222, 0.234, 0.987], [0.444, 0.123, 0.003]]
        >>> a= Allocation([[1.95517154e-08 ,1.10159480e-08 ,1.03259828e-08 ,7.43142069e-01],[5.52419621e-02 ,1.00000000e+00 ,1.00000000e+00 ,3.13131120e-02],[9.44758043e-01 ,6.16284544e-09 ,9.16259668e-09 ,2.25544833e-01]])
        >>> a.round()
        >>> print(a.get_allocation())
        [[0.0, 0.0, 0.0, 0.743], [0.055, 1.0, 1.0, 0.031], [0.944, 0.0, 0.0, 0.225]]
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