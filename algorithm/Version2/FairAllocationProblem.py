from algorithm.Version2.GraphGenerator import GraphGenerator


class FairAllocationProblem():


    def __init__(self ,valuation):
        self.valuation = valuation
        self.num_of_agents = len(valuation)
        self.num_of_items = len(valuation[0])
        self.min_sharing_number = len(valuation)
        self.min_sharing_allocation = valuation
        self.graph_generator = GraphGenerator(valuation)


    def find_proportional_allocation_with_min_shering(self):
        pass

    def find_envy_free_allocation_with_min_shering(self):
        pass

    def __find_proportional_allocation_for_graph(self):
        pass

    def __find_envy_free_allocation_for_graph(self):
        pass





