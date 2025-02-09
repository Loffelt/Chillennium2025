import glm
from basilisk import Node
from scenes.game_scene import GameScene
from scenes.helper import rect_room
from entities.enemy import Enemy
from weapons.gun import Gun

################################################################################
def level1(game) -> GameScene:
    gs = GameScene()
    
    gs.nodes += rect_room(0, -15, 15, 20, 10, game)
    
    gs.enemies += [Enemy(
        game, 
        glm.vec3(vec),
        ai=None
    ) for vec in ((10, 0, -15), (-10, 0, -20))]
    
    gs.nodes.append(Node(
        position = (0, 5, -25),
        scale = (1.5, 1.5, 1.5),
        collision=True,
        physics=True,
        mass = 10
    ))
    
    for enemy in gs.enemies: enemy.gun.cooldown = 1e8
    
    return gs


################################################################################
def level2(game) -> GameScene:
    gs = GameScene()
    
    gs.nodes += rect_room(0, -15, 10, 20, 10, game)
    
    gs.enemies.append(Enemy(
        game, 
        glm.vec3(5, 0, -25)
    ))
    
    return gs

################################################################################
def level3(game) -> GameScene:
    gs = GameScene()
    
    gs.nodes += rect_room(0, -15, 20, 20, 10, game)
    gs.nodes.append(Node(
        position = (0, 10, -15),
        scale = (5, 20, 5),
        collision = True
    ))
    
    gs.enemies.append(Enemy(
        game, 
        glm.vec3(10, 0, -25)
    ))
    
    gs.enemies.append(Enemy(
        game, 
        glm.vec3(-10, 0, -25)
    ))
    
    return gs

###############################################################################
def level4(game) -> GameScene:
    gs = GameScene()
    gs.guns.append(('smg', glm.vec3(1, 1, -10)))
    
    gs.nodes += rect_room(0, -5, 10, 10, 10, game)
    
    dummy = Enemy(
        game, 
        glm.vec3(-5, 0, -10),
        ai=None
    )
    
    dummy.gun.cooldown = 1e8
    
    gs.enemies.append(dummy)
    
    return gs
    
###############################################################################
def level5(game) -> GameScene:
    gs = GameScene()
    
    gs.nodes += rect_room(0, -15, 20, 20, 10, game)
    
    for x in range(-15, 20, 5):
        for z in range(-15, 20, 5):
            gs.nodes.append(Node(
                position = (x, 10, z - 15),
                scale = (1, 20, 1),
                collision = True
            ))
            
            if not x % 2 or z % 2 or z > -5: continue
            dummy = Enemy(
                game, 
                glm.vec3(x, 0, z - 15 + 2),
                ai='direct'
            )
            
            gs.enemies.append(dummy)
            
    return gs