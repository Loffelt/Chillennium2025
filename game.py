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


class Game():
    
    def __init__(self) -> None:
        self.engine = bsk.Engine()

        self.plain_scene = bsk.Scene()
        self.sight_scene = bsk.Scene()
        self.dimension_scene = bsk.Scene()
        self.engine.scene = self.plain_scene
        self.engine.scene = self.sight_scene
        self.engine.scene = self.dimension_scene 
        
        # add player to scene
        player_node = bsk.Node(
            physics = True,
            collision = True
        )
        
        self.player = Player(
            position = glm.vec3(0, 0, 0), 
            health = 3,
            speed = 10,
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
            game = self
        )
        
        self.plain_scene.add(player_node)
        self.plain_scene.camera = bsk.FollowCamera(player_node)
        
        # add handlers
        self.enemy_handler = EnemyHandler(self)
        self.bullet_handler = BulletHandler(self)

    def load_level(self, scene: bsk.Scene, game_scene: GameScene) -> None:
        """
        Add all nodes to the scene
        """ 
        scene.remove(*self.plain_scene.nodes)
        scene.add(*game_scene.nodes, self.player.node)
        
        self.bullet_handler.bullets = []
        self.enemy_handler.enemies = game_scene.enemies

    def start(self) -> None:
        """
        Starts the engine and the game
        """
        
        self.render_handler = RenderHandler(self)
        self.load_level(self.plain_scene, test_scene(self.player))

        while self.engine.running:
            self.bullet_handler.update(self.engine.delta_time)
            self.enemy_handler.update(self.engine.delta_time)
            self.player.update(self.engine.delta_time)

            self.engine.update(render=False)
            self.render_handler.render()


game = Game()
game.start()