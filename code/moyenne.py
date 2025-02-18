from table import Table
from estimateur import Estimateur
from valeurs_manquantes import ValeursManquantes

class Moyenne(Estimateur):
    """ Classe creant un objet "moyenne" permettant de calculer la moyennes d'une variables d'une table. C'est une sous classe de de estimateur donc d'operation
            Attributes
            ----------
            variables : list
                        liste des variables dont on veut la moyenne
    """
    
    def __init__(self, variables) -> None:
        self.variables = variables
        
        
    def run(self,table:Table):
        """La methode run calcule la moyennes des variables choisies

           Parameters
           ----------
           table: Table
                table contenant les variables et leurs données

            Returns
            -------
            frotable
                retourne la table avec le nom des variables et leurs moyennes

            Examples
            ------- 
            >>> table = Table(False, variables=['age', 'taille', 'poids', 'nom'], data={'age': [12,7,9], 'taille' : ['mq', 170, 140], 'poids': ['mq', 'mq', 'mq'],'nom' : ['Laurent', 'Clara','Lucas']})
            >>> Moyenne(['taille', 'age']).run(table).data
            {'taille': 155.0, 'age': 9.333333333333334}
        """
        
        liste_moy={var : None for var in self.variables}
        for k in self.variables:
            table_pleine = ValeursManquantes([k]).run(table)
            try:
                table_pleine.change_type([k], float)
                liste_moy[k] = sum(table_pleine.data[k])/len(table_pleine.data[k])
            except TypeError:
                liste_moy[k] = 'Mauvais type de variable'
            except ZeroDivisionError:
                liste_moy[k] = "Il n'y a que des valeurs manquantes"
            
        return(Table(False, variables = [f"moyenne_de_{var}" for var in self.variables], data = liste_moy))
        