import numpy as np
import datetime

from algorithm.Version2.FairProportionalAllocationProblem import FairProportionalAllocationProblem
from algorithm.Version2.GraphGenerator import GraphGenerator

if __name__ == '__main__':
    num_of_agents = 3
    num_of_items =  4
    #max_item_value = 100
    #v = np.random.randint(max_item_value, size=(num_of_agents, num_of_items)).tolist()
    v = [[1,2,3,4],[4,5,6,5],[6,7,9,8],[4,5,1,9]]
    fpap = FairProportionalAllocationProblem(v)
    start = datetime.datetime.now()
    # THE TEST EXECUTION
    print(fpap.find_allocation_with_min_shering())
    end = datetime.datetime.now()
    #print("the number of graph: {}".format(count))
    print("Total time for {} agents and {} items  :{}".format(num_of_agents,num_of_items,end-start))

""""
v = [[1,2,3,4],[4,5,6,5],[6,7,9,8]]
   [[0.    0.    0.    1.   ]
    [0.999 0.649 0.    0.   ]
    [0.    0.35  0.999 0.   ]]
Total time for 3 agents and 4 items  :0:00:05.180224
   
   """