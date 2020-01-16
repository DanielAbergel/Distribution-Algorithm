import numpy as np
import datetime




if __name__ == '__main__':
    num_of_agents = 3
    num_of_items =  10
    max_item_value = 100
    v = np.random.randint(max_item_value, size=(num_of_agents, num_of_items)).tolist()
    start = datetime.datetime.now()
    # THE TEST EXECUTION
    end = datetime.datetime.now()
    print("Total time for {} agents and {} items  :{}".format(num_of_agents,num_of_items,end-start))