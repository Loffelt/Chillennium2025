import basilisk as bsk
import glm
from entities.player import Player
from entities.enemy_handler import EnemyHandler
from weapons.bullet_handler import BulletHandler
from weapons.gun import Gun
from weapons.bullet import Bullet
from scenes.game_scene import GameScene
from scenes.test_scene import test_scene
from render.render_handler import RenderHandler


class Game:
    
    def __init__(self) -> None:
        self.engine = bsk.Engine()
        self.scene = bsk.Scene()
        
        # add player to scene
        player_node = bsk.Node(
            physics = True,
            collision = True
        )
        
        self.player = Player(
            position = glm.vec3(0, 0, 0), 
            health = 3,
            speed = 6,
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
            engine = self.engine
        )
        
        self.scene.add(player_node)
        
        # add handlers
        self.enemy_handler = EnemyHandler()
        self.bullet_handler = BulletHandler()

    def load_level(self, game_scene: GameScene) -> None:
        """
        Add all nodes to the scene
        """ 
        self.scene.remove(*self.scene.nodes)
        self.scene.add(*game_scene.nodes, self.player.node)
        
        self.bullet_handler.bullets = []
        self.enemy_handler.enemies = game_scene.enemies

    def start(self) -> None:
        """
        Starts the engine and the game
        """
        
        self.render_handler = RenderHandler(self)
        self.load_level(test_scene(self.player))

        while self.engine.running:
            
            self.player.update(self.engine.delta_time)
            
            self.engine.update(render=True)
            # self.render_handler.render()
            
    @property
    def scene(self) -> bsk.Scene: return self.engine.scene
    
    @scene.setter
    def scene(self, value): 
        self.engine.scene = value

game = Game()
game.start()