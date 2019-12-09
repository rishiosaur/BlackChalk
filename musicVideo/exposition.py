from manimlib.imports import *

class Intro(Scene):
    def construct(self):
        pragmathic = TextMobject("Pragmathic")
        pragmathic.scale(2)
        pragmathic.set_color_by_gradient(BLUE, PURPLE)

        intro_text = TextMobject("The music of thought.")

        self.play(Write(pragmathic))
        self.wait()
        self.play(pragmathic.set_color_by_gradient, (GREEN, BLUE))
        self.wait(1)
        self.play(Transform(pragmathic, intro_text))


class Thing(Scene):
    def construct(self):
        pragmathic = TextMobject("Pragmathic")
        pragmathic.scale(2)
        pragmathic.set_color_by_gradient(BLUE, PURPLE)

        intro_text = TexMobject("(a^2-b^2) < (a^2)")

        self.play(Write(pragmathic))
        self.wait()
        self.play(pragmathic.set_color_by_gradient, (GREEN, BLUE))
        self.wait(1)
        self.play(Transform(pragmathic, intro_text))