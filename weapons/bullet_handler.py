import glm
from weapons.bullet import Bullet
from basilisk import Scene, Material


class BulletHandler():
    
    def __init__(self, game) -> None:
        self.bullets: list[Bullet] = []
        self.game = game
        self.red = Material(color=(255, 0, 0))
        
    def update(self, dt: float) -> None:
        """
        Updates the positions of all bullets in the list
        """
        for bullet in self.bullets: 
            
            if bullet.is_dead: ...
            
            bullet.update(dt)
            particle_position = bullet.get_particle_position()
            if not particle_position: continue
            
            self.sight_scene.particle.add(
                position = particle_position,
                material = self.red,
                scale = 1,
                life = 0.2
            )
            
    @property
    def sight_scene(self) -> Scene: return self.game.sight_scene