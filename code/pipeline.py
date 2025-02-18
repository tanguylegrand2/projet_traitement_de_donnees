class Pipeline():
    
    '''Classe creant un objet "pipeline" permettant de combiner de façon intuitive les Operations des autres du classes du paquet 
            Attributes
            ----------
            operations : list
                liste des operation à faire'''
                
                
    def __init__(self):
        self.operations=[]
    
    def add_operation(self,operation):
        
        '''Methode qui permet d'ajouter une opération à la liste de celles à faire
            
           Parameters
           ----------
           operation: Operation
                Objet operation qui est l'operation qu'on souhaite ajouter à la liste

                '''
                
        self.operations.append(operation)
        
    def process(self,table):
        
        '''Methode lance succesivement les operations de la liste sur la table choisie
            
           Parameters
           ----------
           table: Table
                la table sur laquelle on souhaite faire les operations 

            Return
            ------
            liste des resultat de chaques operations sur la table
                '''
                
        return [operation.run(table) for operation in self.operations]