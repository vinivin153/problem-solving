import random

class RandomizedSet:

    def __init__(self):
        self.s = set()
        

    def insert(self, val: int) -> bool:
        if val in self.s:
            return False
        
        self.s.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.s:
            return False
        
        self.s.remove(val)
        return True
            

    def getRandom(self) -> int:
        return random.choice(list(self.s))

