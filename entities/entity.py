import glm


class Entity():
    
    def __init__(self, position: glm.vec3, health: int, speed: float) -> None:
        self.position = position
        self.health = health
        self.speed = speed
        
    def update(dt: float) -> None: ... # abstract function for children