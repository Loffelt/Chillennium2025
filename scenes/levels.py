import glm
from basilisk import Node
from scenes.game_scene import GameScene
from scenes.helper import rect_room
from entities.enemy import Enemy
from weapons.gun import Gun


def level1(game) -> GameScene:
    gs = GameScene()
    
    gs.nodes += rect_room(0, -15, 15, 20, 10)
    
    gs.enemies += [Enemy(
        game, 
        glm.vec3(vec),
        ai=None
    ) for vec in ((10, 0, -15), (-10, 0, -20))]
    
    return gs