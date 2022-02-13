from manim import *

edges = [
    (0, 1),
    (0, 2),
    (0, 5),
    (1, 3),
    (1, 2),
    (2, 4),
    (3, 6),
    (3, 4),
    (4, 6),
    (4, 5),
    (5, 6)
]


def get_diamond():
    vertices = []
    for i in range(0, 7):
        vertices.append(i)
    g = Graph(vertices, edges)
    g[0].move_to([-3, 0, 0])
    g[1].move_to([-1, 2, 0])
    g[2].move_to([-1, 0, 0])
    g[3].move_to([1, 2, 0])
    g[4].move_to([1, 0, 0])
    g[5].move_to([1, -2, 0])
    g[6].move_to([3, 0, 0])
    return g


class NewThumbnail(Scene):
    def construct(self):
        g = get_diamond().scale(1.5)
        # del g[0]
        self.add(g)
        self.wait()


class Chosen(Scene):
    def construct(self):
        title = Text("Find probability using DFS", t2c={'probability': BLUE}).scale(1.2).to_edge(UP)
        title[-3:].set_color(YELLOW)
        g = get_diamond()
        everything = Group(
            title, g
        ).move_to(ORIGIN)
        graph = ImageMobject("img/cool-maze-no-bg.png").scale(0.7).move_to(g)
        self.add(
            title, graph
        )
        self.wait()
