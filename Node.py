class Node:
    def __init__(self, state, parent, cost, heuristic_cost):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic_cost = heuristic_cost
