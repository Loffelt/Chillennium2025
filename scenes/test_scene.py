import glm
from basilisk import Node
from scenes.game_scene import GameScene
from entities.enemy import Enemy
from weapons.gun import Gun
from scenes.helper import rect_room


def test_scene(game) -> GameScene:
    gs = GameScene()
    
    box = Node(
        position=(1, 5, 3),
        physics=True,
        collision=True,
        material=game.green
    )
    
    walls = rect_room(0, 0, 20, 20, 10)
    
    # enemy = Enemy(
    #     game = game,
    #     position = glm.vec3(10, 0, -10), 
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
    gs.nodes.append(box)
    gs.nodes += walls
    
    return gs