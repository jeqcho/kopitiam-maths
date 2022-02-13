from manim import *

quadratic_formula = MathTex(r"x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}")

graph_x_axis = NumberLine(
    x_range=[0, 8, 1]
)
kx = {2: MathTex(r"\alpha", color=YELLOW), 6: MathTex(r"\beta", color=YELLOW)}
points = VGroup(Dot([2, 0, 0], color=YELLOW), Dot([-2, 0, 0], color=YELLOW))
graph_x_axis_labelled = graph_x_axis.copy().add_labels(kx, DOWN)


def f(x):
    return 0.75 * (x - 2) * (x + 2)


graph = FunctionGraph(f, [-3, 3], color=WHITE)
graphs = VGroup(graph, graph_x_axis_labelled)

givens = Tex(r'Given {{$\alpha+\beta$}} and {{$\alpha\beta$}}, can we find $\alpha$ and $\beta$ separately?').scale(
    0.5).to_corner(DL)

entire_graph = VGroup(graph, graph_x_axis_labelled, points)


class Intro(Scene):
    """
    manim visualise-quadratics.py Intro -pql
    """

    def construct(self):
        self.play(
            Write(quadratic_formula, run_time=4)
        )
        self.wait(4)
        self.play(
            Transform(quadratic_formula, graph_x_axis, run_time=3)
        )
        self.wait()
        self.play(
            Create(graph)
        )
        self.wait()
        self.play(
            Create(points)
        )
        self.wait()

        self.play(
            Transform(graph_x_axis, graph_x_axis_labelled)
        )
        self.wait()

        self.play(
            Write(givens)
        )
        self.wait(4)


everything_after_intro = VGroup(graphs, points, givens)

general = MathTex(r'x = \frac{\alpha+\beta}{2}\pm\sqrt{\left(\frac{\alpha+\beta}{2}\right)^2 - \alpha\beta}')


