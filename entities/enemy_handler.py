import glm
from entities.enemy import Enemy


class EnemyHandler():
    
    def __init__(self) -> None:
        self.enemies: list[Enemy] = []
        
    def update(self, dt: float) -> None:
        """
        Updates all nodes and checks for death
        """
        to_remove = []
        
        for enemy in self.enemies:
            if enemy.is_dead:
                enemy.on_death()
                to_remove.append(enemy)
                continue
            
        for enemy in to_remove: del enemy