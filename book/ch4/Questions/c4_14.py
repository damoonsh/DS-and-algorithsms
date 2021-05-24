"""
    Tower of Hanoi
"""

class TowerHanoi:
    def __init__(self, n, baskets: dict, target: str, low: int, high: int, med: int=0):
        self.n = n
        self.low = low
        self.med = med
        self.high = high
        self.baskets = baskets

    def new_target(self):
        # Choose the empty basket:
        for basket, elements in self.baskets.iter():
            if len(elements) == 0 and basket != self.new_target: 
                return basket

        # If all the baskets were full then
        

    def solve(self):
        if len(self.baskets["a"]) == self.n:
            sub = TowerHanoi(
                self.n - 1,
                self.baskets,
                self.new_target(),
                low=self.low,
                high=self.high,
            )
        

        