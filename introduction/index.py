from manimlib.imports import *


class Intro(Scene):
    def construct(self):
        pragmathic = TextMobject("Pragmathic")
        pragmathic.scale(2)
        pragmathic.set_color_by_gradient(BLUE, PURPLE)

        intro_text = TextMobject("An odd sum.")

        self.play(Write(pragmathic))
        self.wait()
        self.play(pragmathic.set_color_by_gradient, (GREEN, BLUE))
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
        self.wait(10)

        self.wait(3)
        self.play(Transform(r_sum_expr, r_sum_expr1))
        self.wait(13)

        self.play(FadeOut(r_sum_expr))
        self.play(ShowCreation(number_line), ShowCreation(sum_goes_this_way), ShowCreation(right_arrow))
        self.wait(6)

        self.play(FadeOut(number_line), FadeOut(sum_goes_this_way), FadeOut(right_arrow))
        self.play(Write(r_sum_expr))
        self.wait(10)

        self.play(Write(analytic_continuation))
        self.wait(15)
        self.play(r_sum_expr.set_color, RED)
        self.wait(12)
        self.play(Transform(r_sum_expr, r_sum_eq))
        self.wait(3)
        self.play(FadeOut(r_sum_expr), FadeOut(analytic_continuation))


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
        introduction = TextMobject("Section 1.1: Mathematical thinking")
        self.play(Write(introduction))
        self.play(FadeOut(introduction))

        # You're a mathematician, so we'll use your powers of deduction to figure this one out.
        self.wait()
        you = TextMobject("You = Mathematician")
        self.play(Write(you))
        self.wait(5)
        self.play(FadeOut(you))


        # First off, we need to figure out what we're actually doing, so we'll lay out a proposition, 
        propositionintro = TextMobject("Proposition")
        self.play(Write(propositionintro))
        self.play(Transform(propositionintro, TextMobject("Proposition?")))
        # which is exactly what you think: a proposition of a fact, that is either true or false
        self.wait()
        proposition = TexMobject(r"\textit{Proposition 1: }", r"\displaystyle\sum_{n=0}^{\infty}n = -\frac{1}{12}")
        self.play(Transform(propositionintro,proposition))
        # In this case, our proposition is that the sum of all natural numbers is equal, or converges to, negative 1/12th.
        self.wait()
        self.play(FadeOut(propositionintro))
        # Let's go about thinking about this. What if there was a way to think differently about this, not as a sum in itself, but as a proportion of two other sums?
        r_sum_expr = "$\\displaystyle\\sum_{n=0}^{\\infty}n$"
        sum_composition = TextMobject(
            r_sum_expr + "   is a combination of other sums!")
        self.play(Write(sum_composition))
        self.wait()
        self.play(FadeOut(sum_composition))

        # To help prove this, we'll enlist the help of two other sums, which are as follows:
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
        self.play(FadeOut(sum_one_textObject), FadeOut(sum_two_textObject))


class Sum1(Scene):
    def construct(self):
        introduction = TextMobject("Section 1.2: The first sum")
        self.play(Write(introduction))
        self.wait()
        self.play(FadeOutAndShiftDown(introduction))

        eq_sigma = TexMobject(r"\displaystyle\sum^{\infty}_{n=0} (-1)^n")
        eq_verbose = TexMobject(r"= 1-1+1-1+1 + \dots").shift(DOWN)
        eq_name = TexMobject(r"S_1").shift(UP*1.5)
        eq_name_equals = TexMobject(r"S_1 = ").shift(UP*1.5)
        grandi_series_text = TextMobject("Grandi", " Series").shift(
            UP*1.5).set_color_by_tex_to_color_map({"Grandi": BLUE})


        self.play(Write(eq_sigma))
        self.play(eq_sigma.shift, UP)
        self.play(ReplacementTransform(
            eq_sigma.copy(), eq_verbose), run_time=1)
        self.wait(2)

        # # This is the sigma notation for it.
        # self.play(eq_sigma.set_color, BLUE, run_time=0.25)
        # self.wait(1)
        # self.play(eq_sigma.set_color, BLACK)
        # self.wait(2)
        # # This is the verbose notation for it.
        # self.play(eq_verbose.set_color, BLUE, run_time=0.25)
        # self.wait(1)
        # self.play(eq_verbose.set_color, BLACK)
        # self.wait(4)
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
        self.play(Transform(eq_name, TexMobject(r"1-1+1-1 + \dots = \frac{1}{2}")))
        self.play(FadeOut(eq_name))

