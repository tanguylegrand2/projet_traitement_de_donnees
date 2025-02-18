from moyenne import Moyenne
from transformation import Transformation
from table import Table



class Centrage(Transformation):
    '''Classe creant un objet "Centrage" permettant de centrer les variables d'une table. C'est une sous classe de Transformation donc d'Operation
            Attributes
            ----------
            variables : list
                     liste des variables qu'on veut centrer'''
    
    def __init__(self, variables) -> None:
        self.variables = variables
        
    def run(self,table:Table):
         '''La methode run fait le centrage des variables choisies
            
           Parameters
           ----------
           table: Table
                table contenant les variables et leurs données

            Returns
            -------
            table : Table
                table avec les variables choisis centrées'''
        for var in self.variables:
            dic_moyenne = Moyenne(self.variables).run(table)    
            for k in range(len(table.data[var])):
                if table.data[var][k] != table.no_value: 
                    table.data[var][k] = table.data[var][k] - dic_moyenne.data[var]
        return table