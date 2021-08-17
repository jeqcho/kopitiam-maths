from manim import *
from manim.mobject.geometry import ArrowTriangleFilledTip


class Intro(Scene):
    def construct(self):
        who = Tex("Who is your mother?")
        name = MathTex(r"\rightarrow \text{A unique human}")
        txt = VGroup(who, name).arrange(RIGHT)
        self.play(
            Write(who)
        )
        self.wait()
        self.play(
            Write(name)
        )
        self.wait()
        func = Text("Function")
        self.play(
            ReplacementTransform(txt, func)
        )
        self.wait(2)
        ex_func = MathTex(r"\text{mother} : \text{A} \rightarrow \text{B}").scale(0.5).next_to(func, DOWN)
        self.play(
            Write(ex_func)
        )
        self.wait(2)
        mother = Text("Fatiha")
        aiman = Text("Aiman")
        faizal = Text("Faizal")
        mother_sons = VGroup(mother, aiman, faizal).arrange(DOWN)
        self.play(
            ReplacementTransform(VGroup(func, ex_func), mother_sons)
        )
        self.wait(3)
        dis = MathTex(r"\text{mother} : \text{Aiman} \rightarrow \text{Fatiha}").move_to(aiman.get_center())
        self.play(
            ReplacementTransform(aiman, dis)
        )
        self.wait(3)
        dis = MathTex(r"\text{mother} : \text{Faizal} \rightarrow \text{Fatiha}").move_to(faizal.get_center())
        self.play(
            ReplacementTransform(faizal, dis)
        )
        self.wait(3)
        son_function = MathTex(r"\text{son} : \text{Fatiha} \rightarrow")
        to_aiman = MathTex(r"\text{Aiman}").next_to(son_function, RIGHT)
        son_function_full = VGroup(son_function, to_aiman.copy()).move_to(mother.get_center())
        to_aiman = MathTex(r"\text{Aiman}").next_to(son_function, RIGHT)
        to_faizal = MathTex(r"\text{Faizal}").next_to(son_function, RIGHT)
        self.play(
            ReplacementTransform(mother, son_function_full)
        )
        self.wait(2)
        self.play(
            Transform(son_function_full[1], to_faizal.copy())
        )
        self.play(
            Transform(son_function_full[1], to_aiman.copy())
        )
        self.play(
            Transform(son_function_full[1], to_faizal.copy())
        )
        self.play(
            Transform(son_function_full[1], to_aiman.copy())
        )
        self.play(
            Transform(son_function_full[1], to_faizal.copy())
        )
        self.play(
            Transform(son_function_full[1], to_aiman.copy())
        )
        self.wait()
        self.play(
            *[FadeOut(x) for x in self.mobjects]
        )
        self.wait()


