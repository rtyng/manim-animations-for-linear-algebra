from manim import *

class ToyExample(Scene):
    def construct(self):
        orange_square = Square(color=ORANGE, fill_opacity=0.5)
        blue_circle = Circle(color=BLUE, fill_opacity=0.5)
        self.add(orange_square)
        self.play(ReplacementTransform(orange_square, blue_circle, run_time=3))
        small_dot = Dot()
        
        small_dot.add_updater(lambda mob: mob.next_to(blue_circle, DOWN))
        dot_product_label = MathTex(r"\text{Example Text}")
        dot_product_label.next_to(orange_square, direction=UP, buff=0.2)
        self.play(Write(dot_product_label))

        self.play(Create(small_dot))
        self.play(blue_circle.animate.shift(RIGHT))
        self.wait()
        self.play(FadeOut(blue_circle, small_dot))

