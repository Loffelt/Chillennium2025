import glm
from basilisk import Node, Scene
from scenes.game_scene import GameScene
from entities.enemy import Enemy
from weapons.gun import Gun
from weapons.bullet import Bullet


def test_scene(player) -> GameScene:
    gs = GameScene()
    
    platform = Node(
        position = (0, -5, 0),
        scale = (20, 1, 20),
        collision = True
    )
    
    enemy = Enemy(
        position = glm.vec3(10, -4, -10), 
        health = 1, 
        speed = 3, 
        spread = 0.1,
        gun = Gun(
            count = 1,
            capacity = 3,
            spread = 0.05,
            cooldown = 1,
            bullet = Bullet(
                ricochet_remaining = 1,
                damage = 1,
                radius = 0
            )
        ),
        player = player
    )
    
    gs.enemies.append(enemy)
    gs.nodes.append(platform)
    
    return gs