class Terminology(Scene):
    def construct(self):
        self.wait()
        tapir = SVGMobject('img/tapir.svg')
        four = MathTex(r'4')
        element_group = VGroup(four, tapir)
        element_group.arrange(buff=2)
        element = Title("Elements")
        self.play(
            Write(element)
        )
        self.wait()
        dis = Tex("A thing").next_to(element, DOWN)
        self.play(
            Write(dis)
        )
        self.wait()
        self.play(
            Write(four)
        )
        self.wait()
        self.play(
            FadeIn(tapir)
        )
        self.wait(2)
        self.play(
            FadeOut(element_group),
            FadeOut(element),
            FadeOut(dis)
        )

        relation = Title("Relation")
        self.play(
            Write(relation)
        )
        self.wait()
        dis = Tex("A connection").next_to(relation, DOWN)
        self.play(
            Write(dis)
        )
        self.wait()
        arrow_1 = Arrow(start=ORIGIN + LEFT * 3, end=ORIGIN + RIGHT * 3).add_tip(tip_shape=ArrowTriangleFilledTip,
                                                                                 at_start=True)

        three = MathTex(r'3').next_to(ORIGIN + LEFT * 3, LEFT)
        seven = MathTex(r'7').next_to(ORIGIN + RIGHT * 3, RIGHT)

        both_odd = Tex(r'odd numbers').next_to(ORIGIN, UP)

        number_relation = VGroup(three, seven, arrow_1, both_odd)
        self.play(
            Create(number_relation)
        )
        self.wait()
        self.play(
            FadeOut(number_relation)
        )
        self.wait()

        you = Tex("You").next_to(ORIGIN + LEFT * 3, LEFT)
        mom = Tex("Your mom").next_to(ORIGIN + RIGHT * 3, RIGHT)
        child_of = Tex('family').next_to(ORIGIN, UP)

        child_relation = VGroup(you, mom, arrow_1, child_of)
        self.play(
            Create(child_relation)
        )
        self.wait()
        self.play(
            FadeOut(child_relation)
        )
        self.wait()

        banana = SVGMobject("img/banana.svg")
        yellow = Tex("Yellow", color=YELLOW)
        Group(banana, yellow).arrange(buff=3)
        arrow_1 = Arrow(start=banana.get_right(), end=yellow.get_left())
        colour_of = Tex('colour of').next_to(arrow_1, UP)

        colour_relation = VGroup(yellow, arrow_1, colour_of)
        self.play(
            Write(banana),
            Create(colour_relation)
        )
        self.wait(3)
        self.play(
            FadeOut(banana),
            FadeOut(colour_relation)
        )
        self.wait()
        self.play(
            FadeOut(relation),
            FadeOut(dis)
        )
        self.wait()

        function_title = Title('Function')
        self.play(
            Write(function_title)
        )
        self.wait()
        dis = Text("A special relation where an element is mapped to exactly one element").scale(0.7).next_to(
            function_title, DOWN)
        self.play(
            Write(dis),
            run_time=4
        )
        self.wait(6)
        condition_1 = Text("Each input cannot have no corresponding output").scale(0.6)
        condition_2 = Text("Each input cannot have more than one output").scale(0.6)
        conditions = VGroup(condition_1, condition_2).arrange(DOWN)
        self.play(
            Write(condition_1)
        )
        self.wait(2)
        self.play(
            Write(condition_2)
        )
        self.wait(2)
        condition = Text("Each input must have exactly one output").scale(0.6)
        self.play(
            ReplacementTransform(conditions, condition)
        )
        self.wait(4)
        self.play(
            FadeOut(dis),
            FadeOut(condition)
        )
        X = Ellipse(2, 5, color=WHITE)
        Y = Ellipse(2, 5, color=WHITE)
        VGroup(X, Y).arrange(buff=3)
        set_x = VGroup(*[MathTex(x) for x in 'abcd'])
        set_x.arrange(DOWN, buff=1).move_to(X)
        set_y = VGroup(*[MathTex(x) for x in 'pqrs'])
        set_y.arrange(DOWN, buff=1).move_to(Y)
        self.play(
            Create(X),
            Create(Y),
            Create(set_x),
            Create(set_y),
        )

        arrows = VGroup()
        for i in range(3):
            arrow = Arrow(start=set_x[i].get_center(), end=set_y[i].get_center())
            self.play(
                Create(arrow)
            )
            arrows += arrow

        self.wait(2)

        arrow = Arrow(start=set_x[3].get_center(), end=set_y[2].get_center())
        valid = Text("Still a function", color=GREEN).to_edge(DOWN)
        self.play(
            Create(arrow),
            Write(valid)
        )
        self.wait(2)
        self.play(
            Uncreate(arrow),
            FadeOut(valid)
        )
        self.wait()

        invalid = Text("NOT a function", color=RED).to_edge(DOWN)
        arrow = Arrow(start=set_x[2].get_center(), end=set_y[3].get_center())
        self.play(
            Create(arrow),
            Write(invalid)
        )
        self.wait()
        self.play(
            Uncreate(arrow),
            FadeOut(invalid)
        )
        self.wait()

        self.play(
            FadeOut(function_title),
            FadeOut(set_x[3])
        )
        self.wait()

        objects = Text("Objects").next_to(X, DOWN)
        self.play(
            Write(objects),
            Indicate(set_x[0])
        )
        self.play(
            Indicate(set_x[1])
        )
        self.play(
            Indicate(set_x[2])
        )
        self.wait()
        self.play(
            FadeOut(objects)
        )
        self.wait()

        images = Text("Images").next_to(Y, DOWN)
        self.play(
            Write(images),
            Indicate(set_y[0])
        )
        self.play(
            Indicate(set_y[1])
        )
        self.play(
            Indicate(set_y[2])
        )
        self.wait()
        self.play(
            FadeOut(images)
        )
        self.wait()

        domain = Text("Domain").next_to(X, DOWN)
        x_title = MathTex('X').next_to(X, UP)
        self.play(
            Write(domain),
            Write(x_title)
        )
        self.wait()
        self.play(
            Indicate(X)
        )
        self.wait()
        self.play(
            FadeOut(domain)
        )
        self.wait()

        codomain = Text("Codomain").next_to(Y, DOWN)
        y_title = MathTex('Y').next_to(Y, UP)
        self.play(
            Write(codomain),
            Write(y_title)
        )
        self.wait()
        self.play(
            Indicate(Y)
        )
        self.wait()
        self.play(
            FadeOut(codomain)
        )
        self.wait()

        range_brace = Brace(Line(set_y[0].get_top(), set_y[2].get_bottom()), direction=RIGHT).shift(RIGHT)
        range_title = Text("Range").next_to(range_brace, RIGHT)
        self.play(
            Write(range_brace),
            Write(range_title)
        )
        self.wait(5)
        self.play(
            FadeOut(range_brace),
            FadeOut(range_title)
        )
        self.wait()

        f_note = MathTex(r"y=f(x)")
        a_note = MathTex(r"f:X \rightarrow Y")
        notations = VGroup(f_note, a_note)
        notations.arrange(DOWN).to_edge(UP)
        self.play(
            Write(f_note)
        )
        self.wait(3)
        self.play(
            Write(a_note)
        )
        self.wait(3)

        self.play(
            FadeOut(arrows),
            FadeOut(set_x[0:3]),
            FadeOut(set_y),
            FadeOut(X),
            FadeOut(Y),
            FadeOut(x_title),
            FadeOut(y_title),
            FadeOut(notations)
        )
        self.wait()


