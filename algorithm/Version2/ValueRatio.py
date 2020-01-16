import numpy as np
import doctest as doctest




class ValueRatio():


    def __init__(self,valuation_matrix):
        self.valuation_matrix = valuation_matrix
        self.all_ratio = buile_all_the_ratio(valuation_matrix)


    def create_the_value_ratio_for_2(self , graph , x, y):
        """
        this function build the array for value ratio between agent x to agent y
        according to the given graph and the properties of agent x in this graph
        and sort it.
        (i check this method in all the tests of the ether function from ver1)
        :param graph: the current graph we working on
        :param x: the index of the first agent
        :param y: the index of the second agent
        :return: the sorted array of tuples (index of location in v, the ratio)
        """
        ans = []
        for i in range(len(graph[0])):
            if(graph[x][i]==1):
                ans.append(self.all_ratio[x][y][i])
        ans.sort(key=second, reverse=True)
        return ans


def second(pair):
    return pair[1]

def buile_all_the_ratio(valuation_matrix):
    """
    this function create a list of matrix .
    each matrix is the ratio between agent i and all the
    ether agents
    for example ans[3] = matrix of the ratio between agent 3 and all ether agents
    so ans[3][4] = the ratio array between agent 3 to agent 4
    :param valuation_matrix: the valuation of the agents represent by matrix
    :return: ans - list of all the matrix
    >>> v = [[1,2],[3,4]]
    >>> buile_all_the_ratio(v)
    [[[(0, 1.0), (1, 1.0)], [(0, 0.3333333333333333), (1, 0.5)]], [[(0, 3.0), (1, 2.0)], [(0, 1.0), (1, 1.0)]]]
    >>> v = [[1,0],[3,7]]
    >>> buile_all_the_ratio(v)
    [[[(0, 1.0), (1, 1.0)], [(0, 0.3333333333333333), (1, 0.0)]], [[(0, 3.0), (1, inf)], [(0, 1.0), (1, 1.0)]]]
    >>> v = [[1,0,2],[3,7,2.5],[4,2,0]]
    >>> buile_all_the_ratio(v)
    [[[(0, 1.0), (1, 1.0), (2, 1.0)], [(0, 0.3333333333333333), (1, 0.0), (2, 0.8)], [(0, 0.25), (1, 0.0), (2, inf)]], [[(0, 3.0), (1, inf), (2, 1.25)], [(0, 1.0), (1, 1.0), (2, 1.0)], [(0, 0.75), (1, 3.5), (2, inf)]], [[(0, 4.0), (1, inf), (2, 0.0)], [(0, 1.3333333333333333), (1, 0.2857142857142857), (2, 0.0)], [(0, 1.0), (1, 1.0), (2, 1.0)]]]
    """
    ans = []
    for i in range(len(valuation_matrix)):
        mat = np.zeros((len(valuation_matrix),len(valuation_matrix[0]))).tolist()
        for j in range(len(valuation_matrix)):
            for k in range(len(valuation_matrix[0])):
                if(valuation_matrix[i][k]==0)and(valuation_matrix[j][k]==0):
                    temp = 1.0
                else:
                    if(valuation_matrix[j][k]==0):
                        temp = np.inf
                    else:
                        temp = valuation_matrix[i][k] / valuation_matrix[j][k]
                mat[j][k] = (k,temp)
        ans.append(mat)
    return ans


if __name__ == '__main__':
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
