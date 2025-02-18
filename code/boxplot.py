import matplotlib.pyplot as plt
from valeurs_manquantes import ValeursManquantes
from estimateur import Estimateur
from table import Table


class Boxplot(Estimateur):
    '''Classe creant un objet "boxplot" permettant de representer un boxplot des variables d'une table. C'est une sous classe de Estimateur donc d'Operation
            Attributes
            ----------
            variables : list
                     liste des variables dont on veut le boxplot'''
    def __init__(self, variables) -> None:
        self.variables = variables
        
    def run(self,table:Table):
        '''La methode run fait le boxplot des variables choisies
            
           Parameters
           ----------
           table: Table
                table contenant les variables et leurs données

            Returns
            -------
            objet  matplotlib.boxplot
                le boxplot des variable choisies

            Examples
            ------- 
            >>>  Boxplot(['age', 'taille', 'poids']).run(Table(False, variables=['age', 'taille', 'poids', 'nom', 'bazard'], data={'age': [12,7,9], 
                                                                             'taille' : ['mq', 170, 140], 
                                                                               'poids': ['mq', 'mq', 'mq'],
                                                                               'nom' : ['Laurent', 'Clara','Lucas'],
                                                                               'bazard': [12, 'Tomate', 'mq']}))
           '''

        d = [ValeursManquantes([var]).run(table).data[var] for var in self.variables]
        plt.boxplot(d)
        plt.show()