class Analogy(Scene):
    def construct(self):
        self.wait()
        mfm_title = VGroup(*[Text(x) for x in ['Magical', 'Fruit', 'Machine']]).arrange(DOWN)
        mfm_title[0].set_color(PINK).set_sheen(-0.1, DR)
        mfm_title[1].set_color(PURPLE).set_sheen(-0.1, DR)
        mfm_title[2].set_color(TEAL).set_sheen(-0.1, DR)
        mfm_box = Rectangle(width=mfm_title.width * 1.1, height=mfm_title.height * 1.1).set_fill(BLACK).set_opacity(100)
        mfm = VGroup(mfm_box, mfm_title)
        self.bring_to_front(mfm)
        self.play(
            Create(mfm),
            run_time=2
        )
        self.wait(2)
        orange = SVGMobject('img/orange.svg').to_edge(LEFT).shift(RIGHT)
        orange_juice = SVGMobject('img/orange_juice.svg').to_edge(RIGHT).shift(LEFT)
        self.play(
            Write(orange)
        )
        self.wait()
        self.bring_to_front(mfm)
        self.play(
            ReplacementTransform(orange, orange_juice)
        )
        self.wait()
        self.play(
            FadeOut(orange_juice)
        )

        melon = SVGMobject('img/melon.svg').scale(0.7).to_edge(LEFT).shift(RIGHT)
        melon_juice = SVGMobject('img/melon_juice.svg').to_edge(RIGHT).shift(LEFT)
        self.play(
            Write(melon)
        )
        self.bring_to_front(mfm)
        self.play(
            ReplacementTransform(melon, melon_juice)
        )
        self.wait()
        self.play(
            FadeOut(melon_juice)
        )
        self.wait()

        blender = SVGMobject('img/blender.svg').scale(1.2)
        self.play(
            ReplacementTransform(mfm, blender)
        )
        self.wait(3)
        function_title = Text("Function").next_to(blender, DOWN)
        self.play(
            Write(function_title)
        )
        self.wait(2)

        orange = SVGMobject('img/orange.svg').to_edge(LEFT).shift(RIGHT)
        self.play(
            Write(orange)
        )
        self.wait()
        objects = Text("Object").next_to(orange, DOWN)
        self.play(
            Write(objects)
        )
        self.wait()

        orange_juice = SVGMobject('img/orange_juice.svg').to_edge(RIGHT).shift(LEFT)
        self.play(
            Write(orange_juice)
        )
        self.wait()
        images = Text("Image").next_to(orange_juice, DOWN)
        self.play(
            Write(images)
        )
        self.wait()
        self.play(
            FadeOut(objects),
            FadeOut(images),
            FadeOut(function_title)
        )
        self.wait()

        melon = SVGMobject('img/melon.svg').scale(0.7)
        fruits = VGroup(orange.copy(), melon).arrange(DOWN).to_edge(LEFT).shift(RIGHT)
        melon_juice = SVGMobject('img/melon_juice.svg')
        juices = VGroup(orange_juice.copy(), melon_juice).arrange(DOWN).to_edge(RIGHT).shift(LEFT)

        self.play(
            orange.animate.move_to(fruits[0])
        )
        self.wait()
        self.play(
            Write(melon)
        )
        self.wait()
        domain = Text("Domain").next_to(fruits, DOWN)
        set_fruit = SurroundingRectangle(fruits)
        self.play(
            Create(set_fruit),
            Write(domain)
        )
        self.wait()

        self.play(
            orange_juice.animate.move_to(juices[0])
        )
        self.wait()
        self.play(
            Write(melon_juice)
        )
        self.wait()
        range_title = Text("Range").next_to(juices, DOWN)
        set_juices = SurroundingRectangle(juices)
        self.play(
            Create(set_juices),
            Write(range_title)
        )
        self.wait()

        self.play(
            Uncreate(set_fruit),
            FadeOut(domain),
            Uncreate(set_juices),
            FadeOut(range_title)
        )
        self.wait()

        coconut = SVGMobject('img/coconut.svg').scale(1.2)
        coconut_juice = SVGMobject('img/coconut_juice.svg')
        ordered_fruits = fruits.copy()
        ordered_fruits += coconut
        ordered_fruits.arrange(DOWN).to_edge(LEFT).shift(RIGHT)
        ordered_juices = juices.copy()
        ordered_juices += coconut_juice
        ordered_juices.arrange(DOWN).to_edge(RIGHT).shift(LEFT)
        self.play(
            orange.animate.move_to(ordered_fruits[0]),
            melon.animate.move_to(ordered_fruits[1]),
            orange_juice.animate.move_to(ordered_juices[0]),
            melon_juice.animate.move_to(ordered_juices[1])
        )
        self.wait()
        self.play(
            Write(coconut),
            Write(coconut_juice)
        )
        self.wait()
        arrow = Arrow(start=coconut.get_right(), end=coconut_juice.get_left())
        slash = Cross(arrow.copy().scale(0.1))
        self.play(
            Create(arrow),
            Create(slash)
        )
        self.wait()

        codomain = Text('Codomain').next_to(ordered_juices, DOWN)
        set_codomain = SurroundingRectangle(ordered_juices)
        self.play(
            Write(codomain),
            Create(set_codomain)
        )
        self.wait(4)
        self.play(
            FadeOut(codomain),
            Uncreate(set_codomain)
        )
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        self.wait()


