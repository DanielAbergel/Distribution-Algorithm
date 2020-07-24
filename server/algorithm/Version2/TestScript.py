import numpy as np
import datetime

from algorithm.Version2.ConsumptionGraph import ConsumptionGraph
from algorithm.Version2.FairEnvyFreeAllocationProblem import FairEnvyFreeAllocationProblem
from algorithm.Version2.FairProportionalAllocationProblem import FairProportionalAllocationProblem
from algorithm.Version2.GraphGenerator import GraphGenerator


def is_envy_free(v,z):
    for i in range(len(v)):
        agent_sum = 0
        for j in range(len(v[0])):
            agent_sum += z[i][j] * v[i][j]
        anther_agent_sum = 0
        for j in range(len(v)):
            anther_agent_sum = 0
            for k in range(len(v[0])):
                anther_agent_sum += z[j][k] * v[i][k]
            if(agent_sum < anther_agent_sum):
                print("the agent {}".format(i))
                print("the anther_agent {}".format(j))
                print("efresh {}".format(anther_agent_sum - agent_sum))
                #return False
    return True

"""
    
     v = [[300. ,300. ,400.],
         [307. ,308. ,385.],
         [312., 313. ,375.]]
         
        v = [[555., 444., 1.],
         [589., 410., 1.],
         [610., 389., 1.]]
         
         prob
         v = [[166. ,166. ,166. ,166. ,166. ,170.], his 333.328
        [166. ,166. ,166. ,166. ,166. ,170.], his 333.162
        [166. ,166. ,166. ,166. ,166. ,170.]] his 333.008
        
        ans: (prop and envy)
        [[1.    1.    0.008 0.    0.    0.   ]
         [0.    0.    0.    0.497 1.    0.498]
         [0.    0.    0.991 0.502 0.    0.501]]
         
         
          v =  [[242. ,322. ,157. ,188.  ,91.  , 0.],
         [257. ,330. ,137.,186.  ,90.  , 0.],
         [265., 339. ,136., 185. , 75. ,  0.]]
         
         
    v =  [[300., 300.,400.],
         [307. ,308. ,385.],
         [312. ,313., 375.]]
         
        v = [[413., 587.],
            [427. ,573.],
            [397., 603.]]

    v =[[397. ,603.],
       [484. ,516.],
       [374., 626.]]
       
    v = [[416., 584.],
        [422., 578.],
        [349. ,651.]]
        
        
      prob  
    v =  [[150., 150. ,150. ,150., 150. ,250.],
         [150., 150. ,150. ,150., 150. ,250.],
         [150., 150. ,150. ,150., 150. ,250.]]
    prop ans:
    [[1.    1.    0.222 0.    0.    0.   ]
 [0.    0.    0.    0.444 0.999 0.466]
 [0.    0.    0.777 0.555 0.    0.533]]
 
 v =   [[340. ,230. ,220., 210.],
 [270. ,260. ,240. ,230.],
 [400. ,200., 200. ,200.]]
   envy ans
   [[0.494 0.    0.757 0.   ]
 [0.    1.    0.242 0.232]
 [0.505 0.    0.    0.767]]
"""

if __name__ == '__main__':
    num_of_agents = 4
    num_of_items = 10
    max_item_value = 100
    v = np.random.randint(max_item_value, size=(num_of_agents, num_of_items)).tolist()

    v = [[340., 230., 220., 210.],
         [270., 260., 240., 230.],
         [400., 200., 200., 200.]]
    fpap = FairEnvyFreeAllocationProblem(v)
    fpap1 = FairProportionalAllocationProblem(v)
    #fpap =  FairProportionalAllocationProblem(v)
    print(v)
    start = datetime.datetime.now()
    # THE TEST EXECUTION
    ans = fpap.find_allocation_with_min_shering()
    print(ans)
    print(is_envy_free(v,ans))
    end = datetime.datetime.now()
    # print("the number of graph: {}".format(count))
    print("Total time for {} agents and {} items  :{}".format(num_of_agents, num_of_items, end - start))

    """
    
    
    execution test for graphgenerator:
    num_of_agents = 4
    num_of_items =  11
    
    original:
    max_item_value = 100
    v = np.random.randint(max_item_value, size=(num_of_agents, num_of_items)).tolist()
    start = datetime.datetime.now()
    #print("start time: {}".format(start))
    #print(v)
    count=0
    for i in generate_all_consumption_graphs(v):
        count+=1
    end = datetime.datetime.now()
    Total time for 4 agents and 11 items  :0:00:17.308427
    
    opp:
    Total time for 4 agents and 11 items  :0:00:16.746100
    
    
    num_of_agents = 4
    num_of_items =  12
    original:
    Total time for 4 agents and 12 items  :0:00:30.094190
    Total time for 4 agents and 12 items  :0:00:26.987285
    Total time for 4 agents and 12 items  :0:00:27.328374
    Total time for 4 agents and 12 items  :0:00:30.018934
    
    opp:
    Total time for 4 agents and 12 items  :0:00:32.690350
    Total time for 4 agents and 12 items  :0:00:27.480823
    Total time for 4 agents and 12 items  :0:00:25.674750
    Total time for 4 agents and 12 items  :0:00:25.539187
    Total time for 4 agents and 12 items  :0:00:25.921934
    """