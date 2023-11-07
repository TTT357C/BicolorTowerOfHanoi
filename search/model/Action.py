"""
classe che rappresenta una generica azione:
    - i: rod di partenza
    - j: rod di arrivo
"""
class Action:

    def __init__(self, i, j) -> None:
        self.i = i
        self.j = j

    def toString(self):
        return f"{str(self.i+1)} --> {str(self.j+1)}"
    
    def __eq__(self, other) -> bool:
        return self.i == other.i and self.j == other.j
    
    def isnull(self):
        return self.i == self.j