class DiscreteVSContinuous(Scene):
    def construct(self):
        self.wait(2)
        linear = MathTex(r"f(x)=mx+c")
        self.play(
            Write(linear)
        )
        self.wait(2)
        binomial = MathTex(r"P(X=r)=\binom{n}{r}p^r q^{n-r}")
        self.play(
            Transform(linear, binomial)
        )
        self.wait(2)
        self.play(
            FadeOut(linear)
        )

        func = Text("Function")
        self.play(
            Write(func)
        )
        self.wait()
        txt = VGroup(Text("Discrete"), Text("Continuous")).arrange(RIGHT, buff=2)
        self.play(
            Transform(func, txt)
        )
        self.wait()
        self.play(
            FadeOut(func)
        )

        continuous_title = Title("Continuous Functions")
        self.play(
            Write(continuous_title)
        )
        self.wait()
        number_line = NumberLine().to_edge(DOWN)
        tracker = ValueTracker(0)

        pointer = Vector(DOWN).next_to(number_line.n2p(0), UP)
        pointer.add_updater(
            lambda m: m.next_to(
                number_line.n2p(tracker.get_value()),
                UP
            )
        )

        def upd():
            return MathTex('{0:.1f}'.format(tracker.get_value())).next_to(pointer, UP)

        label = always_redraw(upd)

        self.play(
            Create(number_line),
            Create(pointer),
            Write(label)
        )

        self.play(tracker.animate.set_value(5))
        self.play(tracker.animate.set_value(-3))
        self.play(tracker.animate.increment_value(+2))
        self.wait(0.5)

        fx = MathTex(r"f(x)", r" = 2", r"x+1").shift(UP)
        self.play(
            Write(fx)
        )
        self.wait()
        result = MathTex(r"=", "5").next_to(fx, DOWN).align_to(fx[1], LEFT)
        self.play(
            Transform(fx[0], MathTex(r"f(2)").move_to(fx[0].get_center()).align_to(fx[0], RIGHT)),
            Transform(fx[2], MathTex(r"(2)+1").move_to(fx[2].get_center()).align_to(fx[2], LEFT)),
            tracker.animate.set_value(2),
            Write(result)
        )
        self.wait()
        self.play(
            Transform(fx[0], MathTex(r"f(1)").move_to(fx[0].get_center()).align_to(fx[0], RIGHT)),
            Transform(fx[2], MathTex(r"(1)+1").move_to(fx[2].get_center()).align_to(fx[2], LEFT)),
            tracker.animate.set_value(1),
            Transform(result[1], MathTex(r"3").move_to(result[1].get_center()).align_to(result[1], LEFT))
        )
        self.wait()
        self.play(
            Transform(fx[0], MathTex(r"f(1.5)").move_to(fx[0].get_center()).align_to(fx[0], RIGHT)),
            Transform(fx[2], MathTex(r"(1.5)+1").move_to(fx[2].get_center()).align_to(fx[2], LEFT)),
            tracker.animate.set_value(1.5),
            Transform(result[1], MathTex(r"4").move_to(result[1].get_center()).align_to(result[1], LEFT))
        )
        self.wait()
        self.play(
            FadeOut(continuous_title),
            FadeOut(fx),
            FadeOut(result),
            FadeOut(number_line),
            FadeOut(pointer),
            FadeOut(label)
        )
        self.wait()
        discrete_title = Title("Discrete Functions")
        self.play(
            Write(discrete_title)
        )
        blender = SVGMobject('img/blender.svg').shift(UP)
        orange = SVGMobject('img/orange.svg').shift(DOWN)
        melon = SVGMobject('img/melon.svg').scale(0.7).shift(DOWN)
        oron = orange.copy()
        orange.to_edge(LEFT, buff=1)
        melon.to_edge(RIGHT, buff=1)
        self.play(
            Write(blender)
        )
        self.wait(2)
        self.play(
            Write(orange),
            Write(melon)
        )
        self.wait()
        self.play(
            ReplacementTransform(melon.copy(), oron)
        )
        self.play(
            Transform(oron, melon.copy().move_to(oron.get_center()))
        )
        self.play(
            Transform(oron, orange.copy().move_to(oron.get_center()))
        )
        self.play(
            Transform(oron, melon.copy().move_to(oron.get_center()))
        )
        self.play(
            FadeOut(blender),
            FadeOut(oron),
            FadeOut(orange),
            FadeOut(melon),
        )
        des = MathTex(r"\text{Let }f(x)\text{ be the number of ways to arrange }x\text{ people in a line}") \
            .next_to(discrete_title, DOWN)
        dis = MathTex(r"f(x)=x!").to_edge(DL)
        self.play(
            Write(des),
            FadeIn(dis)
        )
        self.wait()
        fx = MathTex(r"f(4)", r"=", r"24")
        self.play(
            Write(fx)
        )
        self.wait(2)
        nfx = MathTex(r"f(7.5)", r"???")
        self.play(
            Transform(fx[0], nfx[0].move_to(fx[0].get_center()).align_to(fx[0], RIGHT)),
            Transform(fx[2], nfx[1].move_to(fx[2].get_center()).align_to(fx[2], LEFT))
        )
        self.wait(3)
        nfx = MathTex(r"f(???)", r"2.3")
        self.play(
            Transform(fx[0], nfx[0].move_to(fx[0].get_center()).align_to(fx[0], RIGHT)),
            Transform(fx[2], nfx[1].move_to(fx[2].get_center()).align_to(fx[2], LEFT))
        )
        self.wait(2)
        self.play(
            *[FadeOut(x) for x in self.mobjects]
        )
        self.wait()


