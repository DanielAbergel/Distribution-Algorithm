import numpy as np
import datetime
from GraphGenerator import all_graph


if __name__ == '__main__':
    num_of_agents = 3
    num_of_items =  30
    max_item_value = 100
    v = np.random.randint(max_item_value, size=(num_of_agents, num_of_items)).tolist()
    start = datetime.datetime.now()
    print("start time: {}".format(start))
    for i in all_graph(v):
        pass
    end = datetime.datetime.now()
    print("end time: {}".format(end))
    print("Total time for {} agents and {} items  :{}".format(num_of_agents,num_of_items,end-start))