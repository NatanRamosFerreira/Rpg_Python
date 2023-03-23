from entites.Character.Character import Character
from entites.Monsters.Wolf import Wolf
from entites.Monsters.Goblin import Goblin

hero = Character("Rouba vagas", 250, 50)
# hero.attack(10)
# print(hero.__dict__)

goblin = Goblin(100, 25, 1)
# print(goblin.__dict__)

wolf = Wolf(200, 30, 1)

AttackHero = ()
selectMonster = ()
selectAttack = ()
selectCharacter = ()
selecionarMonstro = ()
try:
    selectCharacter = int(
        input("Bem Vindo ao RPG , selecione uma classe, 1 = Hero, 2 = Monstro : "))

    if selectCharacter == 1:
        print('Você selecionou a classe hero! ')
        selectMonster = int(input('Você que atacar um Monstro  ? 1 = sim 2 = não : '))

    elif selectCharacter == 2:
        selecionarMonstro = int(input("Você que ser um 1 = lobo ou 2 = goblin : "))
        print('Você selecionou a o seu monstro')
        AttackHero = int(input('Você que atacar o  Rouba Vagas ? 1 = sim 2 = não : '))

    if AttackHero == 1:
        hero.attack(50)
        print(hero.statusLife())

    elif AttackHero == 2:
        print('Você escolheu não atacar')

    if selectMonster == 1:
        selectAttack = int(input('voce que atacar o goblin ou o lobo  ? 1 = goblin 2 = Lobo : '))

    elif selectMonster == 2:
        print('Você escolheu não atacar')
    
    if selectAttack == 1:
        goblin.attack(25)
        print(goblin.statusLife())

    elif selectAttack == 2:
        wolf.attack(30)
        print(wolf.statusLife())

    elif selectCharacter not in (1,2):
        raise ValueError and NameError
    
    elif selectAttack not in (1,2):
        raise ValueError and NameError
    
    elif selectMonster not in (1,2):
        raise ValueError and NameError
    
    elif AttackHero not in (1,2):
        raise ValueError and NameError


except (ValueError, NameError):
    print('Você precisa digitar o número 1 ou 2')

