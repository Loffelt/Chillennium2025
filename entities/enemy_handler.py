import glm
import random
from entities.enemy import Enemy
from basilisk import Material, Scene, pg
from weapons.gun import Gun


class EnemyHandler():
    
    def __init__(self, game) -> None:
        self.game = game
        self.enemies: list[Enemy] = []
        self.red = Material(color = (255, 0, 0))
        
    def update(self, dt: float) -> None:
        """
        Updates all nodes and checks for death
        """
        to_remove = []
        
        # print(len(self.enemies))
        
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
            self.sight_scene.particle.add(
                position = particle_position,
                material = self.red,
                scale = random.uniform(.8, 1.2),
                life = 0.2,

            )
            
        for enemy in to_remove:
            self.enemies.remove(enemy)
            self.game.sight_scene.remove(enemy.node)
        
        if self.game.engine.keys[pg.K_e] and not self.game.engine.previous_keys[pg.K_e]:
            self.enemies.append(Enemy(
                game = self.game,
                position = glm.vec3([random.uniform(-7, 7) for _ in range(3)]),
                health = 1,
                speed = 3, 
                spread = 0.1,
                gun = Gun(
                    game = self.game,
                    count = 1,
                    capacity = 3,
                    spread = 0.05,
                    cooldown = 1,
                    ricochets = 1,
                    damage = 1,
                    radius = 0,
                    color  = 'red',
                )
            ))
            
    def get_enemy_by_node(self, node) -> Enemy:
        for enemy in self.enemies:
            if enemy.node == node: return enemy
        return None
        
    @property
    def sight_scene(self) -> Scene: return self.game.sight_scene