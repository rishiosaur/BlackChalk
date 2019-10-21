from manimlib.imports import *


class Intro(Scene):
    def construct(self):
        pragmathic = TextMobject("Pragmathic")
        pragmathic.scale(2)
        pragmathic.set_color_by_gradient(BLUE, PURPLE)

        intro_text = TextMobject("An odd sum.")

        self.add(pragmathic)
        self.play(pragmathic.set_color_by_gradient, (RED, BLUE))
        self.wait(1)
        self.play(Transform(pragmathic, intro_text))
        self.wait(1.75)
        self.play(FadeOut(pragmathic))


class SumIntro(Scene):
    def construct(self):
        self.wait()
        infinity = TexMobject(r"\infty").scale(2)
        self.play(Write(infinity))
        self.wait(8.5)
        self.play(FadeOut(infinity))
        # A couple days ago, I came across this expression.
        r_sum_expr \
            = TexMobject(r"\displaystyle\sum_{n=0}^{\infty}n")


        # What it's expressing is this:
        r_sum_verbose \
            = TexMobject(r"\displaystyle\sum_{n=0}^{\infty}n = ", r"1 + 2 + 3 + 4 + \dots")
        # Which is the sum of all natural numbers.
        text_sum_natural_numbers \
            = TextMobject("The sum of all ", "natural ", "numbers").set_color_by_tex_to_color_map({"natural": BLUE}).shift(UP*1.5)
        

        # Today, my job is to tell you what this sum equals.
        text_sum_inquiry \
            = TexMobject(r"\displaystyle\sum_{n=0}^{\infty}n = ", r"?")


        # I say, "From the looks of it, it tends to infinity, right?"   
        r_sum_expr1 \
            = TexMobject(r"\displaystyle\sum_", r"{n=0}^",r"{\infty}",r"n"," = ", r"~\infty")
        
        number_line = NumberLine().add_numbers()
        sum_goes_this_way = TextMobject("Numbers go this way...").to_edge(LEFT).shift(RIGHT * (FRAME_X_RADIUS + 1) + DOWN)
        right_arrow = Arrow(LEFT,RIGHT).to_edge(RIGHT).shift(LEFT*0.25).scale(2).set_color(BLUE)

        # The equality: When I say, "Well, it's actually equal to NEGATIVE 12!"
        r_sum_eq \
            = TexMobject(r"\displaystyle\sum_{n=0}^{\infty}n = ", r"-\frac{1}{12}") \
            .set_color(GREEN)

        analytic_continuation \
            = TextMobject("Ramanujan's", " summation") \
            .set_color_by_tex_to_color_map({"Ramanujan's": BLUE}) \
            .shift(UP * 1.5)

        self.play(Write(r_sum_expr))
        self.wait(10)

        self.play(Transform(r_sum_expr, r_sum_verbose))
        self.play(Write(text_sum_natural_numbers))
        self.wait(2)
        self.play(FadeOut(text_sum_natural_numbers))
        self.play(Transform(r_sum_expr, text_sum_inquiry))
        self.wait(8)

        self.wait(3)
        self.play(Transform(r_sum_expr, r_sum_expr1))
        self.wait(13)

        self.play(FadeOut(r_sum_expr))
        self.play(ShowCreation(number_line), ShowCreation(sum_goes_this_way), ShowCreation(right_arrow))
        self.wait(6)

        self.play(FadeOut(number_line), FadeOut(sum_goes_this_way), FadeOut(right_arrow))
        self.play(Write(r_sum_expr))
        self.play(Write(analytic_continuation))
        self.play(r_sum_expr.set_color, RED)
        self.wait()
        self.play(Transform(r_sum_expr, r_sum_eq))
        self.wait(3)


class HowTrue(Scene):
    def construct(self):
        text_how = TextMobject("Wait, what?")

        number_line = NumberLine() \
            .add_numbers()

        this_way = TextMobject("Sum goes this way...")
        this_way.to_edge(LEFT).shift(RIGHT * (FRAME_X_RADIUS + 1) + DOWN)
        how_here = TextMobject("How does it end up here?")
        how_here.shift(1.5 * UP + LEFT)
        neg_1_arrow = Arrow(
            (-1, 0.3, 0),
            tail=how_here.get_center() + 0.5 * DOWN,

        )
        neg_1_arrow.set_color(BLUE)

        number_line.number_to_point(2)

        self.play(Write(text_how))
        self.add(how_here)
        self.play(ShowCreation(neg_1_arrow))
        self.add(this_way)
        self.wait(0.25)
        self.play(FadeOut(text_how))
        self.play(ShowCreation(number_line))


class HowWillProve(Scene):
    def construct(self):
        # How does it work?
        introduction = TextMobject("How", "\\textit{does}", "it work?")
        self.play(Write(introduction))
        self.play(FadeOut(introduction))

        # There are two other sums.
        r_sum_expr = "$\\displaystyle\\sum_{n=0}^{\\infty}n$"
        sum_composition = TextMobject(
            r_sum_expr + "   is proportional to two \\textit{other} sums!")
        self.play(Write(sum_composition))
        self.wait()
        self.play(FadeOut(sum_composition))

        # Two sums
        sum_one_textObject = TexMobject(
            r"\textbf{First sum}: ", r"\displaystyle\sum_{n=0}^{\infty}(-1)^n", " = ", r"1-1+1-1+1 \dots", r" = \frac{1}{2}").shift(UP)
        sum_two_textObject = TexMobject(
            r"\textbf{Second sum}: ", r"1-2+3-4+5 \dots = \frac{1}{4}").shift(DOWN)

        changes = [
            [(0, 3), (0, 1)],
        ]

        self.play(Write(sum_one_textObject))
        for pre_ind, post_ind in changes:
            self.play(*[
                ReplacementTransform(
                    sum_one_textObject[i].copy(), sum_two_textObject[j]
                )
                for i, j in zip(pre_ind, post_ind)
            ],
                run_time=1
            )
            self.wait()


