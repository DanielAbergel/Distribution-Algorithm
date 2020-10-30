import numpy as np
import datetime

from algorithm.Version3.FairEnvyFreeAllocationProblem import FairEnvyFreeAllocationProblem
from algorithm.Version3.FairProportionalAllocationProblem import FairProportionalAllocationProblem


"""
This script demonstrates the use of the algorithms (Envy-Free and Proportional)
both on random input and personal input .
the input in the algorithm is given by a matrix  
and if your putting your own input you need to put it in this order :
the element [i][j] in the matrix  = the valuation of the participant number i
for the object number j.
"""


if __name__ == '__main__':

    # Selects the number of objects, participants and the rate range for random input
    num_of_agents = 4
    num_of_items = 10
    max_item_value = 100
    # create random input
    v = np.random.randint(max_item_value, size=(num_of_agents, num_of_items)).tolist()

    # or you can create your own input
    v =  [[150., 150. ,150. ,150., 150. ,250.],
         [150., 150. ,150. ,150., 150. ,250.],
         [150., 150. ,150. ,150., 150. ,250.]]
    """
    v =  [[1., 15. ,7. ,9., 2. ,5.],
         [9., 20. ,3. ,5., 1. ,30.],
         [12., 8. ,7. ,6., 3. ,23.]]
    """
    # create an object of Envy-Free algorithm with the input matrix
    fefap = FairEnvyFreeAllocationProblem(v)

    # create an object of Proportional algorithm with the input matrix
    fpap =  FairProportionalAllocationProblem(v)

    # print the input
    print(v)

    # start time - to measure the algorithm time
    start = datetime.datetime.now()

    # run the Proportional algorithm on the input and put the answer in ans
    ans = fpap.find_allocation_with_min_shering()

    # if you want to run Envy-Free algorithm:
    #ans = fefap.find_allocation_with_min_shering()

    # print the answer
    print(ans)

    # stop the time
    end = datetime.datetime.now()

    # print the time and the properties
    print("Total time for {} agents and {} items  :{}".format(num_of_agents, num_of_items, end - start))