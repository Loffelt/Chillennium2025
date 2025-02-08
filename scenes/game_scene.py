from entities.enemy import Enemy
from basilisk import Node

class GameScene():

    def __init__(self) -> None:
        self.nodes: list[Node] = []
        self.enemies: list[Enemy] = []