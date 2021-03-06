import random
class Character:
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
    def attack(self, enemy):
        if self == hero:
            num = random(1,5)
            if num == 5:
                enemy.health -= 2*self.power
            else:
                enemy.health -= self.power
            print('You do {} damage to the goblin.'.format(self.power))
            if enemy.health <= 0:
                print('The goblin is dead')
        else:
            enemy.health -= self.power
            print('The goblin does {} damage to you.'.format(self.power))
            if enemy.health <= 0:
                print('You are dead...scrub')
        
class Hero(Character):
    def __init__(self, health, power):
        self.health = health
        self.power = power
    def print_status(self):
        print("You have {} health and {} power.".format(self.health, self.power))
    
class Goblin(Character):
    def __init__(self, health, power):
        self.health = health
        self.power = power
    def print_status(self):
        print("The goblin has {} health and {} power.".format(self.health, self.power))

class Medic(Character):

    
hero = Hero(10, 5)
goblin = Goblin(6, 2)
medic = Medic(10,2)

while goblin.alive() and hero.alive():
    print()
    print("What do you want to do?")
    print("1. fight goblin")
    print("2. do nothing")
    print("3. flee")
    print("> ", end=' ')
    raw_input = input()
    if raw_input == "1":
        hero.attack(goblin)
        if goblin.alive():
            goblin.attack(hero)
    elif raw_input == "2":
        pass
    elif raw_input == "3":
        print("Goodbye.")
        break
    else:
        print("Invalid input {}".format(raw_input))


