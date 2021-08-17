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

adj = {
    0: [1, 2, 5],
    1: [3, 2, 0],
    2: [1, 4, 0],
    3: [6, 4, 1],
    4: [3, 6, 5, 2],
    5: [4, 6, 0],
    6: [5, 4, 3]
}

SLOW = 1.0
FAST = 0.5

HIGHLIGHT = GREEN_C


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


class Intro(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        world_map = SVGMobject("img/world.svg", height=6)
        self.play(
            DrawBorderThenFill(world_map),
            run_time=5
        )

        mys = world_map.submobjects[159]
        self.play(
            self.camera.frame.animate.scale(0.05).move_to(mys.get_center()),
            run_time=2
        )
        self.play(
            mys.animate.set_fill(GREEN)
        )
        title = Text("Malaysia").scale(0.05).set_color(GREEN_D)
        subtitle = Text("SPM Additional Mathematics 2020").scale(0.03).next_to(title.get_center(), DOWN * 0.06)
        txt = VGroup(
            title,
            subtitle
        ).next_to(mys.get_center(), UP * 0.1)

        self.play(
            FadeIn(title)
        )
        self.play(
            FadeIn(subtitle)
        )
        self.wait(2)
        self.play(
            FadeOut(txt)
        )
        self.play(
            Restore(self.camera.frame),
            run_time=3
        )
        self.play(
            FadeOut(world_map),
            run_time=2
        )
        self.wait()


class Problem(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        g = get_diamond()
        tapir = SVGMobject("img/tapir.svg")
        self.play(
            FadeIn(tapir)
        )
        self.play(
            tapir.animate.scale(0.2).next_to(g[0].get_center(), UL * 0.5)
        )
        self.play(
            Create(g),
            run_time=2
        )
        self.wait()

        self.play(self.camera.frame.animate.scale(0.1).move_to(tapir))
        self.wait()
        self.play(Restore(self.camera.frame))

        # trails of at most length 3
        txt = Text("At most 3 steps").to_edge(DOWN)
        self.play(
            Write(txt)
        )
        self.wait()
        line_1 = Line(g[0], g[2], color=GREEN)
        line_2 = Line(g[2], g[4], color=GREEN)
        line_3 = Line(g[4], g[3], color=GREEN)
        line_4 = Line(g[3], g[1], color=RED_C)
        lines = [
            line_1, line_2, line_3, line_4
        ]

        self.play(
            g[0].animate.set_fill(GREEN)
        )

        self.play(
            tapir.animate.next_to(g[2].get_center(), UL * 0.5),
            g[2].animate.set_fill(GREEN),
            Create(line_1)
        )
        self.wait(0.5)

        self.play(
            tapir.animate.next_to(g[4].get_center(), UL * 0.5),
            g[4].animate.set_fill(GREEN),
            Create(line_2)
        )
        self.wait(0.5)

        self.play(
            tapir.animate.next_to(g[3].get_center(), UL * 0.5),
            g[3].animate.set_fill(GREEN),
            Create(line_3)
        )
        self.wait(0.5)

        self.play(
            Create(line_4)
        )
        self.wait()

        self.play(
            *[x.animate.set_fill(WHITE) for x in g],
            Uncreate(VGroup(*lines)),
            FadeOut(txt)
        )
        self.play(
            tapir.animate.next_to(g[0].get_center(), UL * 0.5)
        )
        self.wait()

        # cannot go back
        txt = Text("Roads cannot be reused").to_edge(DOWN)
        line_1 = Line(g[0].get_center(), g[5].get_center(), color=GREEN)
        line_2 = Line(g[5].get_center(), g[4].get_center(), color=GREEN)
        line_3 = Line(g[4].get_center(), g[5].get_center(), color=RED_C)
        lines = [
            line_1, line_2, line_3
        ]

        self.play(
            Write(txt),
            g[0].animate.set_fill(GREEN)
        )

        self.play(
            g[5].animate.set_fill(GREEN),
            tapir.animate.next_to(g[5].get_center(), UL * 0.5),
            Create(line_1)
        )

        self.play(
            g[4].animate.set_fill(GREEN),
            tapir.animate.next_to(g[4].get_center(), UL * 0.5),
            Create(line_2)
        )
        g[4].set_z_index(100)
        g[5].set_z_index(100)

        self.play(
            Create(line_3)
        )

        self.play(
            *[x.animate.set_fill(WHITE) for x in g],
            FadeOut(VGroup(*lines)),
            FadeOut(txt)
        )
        self.play(
            tapir.animate.next_to(g[0].get_center(), UL * 0.5)
        )
        self.wait()

        # can repeat nodes
        txt = Text("Stops can be revisited").to_edge(DOWN)
        line_1 = Line(g[0], g[2], color=GREEN)
        line_2 = Line(g[2], g[1], color=GREEN)
        line_3 = Line(g[1], g[0], color=GREEN)
        lines = [
            line_1, line_2, line_3
        ]

        self.play(
            Write(txt),
            g[0].animate.set_fill(GREEN),
        )

        self.play(
            g[2].animate.set_fill(GREEN),
            tapir.animate.next_to(g[2].get_center(), UL * 0.5),
            Create(line_1)
        )

        self.play(
            g[1].animate.set_fill(GREEN),
            tapir.animate.next_to(g[1].get_center(), UL * 0.5),
            Create(line_2)
        )

        self.play(
            g[0].animate.set_fill(GREEN),
            tapir.animate.next_to(g[0].get_center(), UL * 0.5),
            Create(line_3)
        )

        self.play(
            *[x.animate.set_fill(WHITE) for x in g],
            Uncreate(VGroup(*lines)),
            FadeOut(txt)
        )
        self.wait()

        A = Text("A").next_to(g[0], LEFT)
        B = Text("B").next_to(g[6], RIGHT)
        self.play(
            Write(A)
        )
        self.play(
            Write(B)
        )
        g_group = VGroup(
            A, B, g, tapir
        )
        self.play(
            g_group.animate.to_edge(DOWN)
        )

        txt = Text("Find the probability that the tapir reaches B from A.").scale(
            0.7).to_edge(UP)
        self.play(
            Write(txt)
        )
        conditions = [
            "1. The tapir must move.",
            "2. The tapir can move 3 steps maximum.",
            "3. Roads cannot be reused.",
            "4. Each sequence of moves has an equal probability of being chosen."
        ]
        clarifications = VGroup(*[Text(x).scale(0.5) for x in conditions])
        clarifications.arrange(DOWN, center=False, aligned_edge=LEFT).next_to(txt, DOWN)
        for x in clarifications:
            self.play(
                FadeIn(x),
                run_time=0.75
            )
        self.wait(3)
        self.play(
            FadeOut(txt),
            FadeOut(clarifications),
            FadeOut(A),
            FadeOut(B),
            FadeOut(tapir)
        )
        self.play(
            g.animate.move_to(ORIGIN)
        )


class Terminology(Scene):
    def construct(self):
        g = get_diamond()
        self.add(g)
        self.wait(2)
        self.play(
            g.animate.change_layout("spring"),
            run_time=3
        )
        self.wait()

        # graph terminology
        arrow1 = Arrow(start=g[3].get_center() + UR, end=g[3].get_center())
        self.play(
            Create(arrow1),
            g[3].animate.set_fill(HIGHLIGHT)
        )
        txt_node = Text("Node").next_to(arrow1.get_start(), RIGHT)
        self.play(
            Write(txt_node)
        )
        self.wait()

        arrow2 = Arrow(start=g.edges[(1, 3)].get_center() + UR, end=g.edges[(1, 3)].get_center())
        txt_edge = Text("Edge").next_to(arrow2.get_start(), RIGHT)
        self.play(
            g[3].animate.set_fill(WHITE),
            ReplacementTransform(arrow1, arrow2),
            g.edges[(1, 3)].animate.set_color(HIGHLIGHT),
            ReplacementTransform(txt_node, txt_edge)
        )
        self.wait()
        self.play(
            FadeOut(txt_edge),
            g.edges[(1, 3)].animate.set_color(WHITE),
            FadeOut(arrow2)
        )
        self.wait()

        # trail
        g[0].set_z_index(100)
        g[1].set_z_index(100)
        g[3].set_z_index(100)
        g[4].set_z_index(100)

        line_1 = Line(g[0].get_center(), g[1].get_center(), color=HIGHLIGHT)
        line_2 = Line(g[1].get_center(), g[3].get_center(), color=HIGHLIGHT)
        line_3 = Line(g[3].get_center(), g[4].get_center(), color=HIGHLIGHT)
        lines = [
            line_1, line_2, line_3
        ]
        for line in lines:
            self.play(Create(line))

        txt = Text("Trail").to_edge(UP, buff=1)
        self.play(
            Write(txt)
        )
        self.wait()

        self.play(
            FadeOut(txt),
            FadeOut(VGroup(*lines))
        )
        self.wait()
        self.play(
            Indicate(g)
        )
        txt = Text("Graph").to_edge(UP, buff=1)
        self.play(
            Write(txt)
        )
        self.wait()

        self.play(
            FadeOut(txt),
        )
        self.wait()
        g1 = get_diamond()
        self.play(
            Transform(g, g1)
        )
        self.wait()


class StrategyIntro(Scene):
    def construct(self):
        g = get_diamond()
        A = Text("A").next_to(g[0], LEFT)
        B = Text("B").next_to(g[6], RIGHT)
        self.add(
            g
        )
        self.play(
            Write(A),
            Write(B)
        )
        graph_group = VGroup(g, A, B)
        self.play(
            graph_group.animate.to_edge(UP),
            run_time=2
        )
        self.wait(3)

        equation = MathTex(r"P = {", r"\text{Number of valid trails from A to B}", r" \over",
                           r"\text{Total number of valid trails}", '}')
        equation.next_to(g, DOWN)
        self.play(
            Write(equation[0]),
            run_time=2
        )
        self.wait(1.25)

        self.play(
            Write(equation[1]),
            run_time=3
        )
        self.wait(0.25)

        self.play(
            Write(equation[2]),
            run_time=1
        )

        self.play(
            Write(equation[3:]),
            run_time=3
        )
        self.wait()

        notes = MathTex(r"\text{*Valid: Trail length }\leq\text{ 3}").scale(0.5)
        notes.to_corner(DL)
        self.play(
            FadeIn(notes)
        )

        self.play(
            Indicate(equation[1])
        )
        self.play(
            Indicate(equation[3])
        )
        self.wait()
        self.play(
            FadeOut(equation),
            FadeOut(notes)
        )


class Strategy(Scene):
    def construct(self):
        g = get_diamond().to_edge(UP)
        A = Text("A").next_to(g[0], LEFT)
        B = Text("B").next_to(g[6], RIGHT)
        self.add(
            g, A, B
        )
        graph_group = VGroup(g, A, B)
        self.play(
            graph_group.animate.shift(DOWN)
        )
        tapir = SVGMobject("img/tapir.svg").scale(0.2).next_to(g[0].get_center(), UL*0.5)
        self.play(
            FadeIn(tapir)
        )
        self.play(
            tapir.animate.next_to(g[2].get_center(), UL*0.6)
        )
        self.play(
            tapir.animate.next_to(g[4].get_center(), UL * 0.6)
        )
        self.play(
            tapir.animate.next_to(g[3].get_center(), UL * 0.6)
        )
        self.play(
            tapir.animate.next_to(g[1].get_center(), UL * 0.6)
        )
        self.play(
            tapir.animate.next_to(g[2].get_center(), UL * 0.6)
        )
        shit = Text("?!").scale(0.5).move_to(tapir.get_center()+UR*0.3)
        self.wait()
        self.play(
            Write(shit)
        )
        self.wait(2)
        self.play(
            FadeOut(shit)
        )
        self.wait()
        self.play(
            FadeOut(tapir),
        )
        self.wait()

        # clockwise
        hand = Arrow(start=g[0].get_center(), end=g[0].get_center() + UP * 0.5, buff=0).set_color(YELLOW)

        self.play(
            Create(hand),
            run_time=2
        )
        self.play(Rotating(hand, about_point=g[0].get_center(), run_time=3, radians=-TAU))

        self.play(
            Flash(g[1]),
            run_time=1
        )
        self.play(
            Flash(g[2]),
            run_time=1
        )
        self.play(
            Flash(g[5]),
            run_time=1
        )
        self.play(
            FadeOut(hand),
            run_time=1
        )
        self.play(
            Uncreate(graph_group)
        )

        # tree diagram
        image = SVGMobject("img/tree.svg").scale(3)
        vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        tree_edges = [(1, 2), (1, 3), (2, 4), (2, 5), (2, 6), (3, 7), (3, 8), (3, 9)]
        g = Graph(vertices, tree_edges, labels=True, layout="tree", root_vertex=1).rotate(PI / 2).scale(2)
        g[3].move_to(g[3].get_center() + DOWN)
        g[2].move_to(g[2].get_center() + UP)
        for vertex in g:
            vertex.rotate(-PI / 2).scale(0.5)
        txt = Text("Tree Diagram").next_to(g, UP)
        self.play(
            FadeIn(image),
            Write(txt)
        )
        self.wait(0.5)
        self.play(
            FadeOut(image, UP)
        )

        self.play(
            Create(g),
        )
        self.wait(2)
        self.play(
            Uncreate(g),
            FadeOut(txt)
        )
        self.wait()


class Implementation(Scene):
    dx = 1
    dy = 1
    tree_group = VGroup()
    shrinked = False
    # for numbers to update cur coordinates
    tree_diagram = []
    tree_id = 0
    speed = SLOW

    # dictionary of list
    path_of_length = {1: VGroup(), 2: VGroup(), 3: VGroup()}

    number_7 = VGroup()

    def dfs_and_color(self, g, now, parent, length, cur_x, cur_y):
        txt = Text(str(now + 1)).move_to([cur_x, cur_y, 0]).set_color(HIGHLIGHT)
        self.tree_diagram += txt
        if now == 6:
            self.number_7 += txt
        now_id = self.tree_id
        self.tree_id += 1
        if self.shrinked:
            txt.scale(0.5)
        self.play(
            Write(txt),
            ApplyMethod(g[now].set_fill, HIGHLIGHT),
            run_time=self.speed
        )
        self.tree_group += txt

        # animation annotation exceptions
        if now_id == 0:
            self.wait()
            self.play(
                Flash(g[1])
            )
            self.play(
                Flash(g[2])
            )
            self.play(
                Flash(g[5])
            )
            self.wait()

        if now_id == 3:
            self.wait()
            for x in self.tree_group:
                if type(x) == Line:
                    self.play(
                        Indicate(x)
                    )
            self.wait()

        if now_id == 5:
            self.wait()
            self.play(
                Flash(g[4])
            )
            self.play(
                Flash(g[0])
            )
            self.wait()

        if now_id == 5:
            self.wait()

        if now_id == 8:
            self.speed *= 0.5

        if length == 3:
            animations = [ApplyMethod(txt.set_color, WHITE)]
            if (now == 0 and length == 0) or now != 0:
                animations.append(ApplyMethod(g[now].set_fill, WHITE))
            self.play(
                *animations,
                run_time=self.speed / 2
            )
            return cur_y - self.dy

        hand = Arrow(start=g[now].get_center(), end=g[now].get_center() + UP * 0.5, buff=0).set_color(YELLOW)
        self.play(
            Create(hand, run_time=self.speed)
        )
        self.play(Rotating(hand, about_point=g[now].get_center(), run_time=self.speed, radians=-TAU))
        self.play(
            Uncreate(hand, run_time=self.speed)
        )

        nxt_y = cur_y
        for nxt in adj[now]:
            if nxt == parent:
                continue

            # graph
            line1 = Line(g[now].get_center(), g[nxt].get_center(), color=HIGHLIGHT)

            # tree
            cur_x, cur_y, _ = self.tree_diagram[now_id].get_center()
            nxt_x = cur_x + self.dx
            tree_line = Line([cur_x + 0.2 * self.dx, cur_y, 0], [nxt_x - 0.2 * self.dx, nxt_y, 0])
            tree_line.set_color(HIGHLIGHT)
            self.tree_group += tree_line

            # draw
            self.play(
                Create(line1, run_time=self.speed),
                Create(tree_line, run_time=self.speed)
            )

            nxt_y = self.dfs_and_color(g, nxt, now, length + 1, nxt_x, nxt_y)
            if nxt_y == -3 and not self.shrinked:
                self.speed *= 0.5
                self.shrinked = True
                self.play(
                    self.tree_group.animate.scale(0.5).to_edge(UP)
                )
                self.dx *= 0.5
                self.dy *= 0.5
                nxt_y = self.tree_diagram[-1].get_y()-self.dy

            tree_line_back = Line(tree_line.get_end(), tree_line.get_start())
            self.tree_group += tree_line_back
            self.path_of_length[length + 1] += tree_line_back

            # draw
            self.play(
                Uncreate(line1, run_time=self.speed),
                Create(tree_line_back, run_time=self.speed)
            )

            self.tree_group -= tree_line
            self.remove(tree_line)

        animations = [ApplyMethod(txt.set_color, WHITE)]
        if (now == 0 and length == 0) or now != 0:
            animations.append(ApplyMethod(g[now].set_fill, WHITE))
        self.play(
            *animations,
            run_time=self.speed / 2
        )
        return nxt_y

    def construct(self):
        g = get_diamond()
        self.play(Create(g))
        A = Text("A").next_to(g[0], LEFT)
        B = Text("B").next_to(g[6], RIGHT)
        self.play(
            Write(A),
            Write(B)
        )
        self.wait()
        self.play(
            FadeOut(VGroup(A, B))
        )
        graph_group = VGroup(
            g
        )
        txt = []
        for i in range(7):
            if i == 6:
                txt.append(Text(str(i + 1)).next_to(g[i], UP))
            else:
                txt.append(Text(str(i + 1)).next_to(g[i], UP + LEFT))
            graph_group += txt[-1]

        self.play(
            *[Write(x) for x in txt]
        )

        self.wait()

        self.play(
            graph_group.animate.scale(0.5).to_corner(UR)
        )

        self.dfs_and_color(g, 0, -1, 0, -2, 3)
        self.wait()


class Calculation(Scene):
    dx = 1
    dy = 1
    tree_group = VGroup()
    shrinked = False
    # for numbers to update cur coordinates
    tree_diagram = []
    tree_id = 0
    speed = SLOW

    # dictionary of list
    path_of_length = {1: VGroup(), 2: VGroup(), 3: VGroup()}

    number_7 = VGroup()

    def dfs_and_color(self, g, now, parent, length, cur_x, cur_y):
        txt = Text(str(now + 1)).move_to([cur_x, cur_y, 0])
        self.tree_diagram += txt
        if now == 6:
            self.number_7 += txt
        now_id = self.tree_id
        self.tree_id += 1
        if self.shrinked:
            txt.scale(0.5)
        self.add(
            txt
        )
        self.tree_group += txt

        if length == 3:
            return cur_y - self.dy

        nxt_y = cur_y
        for nxt in adj[now]:
            if nxt == parent:
                continue

            # graph

            # tree
            cur_x, cur_y, _ = self.tree_diagram[now_id].get_center()
            nxt_x = cur_x + self.dx
            tree_line = Line([cur_x + 0.2 * self.dx, cur_y, 0], [nxt_x - 0.2 * self.dx, nxt_y, 0])
            self.tree_group += tree_line

            nxt_y = self.dfs_and_color(g, nxt, now, length + 1, nxt_x, nxt_y)
            if nxt_y == -3 and not self.shrinked:
                self.speed *= 0.5
                self.shrinked = True
                self.tree_group.scale(0.5).to_edge(UP)
                self.dx *= 0.5
                self.dy *= 0.5
                nxt_y = self.tree_diagram[-1].get_y()-self.dy

            tree_line_back = Line(tree_line.get_end(), tree_line.get_start())
            self.tree_group += tree_line_back
            self.path_of_length[length + 1] += tree_line_back

            # draw
            self.add(
                tree_line_back
            )
            self.tree_group -= tree_line
        return nxt_y

    def construct(self):
        g = get_diamond()
        self.add(g)
        graph_group = VGroup(
            g
        )
        txt = []
        for i in range(7):
            if i == 6:
                txt.append(Text(str(i + 1)).next_to(g[i], UP))
            else:
                txt.append(Text(str(i + 1)).next_to(g[i], UP + LEFT))
            graph_group += txt[-1]

        self.add(
            *txt
        )
        graph_group.scale(0.5).to_corner(UR)
        self.dfs_and_color(g, 0, -1, 0, -2, 3)
        self.wait()
        self.play(
            self.tree_group.animate.to_edge(LEFT)
        )

        self.wait()

        equation_1 = MathTex(r"P ={\text{Number of trails ending at B} \over \text{Total number of trails} }")
        equation_2 = MathTex(r"P = {", r"\text{Number of trails ending at B}", r" \over",
                             r"\text{Total number of trails}", '}')
        equation_3 = MathTex(r"P = {4 \over 23}")
        equations = VGroup(equation_1, equation_2, equation_3)
        equations.arrange(DOWN, center=True, aligned_edge=LEFT)
        self.play(
            Write(equation_1)
        )
        self.wait()
        self.play(
            ReplacementTransform(equation_1.copy(), equation_2)
        )
        self.wait()

        self.play(
            *[Flash(x) for x in self.path_of_length[1]],
            self.path_of_length[1].animate.set_color(HIGHLIGHT)
        )
        self.wait()
        self.play(
            Transform(equation_2[-2], MathTex(r"3").move_to(equation_2[-2]))
        )

        self.wait()
        self.play(
            *[Flash(x) for x in self.path_of_length[2]],
            self.path_of_length[2].animate.set_color(HIGHLIGHT)
        )
        self.wait()
        self.play(
            Transform(equation_2[-2], MathTex(r"3+6").move_to(equation_2[-2]))
        )
        self.wait()

        self.play(
            *[Flash(x) for x in self.path_of_length[3]],
            self.path_of_length[3].animate.set_color(HIGHLIGHT)
        )
        self.wait()
        self.play(
            Transform(equation_2[-2], MathTex(r"3+6+14").move_to(equation_2[-2]))
        )

        self.play(
            *[self.path_of_length[length].animate.set_color(WHITE) for length in range(1, 4)]
        )
        self.wait()

        B = Text("B").move_to(txt[-1]).scale(0.5)
        self.play(
            Transform(txt[-1], B)
        )
        self.wait()
        self.play(
            FocusOn(txt[-1].get_center())
        )
        self.wait()

        self.play(
            Transform(txt[-1], Text("7").move_to(txt[-1]).scale(0.5))
        )
        self.wait()

        boxes = VGroup()
        for seven in self.number_7:
            box = SurroundingRectangle(seven, buff=0.05)
            boxes += box
        self.play(
            Create(boxes)
        )

        self.wait()
        odd_7_arrow = Arrow(start=self.number_7[-1].get_center() + DL, end=self.number_7[-1].get_center())
        self.play(
            Create(odd_7_arrow)
        )
        self.wait()
        self.play(
            g.edges[(0, 5)].animate.set_color(HIGHLIGHT)
        )
        self.play(
            g.edges[(5, 6)].animate.set_color(HIGHLIGHT)
        )
        self.play(
            FocusOn(g[5])
        )
        self.play(
            g.edges[(0, 5)].animate.set_color(WHITE),
            g.edges[(5, 6)].animate.set_color(WHITE)
        )
        self.play(
            Uncreate(odd_7_arrow)
        )

        self.play(
            Transform(equation_2[1], MathTex(r"4").move_to(equation_2[1]))
        )
        self.wait()

        self.play(
            FadeOut(boxes)
        )
        self.wait()
        self.play(
            Transform(equation_2.copy(), equation_3)
        )
        self.wait()
        self.play(
            Create(SurroundingRectangle(equation_3, buff=0.1))
        )
        self.play(
            FadeOut(graph_group)
        )
        self.play(
            FadeOut(self.tree_group)
        )
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        self.wait()


class Reflection(Scene):
    def construct(self):
        tapir1 = SVGMobject("img/tapir.svg")
        tapir2 = SVGMobject("img/tapir-left.svg").next_to(tapir1, RIGHT)
        Group(tapir1, tapir2).arrange()
        self.play(
            Write(tapir1),
            Write(tapir2),
            run_time=2
        )

        speech1 = Text("That's quite easy").next_to(tapir1, DOWN)
        self.play(
            Write(speech1)
        )
        speech2 = Text("Yeah just count all the trails").next_to(tapir2, UP)
        self.play(
            Write(speech2)
        )
        self.wait(2)
        self.play(
            Transform(speech1, Text("You counted 19 trails right?").move_to(speech1))
        )
        self.wait()
        self.play(
            Transform(speech2, Text("Wasn't it 21?").move_to(speech2))
        )
        self.wait(2)
        self.play(
            FadeOut(speech1),
            FadeOut(speech2)
        )
        self.wait()
        self.play(
            FadeOut(tapir1),
            FadeOut(tapir2)
        )
        self.wait()


class DFS(Scene):
    def dfs(self, now, par, g, length):
        self.play(
            g[now].animate.set_fill(GREEN),
            run_time=0.07
        )
        if length == 3:
            if now != 0 or par == -1:
                self.play(
                    g[now].animate.set_fill(WHITE),
                    run_time=0.07
                )
            return
        for nxt in adj[now]:
            if nxt == par:
                continue
            arrow = Arrow(start=g[now].get_center(), end=g[nxt].get_center(), color=GREEN, buff=0)
            self.play(
                GrowArrow(arrow),
                run_time=0.4
            )
            self.dfs(nxt, now, g, length + 1)
            self.play(
                arrow.animate.scale(0, scale_tips=True, about_point=g[now].get_center()),
                run_time=0.4
            )
            self.remove(arrow)

        if now != 0 or par == -1:
            self.play(
                g[now].animate.set_fill(WHITE),
                run_time=0.07
            )

    def construct(self):
        g = get_diamond()
        self.play(
            Create(g)
        )
        self.wait()
        txt = Text("Depth-first search").next_to(g, DOWN)
        self.play(
            Write(txt)
        )
        self.dfs(0, -1, g, 0)
        self.play(
            Uncreate(g),
            FadeOut(txt)
        )
        self.wait()


class Ending(Scene):
    def construct(self):
        # tapir = ImageMobject("img/cute-tapir.png")
        # self.play(
        #     FadeIn(tapir)
        # )
        # self.play(
        #     tapir.animate.shift(LEFT)
        # )
        kopi = ImageMobject("img/kopi.png").scale(0.5)
        self.play(
            FadeIn(kopi)
        )
        kopi_2 = ImageMobject("img/kopi.png").scale(0.5)
        title = Text("Kopitiam Maths")
        closing = Group(
            kopi_2, title
        )
        closing.arrange()
        self.play(
            Transform(kopi, kopi_2)
        )
        self.play(
            Write(title)
        )
        self.wait(2)


class ClockHand(Scene):
    def construct(self):
        g = get_diamond()
        self.play(Create(g))
        hand = Arrow(start=g[0].get_center(), end=g[0].get_center() + UP * 0.5, buff=0).set_color(YELLOW)

        self.play(
            Create(hand)
        )
        self.play(Rotating(hand, about_point=g[0].get_center(), run_time=2, radians=-TAU))
        self.play(
            FadeOut(hand)
        )


class lts(Scene):
    def construct(self):
        g = get_diamond()
        autolayouts = ["spring", "circular", "kamada_kawai",
                       "planar", "random", "shell",
                       "spectral", "spiral"]
        self.play(Create(g))
        for lt in autolayouts:
            self.play(
                g.animate.change_layout(lt)
            )
        for i in range(5):
            self.play(
                g.animate.change_layout("random")
            )


class Colors(Scene):
    def construct(self):
        self.play(
            Create(
                VGroup(
                    Text("G").set_color(BLUE),
                    Text("A").set_color(BLUE_A),
                    Text("B").set_color(BLUE_B),
                    Text("C").set_color(BLUE_C),
                    Text("D").set_color(BLUE_D),
                    Text("E").set_color(BLUE_E)
                ).arrange()
            )
        )


# Thumbnails
class Thumbnail(Scene):
    def construct(self):
        tapir = SVGMobject("img/tapir.svg").scale(1.2)
        g = get_diamond().set_color(color=[BLUE_D, BLUE_A])
        VGroup(tapir, g).arrange()
        tapir.shift(LEFT)
        g.shift(RIGHT)
        tapir.align_to(g, DOWN)
        txt = Text("?!#%").next_to(tapir, UR * 0.05, buff=0)
        title = MathTex(r"\text{Find }").to_edge(UP).scale(2)
        maths_str = MathTex(r"P(v_0=A \wedge v_r=B|m(v_0...v_r)\leq3)").next_to(title, DOWN)
        maths_str.set_color(color=[GREEN, YELLOW])
        everything = VGroup(
            tapir, txt, g, title, maths_str
        ).move_to(ORIGIN)
        self.add(
            everything
        )
        self.wait()


class Thumbnail_B(Scene):
    def construct(self):
        tapir = SVGMobject("img/tapir.svg").scale(1.2)
        g = get_diamond().set_color(color=[PINK, YELLOW])
        VGroup(tapir, g).arrange()
        tapir.shift(LEFT)
        g.shift(RIGHT)
        tapir.align_to(g, DOWN)
        txt = Text("?!#%").next_to(tapir, UR * 0.05, buff=0)

        kopi = ImageMobject("img/kopi.png").scale(0.2)
        title_txt = Text("Kopitiam Maths")
        title = Group(
            kopi, title_txt
        ).arrange().to_edge(UP)

        props = VGroup(
            tapir, txt, g
        ).move_to(ORIGIN)

        everything = Group(
            props, title
        )
        self.add(
            everything
        )
        self.wait()


class Minimalist(Scene):
    def construct(self):
        g = get_diamond().scale(1.5)
        del g[0]
        self.add(g)
        self.wait()


class Gradient(Scene):
    def construct(self):
        s = Square(fill_color=[RED, YELLOW], fill_opacity=1, stroke_opacity=0).scale(5)
        self.add(s)
        self.wait()


class Tapir(Scene):
    def construct(self):
        tapir = SVGMobject("img/tapir.svg").scale(2)
        txt = Text("?!#%").scale(3).next_to(tapir, UR)
        VGroup(tapir, txt).move_to(ORIGIN)
        self.add(
            tapir, txt
        )


class Chosen(Scene):
    def construct(self):
        tapir = SVGMobject("img/tapir.svg").scale(1.4)
        g = get_diamond()
        VGroup(tapir, g).arrange()
        tapir.shift(LEFT*0.5)
        g.shift(RIGHT*0.5)
        tapir.align_to(g, DOWN)
        txt = Text("?!#%").next_to(tapir, UR * 0.00001, buff=0)
        everything = Group(
            tapir, txt, g
        ).move_to(ORIGIN)
        graph = ImageMobject("img/cool-maze-no-bg.png").scale(0.7).move_to(g)
        kopi = ImageMobject("img/kopi.png").scale(0.3).to_corner(DR, buff=0)
        self.add(
            tapir, txt, kopi, graph
        )
        self.wait()


class ProblemStatement(Scene):
    def construct(self):

        g = get_diamond()
        tapir = SVGMobject("img/cute-tapir.svg")
        tapir.scale(0.2).next_to(g[0].get_center(), UL * 0.5 + UP+0.25),
        A = Text("A").next_to(g[0], LEFT)
        B = Text("B").next_to(g[6], RIGHT)

        g_group = VGroup(
            A, B, g, tapir
        )
        g_group.to_edge(DOWN)
        self.add(
            g_group
        )

        txt = Text("Find the probability that the tapir reaches B from A.").scale(
            0.7).to_edge(UP)
        self.add(
            txt
        )
        conditions = [
            "1. The tapir must move.",
            "2. The tapir can move 3 steps maximum.",
            "3. Roads cannot be reused.",
            "4. Each sequence of moves has an equal probability of being chosen."
        ]
        clarifications = VGroup(*[Text(x).scale(0.5) for x in conditions])
        clarifications.arrange(DOWN, center=False, aligned_edge=LEFT).next_to(txt, DOWN)
        for x in clarifications:
            self.add(
                x
            )
        self.wait()