class Mapping(Scene):
    def construct(self):
        self.wait()
        function_title = MathTex("f(x)=2x+1")
        self.play(
            Write(function_title)
        )
        self.play(
            function_title.animate.to_edge(UP)
        )
        x_min = 0
        x_max = 6
        axes = Axes(x_range=[x_min, x_max, 1],
                    y_range=[0, 11, 1],
                    axis_config={"include_numbers": True}
                    )
        x = ValueTracker(0)

        def f(x1):
            return 2 * x1 + 1

        g = axes.get_graph(f, [x_min, x_max])

        mx_obj = 0
        mx_img = 0

        def eq_text():
            return MathTex('{0:.1f}'.format(f(x.get_value())), r"=",
                           "2(" + '{0:.2f}'.format(x.get_value()) + ")+1").to_corner(UR)

        def trace_dot():
            nonlocal mx_obj, mx_img
            mx_obj = max(mx_obj, x.get_value())
            mx_img = max(mx_img, f(x.get_value()))
            return axes.get_line_graph([0, mx_obj], [f(0), mx_img], add_vertex_dots=False)

        def trace_x():
            return axes.get_T_label(x.get_value(), g, label=Tex('{0:.2f}'.format(x.get_value())))

        def trace_y():
            pointy = axes.coords_to_point(0, f(x.get_value()))
            label_y = Tex('{0:.1f}'.format(f(x.get_value()))).next_to(pointy, UR)
            return VGroup(label_y, axes.get_horizontal_line(axes.coords_to_point(x.get_value(), f(x.get_value()))))

        eq_line = always_redraw(trace_dot)
        object_line = always_redraw(trace_x)
        image_line = always_redraw(trace_y)
        eq = always_redraw(eq_text)

        obj = Tex("Object").to_corner(DR)
        img = Tex("Image").move_to(axes.get_axes()[1].get_center()).to_edge(UP, buff=0.2)

        self.play(
            Create(axes),
            Write(obj),
            Write(img)
        )

        self.play(
            Write(eq),
            Create(eq_line),
            Create(object_line),
            Create(image_line),
            run_time=3
        )

        self.play(
            x.animate.set_value(4.5),
            run_time=7
        )
        self.wait(3)
        self.play(
            x.animate.set_value(1),
            run_time=2
        )
        self.play(
            x.animate.set_value(3),
            run_time=2
        )
        self.play(
            x.animate.set_value(2)
        )
        self.wait(2)
        self.play(
            x.animate.set_value(3.5)
        )
        self.wait(2)
        self.play(
            *[FadeOut(x) for x in self.mobjects]
        )


