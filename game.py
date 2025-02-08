import basilisk as bsk
import glm
from entities.player import Player
from weapons.gun import Gun
from weapons.gun import Bullet
from scenes.test_scene import test_scenefrom render.render_handler import RenderHandler


class Game:
    
    def __init__(self) -> None:
        self.engine = bsk.Engine()
        self.scene = bsk.Scene()
        self.engine.scene = self.scene

    def load_level(self) -> None:
        """
        Add all nodes to the scene
        """ 
        self.replace_nodes(test_scene())

    def start(self) -> None:
        """
        Starts the engine and the game
        """
        
        self.render_handler = RenderHandler(self)

        self.load_level()

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