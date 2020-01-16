




class FairAllocationProblem():


    def __init__(self ,valuation):
        self.valuation = valuation
        self.num_of_agents = len(valuation)
        self.num_of_items = len(valuation[0])
        self.min_sharing_number = len(valuation)
        self.min_sharing_allocation = valuation
        self.valuation_ratios = self.creat_valuation_ratios()

    def find_proportional_allocation_with_min_shering(self):
        pass

    def find_envy_free_allocation_with_min_shering(self):
        pass

    def __find_proportional_allocation_for_graph(self):
        pass

    def __find_envy_free_allocation_for_graph(self):
        pass

    def __creat_valuation_ratios(self):
        pass

    def __generate_all_consumption_graph(self):
        pass

    def __add_agent(self):
        pass