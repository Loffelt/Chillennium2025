import basilisk as bsk
import glm
from entities.player import Player, get_player_node, get_player_gun
from entities.enemy_handler import EnemyHandler
from weapons.bullet_handler import BulletHandler
from weapons.gun import Gun
from weapons.bullet import Bullet
from scenes.game_scene import GameScene, get_plain_nodes
from scenes.test_scene import test_scene
from scenes.levels import level1
from render.render_handler import RenderHandler
from ui.ui import UI
# import cudart


class Game():
    
    def __init__(self) -> None:
        self.engine = bsk.Engine()

        self.default_scene = bsk.Scene()
        self.plain_scene = bsk.Scene()
        self.sight_scene = bsk.Scene()
        self.dimension_scene = bsk.Scene()

        self.engine.scene = self.default_scene
        self.engine.scene = self.plain_scene
        self.engine.scene = self.sight_scene
        self.engine.scene = self.dimension_scene 
        
        self.sight_scene.physics_engine.accelerations = [glm.vec3(0, -25, 0)]
        
        self.default_shader = self.engine.shader
        self.particle_shader = bsk.Shader(self.engine, 'shaders/particle_sight.vert', 'shaders/particle_sight.frag')
        self.invisible_shader = bsk.Shader(self.engine, 'shaders/invisible.vert', 'shaders/invisible.frag')
        self.sight_scene.particle = bsk.ParticleHandler(self.sight_scene, self.particle_shader)
        
        self.levels = [level1]
        
        self.pistol = Gun(
            game = self,
            count = 1,
            capacity = 7,
            cooldown = 0.2,
            spread = 0.02,
            ricochets = 2,
            damage = 1,
            radius = 0.2,
            color  = 'black',
            owner  = 'player'
        )
        
        self.shotgun = Gun(
            game = self,
            count = 7,
            capacity = 3,
            cooldown = 0.6,
            spread = 0.1,
            ricochets = 1,
            damage = 1,
            radius = 0.125,
            color = 'black',
            owner = 'player'
        )
        
        self.submachine = Gun(
            game = self,
            count = 1,
            capacity = 3,
            cooldown = 0.1,
            spread = 0.1,
            ricochets = 0,
            damage = 1,
            radius = 0.03,
            color = 'black',
            owner = 'player'
        )

        # add player to scene
        player_node = get_player_node()
        
        self.player_gun = get_player_gun()
        self.default_scene.add(self.player_gun)
        
        self.player = Player(
            position = glm.vec3(0, 0, 0), 
            health = 3,
            speed = 10,
            gun = self.submachine,
            node = player_node,
            game = self
        )
        
        self.sight_scene.add(player_node)
        self.sight_scene.camera = bsk.FollowCamera(player_node, offset=(0, 1, 0))
        self.plain_scene.camera = self.sight_scene.camera
        self.dimension_scene.camera = self.sight_scene.camera
        self.default_scene.camera = self.sight_scene.camera
        self.sky = self.sight_scene.sky
        
        # add handlers
        self.load_materials()
        self.enemy_handler = EnemyHandler(self)
        self.bullet_handler = BulletHandler(self)

        #UI
        self.ui = UI(self)

    def load_meshes(self):
        self.pistol_mesh = bsk.Mesh('meshes/pistol.obj')
        self.wedge_mesh = bsk.Mesh('meshes/wedge.obj')
        self.cylinder_mesh = bsk.Mesh('meshes/cylinder.obj')

    def load_level(self, game_scene: GameScene) -> None:
        """
        Add all nodes to the scene
        """ 
        # plain scene
        self.plain_scene.remove(*self.plain_scene.nodes)
        self.plain_scene.add(*get_plain_nodes(game_scene))
        #UI
        self.ui = UI(self)

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
        nodes = self.sight_scene.nodes[:]
        nodes.remove(self.player.node)
        self.sight_scene.remove(*nodes)
        self.sight_scene.add(*game_scene.nodes)
        for enemy in game_scene.enemies: self.sight_scene.add(enemy.node)
        
        self.bullet_handler.bullets = []
        self.enemy_handler.enemies = game_scene.enemies
        
        # dimensions scene
        self.dimension_scene.remove(*self.dimension_scene.nodes)

    def load_materials(self):
        saturation = 80
        self.red = bsk.Material(color=(255, saturation - 50, saturation - 50), roughness=.8, metallicness=0.0, specular=0.25)
        self.green = bsk.Material(color=(saturation, 255, saturation), roughness=.8, metallicness=0.0, specular=0.25)
        self.blue = bsk.Material(color=(saturation, saturation, 255), roughness=.8, metallicness=0.0, specular=0.25)
        self.white = bsk.Material(color=(255, 255, 255))
        
    def next_level(self):
        level = self.levels.pop(0)
        return level

    def start(self) -> None:
        """
        Starts the engine and the game
        """
        
        self.render_handler = RenderHandler(self)
        self.load_meshes()
        
        self.load_level(self.next_level()(self))

        while self.engine.running:

            if self.engine.keys[bsk.pg.K_1] and not self.engine.previous_keys[bsk.pg.K_1]:
                self.ui.add_transition()
                self.ui.add_transition(duration=1.5, callback= lambda: self.load_level(self.next_level()(self)))

            self.bullet_handler.update(self.engine.delta_time)
            self.enemy_handler.update(self.engine.delta_time)
            self.player.update(self.engine.delta_time)

            self.render_handler.render()

            self.engine.update(render=False)
            bsk.pg.display.flip()

game = Game()
game.start()