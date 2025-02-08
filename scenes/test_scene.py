import glm
from basilisk import Node, Scene

def test_scene() -> list[Node]:
    platform = Node(
        position = (0, -5, 0),
        scale = (10, 1, 10),
        collision = True
    )
    
    return [platform]