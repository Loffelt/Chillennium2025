import glm

class MistMan():
    
    def __init__(self, position: glm.vec3, torso: float=0.5, leg: float=0.5, head: float=0.1) -> None:
        
        self.right_leg = self.left_leg = position
        self.position = position
        self.hip = self.position + (0, leg, 0)
        self.chest = self.hip + (0, torso, 0)
        self.head = self.chest + (0, head, 0)
    
    @property
    def position(self): return self._position
    
    @position.setter
    def position(self, value): 
        self._position = value