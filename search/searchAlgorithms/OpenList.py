import heapq

import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent+"\model")
from Node import Node
from State import State
from Rod import Rod


class OpenList:
    def __init__(self, n_rods):
        self.heap = [] 
        self.entry_finder = {} 
        r = [Rod()]*n_rods
        self.REMOVED = Node(State(r, 0), None, g =-100, e=-100) 
        
    def add_item(self, item, priority):
        """ if item in self.entry_finder:
            self.remove_item(item) """
        entry = [priority, item]
        self.entry_finder[item] = entry
        heapq.heappush(self.heap, entry)

    def remove_item(self, item):
        entry = self.entry_finder.pop(item)
        entry[1] = self.REMOVED

    def extract_item(self, item):
        return self.entry_finder.get(item)

    def pop_item(self):
        while self.heap:
            priority, item = heapq.heappop(self.heap)
            if item is not self.REMOVED:
                del self.entry_finder[item]
                return item, priority
        raise KeyError('Priority queue is empty')

    def is_empty(self):
        return len(self.entry_finder) == 0

    def __contains__(self, item):
        return item in self.entry_finder


'''# Example usage:
pq = OpenList(6)
pq.add_item('B', [9, 4])
pq.add_item('A', [8, 9])


print(pq.pop_item())
'''


