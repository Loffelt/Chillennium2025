from weapons.bullet import Bullet
from basilisk import Node
import glm
import random


class Gun():
    
    def __init__(self, game, count: int, capacity: int, cooldown: float, spread: float, ricochets: int, damage: int, radius: float, color: str) -> None:
        self.game = game
        self.count = count
        self.capacity = capacity
        self.cooldown = cooldown
        self.spread = spread
        
        self.time = cooldown
        
        def get_bullet(position: glm.vec3, path: glm.vec3) -> Bullet: 
            cylinder = Node(
                position, 
                scale = (radius, 0.01, radius),
                mesh = self.game.cylinder_mesh,
                rotation = glm.quatLookAt(path, (0, 1, 0))
            )
            self.game.dimension_scene.add(cylinder)
            return Bullet(ricochets, damage, radius, color, cylinder, path, position)
        self.get_bullet = get_bullet
        
    def update(self, dt: float) -> None:
        """
        Updates cooldown timer
        """
        self.time += dt
    
    def shoot(self, position: glm.vec3, forward: glm.vec3) -> list:
        """
        Returns a list of fired bullets if the gun is shot
        """
        if self.time < self.cooldown: return
        self.time = 0
        
        bullets = []
        for _ in range(self.count):
            path = glm.normalize(forward + [random.uniform(-self.spread, self.spread) for _ in range(3)])
            bullets.append(self.get_bullet(position, path))
            
        return bullets
    
    def __repr__(self) -> str:
        return f'Gun - bullets: {self.count}, capacity: {self.capacity}, cooldown: {self.cooldown}, spread: {self.spread}'