class Visualisation(Scene):
    """
    manim visualise-quadratics.py Visualisation -pql
    """

    def construct(self):
        global entire_graph
        self.add(everything_after_intro)
        self.wait(4)
        midpoint_dot = Dot()
        midpoint_label = MathTex("m").next_to(midpoint_dot, DOWN)

        self.play(
            Create(midpoint_dot),
            Write(midpoint_label)
        )
        self.wait(4)
        br1 = BraceBetweenPoints([2, 0, 0], [0, 0, 0]).shift(UP * 0.25)
        br2 = BraceBetweenPoints([0, 0, 0], [-2, 0, 0]).shift(UP * 0.25)
        t1 = MathTex("d").next_to(br1, UP)
        t2 = MathTex("d").next_to(br2, UP)

        self.play(Write(br1), Write(br2), Write(t1), Write(t2))
        self.wait(3)
        original_graph = entire_graph.copy()
        original_graph.add(*[br1, br2, midpoint_dot])
        entire_graph.add(*[br1, br2, t1, t2, midpoint_dot, midpoint_label])
        self.play(
            entire_graph.animate.scale(0.7)
        )
        self.play(
            entire_graph.animate.shift(LEFT * 3)
        )
        deletable = [entire_graph, graphs, points]
        self.wait(2)
        def_a = MathTex(r'{{\alpha}} = {{m}}-{{d}}')
        def_b = MathTex(r'{{\beta}} = {{m}}+{{d}}')
        def_x = MathTex(r'{{x}} = {{m}}\pm{{d}}')
        relations = VGroup(*[
            def_a,
            def_b,
            def_x
        ]).arrange(DOWN).shift(RIGHT * 2)

        self.play(
            Write(def_a)
        )
        self.wait(4)
        self.play(
            Write(def_b)
        )
        self.wait(5)
        self.play(
            Write(def_x)
        )
        self.wait(5)
        self.play(
            relations.animate.scale(0.7).to_corner(UR)
        )
        self.wait()

        midpoint_def = MathTex(r"m=\frac{\alpha+\beta}{2}").shift(RIGHT * 2)

        self.play(
            Write(midpoint_def)
        )
        self.wait(7)
        self.play(
            midpoint_def.animate.scale(0.7).next_to(relations, DOWN)
        )
        relations.add(midpoint_def)
        sr = SurroundingRectangle(relations)
        self.play(
            Create(sr)
        )
        self.wait(5)
        start_por = MathTex(r'{{\alpha\beta}} = {{\alpha\beta}}')
        por_defined_a = MathTex(r'{{\alpha\beta}}', r'= (m-d)\beta')
        por_defined_ab = MathTex(r'{{\alpha\beta}}', r'= (m-d)(m+d)')
        por_defined_expand = MathTex(r'{{\alpha\beta}}', r'= m^2 + md -md - d^2')
        por_defined_simplified = MathTex(r'{{\alpha\beta}}', r'= m^2 - d^2')
        d_define = MathTex(r'{{d^2}}= m^2 - \alpha\beta')
        d_end = MathTex(r'{{d}}= \sqrt{m^2 - \alpha\beta}')
        d_full = MathTex(r'{{d}}= \sqrt{\left( \frac{\alpha+\beta}{2} \right)^2 - \alpha\beta}')
        all_eq = VGroup(*[
            start_por,
            por_defined_a,
            por_defined_ab,
            por_defined_expand,
            por_defined_simplified,
            d_define,
            d_end,
            d_full
        ]).arrange(DOWN).shift(RIGHT)
        for x in all_eq[1:]:
            x[0].align_to(start_por[0], RIGHT)
        for x in all_eq[1:]:
            x[1].align_to(start_por[1], LEFT)
        self.play(
            Write(start_por)
        )
        self.wait(3)
        self.play(
            ReplacementTransform(start_por[1].copy(), por_defined_a)
        )
        self.wait()
        self.play(
            ReplacementTransform(por_defined_a.copy(), por_defined_ab)
        )
        self.wait()
        self.play(
            ReplacementTransform(por_defined_ab.copy(), por_defined_expand)
        )
        self.wait()
        self.play(
            ReplacementTransform(por_defined_expand.copy(), por_defined_simplified)
        )
        self.wait()
        self.play(
            ReplacementTransform(por_defined_simplified.copy(), d_define)
        )
        self.wait()
        self.play(
            ReplacementTransform(d_define.copy(), d_end)
        )
        self.wait(2)
        self.play(
            ReplacementTransform(d_end.copy(), d_full)
        )
        self.wait(7)
        deletable += [x for x in all_eq if x != d_full]
        deletable += sr
        self.play(
            FadeOut(*deletable)
        )
        self.wait()
        self.play(
            d_full.animate.scale(0.7).next_to(midpoint_def, DOWN).align_to(midpoint_def, RIGHT)
        )
        self.wait()
        self.play(
            def_x.animate.scale(1 / 0.7).move_to(Point([-3, 2, 0]))
        )
        self.wait(2)
        sub_a1 = MathTex(r'{{x}} = \frac{\alpha+\beta}{2}\pm{{d}}').next_to(def_x, DOWN).align_to(def_x, LEFT)
        sub_a2 = MathTex(r'{{x}} = \frac{\alpha+\beta}{2}\pm\sqrt{\left(\frac{\alpha+\beta}{2}\right)^2 - \alpha\beta}') \
            .next_to(sub_a1, DOWN).align_to(def_x, LEFT)

        self.play(
            ReplacementTransform(def_x.copy(), sub_a1)
        )
        self.wait(2)
        self.play(
            ReplacementTransform(sub_a1.copy(), sub_a2)
        )
        self.wait(4)
        self.play(
            Circumscribe(givens, run_time=2)
        )
        self.wait(2)
        self.play(
            *[FadeOut(x) for x in self.mobjects if x != sub_a2]
        )
        self.play(
            sub_a2.animate.scale(0.7).move_to(Point([0, 0, 0])).to_edge(UP)
        )
        self.wait()
        _kx = {2: MathTex(r"\alpha", color=YELLOW), 6: MathTex(r"\beta", color=YELLOW)}
        _graph_x_axis = NumberLine(
            x_range=[0, 8, 1]
        ).add_labels(_kx, DOWN)
        _points = VGroup(Dot([2, 0, 0], color=YELLOW), Dot([-2, 0, 0], color=YELLOW))

        _graph = FunctionGraph(f, [-3, 3], color=WHITE)
        midpoint_dot = Dot()
        midpoint_label = MathTex(r"\frac{\alpha+\beta}{2}").scale(0.5).next_to(midpoint_dot, DOWN)
        br1 = BraceBetweenPoints([2, 0, 0], [0, 0, 0]).shift(UP * 0.25)
        br2 = BraceBetweenPoints([0, 0, 0], [-2, 0, 0]).shift(UP * 0.25)
        t1 = MathTex(r"\sqrt{\left(\frac{\alpha+\beta}{2}\right)^2 - \alpha\beta}").scale(0.45).next_to(br1, UP)
        t2 = MathTex(r"\sqrt{\left(\frac{\alpha+\beta}{2}\right)^2 - \alpha\beta}").scale(0.45).next_to(br2, UP)
        _graph_container = [
            _graph, _points, midpoint_dot, _graph_x_axis
        ]
        _text_container = [
            midpoint_label, br1, br2, t1, t2,
        ]
        self.play(
            *[Create(x) for x in _graph_container]
        )
        self.play(
            *[Write(x) for x in _text_container], run_time=2
        )
        self.wait(6)
        self.play(
            FadeOut(*_graph_container),
            FadeOut(*_text_container), run_time=2
        )


