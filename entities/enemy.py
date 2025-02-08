import glm
from .entity import Entity
from .player import Player
from ..weapons.gun import Gun


class Enemy(Entity):
    
    def __init__(self, position: glm.vec3, health: int, speed: float, spread: float, gun: Gun, player: Player) -> None:
        super().__init__(position, health, speed)
        self.spread = spread
        
        self.gun = gun
        self.player = player
        
    def update(self, dt: float) -> None:
        """
        Moves the enemt and controls shooting
        """
        self.move(dt)
        self.shoot(dt)
        
    def move(self, dt: float) -> None:
        """
        Main movement AI for enemies
        """
        
        
    def shoot(self, dt: float) -> None:
        """
        Attempts to fire the gun
        """
        self.gun.update(dt)
        self.gun.shoot(self.player.position - self.position)