import basilisk as bsk


class UI:
    def __init__(self, game):
        self.game = game

    def render(self):
        bsk.draw.circle(self.game.engine, (225,225,225), tuple((map(lambda x: int(x/2), self.game.engine.win_size))), 2)
        bsk.draw.circle(self.game.engine, (15, 15, 15 ), tuple((map(lambda x: int(x/2), self.game.engine.win_size))), 4)