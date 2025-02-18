from abc import ABC, abstractmethod
from operation import Operation

class Transformation(Operation,ABC):

    ''' Classe creant un objet "Transformation" qui est une sous classe d'operation
            Attributes
            ----------
            variables : list
                  liste des variables sur lesquelles on veut faire des operations'''
    @abstractmethod
    def run(self,table):
        pass