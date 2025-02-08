from .bullet import Bullet
import glm
import random


class Gun():
    
    def __init__(self, count: int, capacity: int, cooldown: float, spread: float, bullet: Bullet) -> None:
        self.count = count
        self.capacity = capacity
        self.cooldown = cooldown
        self.spread = spread
        
        self.time = cooldown
        
        def get_bullet(path: glm.vec3) -> Bullet: return Bullet(bullet.ricochet_remaining, bullet.damage, bullet.radius, path)
        self.get_bullet = get_bullet
        
    def update(self, dt: float) -> None:
        """
        Updates cooldown timer
        """
        self.time += dt
    
    def shoot(self, forward: glm.vec3) -> list:
        """
        Returns a list of fired bullets if the gun is shot
        """
        if self.time < self.cooldown: return
        self.time = 0
        
        bullets = []
        for _ in range(self.count):
            rotation = glm.quat([random.uniform(-self.spread, self.spread) for _ in range(3)])
            path = rotation * forward
            bullets.append(self.get_bullet(path))
            
        return bullets
    
    def __repr__(self) -> str:
        return f'Gun - bullets: {self.count}, capacity: {self.capacity}, cooldown: {self.cooldown}, spread: {self.spread}'