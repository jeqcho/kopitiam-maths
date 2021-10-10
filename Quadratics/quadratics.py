from manim import *


# py -m manim quadratics.py part1 -pql
class part1(Scene):
    def construct(self):
        tex0 = Text("Quadratic Functions").shift(UP)
        tex1 = MathTex(r"f(x)=ax^2+bx+c").next_to(tex0, DOWN)
        self.wait()
        self.play(Write(tex0))
        self.play(Write(tex1))
        self.wait(5)
        self.play(FadeOut(tex0, tex1))
        axes = Axes(
            x_range=[-10, 10, 1],
            y_range=[-50, 100, 10],
            x_length=10,
            axis_config={"color": GREEN},
            tips=False,
        )

        graphs = []
        texts = []
        a1 = [-2, -1, 1, 2, -3, -4]
        b1 = [8, 16, 8, -8, -16, -8, ]
        c1 = [10, 20, 10, -10, -20]
        for a in a1:
            b = b1[0]
            c = c1[0]

            def f1(x1):
                return a * x1 * x1 + b * x1 + c

            g = axes.get_graph(f1, [-10, 10])
            graphs.append(VGroup(axes, g))
            texts.append(MathTex(
                f"f(x)={'-' if a == -1 else ''}{a if abs(a) != 1 else ''}x^2{'+' if b >= 0 else ''}{b}x{'+' if c >= 0 else ''}{c}").shift(
                UP * 3.5).shift(RIGHT))
        for b in b1:
            a = a1[3]
            c = c1[0]

            def f1(x1):
                return a * x1 * x1 + b * x1 + c

            g = axes.get_graph(f1, [-10, 10])
            graphs.append(VGroup(axes, g))
            texts.append(MathTex(
                f"f(x)=2x^2{'+' if b >= 0 else ''}{b}x{'+' if c >= 0 else ''}{c}").shift(UP * 3.5).shift(RIGHT))
        for c in c1:
            a = a1[3]
            b = b1[0]

            def f1(x1):
                return a * x1 * x1 + b * x1 + c

            g = axes.get_graph(f1, [-10, 10])
            graphs.append(VGroup(axes, g))
            texts.append(MathTex(
                f"f(x)=2x^2{'+' if b >= 0 else ''}{b}x{'+' if c >= 0 else ''}{c}").shift(UP * 3.5).shift(RIGHT))
        self.play(FadeIn(graphs[0], axes))
        for i in range(3):
            self.play(Transform(graphs[0], graphs[i + 1]),
                      Transform(texts[0], texts[i + 1]))
            self.wait(1)
        for i in range(3, len(graphs) - 1):
            self.play(Transform(graphs[0], graphs[i + 1]),
                      Transform(texts[0], texts[i + 1]))
            self.wait(0.5)

        self.wait(7)
        b = 10
        c = 20
        a = 0

        def f2(x1):
            return a * x1 * x1 + b * x1 + c

        g = axes.get_graph(f2, [-10, 10])
        gr = VGroup(axes, g)
        text = MathTex(
            f"f(x)={a}x^2{'+' if b >= 0 else ''}{b}x+{c}").shift(UP * 3.5).shift(RIGHT)
        self.play(Transform(graphs[0], gr), Transform(texts[0], text))
        self.wait(6)
        a = 2
        b = 0
        c = 10

        g = axes.get_graph(f2, [-10, 10])
        gr = VGroup(axes, g)
        text = MathTex(
            f"f(x)={a}x^2{'+' if b >= 0 else ''}{b}x+{c}").shift(UP * 3.5).shift(RIGHT)
        self.play(Transform(graphs[0], gr), Transform(texts[0], text))
        self.wait(2)
        a = 2
        b = 8
        c = 0

        g = axes.get_graph(f2, [-10, 10])
        gr = VGroup(axes, g)
        text = MathTex(
            f"f(x)={a}x^2{'+' if b >= 0 else ''}{b}x+{c}").shift(UP * 3.5).shift(RIGHT)
        self.play(Transform(graphs[0], gr), Transform(texts[0], text))
        self.wait(2)
        self.play(FadeOut(gr, graphs[0], texts[0]))
        self.wait(2)
        axes = Axes(
            x_range=[-10, 10, 1],
            y_range=[-60, 100, 10],
            x_length=10,
            axis_config={"color": GREEN},
            tips=False,
        )

        def f2(x1):
            return (x1 - 3) * (x1 + 7)

        g = axes.get_graph(f2, [-10, 10])
        axis = VGroup(axes)
        r1 = Dot(axes.i2gp(3, g))
        r2 = Dot(axes.i2gp(-7, g))
        gr = VGroup(g)
        self.play(FadeIn(gr, axis))
        self.wait(2)
        self.play(FadeOut(gr), FadeIn(r1, r2), run_time=3)
        self.wait(3)
        self.play(FadeOut(r1, r2))
        graphs = []
        texts = []
        for x in reversed(range(-3, 4)):
            if x == 0:
                continue

            def f1(x1):
                return x * (x1 - 5) * (x1 + 5)

            g = axes.get_graph(f1, [-10, 10])
            graphs.append(VGroup(g))
            texts.append(MathTex(
                f"f(x)={x}\cdot(x^2-25)").to_corner(UR))
        r1 = Dot(axes.i2gp(-5, g))
        r2 = Dot(axes.i2gp(5, g))
        self.play(FadeIn(graphs[0]))
        self.play(FadeIn(r1, r2))
        for i in range(len(graphs) - 1):
            if i > 0:
                self.remove(graphs[i - 1], texts[i - 1])
            self.play(Transform(graphs[0], graphs[i + 1]),
                      Transform(texts[0], texts[i + 1]))
            self.wait(1)

        self.play(
            *[FadeOut(x) for x in self.mobjects]
        )

        a = [3, 6, 9, -2]
        b = [9, 3, -2, 32]
        c = [10, -4, 7, 3]
        instruction = Tex(f'Find $x$ where ')
        animations = VGroup(
            *[Tex(f"${a[i]}x^2{'+' if b[i] >= 0 else ''}{b[i]}x{'+' if c[i] >= 0 else ''}{c[i]}=0$") for i in
              range(len(a))])
        self.play(
            Write(instruction.shift(LEFT * 2))
        )
        self.play(
            Write(animations[0].next_to(instruction, RIGHT))
        )
        for i in range(len(a) - 1):
            self.play(
                ReplacementTransform(animations[i], animations[i + 1].align_to(animations[i], LEFT))
            )
            self.wait()
        self.play(
            FadeOut(instruction),
            FadeOut(animations[-1])
        )


