import basilisk as bsk
import pygame as pg
import numpy as np


class RenderHandler:
    def __init__(self, game) -> None:
        self.game = game
        self.engine = game.engine


        self.default_shader = self.engine.shader
        # Shaders
        self.geo_shader   = bsk.Shader(self.engine, vert='shaders/geometry.vert', frag='shaders/geometry.frag')
        self.norm_shader  = bsk.Shader(self.engine, vert='shaders/normal.vert',   frag='shaders/normal.frag')

        # First render pass
        self.geometry   = bsk.Framebuffer(self.engine)
        self.normals    = bsk.Framebuffer(self.engine)
        self.dimensions = bsk.Framebuffer(self.engine)

        # Level destinations
        self.plain = bsk.Framebuffer(self.engine)
        self.sight = bsk.Framebuffer(self.engine)

        self.show = self.geometry

    def update_scenes(self):
        """
        Updates the nessecary data in the scenes
        """
        
        self.game.plain_scene.node_handler.update()
        self.game.dimension_scene.node_handler.update()

    def render(self) -> None:
        """
        
        """
        
        self.update_scenes()
        self.first_pass()

        self.engine.ctx.screen.use()
        self.engine.ctx.clear()
        self.show.render()

        pg.display.flip()

    def first_pass(self) -> None:
        """
        
        """
        # self.engine.scene = self.game.sight_scene
        self.engine.shader = self.norm_shader
        self.game.sight_scene.sky = self.game.sky
        self.game.sight_scene.render(self.normals)

        # self.engine.scene = self.game.plain_scene
        self.engine.shader = self.geo_shader
        self.game.plain_scene.sky = self.game.sky
        self.game.plain_scene.render(self.geometry)

        self.engine.scene = self.game.dimension_scene
        self.engine.shader = self.geo_shader
        self.game.dimension_scene.sky = None
        self.game.dimension_scene.render(self.dimensions)