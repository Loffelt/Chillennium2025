import basilisk as bsk
import pygame as pg
import numpy as np


class RenderHandler:
    def __init__(self, game) -> None:
        self.game = game
        self.engine = game.engine


        self.default_shader = self.engine.shader
        # Shaders
        self.dim_shader    = bsk.Shader(self.engine, vert='shaders/dim.vert',      frag='shaders/dim.frag')
        self.geo_shader    = bsk.Shader(self.engine, vert='shaders/geometry.vert', frag='shaders/geometry.frag')
        self.norm_shader   = bsk.Shader(self.engine, vert='shaders/normal.vert',   frag='shaders/normal.frag')
        self.output_shader = bsk.Shader(self.engine, vert='shaders/output.vert',   frag='shaders/output.frag')

        # First render pass
        self.geometry   = bsk.Framebuffer(self.engine)
        self.normals    = bsk.Framebuffer(self.engine)
        self.dimensions = bsk.Framebuffer(self.engine)

        # Level destinations
        self.plain = bsk.Framebuffer(self.engine)
        self.sight = bsk.Framebuffer(self.engine)

        # Output vao        
        self.vbo = self.engine.ctx.buffer(np.array([[-1, -1, 0, 0, 0], [1, -1, 0, 1, 0], [1, 1, 0, 1, 1], [-1, 1, 0, 0, 1], [-1, -1, 0, 0, 0], [1, 1, 0, 1, 1]], dtype='f4'))
        self.vao = self.engine.ctx.vertex_array(self.output_shader.program, [(self.vbo, '3f 2f', 'in_position', 'in_uv')], skip_errors=True)
        
        self.output_shader.program['dimensionMap'] = 0
        self.dimensions.texture.use(location=0)
        self.output_shader.program['plainView'] = 1
        self.geometry.texture.use(location=1)
        self.output_shader.program['sightView'] = 2
        self.normals.texture.use(location=2)

        self.show = self.geometry

    def update_scenes(self):
        """
        Updates the nessecary data in the scenes
        """
        
        self.game.plain_scene.node_handler.update()
        self.game.plain_scene.particle.update()
        self.game.dimension_scene.node_handler.update()
        self.game.dimension_scene.particle.update()

    def render(self) -> None:
        """
        
        """
        
        self.update_scenes()

        # Render the dimesions map and depth
        self.engine.scene = self.game.dimension_scene
        self.engine.shader = self.dim_shader
        self.game.dimension_scene.sky = None
        self.game.dimension_scene.render(self.dimensions)

        # Render the sight scene with the dimensions depth
        self.norm_shader.program['depthMap'] = 0
        self.dimensions.texture.use(location=0)
        self.engine.scene = self.game.sight_scene
        self.engine.shader = self.norm_shader
        self.game.sight_scene.sky = self.game.sky
        self.game.sight_scene.render(self.normals)

        # Render plain
        self.engine.scene = self.game.plain_scene
        self.engine.shader = self.geo_shader
        self.game.plain_scene.sky = None
        self.game.plain_scene.render(self.geometry)

        # Show to the screen
        self.engine.ctx.screen.use()
        self.engine.ctx.clear()
        self.output_shader.program['dimensionMap'] = 0
        self.dimensions.texture.use(location=0)
        self.output_shader.program['plainView'] = 1
        self.geometry.texture.use(location=1)
        self.output_shader.program['sightView'] = 2
        self.normals.texture.use(location=2)
        self.vao.render()
        # self.show.render()
        pg.display.flip()
