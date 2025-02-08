import glm
from weapons.bullet import Bullet
from basilisk import Scene, Material, Node
import random


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
        to_remove = []
        
        for bullet in self.bullets: 
            
            # update bullet position and direction
            bullet_origin = glm.vec3(bullet.position)
            cast = self.sight_scene.raycast(bullet.position, bullet.path)
            d1 = glm.length2(cast.position - bullet_origin) if cast.node else None
            
            bullet.update(dt)
            
            d2 = glm.length2(bullet.position - bullet_origin)
            
            if d1 and d1 <= d2: # detect a ricochet/collision
                if 'player' not in cast.node.tags and 'enemy' not in cast.node.tags: 
                    bullet.ricochet(cast.normal if glm.dot(cast.normal, bullet.path) < 0 else -cast.normal)
                    bullet.position = cast.position + cast.normal * 0.01
                    
                    # remove bullet node so the viewer is the sole owner, replace node
                    if bullet.ricochet_remaining >= 0 and bullet.color == 'black': 
                        bullet.last_hit = cast.position
                        bullet.node = Node(
                            position = bullet.position, 
                            scale = (bullet.radius, 0.01, bullet.radius),
                            mesh = self.game.cylinder_mesh
                        )
                        
                        self.game.dimension_scene.add(bullet.node)
                    
                elif 'enemy' in cast.node.tags: bullet.ricochet_remaining = -1
                    
                if bullet.is_dead: # bullet on death sequence
                    to_remove.append(bullet)
                    self.particle_splatter(cast.position, cast.normal, bullet.color)
            
            # always add the bullet particle so player can see where its going
            self.add_bullet_particles(bullet)
        
        # remove dead bullets from the bullet handler
        for bullet in to_remove: self.bullets.remove(bullet)
        
    def add_bullet_particles(self, bullet: Bullet) -> None:
        
        # update bullet particles
            particle_position = bullet.get_particle_position()
            if not particle_position: return
            
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
            
    def particle_splatter(self, position: glm.vec3, normal: glm.vec3, color: tuple) -> None:
        for _ in range(10):
            self.sight_scene.particle.add(
                position = position,
                material = self.materials['red'],
                # velocity = normal,
                # scale = random.uniform(0.2, 0.5),
                life = 0.2
            )
            
    @property
    def sight_scene(self) -> Scene: return self.game.sight_scene
    @property
    def plain_scene(self) -> Scene: return self.game.plain_scene