import glm
from basilisk import Node
from scenes.game_scene import GameScene
from scenes.helper import rect_wall_nodes
from entities.enemy import Enemy
from weapons.gun import Gun


def level1(game) -> GameScene:
    gs = GameScene()
    
    gs.nodes.append(Node(
        position=(0, -1, 25),
        scale = (15, 1, 25)
    ))