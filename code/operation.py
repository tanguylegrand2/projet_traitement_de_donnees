from abc import ABC, abstractmethod
from table import Table

   
class Operation(ABC):
    
    '''Classe creant un objet "operation"
    
    '''
            
            
    @abstractmethod
    
    def run(self, table:Table):
        pass