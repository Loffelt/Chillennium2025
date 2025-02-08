import glm
import random


HEAD_RADIUS = 0.2
FOOT_RADIUS = 0.3

TORSO_LENGTH = 1
LEG_LENGTH = 1
NECK_LENGTH = 0.5

FORWARD_OFFSET = 0.1

class MistMan():
    
    def __init__(self, position: glm.vec3, cooldown: float=0.01) -> None:
        
        self.forward  = glm.vec3(0, 0, -1)
        self.position = position
        
        right = (0.4, 0, 0)
        left = (-0.4, 0, 0)
        self.right_foot = position + right
        self.left_foot = position + left
        self.right_hand = self.chest + right
        self.left_hand = self.chest + left
        
        self.cooldown = cooldown
        self.time = 0
        
    def update(self, dt: float) -> None:
        """
        Updates particle timer
        """
        self.time += dt
        
    def get_particle_position(self) -> glm.vec3|None:
        """
        Creates particles on the mist figure
        """
        if self.time < self.cooldown: return None
        self.time = 0
        
        choice = random.randint(0, 5)
        if not choice: # spawn on head
            offset = glm.normalize([random.uniform(-1, 1) for _ in range(3)])
            offset *= HEAD_RADIUS
            return self.head + offset

        # if the particle spawns on the body
        percent = random.uniform(0, 1)
        match choice:
            case 1: return self.hip + (self.chest      - self.hip) * percent
            case 2: return self.hip + (self.right_foot - self.hip) * percent
            case 3: return self.hip + (self.left_foot  - self.hip) * percent
            case 4: return self.chest + (self.right_hand - self.chest) * percent
            case 5: return self.chest + (self.left_hand  - self.chest) * percent
    
    @property
    def position(self): return self._position
    @property
    def hip(self): return self.position + (0, LEG_LENGTH, 0)
    @property
    def chest(self): return self.hip + (0, TORSO_LENGTH, 0)
    @property
    def head(self): return self.chest + (0, NECK_LENGTH, 0)
    
    
    @position.setter
    def position(self, value): 
        self._position = value
        
        # compute the positions of the feet
        center = self._position + self.forward * FORWARD_OFFSET
        if (center.x - self.right_foot.x) ** 2 + (center.z - self.right_foot.z) ** 2 > FOOT_RADIUS ** 2:
            ...