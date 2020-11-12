import random
import hero
import mob
# import stats

mobs = [hero.player, mob.rat, mob.crow]


class Attacks:
    def __init__(self, c, o):
        self.challenger = c
        self.opponent = o

    def win(self):
        if self.opponent.hp <= 0:
            print(self.opponent.name, 'Is dead', self.challenger.name, 'wins')

    def loss(self):
        if self.challenger.hp <= 0:
            print(self.challenger.name, 'Is dead', self.opponent.name, 'wins')

    def slash(self):
        roll = random.randint(0, 100)
        self.challenger.tp -= 1
        if self.challenger.hit <= roll:
            bef = self.opponent.hp
            self.opponent.hp -= (self.challenger.att-self.opponent.defence)
            aft = self.opponent.hp
            diff = bef-aft
            print(self.challenger.name, 'Used slash on', self.opponent.name, 'dealing', diff, 'Damage')
            print('Opponent rolled', roll, '/ 100 to score', self.challenger.hit)
            self.win()
        else:
            print(self.challenger.name, 'used slash on', self.opponent.name)
            print('and missed with a roll of', roll, '/ 100 to score', self.challenger.hit)
            self.counter_attack(roll)

    def counter_attack(self, roll):
        if roll <= 10:
            self.challenger.hp -= self.opponent.att
            print(self.challenger.name, 'rolled a', roll, 'so', self.opponent.name, 'Counter-attacked dealing',
                  self.opponent.att, 'damage')


def attack(a, b):
    game_master = Attacks(a, b)
    game_master.slash()


running = True
while running:

    attack(mobs[0], mobs[1])

