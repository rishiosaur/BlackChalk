from manimlib.imports import *

class Intro(Scene):
    def construct(self):

        boring = TextMobject("School", "math is boring.").set_color_by_tex_to_color_map({"School": RED})
        math = TextMobject("Math", "math is hella fun.").set_color_by_tex_to_color_map({"Math": BLUE})
        welcome = TextMobject("Welcome to ", "Pragmathic.").set_color_by_tex_to_color_map({"Pragmathic": BLUE})
        # pragmathic = TextMobject("Pragmathic.").next_to(welcome, RIGHT).set_color_by_gradient(BLUE, GREEN)
        eq1 = TexMobject(r"y(x_{0})=y_{0},y'(x_{0})=y'_{0},y''(x_{0})=y''_{0},\cdots ").next_to(welcome, UP, buff=2)
        eq2 = TexMobject(r"f_{n}(x){\frac {\mathrm {d} ^{n}y}{\mathrm {d} x^{n}}}+\cdots +f_{1}(x){\frac {\mathrm {d} y}{\mathrm {d} x}}+f_{0}(x)y=g(x)").shift(DOWN*1.5)
        eq3 = TexMobject(r"\operatorname {li}(x)=\int _{0}^{x}{\frac  {dt}{\log(t)}}.").shift(RIGHT*2)

        self.play(Write(boring))
        self.wait()
        self.play(Transform(boring, math))
        self.wait()
        self.play(FadeOut(boring))
        self.play(Write(welcome))
        # self.play(Write(eq1),Write(eq2),Write(eq3))
