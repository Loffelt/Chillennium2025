import basilisk as bsk
import pygame as pg


class RenderHandler:
    def __init__(self, game) -> None:
        self.game = game
        self.engine = game.engine

        # Shaders
        self.geo_shader   = bsk.Shader(self.engine, vert='shaders/geometry.vert', frag='shaders/geometry.frag')
        self.norm_shader  = bsk.Shader(self.engine, vert='shaders/normal.vert',   frag='shaders/normal.frag')
        # self.depth_shader = bsk.Shader(self.engine, vert='', frag='')

        # First render pass
        self.geometry = bsk.Framebuffer(self.engine)
        self.normals = bsk.Framebuffer(self.engine)

        # Level destinations
        self.plain = bsk.Framebuffer(self.engine)
        self.sight = bsk.Framebuffer(self.engine)

    def render(self) -> None:
        """
        
        """
        
        self.first_pass()

        self.engine.ctx.screen.use()
        self.engine.ctx.clear()

        self.engine.shader = self.geo_shader
        self.engine.shader = self.norm_shader
        self.geometry.render()

        pg.display.flip()

    def first_pass(self) -> None:
        """
        
        """
        

        self.engine.shader = self.geo_shader
        self.engine.scene.render(self.geometry)

        self.engine.shader = self.norm_shader
        self.engine.scene.render(self.normals)
        
        # self.engine.shader = self.geo_shader