class QuadraticFormula(Scene):
    """
    manim visualise-quadratics.py QuadraticFormula -pql
    """

    def construct(self):
        global general
        self.add(general.scale(0.7).to_edge(UP))
        self.wait()
        alt_def = Tex(
            r"$\alpha + \beta=-\frac{b}{a}$ , $\alpha\beta=\frac{c}{a}$", color=YELLOW)
        alt_def_des = MathTex(r'\text{for }ax^2+bx+c=0').scale(0.6).next_to(alt_def, DOWN)
        self.play(
            Write(alt_def),
            Write(alt_def_des)
        )
        self.wait(5)
        self.play(
            alt_def.animate.scale(0.8).to_corner(DR),
            FadeOut(alt_def_des)
        )
        self.wait()
        derive = VGroup(*[
            MathTex(r'x = \frac{1}{2}\left(\frac{-b}{a}\right)\pm\sqrt{\left(\frac{-b}{2a}\right)^2 - \frac{c}{a}}'),
            MathTex(r'x = \frac{-b}{2a}\pm\sqrt{\frac{b^2}{4a^2} - \frac{c}{a}}'),
            MathTex(r'x = \frac{-b}{2a}\pm\sqrt{\frac{b^2}{4a^2} - \frac{4ac}{4a^2}}'),
            MathTex(r'x = \frac{-b}{2a}\pm\sqrt{\frac{b^2-4ac}{4a^2}}'),
            MathTex(r'x = \frac{-b}{2a}\pm\frac{\sqrt{b^2-4ac}}{2a}'),
            MathTex(r'x = \frac{-b\pm\sqrt{b^2-4ac}}{2a}'),
        ]).scale(0.7).arrange(DOWN).next_to(general, DOWN).align_to(general, LEFT)
        self.play(
            Write(derive[0].copy())
        )
        self.wait()
        for x in range(1, len(derive)):
            self.play(Transform(derive[x - 1], derive[x].copy()))
            self.wait()
        self.play(
            *[FadeOut(x) for x in self.mobjects if x != derive[-2]]
        )
        self.play(
            derive[-2].animate.scale(1 / 0.7).to_edge(UP)
        )
        _kx = {2: MathTex(r"\alpha", color=YELLOW), 6: MathTex(r"\beta", color=YELLOW)}
        _graph_x_axis = NumberLine(
            x_range=[0, 8, 1]
        ).add_labels(_kx, DOWN)
        _points = VGroup(Dot([2, 0, 0], color=YELLOW), Dot([-2, 0, 0], color=YELLOW))

        _graph = FunctionGraph(f, [-3, 3], color=WHITE)
        midpoint_dot = Dot()
        midpoint_label = MathTex(r"\frac{-b}{2a}").scale(0.5).next_to(midpoint_dot, DOWN)
        br1 = BraceBetweenPoints([2, 0, 0], [0, 0, 0]).shift(UP * 0.25)
        br2 = BraceBetweenPoints([0, 0, 0], [-2, 0, 0]).shift(UP * 0.25)
        t1 = MathTex(r"\frac{\sqrt{b^2-4ac}}{2a}").scale(0.5).next_to(br1, UP)
        t2 = MathTex(r"\frac{\sqrt{b^2-4ac}}{2a}").scale(0.5).next_to(br2, UP)
        _graph_container = [
            _graph, _points, midpoint_dot, _graph_x_axis
        ]
        _text_container = [
            midpoint_label, br1, br2, t1, t2,
        ]
        self.play(
            *[Create(x) for x in _graph_container]
        )
        self.play(
            *[Write(x) for x in _text_container]
        )
        self.wait()


