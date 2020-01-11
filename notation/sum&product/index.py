from manimlib.imports import *

class Intro(Scene):
    def construct(self):
        pragmathic = TextMobject("Pragmathic")
        pragmathic.scale(2)
        pragmathic.set_color_by_gradient(BLUE, PURPLE)

        intro_text = TextMobject("Two functions of range.")

        self.play(Write(pragmathic))
        self.wait()
        self.play(pragmathic.set_color_by_gradient, (GREEN, BLUE))
        self.wait(1)
        self.play(Transform(pragmathic, intro_text))

class Introduction(Scene):
    def construct(self):
        itext = TextMobject("Let's say you have a large sum:")
        self.play(Write(itext))
        self.wait()
        self.play(itext.shift, UP)

        large_sum = TexMobject(r"1+2+3+4+5+...+70").shift(DOWN)
        self.play(Write(large_sum))