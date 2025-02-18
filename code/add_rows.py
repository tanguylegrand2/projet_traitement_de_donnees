from table import Table
from transformation import Transformation

class Add_rows(Transformation):
    '''Classe creant un objet "Add_rows" permettant réaliser la concaténation de deux tables. C'est une sous classe de Transformation donc d'Operation
            Attributes
            ----------
            table : Table
                     table que l'on veut concaténer'''
    
    def __init__(self, table:Table) -> None:
        self.table = table
                
    def run(self, table2:Table):
        '''La methode run concaténe les deux tables
            
           Parameters
           ----------
           table2: Table
                table contenant les variables et leurs données

            Returns
            -------
            table2 : table
                retourne la table résultante de la concaténation des deux 

            Examples
            ------- '''
        for var in self.table.variables:
            table2.data[var].extend(self.table.data[var])
        return table2