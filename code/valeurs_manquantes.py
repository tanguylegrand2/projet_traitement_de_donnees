from table import Table
from transformation import Transformation


class ValeursManquantes(Transformation):
    """ Classe permettant de cibler et retirer les valeurs manquantes des données 
             Attributes
            ----------
            variables : list
                        liste des variables dont on veut cibler les valeurs manquantes 
    """
    
    def __init__(self, variables) -> None:
        self.variables = variables

    def run(self, table:Table):
        
        """La methode run permet d'enlever les valeurs manquantes des variables choisies

            Parameters
            ----------
            table: Table
                table contenant les variables et leurs données
            
            return
            ------
                table_pleine 
                    table qui ne contient pas de valeurs manquantes pour les variables choisis

            Examples
            --------
            
            >>> table = Table(False, variables= ['age', 'taille', 'poids', 'nom'], data={'age': [12,7,9], 'taille' : ['mq', 170, 140], 'poids': ['mq', 'mq', 'mq'] ,'nom' : ['Laurent', 'Clara','Lucas']})
            
            >>> ValeursManquantes(['taille', 'age'])
            >>> table.data
            {'age': [7,9], 'taille' : [170, 140], 'poids': ['mq', 'mq'],'nom' : ['Clara','Lucas']}  
            
            -------

        
        """
        liste_id = []
        for variable in self.variables:
            for k in range(len(table.data[variable])):
                if k not in liste_id and table.data[variable][k] == table.no_value:
                    liste_id.append(k)
        
        table_pleine = Table(False, variables=table.variables, data={variable : [] for variable in table.variables})
        for k in range(len(table.data[table.variables[0]])):
            if k not in liste_id:
                for variable in table.variables:
                    table_pleine.data[variable].append(table.data[variable][k])
        return table_pleine
    
    table = Table(False, variables= ['age', 'taille', 'poids', 'nom'], data={'age': [12,7,9], 'taille' : ['mq', 170, 140], 'poids': ['mq', 'mq', 'mq'] ,'nom' : ['Laurent', 'Clara', 'Lucas']})