# py -m manim quadratics.py part2 -pql
class part2(Scene):
    def construct(self):
        tex1 = MathTex(r"(x-h)^2=k").shift(UP * 2)
        tex2 = MathTex(r"x=h\pm\sqrt{k}").next_to(tex1, DOWN)
        self.play(Write(tex1))
        self.wait(7)
        self.play(Write(tex2))
        self.wait(7)
        v = Group()
        for i in self.mobjects:
            v.add(i)
        self.play(FadeOut(v))
        self.wait()

        # completing the square trick
        tex9 = MathTex(
            r"x^2+bx", r"&=x^2+bx+\left(\frac{b}{2}\right)^2-\left(\frac{b}{2}\right)^2\\&=(", r"x",
            r"+\frac{b}{2})^2-\left(\frac{b}{2}\right)^2")
        self.play(Write(tex9))
        self.wait(6)
        self.play(
            Circumscribe(tex9[0], run_time=3)
        )
        self.wait(6)
        self.play(
            Circumscribe(tex9[2], run_time=3)
        )
        self.wait(6)
        v = Group()
        for i in self.mobjects:
            v.add(i)
        self.play(FadeOut(v))

        # completing the square example
        text1 = MathTex(r"2x^2+6x-20=0").shift(UP * 3.5).shift(LEFT * 2.5)
        text2 = MathTex(r"x^2+3x-10=0").next_to(text1, DOWN)
        text3 = MathTex(r"x^2+3x=10").next_to(text2, DOWN)
        text4 = MathTex(
            r"\left(x+\frac{3}{2}\right)^2-\left(\frac{3}{2}\right)^2=10").next_to(text3, DOWN)
        text5 = MathTex(
            r"\left(x+\frac{3}{2}\right)^2=10+\left(\frac{3}{2}\right)^2").next_to(text4, DOWN)
        text6 = MathTex(
            r"\left(x+\frac{3}{2}\right)^2=10+\frac{9}{4}").next_to(text5, DOWN)
        text7 = MathTex(
            r"\left(x+\frac{3}{2}\right)^2=\frac{49}{4}").next_to(text1, RIGHT).shift(RIGHT * 1.5).shift(DOWN * 0.5)
        text8 = MathTex(
            r"x+\frac{3}{2}=\pm\sqrt{\frac{49}{4}}").next_to(text7, DOWN)
        text9 = MathTex(r"x+\frac{3}{2}=\pm\frac{7}{2}").next_to(text8, DOWN)
        text10 = MathTex(r"x=-\frac{3}{2}\pm\frac{7}{2}").next_to(text9, DOWN)
        text11 = MathTex(r"x=2,x=-5").next_to(text10, DOWN)
        t0 = text1.copy()
        self.play(Write(t0))
        texts2 = [text1, text2, text3, text4, text5,
                  text6, text7, text8, text9, text10, text11, ]
        self.wait(3)
        for i in range(len(texts2) - 1):
            self.play(Transform(texts2[i], texts2[i + 1]))
            self.wait(3)
        self.wait(3)

        self.play(FadeOut(text1, text2, text3, text4, text5,
                          text6, text7, text8, text9, text10, text11))

        # plugging it back
        te0 = MathTex(r"x=2").next_to(t0, DOWN).shift(LEFT * 1.25)
        te1 = MathTex(r"x=-5").next_to(te0, RIGHT).shift(RIGHT * 5.25)
        te2 = MathTex(
            r"&2x^2+6x-20\\&=2(2)^2+6(2)-20\\&=2(4)+12-20\\&=8+12-20\\&=0").next_to(te0, DOWN)
        te3 = MathTex(
            r"&2x^2+6x-20\\&=2(-5)^2+6(-5)-20\\&=2(25)-30-20\\&=50-30-20\\&=0").next_to(te1, DOWN)
        self.play(Write(te0), Write(te1))
        self.play(Write(te2), Write(te3), run_time=5)
        self.wait(3)
        v = Group()
        for i in self.mobjects:
            v.add(i)
        self.play(FadeOut(v))
        self.wait(2)

        # completing the square trick
        tex9 = MathTex(
            r"x^2+bx&=x^2+bx+\left(\frac{b}{2}\right)^2-\left(\frac{b}{2}\right)^2\\&=(", r"x",
            r"+\frac{b}{2})^2-\left(\frac{b}{2}\right)^2")
        self.play(Write(tex9))
        self.wait(7)
        v = Group()
        for i in self.mobjects:
            v.add(i)
        self.play(FadeOut(v))

        # completing the square derivation
        tex3 = MathTex(r"ax^2+bx+c=0").shift(UP * 2).shift(LEFT * 3)
        tex4 = MathTex(
            r"x^2+\frac{b}{a}x+\frac{c}{a}=0").next_to(tex3, DOWN).shift(DOWN * 0.5)
        tex5 = MathTex(
            r"x^2+\frac{b}{a}x+\left(\frac{b}{2a}\right)^2+\frac{c}{a}=\left(\frac{b}{2a}\right)^2").next_to(tex4,
                                                                                                             DOWN).shift(
            DOWN * 0.5)
        tex6 = MathTex(
            r"\left(x+\frac{b}{2a}\right)^2+\frac{c}{a}=\left(\frac{b}{2a}\right)^2").next_to(tex3, RIGHT).shift(
            RIGHT * 1.5)
        tex7 = MathTex(
            r"\left(x+\frac{b}{2a}\right)^2=\left(\frac{b}{2a}\right)^2-\frac{c}{a}").next_to(tex6, DOWN).shift(
            DOWN * 0.5)
        tex8 = MathTex(
            r"(x-h)^2=k"
        ).next_to(tex7, DOWN).shift(DOWN * 0.5)
        texts = [tex3, tex4, tex5, tex6, tex7, tex8]
        self.play(Write(tex3.copy()))
        for i in range(len(texts) - 1):
            self.play(Transform(texts[i], texts[i + 1]))
            self.wait(2)
        v = Group()
        for i in self.mobjects:
            v.add(i)
        self.play(FadeOut(v))
        self.wait(6)

        # quadratic formula
        tex1 = MathTex(r"x=\frac{-b\pm \sqrt{b^2-4ac}}{2a}")
        self.play(Write(tex1))
        line = Line([0, 0, 0], [-1, 2, 0])
        self.play(MoveAlongPath(tex1, line))
        self.wait(5)
        text1 = MathTex(r"2x^2+6x-20=0").next_to(tex1, DOWN)
        self.play(Write(text1))
        self.wait()
        tex2 = MathTex(
            r"x=&\frac{-6\pm \sqrt{6^2-4(2)(-20))}}{2(2)}\\x&=2,x=-5").next_to(text1, DOWN)
        self.play(Write(tex2), run_time=5)
        self.wait(3)

        self.play(
            *[FadeOut(x) for x in self.mobjects]
        )


