import numpy as np
import datetime

from algorithm.Version2.GraphGenerator import GraphGenerator

if __name__ == '__main__':
    num_of_agents = 4
    num_of_items =  12
    max_item_value = 100
    v = np.random.randint(max_item_value, size=(num_of_agents, num_of_items)).tolist()
    start = datetime.datetime.now()
    # THE TEST EXECUTION
    g = GraphGenerator(v)
    count = 0
    for i in g.generate_all_consumption_graph():
        count += 1
    end = datetime.datetime.now()
    print("the number of graph: {}".format(count))
    print("Total time for {} agents and {} items  :{}".format(num_of_agents,num_of_items,end-start))

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