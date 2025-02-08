import basilisk as bsk
import glm
from entities.player import Player
from entities.enemy_handler import EnemyHandler
from weapons.bullet_handler import BulletHandler
from weapons.gun import Gun
from weapons.bullet import Bullet
from scenes.game_scene import GameScene, get_plain_nodes
from scenes.test_scene import test_scene
from render.render_handler import RenderHandler
import moderngl as mgl


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
            collision = True,
            scale = (1, 2, 1),
            tags = ['player'],
            collision_group = 'entity'
        )
        
        self.player = Player(
            position = glm.vec3(0, 0, 0), 
            health = 3,
            speed = 10,
            gun = Gun(
                game = self,
                count = 1,
                capacity = 7,
                cooldown = 0.2,
                spread = 0.02,
                ricochets = 1,
                damage = 1,
                radius = 1.0,
                color  = 'black'
            ),
            node = player_node,
            game = self
        )
        
        self.sight_scene.add(player_node)
        self.sight_scene.camera = bsk.FollowCamera(player_node, offset=(0, 1, 0))
        self.plain_scene.camera = self.sight_scene.camera
        self.dimension_scene.camera = self.sight_scene.camera
        self.sky = self.sight_scene.sky
        
        # add handlers
        self.enemy_handler = EnemyHandler(self)
        self.bullet_handler = BulletHandler(self)

    def load_meshes(self):
        self.cylinder_mesh = bsk.Mesh('meshes/cylinder.obj')

    def load_level(self, game_scene: GameScene) -> None:
        """
        Add all nodes to the scene
        """ 
        # plain scene
        self.plain_scene.remove(*self.plain_scene.nodes)
        self.plain_scene.add(*get_plain_nodes(game_scene))
        
        # sight scene
        self.sight_scene.remove(*self.sight_scene.nodes)
        self.sight_scene.add(*game_scene.nodes, self.player.node)
        for enemy in game_scene.enemies: self.sight_scene.add(enemy.node)
        
        self.bullet_handler.bullets = []
        self.enemy_handler.enemies = game_scene.enemies
        
        # dimensions scene
        self.dimension_scene.remove(*self.dimension_scene.nodes)

    def start(self) -> None:
        """
        Starts the engine and the game
        """
        
        self.render_handler = RenderHandler(self)
        self.load_meshes()
        
        self.load_level(test_scene(self))

        # self.dimension_scene.add(bsk.Node(scale=(3, 3, 3), position=(0, -3, 0)))

        self.dimension_scene.add(bsk.Node(position=(6, -2.5, 0)))
        self.dimension_scene.add(bsk.Node(position=(0, -2.5, 6)))
        self.dimension_scene.add(bsk.Node(position=(6, -2.5, 6)))

        self.sight_scene.add(bsk.Node(scale=(1, 1, 1), position=(-6, -3, -6)))

        # for x in range(-1, 2):
        #     for z in range(-1, 2):
        #         self.dimension_scene.add(bsk.Node(mesh=self.cylinder_mesh, scale=(1, 8, 1), position=(x * 5, 0, z * 5)))

        while self.engine.running:

            if self.engine.keys[bsk.pg.K_1]:
                self.render_handler.show = self.render_handler.geometry
            if self.engine.keys[bsk.pg.K_2]:
                self.render_handler.show = self.render_handler.normals
            if self.engine.keys[bsk.pg.K_3]:
                self.render_handler.show = self.render_handler.dimensions

            self.bullet_handler.update(self.engine.delta_time)
            self.enemy_handler.update(self.engine.delta_time)
            self.player.update(self.engine.delta_time)

            self.engine.scene = self.sight_scene
            self.engine.update(render=False)

            self.render_handler.render()


game = Game()
game.start()