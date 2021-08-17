from manim import *


class Intro(Scene):
    def construct(self):
        self.play(
            Write(Tex('Hello quadratics'))
        )