# py -m manim quadratics.py part3 -pql
class part3(Scene):
    def construct(self):
        p = [
            MathTex(r'f(x)', '=', r'ax^2+bx+c'),
            MathTex(r'f(x)', '=', r'a(x-\alpha)(x-\beta)')
        ]
        self.play(
            Write(p[0])
        )
        self.wait(2)
        for i in range(len(p) - 1):
            self.play(
                ReplacementTransform(p[i], p[i + 1])
            )
            self.wait(2)
        self.wait()
        self.play(
            p[-1].animate.to_corner(UR)
        )
        self.wait()
        axes = Axes(
            x_range=[-10, 10, 1],
            y_range=[-60, 100, 10],
            x_length=10,
            axis_config={"color": GREEN},
            tips=False,
        )
        p1 = [1, 4, -3, 2, -2]
        a1 = [-1, -3, 1, -2, -5]
        b1 = [2, 4, 3, 5, 4]
        graphs1 = []
        texts1 = []
        arrows1 = []
        arrows2 = []
        dots1 = []
        dots2 = []
        for idx in range(len(a1)):
            i = a1[idx]
            pi = p1[idx]
            j = b1[idx]

            def f(x):
                return pi * (x - i) * (x - j)

            g = axes.get_graph(f, [-10, 10])
            graphs1.append(g)
            texts1.append(MathTex(
                f"f(x)={pi}(x-({i}))(x-({j}))").to_corner(UR))
            dot1 = Dot(axes.i2gp(i, g), color=YELLOW)
            dot2 = Dot(axes.i2gp(j, g), color=YELLOW)
            dots1.append(dot1)
            dots2.append(dot2)
            arrows1.append(MathTex(f'{i}', color=YELLOW).next_to(dot1, DOWN))
            arrows2.append(MathTex(f'{j}', color=YELLOW).next_to(dot2, DOWN))
        self.play(
            FadeIn(graphs1[0], axes, arrows1[0], arrows2[0], dots1[0], dots2[0]),
            ReplacementTransform(p[-1], texts1[0])
        )
        self.wait(2)
        for i in range(len(graphs1) - 1):
            self.play(
                Transform(graphs1[0], graphs1[i + 1]),
                Transform(texts1[0], texts1[i + 1]),
                Transform(arrows1[0], arrows1[i + 1]),
                Transform(arrows2[0], arrows2[i + 1]),
                Transform(dots1[0], dots1[i + 1]),
                Transform(dots2[0], dots2[i + 1]),
            )
            self.wait(2)
        self.play(
            FadeOut(graphs1[0], texts1[0], axes,
                    arrows1[0], arrows2[0], dots1[0], dots2[0])
        )
        tx = VGroup(*[
            MathTex(r"f(x)=a(x-\alpha)(x-\beta)"),
            MathTex(r"0=a(x-\alpha)(x-\beta)"),
            MathTex(r"\frac{0}{a}=(x-\alpha)(x-\beta)"),
            MathTex(r"0=(x-\alpha)(x-\beta)"),
            MathTex(r"0=x^2-\beta x-\alpha x+\alpha\beta"),
            MathTex(r"0=x^2-(\alpha+\beta) x+\alpha\beta"),
        ]).arrange(DOWN)
        txc = tx[0].copy()
        self.play(
            Write(txc)
        )
        self.wait(2)
        for i in range(len(tx) - 1):
            self.play(
                Transform(tx[i], tx[i + 1])
            )
            self.wait()
        self.wait()
        self.play(
            FadeOut(txc),
            FadeOut(tx[:-2])
        )
        self.play(
            tx[-2].animate.to_corner(UL)
        )
        self.wait()
        tx2 = VGroup(*[
            MathTex(r"f(x)=ax^2+bx+c"),
            MathTex(r"0=ax^2+bx+c"),
            MathTex(r"\frac{0}{a}=x^2+\frac{b}{a}x+\frac{c}{a}"),
            MathTex(r"0=x^2+\frac{b}{a}x+\frac{c}{a}")
        ]).arrange(DOWN)
        txc2 = tx2[0].copy()
        self.play(
            Write(txc2)
        )
        self.wait(2)
        for i in range(len(tx2) - 1):
            self.play(
                Transform(tx2[i], tx2[i + 1])
            )
            self.wait()
        self.wait()
        self.play(
            FadeOut(txc2),
            FadeOut(tx2[:-2])
        )
        self.play(
            tx2[-2].animate.to_corner(UR)
        )
        self.wait()
        tex6 = MathTex(
            r"\alpha +\beta &= -\frac{b}{a}", r"\\ \alpha\beta &=\frac{c}{a}")
        SOR = Tex(' SOR', color=YELLOW).next_to(tex6[0], RIGHT)
        POR = Tex(' POR', color=YELLOW).next_to(tex6[1], RIGHT).align_to(SOR, RIGHT)
        tex7 = VGroup(SOR, POR)
        self.play(Write(tex6), run_time=3)
        tex8 = Tex(r"$x^2-($SOR$)x+$POR$=0$").next_to(tex6, DOWN).shift(DOWN)
        self.wait(5)
        self.play(Write(tex7))
        self.wait()
        self.play(Write(tex8))
        self.wait(7)
        self.play(
            *[FadeOut(x) for x in self.mobjects]
        )
        tex9 = MathTex(r"x=3 ,x=7").shift(UP * 3.25)
        self.play(Write(tex9))
        self.wait(4)
        tex10 = Tex(r"SOR$= 7+3$, POR$ =7\cdot3$").shift(UP * 3.25)
        tex11 = Tex(r"SOR$= 10$, POR$ =21$").shift(UP * 3.25)
        self.play(Transform(tex9, tex10))
        self.wait(3)
        self.play(Transform(tex9, tex11))
        self.wait(2)
        tex115 = Tex(r"$x^2-($SOR$)x+$POR$=0$").next_to(tex10, DOWN)
        self.play(Write(tex115))
        self.wait(2)
        tex11 = MathTex(r"x^2-10x+21=0").next_to(tex10, DOWN)
        self.play(ReplacementTransform(tex115, tex11))
        self.wait(3)
        tex12 = MathTex(r"x=3").shift(UP).shift(LEFT * 3)
        tex13 = MathTex(r"x=7").shift(UP).shift(RIGHT * 3)
        tex14 = MathTex(
            r"&x^2-10x+21\\=&(3)^2-10(3)+21\\=&9-30+21\\=&0").next_to(tex12, DOWN)
        tex15 = MathTex(
            r"&x^2-10x+21\\=&(7)^2-10(7)+21\\=&49-70+21\\=&0").next_to(tex13, DOWN)
        self.play(Write(tex12), Write(tex13))
        self.wait(2)
        self.play(Write(tex14), Write(tex15))
        self.wait(3)
        self.play(
            *[FadeOut(x) for x in self.mobjects]
        )


