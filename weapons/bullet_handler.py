import glm
from weapons.bullet import Bullet
from basilisk import Scene, Material


class BulletHandler():
    
    def __init__(self, game) -> None:
        self.bullets: list[Bullet] = []
        self.game = game
        
        self.materials = {
            'red' : Material(color=(255, 0, 0)),
            'black' : Material(color=(0, 0, 0))
        }
        
    def update(self, dt: float) -> None:
        """
        Updates the positions of all bullets in the list
        """
        for bullet in self.bullets: 
            
            if bullet.is_dead: ...
            
            # update bullet position and direction
            bullet_origin = glm.vec3(bullet.position)
            cast = self.sight_scene.raycast(bullet.position, bullet.path)
            if cast.node: print(cast.node.tags)
            d1 = glm.length2(cast.position - bullet_origin) if cast.node else None
            
            bullet.update(dt)
            
            d2 = glm.length2(bullet.position - bullet_origin)
            
            if d1 and d1 <= d2: # detect a ricochet
                if 'player' not in cast.node.tags: 
                    bullet.ricochet(cast.normal if glm.dot(cast.normal, bullet.path) < 0 else -cast.normal)
                    bullet.position = cast.position + cast.normal * 0.01
                    print(cast.normal)
            
            # update bullet particles
            particle_position = bullet.get_particle_position()
            if not particle_position: continue
            
            self.sight_scene.particle.add(
                position = particle_position,
                material = self.materials[bullet.color],
                scale = 0.1,
                life = 0.2
            )
            
            self.plain_scene.particle.add(
                position = particle_position,
                material = self.materials[bullet.color],
                scale = 0.1,
                life = 0.2
            )
            
    @property
    def sight_scene(self) -> Scene: return self.game.sight_scene
    @property
    def plain_scene(self) -> Scene: return self.game.plain_scene