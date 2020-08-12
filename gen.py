from random import randint
from point import Point, Inf


class Gen(Point):
    def __init__(self, point, ordre):
        self.point = point
        self.ordre = ordre

    def __eq__(self, G):
        return (self.curve, self.x, self.y, self.ordre) == (G.curve, G.x, G.y, G.ordre)

    def __str__(self):
        return '({}, {}), {}'.format(self.point.x, self.point.y, self.ordre)

    def get_modulo(self):
        return self.point.curve.p

    def gen_keys(self):
        inf = Inf(self.point.curve)
        priv = randint(1, self.ordre - 1)
        pub = self.point * priv
        while pub == inf:
            priv = randint(1, self.ordre - 1)
            pub = self.point * priv

        return priv, pub
