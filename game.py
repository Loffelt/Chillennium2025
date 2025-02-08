import basilisk as bsk
import glm
from entities.player import Player
from weapons.gun import Gun
from weapons.gun import Bullet
from scenes.test_scene import test_scene

class Game:
    
    def __init__(self) -> None:
        self.engine = bsk.Engine()
        self.scene = bsk.Scene()
        
        player_node = bsk.Node(
            physics = True,
            collision = True
        )
        
        self.player = Player(
            position = glm.vec3(0, 0, 0), 
            health = 3,
            speed = 1,
            gun = Gun(
                count = 1,
                capacity = 7,
                cooldown = 0.2,
                spread = 0.02,
                bullet = Bullet(
                    ricochet_remaining = 1,
                    damage = 1,
                    radius = 1.0
                )
            ),
            node = player_node,
            engine = self
        )
        
        self.scene.add(player_node)

    def load_shaders(self) -> None:
        self.plain_shader = bsk.Shader(self.engine, vert="shaders/plain.vert", frag="shaders/plain.frag")
        self.engine.shader = self.plain_shader

    def load_level(self) -> None:
        """
        Add all nodes to the scene
        """ 
        self.replace_nodes(test_scene())

    def start(self) -> None:
        """
        Starts the engine and the game
        """
        
        self.load_level()
        self.load_shaders()

        while self.engine.running:
            self.engine.update()
            
    def replace_nodes(self, nodes: list[bsk.Node]) -> None:
        self.scene.add(*nodes)
            
    @property
    def scene(self) -> bsk.Scene: return self.engine.scene
    
    @scene.setter
    def scene(self, value): 
        self.engine.scene = value

game = Game()
game.start()