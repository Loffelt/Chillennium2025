import glm
from basilisk import Node, Engine, pg, FollowCamera
from entities.entity import Entity
from weapons.gun import Gun


class Player(Entity):
    
    def __init__(self, position: glm.vec3, health: int, speed: float, gun: Gun, node: Node, game) -> None:
        self.node = node
        super().__init__(position, health, speed)
        
        self.game = game
        self.gun = gun
        self.jumping = False
            
        self.fov = 70
        self.target_fov = 80
        self.fov_time = 0
        
    def update(self, dt: float) -> None:
        """
        
        """
        self.node.rotation = glm.conjugate(glm.quatLookAt(glm.vec3(self.camera.forward.x, 0, self.camera.forward.z), self.camera.UP))
        self.game.player_gun.rotation = self.game.sight_scene.camera.rotation
        self.game.player_gun.position = self.node.position.data + glm.vec3(0, 0.35, 0) + self.camera.right * 0.4 + self.camera.forward * 0.75
        
        if self.position.y < 1.1: 
            self.position.y = 1.1
            if not self.jumping: self.node.velocity.y = 0
            elif self.node.velocity.y < 0: self.jumping = False
            
        self.move(dt)
        self.shoot(dt)
        
        # controls fov
        self.fov_time += dt
        if self.fov_time > 0.01 and self.fov != self.target_fov:
            self.fov_time = 0
            self.fov += 1 if self.fov < self.target_fov else -1
        
    def move(self, dt) -> None:
        """
        Sets the player's node's velocity to the input keys (wasd)
        """
        self._position = self.node.position.data - glm.vec3(0, 1, 0)
        
        # contraol the player's position by adding velocity to the node
        keys = self.engine.keys
        x, z = self.camera.forward.x, self.camera.forward.z
        movement = self.camera.right * (keys[pg.K_d] - keys[pg.K_a]) # should change fov when sprinting
        if x != 0 or z != 0: movement += glm.vec3(x, 0, z) * (keys[pg.K_w] - keys[pg.K_s])
        if glm.length2(movement) > 0: movement = self.speed * glm.normalize(movement)
        if keys[pg.K_LSHIFT] and not keys[pg.K_s] and (keys[pg.K_w] or keys[pg.K_a] or keys[pg.K_d]): 
            movement *= 1.5
            self.target_fov = 80
        else:
            self.target_fov = 70
        if keys[pg.K_SPACE] and (not self.jumping or any(glm.dot(collision.normal, (0, 1, 0)) > 0.2 for collision in self.node.collisions)):
            self.node.velocity.y = 15
            self.jumping = True
            
        if glm.length2(movement) == 0 and glm.length2((self.node.velocity.x, 0, self.node.velocity.z)) > 1: movement = glm.vec3(self.node.velocity.x, 0, self.node.velocity.z) * (1 - dt * 10)
        
        self.node.velocity.x = movement.x
        self.node.velocity.z = movement.z
        
    def shoot(self, dt: float) -> None:
        """
        Attemps to fire the player gun if the player is left clicking
        """
        self.gun.update(dt)
        if not self.engine.mouse.left_click: return
        
        fire_position = self.game.player_gun.position.data + self.camera.forward * 1.25
        cast = self.game.sight_scene.raycast(self.camera.position + self.camera.forward * 2, self.camera.forward)
        target = cast.position if cast.node else self.camera.forward * 1e3
        
        bullets = self.gun.shoot(fire_position, glm.normalize(target - fire_position))
        if not bullets: return
        
        self.game.bullet_handler.bullets += bullets
        
    @property
    def position(self): return self._position
    @property
    def camera(self) -> FollowCamera: return self.game.sight_scene.camera
    @property
    def engine(self) -> Engine: return self.game.engine
    @property
    def fov(self): return self.camera.fov
    
    @position.setter
    def position(self, value):
        self._position = value
        self.node.position.data = self._position + glm.vec3(0, 1, 0)
        
    @fov.setter
    def fov(self, value):
        self.camera.fov = value
        
        
def get_player_node() -> Node:
    player_node = Node(
        physics = True,
        collision = True,
        scale = (1, 2, 1),
        tags = ['player'],
        collision_group = 'entity'
    )
    
    return player_node

def get_player_gun() -> Node:
    gun = Node(
        scale = (0.1, 0.1, 1)
    )
    
    return gun