import basilisk as bsk
from .transition import Transition


class UI:
    transitions: list[Transition]
    """"""
    def __init__(self, game):
        self.game = game

        self.transitions = []

    def render(self):
        # Cross
        bsk.draw.circle(self.game.engine, (225,225,225), tuple((map(lambda x: int(x/2), self.game.engine.win_size))), 2)
        bsk.draw.circle(self.game.engine, (15, 15, 15 ), tuple((map(lambda x: int(x/2), self.game.engine.win_size))), 4)

        # Transitions
        i = 0
        while i < len(self.transitions):
            transition = self.transitions[i]
            transition.render()
            if not transition.running: self.transitions.remove(transition)
            i += 1

        

    def add_transition(self, duration: float=1.0):
        self.transitions.append(Transition(self.game.engine, duration))