class VerticalLineTest(Scene):
    def construct(self):
        plane = Axes()
        top = plane.get_graph(lambda x: 3.5)
        bottom = plane.get_graph(lambda x: -3.5)
        title = Text("Vertical Line Test").scale(1.5)
        self.play(
            Write(title)
        )
        self.wait()
        self.play(
            title.animate.scale(1 / 1.5).to_corner(UL)
        )
        self.play(
            Create(plane)
        )
        self.wait()
        a = 1 / 3
        c = -2

        def f(x):
            return a * x ** 2 + c

        equation = MathTex(r"y=\frac{1}{3}x^2-2").to_corner(UR)
        graph = plane.get_graph(f, [-4, 4]).set_color(GREEN)

        self.play(
            Write(equation)
        )
        self.wait()

        self.play(
            Create(graph)
        )
        self.wait()

        vl1 = plane.get_vertical_lines_to_graph(top, [-4, 4], 5, line_func=Line, color=YELLOW, stroke_width=3)
        vl2 = plane.get_vertical_lines_to_graph(bottom, [-4, 4], 5, line_func=Line, color=YELLOW,
                                                stroke_width=3)
        self.play(
            Create(vl1),
            Create(vl2)
        )
        self.wait(4)

        ok = Text("It's a function!", color=GREEN).to_corner(DR)
        self.play(
            Write(ok)
        )
        self.wait(2)

        self.play(
            Uncreate(graph),
            Uncreate(equation),
            Uncreate(vl1),
            Uncreate(vl2),
            FadeOut(ok)
        )
        self.wait()

        a = 4
        b = 2
        equation = MathTex(r"\frac{x^2}{16}+\frac{y^2}{4}=1").to_corner(UR)

        def f(x):
            return b * (1 - (x / a) ** 2) ** 0.5

        def f2(x):
            return -b * (1 - (x / a) ** 2) ** 0.5

        graph = plane.get_graph(f, [-a, a]).set_color(RED)
        graph2 = plane.get_graph(f2, [-a, a]).set_color(RED)
        self.play(
            Write(equation)
        )
        self.wait()
        self.play(
            Create(graph),
            Create(graph2)
        )
        self.wait(2)

        vl1 = plane.get_vertical_lines_to_graph(top, [-5, 5], 5, line_func=Line, color=YELLOW, stroke_width=3)
        vl2 = plane.get_vertical_lines_to_graph(bottom, [-5, 5], 5, line_func=Line, color=YELLOW,
                                                stroke_width=3)
        self.play(
            Create(vl1),
            Create(vl2)
        )
        self.wait(3)
        arrow1 = Arrow(end=plane.coords_to_point(0, 2))
        arrow2 = Arrow(end=plane.coords_to_point(0, -2))
        self.play(
            Create(arrow1),
            Create(arrow2)
        )
        self.wait(4)
        nope = Text("NOT a function!", color=RED).to_corner(DR)
        self.play(
            Write(nope)
        )
        self.wait(5)

        self.play(
            *[FadeOut(x) for x in self.mobjects]
        )


