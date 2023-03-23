from entites.Monsters.MonsterBase import MonsterBase

class Wolf(MonsterBase): 
    def __init__(self, life, attackPoints, strength):
        super().__init__("Wolf", life, attackPoints )
        
        self.strength = strength
