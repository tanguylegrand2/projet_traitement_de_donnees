from transformation import Transformation
from table import Table

class SelectionVariable(Transformation):
    
    def __init__(self, variables) -> None:
        self.variables = variables
        
        
    def run(self, table:Table):
        
        table.variables = self.variables
        
        table.data = {var : table.data[var] for var in self.variables}

        return table