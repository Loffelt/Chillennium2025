import basilisk as bsk

engine = bsk.Engine()
scene = bsk.Scene()
engine.scene = scene

# crt = bsk.PostProcess(engine, "basilisk/shaders/crt.frag")
# scene.add(crt)

while engine.running:
    
    engine.update()
