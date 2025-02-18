from datetime import datetime
import json
import gzip
import csv
import numpy as np


class Table: 
    
    """Classe permettant de modeliser un tableaux de doonnées, avec ses variables et ses données et des informations supplementaire pour certaines données particulière(date etc...)
            Attributes
            ----------
            importe : bool
                permet de savoir si on crer la tables a partir de données que l'on importe ou si o la rempli nous même
            chemin : str
                chemin permettant de recurer les fichiers 
            format_fichier : str
                format des fichiers que j'utilise 
            delimiter : str
                caractere qui delimite mes données a l'ineriers de ma table 
            variables : list
                listes des variables qui constitue ma table
            data : 
                dictionnaire des données par variable
            no_value : str
                valeur des valeurs manquantes du fichier si présent
            new_no_value:
                valeur choisi pour les valeurs manquantes 
            var_date : 
                variable que l'on precise comme étant une date 
            format_date: str
                format de la variable date
                        
                        
                        
"""    
    
    def __init__(self, importe:bool, chemin = None, format_fichier = None, delimiter =';', variables:list = None, data:dict = None, no_value ='mq', new_no_value = 'mq',  var_date = None, format_date = None) -> None:
        self.format_date = format_date
        self.var_date = var_date
        self.no_value = new_no_value
        if importe: 
            if format_fichier == 'csv.gz':
                self.importation_csv_gz(chemin, delimiter, no_value = no_value, new_no_value=self.no_value)
            if format_fichier == 'json.gz':
                self.importation_json_gz(chemin, new_no_value=self.no_value)
            if format_fichier == 'csv':
                self.importation_csv(chemin, delimiter, no_value = no_value, new_no_value=self.no_value)
        else:
            self.variables = variables
            self.data = data
        
        
        
    def importation_csv_gz(self, chemin:str, delimiter:str = ';', no_value = 'mq', new_no_value = 'mq'):
        
        """La methode importation_csv_gz permet d'importer les fichiers au format csv compressé en .gz

           Parameters
           ----------
            chemin: str
                le chemin du fichier

            delimiter : str
                le separateur des données à l'interieur du fichier

            no_value : str
                nom des valeurs manquantes 

            new_no_value
                nouveau nom des valeurs manquantes 
            
            """

        data = []
        with gzip.open(chemin, mode='rt') as gzfile:
            synopreader = csv.reader(gzfile, delimiter=delimiter)
            data.extend(iter(synopreader))
        col_names = data[0]
        lines = list(data[1:])
    
                
        dic =  dict({col_name : [line[col_pose] for line in lines] for col_pose, col_name in enumerate(col_names)})
        dic.pop('', None)
        self.variables = list(dic.keys())
        self.data = dic
            
        if no_value != new_no_value:
            for var in self.variables:
                for k in range(len(self.data[self.variables[0]])):
                    if self.data[var][k] == no_value:
                        self.data[var][k] = new_no_value
        self.no_value = new_no_value
        
        
    def importation_json_gz(self, chemin:str, new_no_value = 'mq'):
        
        """La methode importation_json_gz permet d'importer les fichiers au format json compressé en .gz

           Parameters
           ----------
            chemin: str
                le chemin du fichier

            new_no_value : str
                nouveau nom des valeurs manquantes 
            
            """
        with gzip.open(chemin, mode='rt') as gzfile :
            dic = json.load(gzfile)


        list_variable = list(map(list, [dic[k]['fields'].keys() for k in range(len(dic))]))
        variables = np.unique([item for sublist in list_variable for item in sublist])
        self.variables = variables.tolist()
        values ={ col_name : [] for col_name in variables}
        for line in dic:
            for col_name in variables:
                try:
                    values[col_name].append(line["fields"][col_name])
                except KeyError:
                    values[col_name].append(new_no_value)
        self.data = values
        self.no_value = new_no_value
        
        
    def importation_csv(self, chemin:str, delimiter:str = ';', no_value = 'mq', new_no_value = 'mq'):
        """La methode importation_csv_gz permet d'importer les fichiers au format csv 

           Parameters
           ----------
            chemin: str
                le chemin du fichier

            delimiter : str
                le separateur des données à l'interieur du fichier

            no_value : str
                nom des valeurs manquantes 

            new_no_value
                nouveau nom des valeurs manquantes

"""
        data = []
        with open(chemin, 'r') as file:
            reader = csv.reader(file, delimiter=delimiter)
                
                    
            data.extend(iter(reader))
            col_names = data[0]
            lines = list(data[1:])
            dic =  dict({col_name : [line[col_pose] for line in lines] for col_pose, col_name in enumerate(col_names)})
            dic.pop('', None)
            self.variables = list(dic.keys())
            self.data = dic
                
            if no_value != new_no_value:
                for var in self.variables:
                    for k in range(len(self.data[self.variables[0]])):
                        if self.data[var][k] == no_value:
                             self.data[var][k] = new_no_value
                    
        self.no_value = new_no_value
        
    def exportation(self,chemin:str, delimiter:str = ';'):
        """La methode exportation permet d'exporter les fichiers 

           Parameters
           ----------
            chemin: str
                le chemin du fichier

            delimiter : str
                le separateur des données à l'interieur du fichier


"""
        data_csv = [self.variables]

        data_csv.extend([list(self.data.values())[i][j] for i in range(len(list(self.data.values())))] for j in range(len(list(self.data.values())[0])))

        with open(chemin, 'w', newline='') as f:
            writer = csv.writer(f, delimiter=delimiter)
            for row in data_csv:
                writer.writerow(row)
        
                     
                     
                     
    def change_type(self, variables, var_type):
        
        """La methode change_type permet de changé le type d'une variable
           Parameters
           ----------
            variables : list 
                liste des variables dont on veut changer le type
            
            var_type: type
                nouveau type avec lequel on veut exprimer la variable

            return
            ------
                ne renvoie rien, cette methode fait une modification interne

            Examples
            ------- 
            >>> table = Table(False, variables=
                    ['age', 'taille', 'poids', 'nom'], data={'age': [12,7,9], 'taille' : ['mq', 170, 140], 'poids': ['mq', 'mq', 'mq'],'nom' : ['Laurent', 'Clara','Lucas']})
            >>> table.change_type(['taille], str)
            >>> table.data['taille']
            ['mq', '170', '140']
            


        """ 
        for var in variables:
            for k in range(len(self.data[var])):
                if self.data[var][k] != self.no_value:  
                    try:
                        self.data[var][k] = var_type(self.data[var][k])
                    except ValueError:
                        pass
        
                     
    def summary(self):
        """La methode summary permet de faire un resumé de la classe, donne le nom et le type des variables
            Parameters
            ----------
            return
            ------
                dict : dict
                    retourne le dictionnaire avec le nom et le type de chaque variable 
            Examples
            ------- 
            >>> table = Table(False, variables=
                    ['age', 'taille', 'poids', 'nom'], data={'age': [12,7,9], 'taille' : ['mq', 170, 140], 'poids': ['mq', 'mq', 'mq'],'nom' : ['Laurent', 'Clara','Lucas']})
            >>> table.summary()
            {'age': <class 'int'>, 'taille': <class 'str'>, 'poids': <class 'str'>, 'nom': <class 'str'>}
            """
        return {var : type(self.data[var][0]) for var in self.variables}
                
                
    def set_date(self, var_date, format_date):
        
        """La methode set_date permet de convertir, lorqu'on en a besoin, une variable choisit en date avec un format date unique. Cela permet d 'unfier le format des dates de nos fichiers 
            Parameters
            ----------
                var_date: str
                    nom de la variable que l'on considere comme date
                format_date : str
                    nouveau format date qui permet d'unifier les differentes dates
            return
            ------
                ne renvoie rien, cette methode fait une modification interne 
            """
            
        self.format_date = format_date
        self.var_date = var_date
        
        for k in range(len(self.data[var_date])):
            self.data[var_date][k] = datetime.strptime(self.data[var_date][k], format_date)
            
        
                
    def rename(self, var_name, new_var_name):
        
        """La methode rename permet de renommer une variable
            Parameters
            ----------
                var_name: str
                    nom de la variable dont on veut changer le nom
                new_var_name : str
                    nouveau nom de la variable 
            return
            ------
                ne renvoie rien, cette methode fait une modification interne

        """ 
        for k in range(len(self.variables)):
            if self.variables[k] == var_name:
                self.variables[k] = new_var_name
                
        self.data[new_var_name] = self.data.pop(var_name)
                
    