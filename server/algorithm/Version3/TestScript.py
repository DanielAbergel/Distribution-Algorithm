import numpy as np
import datetime

from algorithm.Version3.ConsumptionGraph import ConsumptionGraph
from algorithm.Version3.FairEnvyFreeAllocationProblem import FairEnvyFreeAllocationProblem
from algorithm.Version3.FairProportionalAllocationProblem import FairProportionalAllocationProblem
from algorithm.Version3.GraphGenerator import GraphGenerator

if __name__ == '__main__':
    num_of_agents = 4
    num_of_items = 4
    max_item_value = 100
    #v = np.random.randint(max_item_value, size=(num_of_agents, num_of_items)).tolist()
   # v = [[333. ,333. ,334.],
    #    [333. ,334. ,333.]]
    v =  [[300. ,300., 400.],
          [307. ,308., 385.],
          [312. ,313. ,375.]]

    #fpap = FairEnvyFreeAllocationProblem(v)
    fpap =  FairProportionalAllocationProblem(v)
    # print(v)
    start = datetime.datetime.now()
    # THE TEST EXECUTION
    print(fpap.find_allocation_with_min_shering())
    end = datetime.datetime.now()
    # print("the number of graph: {}".format(count))
    print("Total time for {} agents and {} items  :{}".format(num_of_agents, num_of_items, end - start))

    """

v = [[1,2,3,4],[4,5,6,5],[6,7,9,8]]
[[0.    0.    0.    0.999]
 [0.623 0.999 0.    0.   ]
 [0.376 0.    0.999 0.   ]]
Total time for 3 agents and 4 items  :0:00:00.188497



[[0.999 0.    1.    0.    1.    0.    0.    0.    0.    0.   ]
 [0.    0.    0.    0.    0.    1.    0.    1.    0.    0.   ]
 [0.    0.    0.    0.    0.    0.    1.    0.    1.    1.   ]
 [0.    1.    0.    1.    0.    0.    0.    0.    0.    0.   ]]
Total time for 4 agents and 10 items  :0:21:33.373481




    a = ConsumptionGraph([[0. ,   0.    ,0.   , 1.  ,  0.   , 0.   , 0.   , 0.999 ,0.    ,0.   ],
    [0.   , 0.   , 0.  ,  0.   , 0.999 ,0.  ,  0.   , 0.   , 0.   , 0.999],
    [0.   , 0.999 ,1.   , 0.   , 0.   , 0.   , 0.   , 0.   , 0.   , 0.   ],
    [1.  ,  0.   , 0.   , 0.   , 0.    ,1. ,   1.   , 0.   , 0.999 ,0.   ]])
    print(a.is_prop([[17, 52, 45, 61, 41, 38, 41, 66, 57, 45], [36, 28, 34, 50, 67, 39, 38, 45, 94, 94], [35, 85, 74, 92, 0, 46, 48, 2, 78, 49], [54, 11, 66, 51, 39, 79, 86, 99, 88, 23]]))



[[9, 23, 19, 62, 66, 75, 44, 28, 56, 27, 61, 56, 69, 91, 8, 40, 96, 22, 70, 15], [98, 68, 87, 60, 32, 20, 30, 9, 64, 0, 62, 20, 97, 22, 64, 64, 87, 28, 26, 31], [19, 47, 51, 12, 17, 90, 21, 49, 69, 16, 64, 49, 70, 0, 73, 25, 49, 96, 34, 55], [12, 14, 83, 53, 47, 27, 51, 6, 39, 8, 80, 91, 66, 72, 71, 10, 58, 26, 94, 19]]
[[0.    0.    0.    0.    0.999 0.    0.    0.    0.    0.    0.    0.
  0.    1.    0.    0.    0.999 0.    0.    0.   ]
 [0.999 1.    0.    1.    0.    0.    0.    0.    0.    0.    0.    0.
  0.    0.    0.    0.999 0.    0.    0.    0.   ]
 [0.    0.    0.    0.    0.    1.    0.    1.    0.    0.    0.    0.
  0.    0.    0.    0.    0.    0.999 0.    0.   ]
 [0.    0.    0.999 0.    0.    0.    0.999 0.    1.    1.    1.    0.999
  1.    0.    1.    0.    0.    0.    1.    1.   ]]
Total time for 4 agents and 20 items  :0:08:13.528924






envy-free 

[[0.    0.    0.    1.    0.    0.    0.    0.    0.    0.    0.    1.
  1.    0.    0.   ]
 [0.    0.    0.    0.    0.    1.    0.    0.    0.    0.999 0.    0.
  0.    0.999 0.   ]
 [0.999 0.    0.    0.    0.999 0.    0.999 0.    0.    0.    0.999 0.
  0.    0.    0.   ]
 [0.    0.999 0.999 0.    0.    0.    0.    0.999 0.999 0.    0.    0.
  0.    0.    0.999]]
Total time for 4 agents and 15 items  :0:04:42.596165


[[0.    0.    0.    0.999 0.    0.    0.    0.    0.    0.    0.999 0.
  0.999 0.    0.    0.    0.    0.    0.999 0.   ]
 [0.    0.    0.    0.    0.    0.    0.    0.    0.    0.999 0.    0.
  0.    0.    0.    0.    0.999 0.999 0.    0.999]
 [1.    1.    1.    0.    0.    0.    1.    0.    1.    0.    0.    0.
  0.    0.    0.    0.    0.    0.    0.    0.   ]
 [0.    0.    0.    0.    1.    1.    0.    1.    0.    0.    0.    1.
  0.    1.    1.    1.    0.    0.    0.    0.   ]]
Total time for 4 agents and 20 items  :0:40:02.282783

    """