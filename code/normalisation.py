from ecart_type import Ecart_type
from table import Table
from transformation import Transformation
from centrage import Centrage

class Normalisation(Transformation):
    '''Classe creant un objet "normalisations" permettant de normaliser des variables d'une table. C'est une sous classe de transormation donc de operation
            Attributes
            ----------
            variables : list
                liste des variables à normaliser
        '''
    def __init__(self, variables) -> None:
        self.variables = variables        
        
    def run(self, table:Table):
        '''La methode run fait la normalisation des variables choisies
            
           Parameters
           ----------
           table: Table
                table contenant les variables et leurs données

            Returns
            -------
            table : Table
                table avec les variables choisis normalisées
                
            Examples
            ------- 
            >>> table = Table(False, variables=
                    ['age', 'taille', 'poids', 'nom'], data={'age': [12,7,9], 'taille' : ['mq', 170, 140], 'poids': ['mq', 'mq', 'mq'],'nom' : ['Laurent', 'Clara','Lucas']})
            >>> Normalisation(['taille', 'age']).run(table)
            >>> table.data
            {'age': [1.2977713690461, -1.135549947915338, -0.16222142113076282], 'taille': ['mq', 1.0, -1.0], 'poids': ['mq', 'mq', 'mq'], 'nom': ['Laurent', 'Clara', 'Lucas']}
            '''
        Centrage(self.variables).run(table)
        for var in self.variables:
            dic_ecart = Ecart_type(self.variables).run(table)    
            for k in range(len(table.data[var])):
                if table.data[var][k] != table.no_value: 
                    table.data[var][k] = table.data[var][k]/dic_ecart.data[var]
        return table
    