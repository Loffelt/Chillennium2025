import glm
import random


class MistMan():
    
    def __init__(self, position: glm.vec3, torso: float=0.5, leg: float=0.5, head: float=0.1, cooldown: float=0.2) -> None:
        
        self.right_leg = self.left_leg = position
        self.position = position
        self.hip = self.position + (0, leg, 0)
        self.chest = self.hip + (0, torso, 0)
        self.head = self.chest + (0, head, 0)
        
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
            ...
            return

        # if the particle spawns on the body
    
    @property
    def position(self): return self._position
    
    @position.setter
    def position(self, value): 
        self._position = value