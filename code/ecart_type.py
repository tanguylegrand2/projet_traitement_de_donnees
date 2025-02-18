from math import sqrt
from table import Table
from estimateur import Estimateur
from variance import Variance
from copy import deepcopy

class Ecart_type(Estimateur):
    '''Classe creant un objet "ecart type" permettant de calculer l'ecart type d'une variables d'une table. C'est une sous classe de estimateur donc d'operation
            Attributes
            ----------
            variables : list
                     liste des variables dont on veut l'écart-type'''
            
    def __init__(self, variables) -> None:
        self.variables = variables
        
    def run(self,table:Table):
        '''La methode run calcule l'écart type des variables choisies
            
           Parameters
           ----------
           table: Table
                table contenant les variables et leurs données

            Returns
            -------
            ecart_type : table
                retourne la table avec le nom des variables et la valeur de leurs écart-types

            Examples
            ------- 
            >>>  Ecart_type(['age', 'taille', 'poids']).run(Table(False, variables=['age', 'taille', 'poids', 'nom', 'bazard'], data={'age': [12,7,9], 
                                                                             'taille' : ['mq', 170, 140], 
                                                                               'poids': ['mq', 'mq', 'mq'],
                                                                               'nom' : ['Laurent', 'Clara','Lucas'],
                                                                               'bazard': [12, 'Tomate', 'mq']}))
            {'age': 2.0548046676563256, 'taille': 15.0, 'poids': "Il n'y a que des valeurs manquantes"}

            '''
        variance = Variance(self.variables).run(table)
        ecart_type = deepcopy(variance)
        for k in self.variables:
            if isinstance(variance.data[k], float) :
                ecart_type.data[k] = sqrt(variance.data[k])
        return ecart_type
        
        