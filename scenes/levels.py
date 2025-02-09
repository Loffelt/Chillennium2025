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
    
    for enemy in gs.enemies: enemy.gun.cooldown = 1e8
    
    box = Node(
        position=(1, 5, -3),
        physics=True,
        collision=True,
        material=game.blue
    )
    
    gs.nodes.append(box)
    
    return gs