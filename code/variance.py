from table import Table
from estimateur import Estimateur
from moyenne import Moyenne 
from valeurs_manquantes import ValeursManquantes

class Variance(Estimateur):
    '''Classe creant un objet "Variance" qui est une sous classe de de estimateur donc d'operation. Elle a pour but de calculer la variance de variables
            Attributes
            ----------
            variables : list
                     liste des variables dont on veut l'écart-type'''
    def __init__(self, variables) -> None:
        self.variables = variables       
            
    def run(self,table:Table):
        '''La methode run calcule la variance des variables choisies
            
           Parameters
           ----------
           table: Table
                table contenant les variables et leurs données

            Returns
            -------
            table
                retourne la table avec le nom des variables et la valeur de leur variance

            Examples
            --------
            
            >>> variance = Variance(['age', 'taille', 'poids', 'nom']).run(Table(False, variables=
                    ['age', 'taille', 'poids', 'nom'], data={'age': [12,7,9], 'taille' : ['mq', 170, 140], 'poids': ['mq', 'mq', 'mq'],'nom' : ['Laurent', 'Clara','Lucas']}))
            >>> variance.data
            {'age': 4.2222222222222, 'taille': 225.0, 'poids': "Il n'y a que des valeurs manquantes"}
           '''
        liste_variance = {var : None for var in self.variables}
        moy = Moyenne(self.variables).run(table)
        for k in self.variables:
            liste_carre = []
            table_pleine = ValeursManquantes([k]).run(table)
            try:
                liste_carre.extend(value**2 for value in table_pleine.data[k])
                liste_variance[k] = sum(liste_carre)/len(liste_carre) - moy.data[k]**2
            except TypeError:
                liste_variance[k] = 'Mauvais type de variable'
            except ZeroDivisionError:
                liste_variance[k] = "Il n'y a que des valeurs manquantes"
        return(Table(False, variables = [f"moyenne_de_{var}" for var in self.variables], data = liste_variance))
        
        