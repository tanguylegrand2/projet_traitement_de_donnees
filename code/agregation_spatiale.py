
import numpy as np
from table import Table
from moyenne import Moyenne
from fenetrage import Fenetrage
from sort import Sort
from transformation import Transformation

class Agregation_spatiale(Transformation):
        '''Classe creant un objet "Agregation_spatiale" permettant de réunir les observations d'une même région dans une unique observation. C'est une sous classe de Transformation donc d'Operation
            Attributes
            ----------
            variable : str
                     variable spatiale à partir de laquelle est réaliser l'agrégation'''
    
    
    def __init__(self, variable) -> None:
        self.variable = variable
        
        
    def run(self, table:Table):
        '''La methode run réalise l'aggration spatiale
            
           Parameters
           ----------
           table: Table
                table contenant les variables et leurs données

            Returns
            -------
            Table : table
                retourne la table avec les régions comme observations

            Examples
            ------- '''
    
        Sort(self.variable).run(table)   
          
        region = table.data[self.variable][0]
        var_list = table.variables
        var_list.remove(self.variable)
        data_result = {var : [] for var in var_list}
        data_result['region'] = []
        n=0
        for region in np.unique(table.data[self.variable]).tolist():
            variables = {var : [] for var in var_list}
            while region == table.data[self.variable][n] and n < len(table.data[self.variable]):
                for var in var_list:
                    variables[var].append(table.data[var][n])
                n+=1
            table_prov = Table(False, variables=var_list, data= variables)
            moyenne = Moyenne(var_list).run(table_prov).data
            for var in var_list:
                data_result[var].append(moyenne[var])

            data_result['region'].append(region)
        var_list.append(self.variable)
        return Table(False, variables=var_list, data=data_result, var_date=table.var_date, format_date=table.format_date)
    