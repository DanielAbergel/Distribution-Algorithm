from algorithm.Version3.ConsumptionGraph import ConsumptionGraph
from algorithm.Version3.GraphGenerator import GraphGenerator


class FairAllocationProblem():
    """
    this class is abstract class for solve Fair Allocation Problem
    meaning - get agents valuation and a Fair Allocation
    """


    def __init__(self ,valuation):
        self.valuation = valuation
        self.num_of_agents = len(valuation)
        self.num_of_items = len(valuation[0])
        self.min_sharing_number = len(valuation)
        self.min_sharing_allocation = valuation
        self.graph_generator = GraphGenerator(valuation)

    def find_allocation_with_min_shering(self):
        pass

    def find_allocation_for_graph(self,consumption_graph : ConsumptionGraph):
        pass







