from datetime import datetime
from table import Table
from copy import deepcopy
from transformation import Transformation

class Fenetrage(Transformation):
    '''Classe creant un objet "Fenetrage" permettant de selectionner les observations comprises dans un intervalle de temps. C'est une sous classe de Transformation donc de Operation
            Attributes
            ----------
            date_debut : datetime
                date à partir de laquelle on conserve les observations
            
            date_fin : datetime
                 date jusqu'à laquelle on conserve les observations
        '''
    def __init__(self, date_debut:datetime, date_fin:datetime) -> None:
        self.date_debut = date_debut
        self.date_fin = date_fin
    
    def run(self, table:Table):
          '''La methode run réalise le fenêtrage de la table
            
           Parameters
           ----------
           table1: Table
                table contenant les variables et leurs données

            Returns
            -------
            Table : table
                table ou seule les observations contenues dans l'intervalle de temps sont conservées
            
            Examples
            ------- 
        '''
        table_fenetre = deepcopy(table)
        dic_var = {var: [] for var in table.variables}
        for k in range(len(table.data[table.var_date])):
            if  self.date_debut < table.data[table.var_date][k] < self.date_fin:
                for var in table.variables:
                    dic_var[var].append(table.data[var][k])
            
        
        return Table(False, variables=table.variables, data=dic_var, var_date='temps_fenetrage', format_date=table.format_date)
                     
     