class Outro(Scene):
    def construct(self):
        title = Title("The Golden Rule of Functions")
        self.play(
            Write(title)
        )
        self.wait()
        rule = Tex("Each object maps to exactly one image").set_color(GOLD).next_to(title, DOWN)
        self.play(
            Write(rule)
        )
        self.wait(2)
        ex_title = VGroup()
        ex_func = VGroup()
        ex_title += Tex("Wavefunction of a free particle, ")
        ex_func += MathTex(r"\Psi(x,t)=Ae^{i(kx-\omega t)}")
        ex_title += Tex("Euler's totient function, ")
        ex_func += MathTex(r"\varphi(n) =n \prod_{p\mid n} \left(1-\frac{1}{p}\right)")
        ex_title += Tex("Riemann zeta function, ")
        ex_func += MathTex(r"\zeta(s) = \frac{1}{\Gamma(s)} \int_0^\infty \frac{x ^ {s-1}}{e ^ x - 1} dx\,")
        txt = VGroup()
        for x in range(3):
            txt += VGroup(ex_title[x], ex_func[x]).arrange(RIGHT)

        txt.arrange(DOWN)
        for x in range(3):
            self.play(
                Write(txt[x])
            )
            self.wait()
        self.wait(2)
        self.play(
            *[FadeOut(x) for x in self.mobjects]
        )
        self.wait()


class Ending(Scene):
    def construct(self):
        kopi = SVGMobject("img/kopi.svg")
        self.play(
            Write(kopi),
            run_time=2
        )
        kopi_2 = SVGMobject("img/kopi.svg")
        title = Tex("Kopi", "tiam Maths").scale(2)
        # title[0].set_color("#905e2e")
        title[0].set_color("#e1dbca")
        title[1].set_color("#e1dbca")
        closing = VGroup(
            kopi_2, title
        )
        closing.arrange()
        title.align_to(kopi, DOWN)
        self.play(
            Transform(kopi, kopi_2)
        )
        self.play(
            Write(title)
        )
        self.wait(8)


class Thumbnail(Scene):
    def construct(self):
        function_title = Tex('Functions').scale(2).to_edge(UP)
        self.play(
            Write(function_title)
        )
        self.wait(2)
        X = Ellipse(2, 5, color=WHITE)
        Y = Ellipse(2, 5, color=WHITE)
        VGroup(X, Y).arrange(buff=3)
        set_x = VGroup(*[MathTex(x) for x in 'abcd'])
        set_x.arrange(DOWN, buff=1).move_to(X)
        set_y = VGroup(*[MathTex(x) for x in 'pqrs'])
        set_y.arrange(DOWN, buff=1).move_to(Y)
        self.play(
            Create(X),
            Create(Y),
            Create(set_x),
            Create(set_y),
        )
        arrows = VGroup()
        for i in range(3):
            arrow = Arrow(start=set_x[i].get_center(), end=set_y[i].get_center())
            self.play(
                Create(arrow)
            )
            arrows += arrow
