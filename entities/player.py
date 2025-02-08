import glm
from basilisk import Node, Engine, pg, FollowCamera
from entities.entity import Entity
from weapons.gun import Gun


class Player(Entity):
    
    def __init__(self, position: glm.vec3, health: int, speed: float, gun: Gun, node: Node, engine: Engine) -> None:
        self.node = node
        super().__init__(position, health, speed)
        
        self.engine = engine

        self.gun = gun
        
    def update(self, dt: float) -> None:
        """
        
        """
        self.node.rotation = glm.conjugate(glm.quatLookAt(glm.vec3(self.camera.forward.x, 0, self.camera.forward.z), self.camera.UP))
        self.move()
        self.shoot(dt)
        
    def move(self) -> None:
        """
        Sets the player's node's velocity to the input keys (wasd)
        """
        self._position = self.node.position.data - glm.vec3(0, 2, 0)
        
        # contraol the player's position by adding velocity to the node
        keys = self.engine.keys
        x, z = self.camera.forward.x, self.camera.forward.z
        movement = self.camera.right * (keys[pg.K_d] - keys[pg.K_a])
        if x != 0 or z != 0: movement += glm.vec3(x, 0, z) * (keys[pg.K_w] - keys[pg.K_s])
        if glm.length2(movement) > 0: movement = self.speed * glm.normalize(movement)
        
        self.node.velocity.x = movement.x
        self.node.velocity.z = movement.z
        
    def shoot(self, dt: float) -> None:
        """
        Attemps to fire the player gun if the player is left clicking
        """
        self.gun.update(dt)
        if not self.engine.mouse.left_click: return
        self.gun.shoot(self.camera.forward)
        
    @property
    def position(self): return self._position
    @property
    def camera(self): return self.engine.scene.camera
    
    @position.setter
    def position(self, value):
        self.node.position = value
        self._position = self.node.position.data - glm.vec3(0, 2, 0)
        