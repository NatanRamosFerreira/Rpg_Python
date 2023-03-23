from ..LivingBeing import LivingBeing

class Character(LivingBeing):
    def __init__(self,name, life, attackPoints):
        super().__init__(life, attackPoints)
        
        self.name = name
        