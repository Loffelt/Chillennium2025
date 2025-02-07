import basilisk as bsk
import glm

engine = bsk.Engine()
scene = bsk.Scene()
engine.scene = scene

while engine.running:
    
    engine.update()
