from valeurs_manquantes import ValeursManquantes
from table import Table
from transformation import Transformation
from sort import Sort

class Jointure(Transformation):
     """ Classe creant un objet "Jointure" permettant de réaliser la jointure. C'est une sous classe de Transformation donc de Operation
             Attributes
            ----------
            variable : str
                        variable commune aux deux tables qui sert d'identifiant pour réaliser la jointure
            
            table2 : Table
                       table avec laquelle on veut réaliser la jointure
            
            inner : booléen
                       booléen qui indique si l'on souhaite conserver ou supprimer les valeurs manquantes de la table jointe
    """
    
    def __init__(self, variable, table2, inner = False) -> None:
        self.variable = variable
        self.inner = inner       
        self.table2 = table2
        
        
    def run(self, table1:Table):
        '''La methode run réalise la jointure des deux tables
            
           Parameters
           ----------
           table1: Table
                table avec laquelle on veut réaliser la jointure

            Returns
            -------
            left_table : table
                retourne la table jointe 
            
            Examples
            ------- 
        '''
        
        if len(self.table2.data[self.variable]) >= len(table1.data[self.variable]):
            
            left_table = self.table2
            right_table = table1
            
        else:
            
            left_table = table1
            right_table = self.table2
        
        Sort(self.variable).run(left_table)
        Sort(self.variable).run(right_table)

        for var in right_table.variables:
            if var not in left_table.variables:
                left_table.data[var] = right_table.data[var]
        
                left_table.variables.append(var)    
        table1.data = left_table.data
        table1.variables = left_table.variables
        if self.inner:
            return ValeursManquantes(left_table.variables).run(left_table)
                
        return left_table
                

        
        
                
                
                
            
            
                
                
        
        
    
