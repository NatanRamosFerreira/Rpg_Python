from ..LivingBeing import LivingBeing

class MonsterBase(LivingBeing):
    def __init__(self, type, life, attackPoints):
        super().__init__(life, attackPoints)
        
        self.type = type


