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
        self.__is_prop = True
        self.__is_envy_free = True
    def __repr__(self):
        pass

    def num_of_shering(self)-> int :
        """
        this function calculate the number of sharing in
        the allocation
        :return: the number of sharing
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

    def is_prop(self,valuation_matrix) -> bool:
        """
        this function return if this graph is
        not proportional
        note - is this phase we can only know if from this graph
        you cant make a prop  allocation
        this function calculate like every agent gets all the objects he is connecting to.
        (and calculate it only one time)
        >>> v = [[1,3,5,2],[4,3,2,4]]
        >>> g = Allocation([[0,0,1,1],[1,1,0,1]])
        >>> g.is_prop(v)
        True
        >>> v = [[11,3],[7,7]]
        >>> g = Allocation([[0,1],[1,0]])
        >>> g.is_prop(v)
        False
        >>> v = [[11,3],[7,7]]
        >>> g = Allocation([[1,0],[0,1]])
        >>> g.is_prop(v)
        True
        >>> v = [[11,3],[7,7],[3,6]]
        >>> g = Allocation([[0,0],[0,1],[1,1]])
        >>> g.is_prop(v)
        False
        """
        flag = True
        i = 0
        while(i < len(self.__alloction_matrix))and(flag):
            if not (self.is_single_proportional(valuation_matrix, i)):
                flag = False
                self.__is_prop = False
            i += 1
        return self.__is_prop


    def is_single_proportional(self, matv, x):
        """
        this function check if the ConsumptionGraph is proportional
        according to single agent i
        for specific i and any j : ui(xi)>=1/n(xi)
        :param matv represent the value for the agents
        :param x the index of agent we check
        :return: bool value if the allocation is proportional
        >>> g = Allocation([[1,1,0,0],[1,1,0,1]])
        >>> v = [[1,3,5,2],[4,3,2,4]]
        >>> g.is_single_proportional(v,0)
        False
        >>> g.is_single_proportional(v,1)
        True
        >>> g = Allocation([[1, 0.0, 0.0], [0.0, 1, 1], [0.0, 0.0, 0.0]])
        >>> v = [[1,3,5],[4,3,2],[4,3,2]]
        >>> g.is_single_proportional(v,0)
        False
        >>> g.is_single_proportional(v,1)
        True
        >>> g.is_single_proportional(v,2)
        False
        >>> g = Allocation([[1, 1, 1], [0.0, 1, 1], [0.0, 0.0, 1]])
        >>> v = [[1,3,5],[4,3,2],[4,3,2]]
        >>> g.is_single_proportional(v,0)
        True
        >>> g.is_single_proportional(v,1)
        True
        >>> g.is_single_proportional(v,2)
        False
        >>> g = Allocation([[0.0, 0.0, 1], [0.0, 1, 0.0], [0.0, 0.0, 1]])
        >>> v = [[1,3,5],[4,1,2],[4,3,2]]
        >>> g.is_single_proportional(v,0)
        True
        >>> g.is_single_proportional(v,1)
        False
        >>> g.is_single_proportional(v,2)
        False
        """
        sum = 0
        part = 0
        for i in range(0, len(self.__alloction_matrix[0])):
            sum += matv[x][i]
            part += matv[x][i] * self.__alloction_matrix[x][i]
        sum = sum / len(self.__alloction_matrix)
        return part >= sum



    def is_envy_free(self,valuation_matrix) -> bool:
        """
        this function return if this graph is
        not proportional
        note - is this phase we can only know if from this graph
        you cant make a prop  allocation
        this function calculate like every agent gets all the objects he is connecting to.
        (and calculate it only one time)
        >>> v = [[1,3,5,2],[4,3,2,4]]
        >>> g = Allocation([[0,0,1,1],[1,1,0,1]])
        >>> g.is_envy_free(v)
        True
        >>> v = [[11,3],[7,7]]
        >>> g = Allocation([[0,1],[1,0]])
        >>> g.is_envy_free(v)
        False
        >>> v = [[11,3],[7,7]]
        >>> g = Allocation([[1,0],[0,1]])
        >>> g.is_envy_free(v)
        True
        >>> v = [[11,3],[7,7],[3,6]]
        >>> g = Allocation([[0,0],[0,1],[1,1]])
        >>> g.is_envy_free(v)
        False
        """
        flag = True
        i = 0
        while(i < len(self.__alloction_matrix))and(flag):
            if not (self.is_single_envy_free(valuation_matrix, i)):
                flag = False
                self.__is_envy_free = False
            i += 1
        return self.__is_envy_free


    def is_single_envy_free(self, matv, x):
        """
        this function check if the ConsumptionGraph is proportional
        according to single agent i
        for specific i and any j : ui(xi)>=1/n(xi)
        :param matv represent the value for the agents
        :param x the index of agent we check
        :return: bool value if the allocation is proportional
        >>> g = Allocation([[1,1,0,0],[1,1,0,1]])
        >>> v = [[1,3,5,2],[4,3,2,4]]
        >>> g.is_single_envy_free(v,0)
        False
        >>> g.is_single_envy_free(v,1)
        True
        >>> g = Allocation([[1, 0.0, 0.0], [0.0, 1, 1], [0.0, 0.0, 0.0]])
        >>> v = [[1,3,5],[4,3,2],[4,3,2]]
        >>> g.is_single_envy_free(v,0)
        False
        >>> g.is_single_envy_free(v,1)
        True
        >>> g.is_single_envy_free(v,2)
        False
        >>> g = Allocation([[1, 1, 1], [0.0, 1, 1], [0.0, 0.0, 1]])
        >>> v = [[1,3,5],[4,3,2],[4,3,2]]
        >>> g.is_single_envy_free(v,0)
        True
        >>> g.is_single_envy_free(v,1)
        False
        >>> g.is_single_envy_free(v,2)
        False
        >>> g = Allocation([[0.0, 0.0, 1], [0.0, 1, 0.0], [0.0, 0.0, 1]])
        >>> v = [[1,3,5],[4,1,2],[4,3,2]]
        >>> g.is_single_envy_free(v,0)
        True
        >>> g.is_single_envy_free(v,1)
        False
        >>> g.is_single_envy_free(v,2)
        False
        >>> g = Allocation([[0.8, 0.3], [0.2, 0.7]])
        >>> v = [[1,3],[2,1]]
        >>> g.is_single_envy_free(v,0)
        False
        >>> g.is_single_envy_free(v,1)
        False
        >>> g = Allocation([[0.2, 0.7],[0.8, 0.3]])
        >>> v = [[1,3],[2,1]]
        >>> g.is_single_envy_free(v,0)
        True
        >>> g.is_single_envy_free(v,1)
        True
        """
        sum = 0
        part = 0
        other_part = 0
        for i in range(0, len(self.__alloction_matrix[0])):
            part += matv[x][i] * self.__alloction_matrix[x][i]
        for i in range(0, len(self.__alloction_matrix)):
            other_part = 0
            for j in range(0 , len(self.__alloction_matrix[0])):
                other_part += matv[x][j]*self.__alloction_matrix[i][j]
            if(part < other_part):
                self.__is_envy_free = False
                return False
        return True

if __name__ == '__main__':
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))