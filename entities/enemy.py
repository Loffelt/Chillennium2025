import glm
import random
from entities.entity import Entity
from entities.player import Player
from entities.mist_man import MistMan
from weapons.gun import Gun
from basilisk import Node


class Enemy(Entity):
    
    def __init__(self, game, position: glm.vec3, health: int, speed: float, spread: float, gun: Gun) -> None:
        self.health = health
        self.speed = speed
        self.spread = spread
        
        self.gun = gun
        self.game = game
        self.player: Player = game.player
        self.mist = MistMan(position)
        self.node = Node(
            position + (0, 1, 0),
            mesh = self.player.game.cylinder_mesh,
            scale = (0.5, 2, 0.5),
            collision = True,
            tags = ['enemy'],
            collision_group = 'entity'
        )
        
        self.position = position # added after bc mistman is used in the position property
        
    def update(self, dt: float) -> None:
        """
        Moves the enemt and controls shooting
        """
        self.move(dt)
        self.shoot(dt)
        
        # mist control
        self.mist.update(dt)
        
    def move(self, dt: float) -> None:
        """
        Main movement AI for enemies
        """
        direction = self.player.position - self.position
        if glm.length2(direction) < 1e-7: return
        direction = glm.normalize(direction)
        self.mist.forward = direction
        
        self.position += self.speed * dt * direction
        
    def shoot(self, dt: float) -> None:
        """
        Attempts to fire the gun
        """
        self.gun.update(dt)
        bullets = self.gun.shoot(self.mist.right_hand, self.player.position - (0, 0.5, 0) - self.position)
        if not bullets: return
        self.game.bullet_handler.bullets += bullets
        
    @property
    def position(self): return self._position
    
    @position.setter
    def position(self, value):
        self._position = value
        self.mist.position = value
        self.node.position = value + glm.vec3(0, 1, 0)