class Test(Scene):
    """
    manim visualise-quadratics.py Test -pql
    """

    def construct(self):
        a = Tex('a')
        b = Tex('b').shift(RIGHT)
        self.play(Create(a))
        self.play(
            ReplacementTransform(a.copy(), b)
        )
        self.play(
            Circumscribe(a)
        )
        self.play(
            Circumscribe(b)
        )
        g = VGroup(a, b)
        for x in g:
            self.play(
                FadeOut(x)
            )
        self.play(
            FadeOut(a)
        )
        self.play(
            FadeOut(b)
        )


class Ending(Scene):
    """
    manim visualise-quadratics.py Ending -pql
    """

    def construct(self):
        txt = VGroup(*[
            Text('Made by:'),
            Text('Tan Chin Peng'),
            Text('Chooi Je Qin'),
            Text('Adel Arif'),
            Text('Nga Tian Ern'),
            Text('Phil Yeh'),
        ]).arrange(DOWN, center=True)
        self.play(
            FadeIn(txt)
        )
        self.wait(3)
        self.play(
            FadeOut(txt)
        )
        discord = ImageMobject('img/discord.png').scale_to_fit_width(3)
        saveSPM = ImageMobject('img/savespm.png').scale_to_fit_width(3)
        images = Group(discord, saveSPM).arrange(LEFT)
        self.play(
            FadeIn(images)
        )
        self.wait()


class Thumbnail(Scene):
    """
    manim visualise-quadratics.py Thumbnail -psqh
    """

    def construct(self):
        graph_x_axis = NumberLine(
            x_range=[0, 8, 1]
        )
        points = VGroup(Dot([1.414, 0, 0]), Dot([-1.414, 0, 0]))

        def f(x):
            return 0.5 * (x - 2) * (x + 2) + 1

        graph = FunctionGraph(f, [-3, 3])
        graphs = VGroup(graph, graph_x_axis)
        midpoint_dot = Dot()
        a = MathTex(r"\alpha").next_to(points[1], DOWN)
        b = MathTex(r"\beta").next_to(points[0], DOWN)
        midpoint_label = MathTex("m").next_to(midpoint_dot, DOWN)

        br1 = BraceBetweenPoints([1.414, 0, 0], [0, 0, 0]).shift(UP * 0.25)
        br2 = BraceBetweenPoints([0, 0, 0], [-1.414, 0, 0]).shift(UP * 0.25)
        t1 = MathTex("d").next_to(br1, UP)
        t2 = MathTex("d").next_to(br2, UP)
        all_g = VGroup(br1, br2, t1, t2, graphs, midpoint_dot, a, b, points, midpoint_label).shift(DOWN * 2)

        self.add(all_g)
        # self.add(MathTex('x = m \pm d').shift(UP * 2))
        self.add(MathTex(r'x = \frac{-b\pm\sqrt{b^2-4ac}}{2a}').shift(UP * 2))
        title = Text('Visualising the Quadratic Formula', color=BLUE).scale(1.4).to_edge(UP)
        self.add(title)
