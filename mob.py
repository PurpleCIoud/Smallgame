import stats


class Rat(stats.Stats):
    def __init__(self):
        super().__init__(hp=5, att=2, defence=0, name='Rat', hit=30)


class Crow(stats.Stats):
    def __init__(self):
        super().__init__(hp=20, att=5, defence=0, name='Crow', hit=50)


rat = Rat()
crow = Crow()
