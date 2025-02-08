import basilisk as bsk


class Game:
    def __init__(self) -> None:
        self.engine = bsk.Engine()
        self.scene = bsk.Scene()
        self.engine.scene = self.scene

    def load_shaders(self) -> None:
        self.plain_shader = bsk.Shader(self.engine, vert="shaders/plain.vert", frag="shaders/plain.frag")
        self.engine.shader = self.plain_shader

    def load_level(self) -> None:
        """
        Add all nodes to the scene
        """

        self.scene.add(bsk.Node())

    def start(self) -> None:
        """
        Starts the engine and the game
        """
        
        self.load_shaders()
        self.load_level()

        while self.engine.running:
            self.engine.update()


game = Game()
game.start()