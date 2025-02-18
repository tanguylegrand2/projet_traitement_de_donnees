from operation import Operation
from abc import ABC, abstractmethod

class Estimateur(Operation, ABC):
     ''' Classe creant un objet "Estimateur" qui est une sous classe d'Operation
            Attributes
            ----------
            variables : list
                  liste des variables sur lesquelles on veut faire des operations'''

    @abstractmethod
    def run(self,table):
        pass