class GrandiSeries(Scene):
    def construct(self):
        introduction = TextMobject("The first sum")
        self.play(Write(introduction))
        self.wait()
        self.play(FadeOutAndShiftDown(introduction))

        # Introduction of Equation
        eq_sigma = TexMobject(r"\displaystyle\sum^{\infty}_{n=0} (-1)^n")
        eq_verbose = TexMobject(r"= 1-1+1-1+1 + \dots").shift(DOWN)
        eq_name = TexMobject(r"S_n").shift(UP*1.5)
        eq_name_equals = TexMobject(r"S_1 = ").shift(UP*1.5)
        grandi_series_text = TextMobject("Grandi", " Series").shift(
            UP*1.5).set_color_by_tex_to_color_map({"Grandi": BLUE})

        self.play(Write(eq_sigma))
        self.play(eq_sigma.shift, UP)
        self.play(ReplacementTransform(
            eq_sigma.copy(), eq_verbose), run_time=1)
        self.wait(2)

        # This is the sigma notation for it.
        self.play(eq_sigma.set_color, BLUE, run_time=0.25)
        self.wait(1)
        self.play(eq_sigma.set_color, WHITE)
        self.wait(2)
        # This is the verbose notation for it.
        self.play(eq_verbose.set_color, BLUE, run_time=0.25)
        self.wait(1)
        self.play(eq_verbose.set_color, WHITE)
        self.wait(4)
        # We're going to be modifying this, so we'll name it S_1.
        self.play(eq_verbose.shift, DOWN)
        self.play(eq_sigma.shift, DOWN)
        self.play(ReplacementTransform(eq_sigma.copy(), eq_name), Transform(
            eq_sigma, TexMobject(r"= \displaystyle\sum^{\infty}_{n=0} (-1)^n")))
        self.wait(2)
        self.play(FadeOut(eq_sigma), FadeOut(eq_verbose))
        self.play(eq_name.shift, DOWN*2)
        self.wait(2)
        # Let's call it S-sub-1, as it is the first sum.
        self.play(Transform(eq_name, TexMobject(
            r"S_1", r" = ", r"1-1+1-1+1 + \dots")))

        # This fascinating sum has an equally fascinating name: Grandi's sum.
        self.play(Write(grandi_series_text))
        self.wait()
        self.play(FadeOut(grandi_series_text))

        # Let's get back to the matter at hand: figuring out what this sum equals. A nice thing about the method I'm telling you about is that you needn't know anything past grade 7 or 8 math to understand this.
        # So, we've set the Grandi Series to S-sub-1, but how do we go about figuring out what the sum of this is?
        # Well, there's a pretty neat trick that we can do with repeating sequences: because they go onto infinity, removing a certain amount won't change it! Here, let me show you.
        self.wait()
        self.play(Transform(eq_name, TexMobject(r"S_1 - (1)", r" = ",r"-1", r"+1", r"-1", r"+1", r" + \dots")))
        self.wait(2)

        # Now, we've subtracted 1 from both sides. But the sum value doesn't change! We can just reshuffle some of the values in the series, and something surprising happens!
        # eq_name = TexMobject(r"S_1 - (1)", r" = ", r"+ 1 - 1 + 1 + \dots")
        surround_verbose = SurroundingRectangle(eq_name[2:7])
        surround_name = TexMobject(r"-S_1").next_to(
            surround_verbose, UP, buff=0.1)
        self.play(ShowCreation(surround_verbose), FadeIn(surround_name))
        # We actually end up where we started! The right side of the equation is still S-sub-1, but we've decreased the left side by 1!
        self.wait(3)
        self.play(FadeOut(surround_verbose), FadeOut(surround_name))

        # This means that we can set the right side of the equation
        
        self.play(Transform(eq_name, TexMobject(r"S_1 - (1)", r" = -S_1")))
        self.wait(2)
        self.play(Transform(eq_name, TexMobject(r"2S_1 = 1")))
        self.wait(2)
        # Dividing both sides by 2, we get S-sub-1 equals 1 half.
        self.play(Transform(eq_name, TexMobject(r"S_1 = \frac{1}{2}")))
        self.wait()
        # Expanding the left side, it's easy to see: 1+1-1+1 and so on all equal 1/2!
        self.play(Transform(eq_name, TexMobject(r"1+1-1+1 + \dots = \frac{1}{2}")))

class IntroBanner(Scene):
    def construct(self):
        pragmathic = TextMobject("Pragmathic")
        pragmathic.scale(2)
        pragmathic.set_color_by_gradient(BLUE, GREEN)

        text = TextMobject("Videos every $e^x$ week, depending on $x$ difficulty.").next_to(pragmathic, DOWN, buff=0.25).scale(0.75)

        self.add(pragmathic)
        self.add(text)

class Logo(Scene):
    def construct(self):
        logo = TextMobject("P").scale(3)
        self.add(logo.set_color(BLUE))