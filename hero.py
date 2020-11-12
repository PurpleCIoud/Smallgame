import stats


class Player(stats.Stats):
    def __init__(self, name):
        super(Player, self).__init__(hp=100, att=5, defence=0, name=name, hit=50)

    def defeat(self):
        if self.hp <= 0:
            print(self.name, 'Has Died')


player = Player(name='Edward')
# player = Player(name=input('Players name:'))
