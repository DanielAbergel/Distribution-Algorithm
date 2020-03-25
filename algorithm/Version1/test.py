import numpy as np
import datetime
from algorithm.Version1 import GraphCheck
from algorithm.Version1.GraphGenerator import generate_all_consumption_graphs

if __name__ == '__main__':
    num_of_agents = 4
    num_of_items =  12
    max_item_value = 100
    v = np.random.randint(max_item_value, size=(num_of_agents, num_of_items)).tolist()
    start = datetime.datetime.now()
    #print("start time: {}".format(start))
    #print(v)
    count=0
    for i in generate_all_consumption_graphs(v):
        count+=1
    end = datetime.datetime.now()
    #print("end time: {}".format(end))
    print("Total time for {} agents and {} items  :{}".format(num_of_agents,num_of_items,end-start))

    """
    find_alloction(v):
    Total time for 3 agents and 10 items  :0:03:50.778506
    g = GraphCheck.find_alloction(v)
    print("the ans is: ")
    print(g)
    """

    """

     num_of_agents = 4
     num_of_items =  13
     before cutting: 
     Total time for 4 agents and 13 items  :0:00:41.599632
     2523039
     
     after cutting n-1 :
     Total time for 4 agents and 13 items  :0:00:41.537103
     2139015
     
     after cutting n-2 :
     Total time for 4 agents and 13 items  :0:00:14.655985
     607568
    """