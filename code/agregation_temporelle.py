import numpy as np
from datetime import datetime
from datetime import timedelta
from table import Table
from moyenne import Moyenne
from fenetrage import Fenetrage
from sort import Sort
from transformation import Transformation


class Agregation_temporelle(Transformation):
    '''Classe creant un objet "Agregation_temporelle" permettant de réunir les observations d'un même intervalle de temps dans une unique observation. C'est une sous classe de Transformation donc d'Operation
            Attributes
            ----------
            intervalle : datetime.detla
                      intervalle sur lequelle les observations vont être réunis

            variables : list
                     liste des variables que l'on veut garder'''
    
    def __init__(self, intervalle, variables) -> None:
        self.intervalle = intervalle
        self.variables = variables
        
    def run(self, table:Table):
        '''La methode run réalise l'aggrégation temporelle
            
           Parameters
           ----------
           table: Table
                table contenant les variables et leurs données

            Returns
            -------
            Table : table
                retourne la table avec les intervalles de temps comme observations et les variables  séléctionnées

            Examples
            ------- '''
    
        Sort(table.var_date).run(table)   
          
        t = table.data[table.var_date][0]
        var_list = self.variables
        variables = {var : [] for var in var_list}
        variables['temps_fenetrage'] = []
        n = 0
        
        while t < table.data[table.var_date][-1] and n < 100000:
            table_delais = Fenetrage(t, t + self.intervalle).run(table)
            variables['temps_fenetrage'].append(t)
            moyenne = Moyenne(self.variables).run(table_delais).data
            for var in self.variables:
                variables[var].append(moyenne[var])
            t = t + self.intervalle
            n+=1
        var_list.append('temps_fenetrage')
        
        table.variables = var_list
        table.data = variables
        table.var_date = 'temps_fenetrage'
        return Table(False, variables=self.variables, data=variables, var_date='temps_fenetrage', format_date=table.format_date)