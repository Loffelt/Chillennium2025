import glm
from weapons.bullet import Bullet


class BulletHandler():
    
    def __init__(self) -> None:
        self.bullets: list[Bullet] = []
        
    def update(self, dt: float) -> None:
        """
        Updates the positions of all bullets in the list
        """
        for bullet in self.bullets: bullet.update(dt)