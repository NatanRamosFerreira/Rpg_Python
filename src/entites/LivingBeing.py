#
class LivingBeing:
    def __init__(self, life, attackPoints):
        self.life = life
        self.attackPoints = attackPoints

    def attack(self, damageSuffered):
        self.life -= damageSuffered

    def statusLife(self):
        print("A vida Atual É :", self.life)
