import glm


class Bullet():
    
    def __init__(self, ricochet_remaining: int, damage: int, radius: float, path: glm.vec3, position: glm.vec3) -> None:
        self.ricochet_remaining = ricochet_remaining
        self.damage = damage
        self.radius = radius
        
        self.position = position
        self.path = path
        
    def update(self, dt: float) -> None:
        """
        Moves the bullet by the descrete time step
        """
        self.position += dt * self.path
        
    def ricochet(self, normal: glm.vec3) -> None:
        """
        Checks to see if the bullet is still alive after collision, updates moving vector if so
        """
        self.path = glm.reflect(self.path, normal)
        
    def __repr__(self) -> str:
        return f'Bullet - ricochet: {self.ricochet_remaining}, damage: {self.damage}, radius: {self.radius}'