class Sum2(Scene):
    def construct(self):
        section = TextMobject("Section 1.3: The Second Sum")
        self.play(Write(section))
        self.wait(2)
        self.play(FadeOutAndShiftDown(section))

        # The second sum that we'll be dealing with is this one:
        eq_with_variable = TexMobject(r"S_2 = 1-2+3-4 + ...")
        eq_equality = TexMobject(r"\frac{1}{4} = 1-2+3-4 + ...")
        eq_first = TexMobject(r"S_1 = 1-1+1-1+...").shift(UP)
        self.play(Write(eq_with_variable))
        self.wait()

        # And we'll be proving that this is equivalent to 1/4.
        self.play(Transform(eq_with_variable, eq_equality))
        self.wait()

        # You might be wondering why I chose this sum to go after the first one, and I'd like to show why by bringing up the first one for you.
        self.play(Transform(eq_with_variable, TexMobject(r"S_2 = 1-2+3-4 + ...")))
        self.play(eq_with_variable.shift, DOWN)
        self.play(Write(eq_first))

        # As you can see, the operators between them are the same!
        self.wait()
        # This means that there is some sort of relationship between them!
        self.play(FadeOut(eq_first), FadeOut(eq_with_variable))
        self.wait()
        # Let's try subtracting one from the other. How about the second sum minus the first sum?
        subtract = TexMobject(r"S_2 - S_1 = (1-2+3-4)-(1-1+1-1)")
        self.play(Write(subtract))
        self.wait()
        #Simplifying the right-hand side expression, we get:
        self.play(Transform(subtract, TexMobject(r"S_2 - S_1 = (1-2+3-4)-1+1-1+1")))
        self.wait()
        # Simplifying one more, we get:
        self.play(Transform(subtract, TexMobject(r"S_2 - S_1 = -1+2-3+...")))
        # Now, we see something interesting! Let me just bring up the second sum once again.
        self.play(subtract.shift, UP)
        self.play(Write(eq_with_variable))
        # As you can see, the difference between the first and the second sum is just the inverse of the second sum!
        self.wait()
        self.play(FadeOut(eq_with_variable), Transform(subtract, TexMobject(r"S_2 - S_1 = -S_2")))
        # From here, we know that the first sum is equivalent to 1/2, and so we'll substitute that into this equation.
        self.play(Transform(subtract, TexMobject(r"S_2 - \frac{1}{2} = -S_2")))
        # Now we can solve for the second sum!
        self.play(Transform(subtract, TexMobject(r"2S_2 - \frac{1}{2} = 0")))
        self.play(Transform(subtract, TexMobject(r"2S_2 = \frac{1}{2}")))
        self.play(Transform(subtract, TexMobject(r"S_2 = \frac{1}{4}")))

