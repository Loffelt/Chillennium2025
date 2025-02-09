import glm
from basilisk import Node
from entities.enemy import Enemy
from weapons.gun import Gun
    
def rect_room(centerx, centerz, width, depth, height) -> list[Node]:
    nodes = [Node(
        position = (data[0], -1 + height, data[1]), 
        scale = (data[2], height, data[3]),
        collision = True 
    ) for data in (
        (centerx + width - 1, 0, 1, depth), 
        (centerx - width + 1, 0, 1, depth), 
        (0, centerz + depth - 1, width, 1), 
        (0, centerz - depth + 1, width, 1)
    )]
    
    nodes += [Node(
        scale = (width, 1, depth),
        collision = True,
        position=(0, y, 0)
    ) for y in (-1, height)]
    return nodes