import doctest as doctest
import itertools
import numpy as np
import math


def cartesian_product(i,o):
    """
    this function generate all the cartesian product of the i agent
    according to o objects (a1,a2,a3,...ai)  0 <= ai <= o*2+1
    :param i: integer represent the number of agents
    :param o: integer represent the number of objects
    :return: generator to all the cartesian product
    >>> g = cartesian_product(2,3)
    >>> print(next(g))
    (0, 0)
    >>> print(next(g))
    (0, 1)
    >>> print(next(g))
    (0, 2)
    >>> g = cartesian_product(4,3)
    >>> print(next(g))
    (0, 0, 0, 0)
    >>> print(next(g))
    (0, 0, 0, 1)
    >>> print(next(g))
    (0, 0, 0, 2)
    """
    for element in itertools.product(list(range(o*2+1)),repeat=i):
        yield element


def takeSecond(elem):
    return elem[1]

def build_the_Distribution_ratio_array(matv,x,y):
    """
    this function build the array for  Distribution ratio between agent x to agent y
    and sort it
    :param matv:  represent- the Agents value for the objects
    :param x: the index of the first agent
    :param y: the index of the second agent
    :return: the sorted array of tuples (index of location in v, the ratio)

    >>> a = [[20,30,40,10],[10,60,10,20]]
    >>> build_the_Distribution_ratio_array(a,0,1)
    [(2, 4.0), (0, 2.0), (1, 0.5), (3, 0.5)]
    >>> a = [[20,30,10],[10,60,40]]
    >>> build_the_Distribution_ratio_array(a,0,1)
    [(0, 2.0), (1, 0.5), (2, 0.25)]
    >>> a = [[1,3,9,2,4,6,5],[2,4,4,3,6,2,1]]
    >>> build_the_Distribution_ratio_array(a,0,1)
    [(6, 5.0), (5, 3.0), (2, 2.25), (1, 0.75), (3, 0.6666666666666666), (4, 0.6666666666666666), (0, 0.5)]
    >>> a = [[0,0,0,0],[0,0,0,0],[20,30,40,10],[10,60,10,20]]
    >>> build_the_Distribution_ratio_array(a,2,3)
    [(2, 4.0), (0, 2.0), (1, 0.5), (3, 0.5)]
    >>> a = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,3,9,2,4,6,5],[2,4,4,3,6,2,1]]
    >>> build_the_Distribution_ratio_array(a,2,3)
    [(6, 5.0), (5, 3.0), (2, 2.25), (1, 0.75), (3, 0.6666666666666666), (4, 0.6666666666666666), (0, 0.5)]
        >>> a = [[0,0,0,0],[0,0,0,0],[20,30,40,10],[10,60,10,20]]
    >>> build_the_Distribution_ratio_array(a,2,3)
    [(2, 4.0), (0, 2.0), (1, 0.5), (3, 0.5)]
    >>> a = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,3,9,2,4,6,5],[2,4,4,3,6,2,1]]
    >>> build_the_Distribution_ratio_array(a,2,3)
    [(6, 5.0), (5, 3.0), (2, 2.25), (1, 0.75), (3, 0.6666666666666666), (4, 0.6666666666666666), (0, 0.5)]
    """
    n = len(matv[0])
    l = []
    for i in range(0,n):
        try:
            temp = matv[x][i]/matv[y][i]
        except ZeroDivisionError:
            temp = float('Inf')
        l.append((i,temp))
    l.sort(key=takeSecond , reverse=True)
    return l


def product_to_matrix(p,arr):
    """
    this function get specific product and convert it to matrix
    :param p: product
    :param arr:ratio_array
    :return: the matrix
    """
    n = len(arr)
    # the properties of a
    prop_a = math.ceil(n - p[0]/2)
    # the properties of b
    prop_b = math.ceil(p[0]/2)

    mat = np.zeros((2, n)).tolist()
    for j in range(prop_a):
         mat[0][arr[j][0]] = 1
    for j in range(n-prop_b, n):
        mat[1][arr[j][0]] = 1
    return mat


def func_for_2(matv):
    """
    this function generate all the matrix for the 2 first agent
    :param matv:
    :return: generator for  all the matrix for the 2 first agent
    """
    arr = build_the_Distribution_ratio_array(matv,0,1)
    gen = cartesian_product(1,len(matv[0]))
    for x in gen:
        yield product_to_matrix(x,arr)



if __name__ == '__main__':
    mat = [[20,30,10],[10,10,40]]
    mat1 = [[40, 30, 20,10], [10, 10, 10,10]]
    a = build_the_Distribution_ratio_array(mat,0,1)
    for x in func_for_2(mat):
        print(x)
    #(failures, tests) = doctest.testmod(report=True)
    #print("{} failures, {} tests".format(failures, tests))