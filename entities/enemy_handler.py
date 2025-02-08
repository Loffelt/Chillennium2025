import glm
from entities.enemy import Enemy
from basilisk import Engine, Material, Scene


class EnemyHandler():
    
    def __init__(self, engine: Engine) -> None:
        self.engine = engine
        self.enemies: list[Enemy] = []
        self.red = Material(
            color = (255, 0, 0)
        )
        
    def update(self, dt: float) -> None:
        """
        Updates all nodes and checks for death
        """
        to_remove = []
        
        for enemy in self.enemies:
            
            # run code if enemy has been killed
            if enemy.is_dead:
                enemy.on_death()
                to_remove.append(enemy)
                continue
            
            # enemy update and particles
            enemy.update(dt)
            
            particle_position = enemy.mist.get_particle_position()
            if not particle_position: continue
            self.scene.particle.add(
                position = particle_position,
                material = self.red,
                scale = 0.07
            )
            
        for enemy in to_remove: del enemy
        
    @property
    def scene(self) -> Scene: return self.engine.scene