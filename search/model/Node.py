"""
classe che rappresenta un nodo dell'albero di ricerca
"""
class Node:

    def __init__(self, state, action, parent = None, g = 0, e = 0) -> None:
        self.state = state
        self.action = action
        self.parent = parent
        self.g = g
        self.e = e

    def __eq__(self, other) -> bool:
        return self.state.__eq__(other.state)

    def toString(self):
        return f"--\n{self.g}{self.e}"
    
    def __hash__(self):
        return hash(self.state.toString_())
    
    def __lt__(self, other):
        return (self.e + self.g) < (other.e + other.g)

    def __le__(self, other) :
       return (self.e + self.g) <= (other.e + other.g)


    
