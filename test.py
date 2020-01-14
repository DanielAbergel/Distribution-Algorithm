import numpy as np
import datetime
from GraphGenerator import all_graph


if __name__ == '__main__':
    num_of_agents = 4
    num_of_items =  13
    max_item_value = 100
    v = np.random.randint(max_item_value, size=(num_of_agents, num_of_items)).tolist()
    start = datetime.datetime.now()
    print("start time: {}".format(start))
    count=0
    for i in all_graph(v):
        count+=1
    end = datetime.datetime.now()
    print("end time: {}".format(end))
    print("Total time for {} agents and {} items  :{}".format(num_of_agents,num_of_items,end-start))
    print(count)


    """
    without f:
    start time: 2020-01-08 08:58:21.718164
    end time: 2020-01-08 08:58:58.811193
    Total time for 4 agents and 13 items  :0:00:37.093029
    2520543
    wuth f
    start time: 2020-01-08 08:56:43.910163
    end time: 2020-01-08 08:57:22.513882
    Total time for 4 agents and 13 items  :0:00:38.603719
    2508991
    """