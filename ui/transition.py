import basilisk as bsk


class Transition:
    def __init__(self, engine: bsk.Engine, duration: float=1.0):
        """
        Plays a transition on instantiation
        """
        
        self.engine = engine
        self.clock = 0
        self.duration = duration

    def render(self) -> None:
        """
        
        """

        # Update the transition's time        
        self.clock += self.engine.delta_time

        # Render

        cross_fade_intensity = 5.0
        alpha = int(155 * min(cross_fade_intensity * ((self.duration / 2) ** 2 - (self.clock - self.duration / 2) ** 2), 1))

        box_h = 150
        win_w, win_h = self.engine.win_size
        rect = (0, win_h // 2 - box_h // 2, win_w, box_h)
        bsk.draw.rect(self.engine, (0, 0, 0, alpha), rect)
        bsk.draw.text(self.engine, "Test", (100, 100))

    @property
    def running(self): return self.clock < self.duration