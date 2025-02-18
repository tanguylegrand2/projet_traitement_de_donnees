from datetime import datetime
from moyenne import Moyenne
from table import Table
from transformation import Transformation
from sort import Sort

class MoyenneGlissante(Transformation):
    
    '''Classe creant un objet "moyenne glissante" permettant de faire la moyennes d'une variable sur un intervalle de temps choisi. C'est une sous classe de transormation donc de operation
            Attributes
            ----------
            variables : list
                    liste des variables dont on veut la moyenne
            intervalle : 
                    intervalle de temps sur lequel on veut faire la moyenne 
    '''
    
    def __init__(self, intervalle:datetime, variables) -> None:
        self.intervalle = intervalle
        self.variables = variables
        
    def run(self, table:Table):
        
        """La methode run calcule la moyenne glissante des variables choisies sur l'intervalle de temps choisi

           Parameters
           ----------
           table: Table
                table contenant les variables et leurs données

            Returns
            -------
            table
                la table d'entrée à laquelle s'ajoute les variables de moyennes glissantes

            Examples
            ------- 
            >>> from datetime import date
            >>> from datetime import timedelta
            >>> table = Table(False, variables=
                    ['age', 'taille', 'poids', 'jour'], data={'age': [12,7,9], 'taille' : ['mq', 170, 140], 'poids': ['mq', 'mq', 'mq'],'jour' : [ date(2019, 4, 13),  date(2019, 4, 14), date(2012, 4, 13)]}, var_date='jour')
            >>> MoyenneGlissante(timedelta(days=5, seconds=0, microseconds=0), ['taille']).run(table).data 
            {'age': [9, 12, 7], 'taille': [140, 'mq', 170], 'poids': ['mq', 'mq', 'mq'], 'jour': [datetime.date(2012, 4, 13), datetime.date(2019, 4, 13), datetime.date(2019, 4, 14)], 'moyenne_glissante_taille': [140.0, 170.0, 170.0]}
        """
        Sort(table.var_date).run(table)   
        for var in self.variables:
            table.variables.append(f"moyenne_glissante_{var}")
            table.data[f"moyenne_glissante_{var}"] = []
            
        for i in range(len(table.data[table.var_date])):
            data = {var : [] for var in self.variables}
            for j in range(len(table.data[table.var_date])):
                if -self.intervalle <= table.data[table.var_date][i] - table.data[table.var_date][j] <= self.intervalle:
                    for var in self.variables:
                        
                        data[var].append(table.data[var][j])
            moy = Moyenne(self.variables).run(Table(False, variables=self.variables, data=data))
            for var in self.variables:
                table.data[f"moyenne_glissante_{var}"].append(moy.data[var])
        
        
        return table
                
                