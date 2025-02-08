import glm
from basilisk import Node, Scene
from scenes.game_scene import GameScene
from entities.enemy import Enemy
from weapons.gun import Gun
from weapons.bullet import Bullet


def test_scene(game) -> GameScene:
    gs = GameScene()
    
    platform = Node(
        position = (0, -5, 0),
        scale = (20, 1, 20),
        collision = True
    )
    
    walls = [Node(
        position = (data[0], 5, data[1]), 
        scale = (data[2], 10, data[3]),
        collision = True 
    ) for data in ((20, 0, 1, 20), (-20, 0, 1, 20), (0, 20, 20, 1), (0, -20, 20, 1))]
    
    # enemy = Enemy(
    #     game = game,
    #     position = glm.vec3(10, -4, -10), 
    #     health = 1, 
    #     speed = 3, 
    #     spread = 0.1,
    #     gun = Gun(
    #         game = game,
    #         count = 1,
    #         capacity = 3,
    #         spread = 0.05,
    #         cooldown = 1,
    #         ricochets = 1,
    #         damage = 1,
    #         radius = 0,
    #         color  = 'red',
    #     )
    # )
    
    # gs.enemies.append(enemy)
    gs.nodes.append(platform)
    gs.nodes += walls
    
    return gs