import glm
from basilisk import Node, Scene
from scenes.game_scene import GameScene

def test_scene() -> GameScene:
    gs = GameScene()
    
    platform = Node(
        position = (0, -5, 0),
        scale = (10, 1, 10),
        collision = True
    )
    
    gs.nodes.append(platform)
    
    return gs