class Sum3(Scene):
    def construct(self):
        # Now, we can get to the heart of the problem: figuring out what the sum of all natural numbers is equivalent to.
        section = TextMobject("Section 1.4: The Third Sum")
        self.play(Write(section))
        self.wait(2)
        self.play(FadeOutAndShiftDown(section))

        # Just like the other sections, here's the sum.
        eq_with_variable = TexMobject(r"S_3 = \displaystyle\sum_{n=0}^{\infty}n = 1+2+3+4+...")
        eq = TexMobject(r"S_3 = 1+2+3+4+...").shift(DOWN)
        second_eq = TexMobject(r"S_2 = 1-2+3-4+...").shift(DOWN)
        self.play(Write(eq_with_variable))

        # And just like the other sums, we'll try to find out some relationships between the others, so let me bring up the last sum.
        self.play(Transform(eq_with_variable, TexMobject(r"S_3 = 1+2+3+4+...")))
        self.play(eq_with_variable.shift, UP)
        self.play(Write(second_eq))

        # Here, we see the relationship: the numbers in this example are the exact same, but the operators are different! Let's try subtracting the last sum and this one, to find some deeper patterns.
        self.play(FadeOutAndShiftDown(second_eq))
        self.play(Transform(eq_with_variable, TexMobject(r"S_2 - S_3 = (1-2+3-4+...)-(1+2+3+4+...)")))

        # Simplifying, we see:
        self.wait()
        self.play(Transform(eq_with_variable, TexMobject(r"S_2 - S_3 = 1-2+3-4-1-2-3-4-...")))
        self.wait()
        self.play(Transform(eq_with_variable, TexMobject(r"S_2 - S_3 = -4-6-8-...")))

        # Now, a very interesting pattern is revealed. Let me pull up the current sum underneath.
        self.play(eq_with_variable.shift, UP)
        self.play(Write(eq))
        # From here, we can analyze the relationship between them. Can you see anything interesting?
        self.wait()

        # Well, I hope you've noticed that -4-6-8 and so on is just equal to 1+2+3+4 and so on times Negative 4! so we can just write that down.
        self.play(FadeOutAndShiftDown(eq))
        self.play(Transform(eq_with_variable, TexMobject(r"S_2 - S_3 = -4-6-8-... = -4S_3")))

        # I'll leave the equations up for a little bit more so that you can get accustomed to it.
        self.wait()
        

        # Removing some of the useless stuff from this relationship, we can see something pretty cool:
        
        self.play(Transform(eq_with_variable, TexMobject(r"S_2 - S_3 = -4S_3")))

        # Now, we can do some simple algebra to figure out the true value of the third sum, starting with substituting 1/4 into the second sum's variable.
        self.play(Transform(eq_with_variable, TexMobject(r"\frac{1}{4}-S_3 = -4S_3")))

        # And here, we can solve for the third sum.
        self.wait()
        self.play(Transform(eq_with_variable, TexMobject(r"\frac{1}{4} = -3S_3")))
        self.play(Transform(eq_with_variable, TexMobject(r"\frac{1}{12} = -S_3")))
        self.play(Transform(eq_with_variable, TexMobject(r"-\frac{1}{12} = S_3")))

        # Thus, we've proven that the sum of all natural numbers is negative one twelfth!
        self.wait()
        self.play(Transform(eq_with_variable, TexMobject(r"\displaystyle\sum_{n=0}^{\infty}n = 1+2+3+4+5 = -\frac{1}{12}")))

class IntroBanner(Scene):
    def construct(self):
        pragmathic = TextMobject("Pragmathic")
        pragmathic.scale(2)
        pragmathic.set_color_by_gradient(BLUE, GREEN)

        text = TextMobject("Videos every $e^x$ week, depending on $x$ difficulty.").next_to(pragmathic, DOWN, buff=0.25).scale(0.75)

        self.add(pragmathic)
        self.add(text)

class Part1(Scene):
    def construct(self):
        part = TextMobject("Part 1: Value")
        self.play(Write(part))
        self.wait(1)
        self.play(FadeOut(part))

class Part2(Scene):
    def construct(self):
        part = TextMobject("Part 2: Implications")
        self.play(Write(part))
        self.wait(1)
        self.play(FadeOut(part))

class Part3(Scene):
    def construct(self):
        part = TextMobject("Part 3: Outro")
        self.play(Write(part))
        self.wait(1)
        self.play(FadeOut(part))

class Logo(Scene):
    def construct(self):
        logo = TextMobject("P").scale(3)
        self.add(logo.set_color(BLUE))

class wait(Scene):
    def construct(self):
        self.wait(1)