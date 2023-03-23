from .MonsterBase import MonsterBase

class Goblin(MonsterBase):
    def __init__(self, life, attackPoints, intelligence):
        super().__init__("Goblin", life, attackPoints)
        
        self.intelligence = intelligence
        