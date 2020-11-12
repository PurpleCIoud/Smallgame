class Stats:
    def __init__(self, hp, att, defence, name, hit):
        self.hp = hp
        self.att = att
        self.defence = defence
        self.name = name
        self.hit = 100-hit
        self.tp = 2