# py -m manim quadratics.py Summary -pql
class Summary(Scene):
    def construct(self):
        text1 = Text("General form of Quadratic Functions:").shift(UP * 3)
        text2 = MathTex(r"f(x) = ax^2+bx+c").next_to(text1, DOWN)
        text3 = Text("Ways to Solve Quadratic Equations:").next_to(text2, DOWN)
        text4 = Text("1) Completing the Square").next_to(text3, DOWN)
        text5 = Text("2) Quadratic Formula").next_to(text4, DOWN).align_to(text4, LEFT)
        text6 = Text("Alternative form of Quadratic Equation:").next_to(
            text5, DOWN)
        text7 = Tex(r"$x ^ 2-($SOR$)x+$POR$=0$").next_to(text6, DOWN)
        self.play(Write(text1))
        self.wait(2)
        self.play(Write(text2))
        self.wait(2)
        self.play(Write(text3))
        self.wait(2)
        self.play(Write(text4), Write(text5))
        self.wait(2)
        self.play(Write(text6))
        self.wait(2)
        self.play(Write(text7))
        self.wait(2)
        self.play(
            *[FadeOut(x) for x in self.mobjects]
        )


class Credits(Scene):
    def construct(self):
        txt = VGroup(*[
            Text('Made by:'),
            Text('Chooi Je Qin'),
            Text('Adel Arif'),
            Text('Tan Chin Peng'),
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


class Entrance(Scene):
    def construct(self):
        kopi = SVGMobject("../img/kopi.svg").scale(1.5).shift(UP)
        title = Tex("Kopitiam Maths").scale(2)
        title.set_color("#e1dbca")
        entrance = VGroup(
            kopi, title
        )
        entrance.arrange(DOWN)
        self.play(
            Write(kopi)
        )
        self.play(
            Write(title)
        )
        self.wait(2)
        self.play(
            *[FadeOut(x) for x in self.mobjects]
        )


class Thumbnail(Scene):
    def construct(self):
        x_min = -10
        x_max = 20
        y_min = -5
        y_max = 15

        axes = Axes(
            x_range=[x_min, x_max, 1],
            y_range=[y_min, y_max, 1],
            x_length=.75*(x_max - x_min),
            y_length=.75*(y_max - y_min),
            axis_config={"color": GREEN},
            tips=False,
        ).shift(UP*2)

        def f1(x1):
            return 0.1*((x1-3)**2)-2

        g = axes.get_graph(f1, [-10, 20])
        title = Tex('Quadratics', color=BLUE).scale(2).to_edge(UP)
        fx = MathTex('f(x)=ax^2+bx+c').next_to(title, DOWN)

        r1 = Dot(axes.i2gp(-1.472, g), color=YELLOW)
        r2 = Dot(axes.i2gp(7.472, g), color=YELLOW)

        self.add(
            title,
            axes,
            g,
            r1,
            r2,
            fx
        )
