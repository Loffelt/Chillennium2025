import basilisk as bsk
from render.render_handler import RenderHandler


class Game:
    
    def __init__(self) -> None:
        self.engine = bsk.Engine()
        self.scene = bsk.Scene()
        self.engine.scene = self.scene

    def load_level(self) -> None:
        """
        Add all nodes to the scene
        """

        self.scene.add(bsk.Node())

    def start(self) -> None:
        """
        Starts the engine and the game
        """
        
        self.render_handler = RenderHandler(self)

        self.load_level()

        while self.engine.running:
            self.engine.update(render=False)
            self.render_handler.render()


game = Game()
game.start()