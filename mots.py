class Mot :
    def __str__(self): 
        return "Le mot "+ self.text + " est un " + self.type + " pour la faiblesse " + self.weakness 

    def __init__(self,text,type,weakness): 
        self.type = type
        self.weakness = weakness
        self.text = text