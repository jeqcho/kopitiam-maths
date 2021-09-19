import fractions

from manim import *
import sympy


class All(Scene):

    def construct(self):
        square = Square(fill_color=BLUE_E)
        self.play(
            Create(square)
        )
        self.play(
            square.animate.set_opacity(1.0)
        )
        self.play(
            square.animate.shift(LEFT * 2)
        )
        w_brace = Tex(r'.', color=BLUE_E).move_to(square)
        h_brace = Tex(r'.', color=BLUE_E).move_to(square)
        h = Tex(r'.', color=BLUE_E).move_to(square)
        w = Tex(r'.', color=BLUE_E).move_to(square)
        eq = Tex(r'.', color=BLACK).shift(RIGHT * 2)
        c = Tex(r'.', color=BLUE_E).move_to(square)

        def area(side_val, side_exp, f=1):
            assert side_val > 0
            a_exp = str(side_val ** 2)
            side_val *= 0.5
            square2 = Square(fill_color=BLUE_E, fill_opacity=1.0, side_length=float(side_val)).move_to(square)
            w_brace2 = Brace(square2, LEFT)
            h_brace2 = Brace(square2, UP)
            w2 = MathTex(side_exp).next_to(w_brace2, LEFT)
            h2 = MathTex(side_exp).next_to(h_brace2, UP)
            c2 = MathTex(a_exp).move_to(square2).scale(float(side_val) * 0.5)
            _anims = [
                Transform(h, h2),
                Transform(w, w2),
                Transform(square, square2),
                Transform(w_brace, w_brace2),
                Transform(h_brace, h_brace2),
                Transform(c, c2)
            ]
            if f:
                eq2 = MathTex(side_exp + '^2=' + a_exp).shift(RIGHT * 2)
                _anims.append(Transform(eq, eq2))
            return _anims

        animations = [
            area(4, '4'),
            area(6, '6'),
            area(5, '5'),
            area(6, '(x+2)'),
            area(7, r'(x-\frac{5}{2})'),
            area(5, '(x-3)'),
        ]
        for animation in animations:
            self.play(
                *animation
            )
            self.wait(0.25)
        self.wait(0.5)
        eq3 = MathTex('x^2-6x+9=25').next_to(eq, DOWN)
        self.play(
            ReplacementTransform(eq.copy(), eq3)
        )
        self.wait(0.5)
        eq4 = MathTex('x^2-6x-16=0').next_to(eq3, DOWN)
        self.play(
            ReplacementTransform(eq3.copy(), eq4)
        )
        self.wait(2)
        eq5 = MathTex('(x-8)(x+2)=0').next_to(eq4, DOWN)
        self.play(
            ReplacementTransform(eq4.copy(), eq5)
        )
        self.wait()
        eqs = VGroup(eq, eq3, eq4, eq5)
        self.play(
            eqs.animate.shift(UP)
        )
        self.play(
            Swap(eq, eq5),
            Swap(eq3, eq4),
            FadeOut(eq3)
        )

        def show(r1, r2):
            x, p, q = sympy.symbols('x h k')

            factor_form = (x - r1) * (x - r2)
            general_form = factor_form.expand()
            res = sympy.solve((x + p) ** 2 - q - general_form, [p, q])[0]
            pv = res[0]
            qv = res[1]
            square_form = (x + pv)

            line3 = MathTex(sympy.latex(square_form ** 2) + '=' + sympy.latex(qv))
            line2 = MathTex(sympy.latex(general_form) + '=0')
            line1 = MathTex(sympy.latex(factor_form) + '=0')

            self.play(
                Transform(eq5, line1.move_to(eq5)),
                Transform(eq4, line2.next_to(line1, DOWN)),
                Transform(eq, line3.next_to(line2, DOWN)),
                *area(sympy.sqrt(qv), sympy.latex(square_form), 0)
            )
            # try:
            #     area(pv, sympy.latex(square_form))
            # except:
            #     print(line1, line2, line3)
            self.wait(0.5)

        roots = [
            (fractions.Fraction(-17, 2), 4),
            (3, -4),
            (-6, 7),
            (6, -7),
            (-4, -5),
        ]
        for root in roots:
            show(*root)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects if mob != eq4]
        )

        eqs_raw = [
            'x^2+9x+20=0',
            'x^2+9x+20=0',
            'x^2+9x=-20',
            r'x^2+9x+(\frac{9}{2})^2=-20+(\frac{9}{2})^2',
            r'(x+\frac{9}{2})^2=\frac{1}{4}',
        ]
        eqs = [MathTex(s).scale(0.7) for s in eqs_raw]

        eqs2_raw = [
            r'ax^2+bx+c=0',
            r'x^2+\frac{b}{a}x+\frac{c}{a}=0',
            r'x^2+\frac{b}{a}x=-\frac{c}{a}',
            r'x^2+\frac{b}{a}x+(\frac{b}{2a})^2=-\frac{c}{a}+(\frac{b}{2a})^2',
            r'(x+\frac{b}{2a})^2=\frac{b^2-4ac}{4a^2}',

            r'x+\frac{b}{2a}=\frac{\pm\sqrt{b^2-4ac}}{2a}',
            r'x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}',
        ]
        eqs2 = [MathTex(s).scale(0.7) for s in eqs2_raw]

        VGroup(*eqs2).arrange(DOWN)
        for j in range(len(eqs)):
            eqs[j].move_to(eqs2[j])
        self.play(
            ReplacementTransform(eq4, eqs[1]),
        )
        for j in range(1, len(eqs) - 1):
            self.play(
                ReplacementTransform(eqs[j].copy(), eqs[j + 1])
            )
            self.wait(0.5)
        self.wait()
        self.play(
            Circumscribe(eqs[-1])
        )
        self.wait()

        self.play(
            Write(eqs2[0])
        )
        self.play(
            Indicate(eqs2[0])
        )
        self.wait(0.5)

        for j in range(1, len(eqs2) - 2):
            self.play(
                ReplacementTransform(eqs[j], eqs2[j].move_to(eqs[j]))
            )
            self.wait(0.5)

        self.play(
            ShowPassingFlash(Underline((eqs[4])))
        )
        self.wait()
        for j in range(len(eqs2) - 3, len(eqs2) - 1):
            self.play(
                ReplacementTransform(eqs2[j].copy(), eqs2[j + 1])
            )
            self.wait(0.75)
        self.wait()
        quad = eqs2[-1]
        self.play(
            *[FadeOut(mob) for mob in self.mobjects if mob != quad],
        )

        self.play(
            quad.animate.move_to(Square()).scale(1 / 0.7 * 2)
        )
        self.wait()
        self.play(
            Circumscribe(quad)
        )
        self.wait()

        square = Square(fill_color=BLUE_E, fill_opacity=1.0)
        w_brace = Brace(square, LEFT)
        h_brace = Brace(square, UP)
        side_exp = r'x+\frac{b}{2a}'
        w2 = MathTex(side_exp).next_to(w_brace, LEFT)
        h2 = MathTex(side_exp).next_to(h_brace, UP)
        a_exp = r'\frac{b^2-4ac}{4a^2}'
        c2 = MathTex(a_exp).move_to(square)

        conclusion = VGroup(
            square,
            w_brace,
            h_brace,
            w2,
            h2,
            c2
        )

        self.play(
            ReplacementTransform(quad, conclusion)
        )
        self.wait(2)
