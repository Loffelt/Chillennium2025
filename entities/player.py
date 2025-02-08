import glm
from basilisk import Node, Engine, pg, FollowCamera
from entities.entity import Entity
from weapons.gun import Gun



class Player(Entity):
    
    def __init__(self, position: glm.vec3, health: int, speed: float, gun: Gun, node: Node, engine: Engine) -> None:
        self.node = node
        super().__init__(position, health, speed)
        
        self.engine = engine
        self.camera: FollowCamera = self.engine.scene.camera

        self.gun = gun
        
    def update(self, dt: float) -> None:
        """
        
        """
        self.move()
        self.shoot()
        
    def move(self) -> None:
        """
        Sets the player's node's velocity to the input keys (wasd)
        """
        keys = self.engine.keys
        movement = self.camera.right * (keys[pg.K_d] - keys[pg.K_a]) + self.camera.horizontal * (keys[pg.K_w] - keys[pg.K_s])
        movement = self.speed * glm.normalize(movement)
        self.node.velocity = movement
        
    def shoot(self, dt: float) -> None:
        """
        Attemps to fire the player gun if the player is left clicking
        """
        self.gun.update(dt)
        if not self.engine.mouse.left_click: return
        self.gun.shoot(self.camera.forward)
        
    @property
    def position(self): return self._position
    
    @position.setter
    def position(self, value):
        self._position = value
        self.node.position = value
        