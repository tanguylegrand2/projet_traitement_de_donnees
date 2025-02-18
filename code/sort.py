import numpy as np
from table import Table
from transformation import Transformation
from copy import deepcopy
class Sort(Transformation):
    '''Classe creant un objet "sort" permettant de trier des variables d'une table dans l'ordre ascendant . C'est une sous classe de transormation donc de operation
            Attributes
            ----------
            variables : str (on ne trie que selon une variable donc un str plutot qu'une liste de varible)'''
            
    def __init__(self, variable) -> None:
        self.variable = variable
        
    def run(self, table:Table):
        '''La methode run fait le tri des variables choisies dans l'ordre ascendant
            
           Parameters
           ----------
           table: Table
                table contenant les variables et leurs données

            return
            ------
                table: Table
                    la table trié selon la variable choisi
            
            Examples
            ------- 
            >>>  Sort('age').run(Table(False, variables=['age', 'taille', 'poids', 'nom', 'bazard'], data={'age': [12,7,9], 
                                                                             'taille' : ['mq', 170, 140], 
                                                                               'poids': ['mq', 'mq', 'mq'],
                                                                               'nom' : ['Laurent', 'Clara','Lucas'],
                                                                               'bazard': [12, 'Tomate', 'mq']}))
           '''
        table_copy = deepcopy(table.data)
        for k in range(len(table.data[self.variable])):
            if table.data[self.variable][k] == table.no_value:
                table.data[self.variable][k] = float('inf')
                
        rang = np.argsort(table.data[self.variable])
        for var in table.variables:
            for i,j in zip(range(len(rang)), rang):
                table.data[var][i] = table_copy[var][j]
            
        for k in range(len(table.data[self.variable])):
            if table.data[self.variable][k] == float('inf') :
                table.data[self.variable][k] = table.no_value
        
        return table
  