import glm
from basilisk import Node
from scenes.game_scene import GameScene
from entities.enemy import Enemy
from weapons.gun import Gun
from scenes.helper import rect_wall_nodes


def test_scene(game) -> GameScene:
    gs = GameScene()
    
    platform = Node(
        position = (0, -1, 0),
        scale = (20, 1, 20),
        collision = True
    )
    
    box = Node(
        position=(1, 2, 3),
        physics=True,
        collision=True
    )
    
    walls = rect_wall_nodes(0, 0, 20, 20, 10)
    
    enemy = Enemy(
        game = game,
        position = glm.vec3(10, 0, -10), 
        health = 1, 
        speed = 3, 
        spread = 0.1,
        gun = Gun(
            game = game,
            count = 1,
            capacity = 3,
            spread = 0.05,
            cooldown = 1,
            ricochets = 1,
            damage = 1,
            radius = 0,
            color  = 'red',
        )
    )
    
    gs.enemies.append(enemy)
    gs.nodes.append(platform)
    gs.nodes.append(box)
    gs.nodes += walls
    
    return gs